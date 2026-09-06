#!/usr/bin/env python3
"""Extract auditable document blocks without modifying the source file."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def block(block_id: str, part: str, kind: str, text: str, **extra: Any) -> dict[str, Any]:
    item: dict[str, Any] = {
        "id": block_id,
        "part": part,
        "kind": kind,
        "text": text,
    }
    item.update(extra)
    return item


def paragraph_text(element: ET.Element) -> str:
    pieces: list[str] = []
    for node in element.iter():
        if node.tag == f"{W}t":
            pieces.append(node.text or "")
        elif node.tag == f"{W}tab":
            pieces.append("\t")
        elif node.tag in {f"{W}br", f"{W}cr"}:
            pieces.append("\n")
    return "".join(pieces)


def paragraph_style(element: ET.Element) -> str | None:
    properties = element.find(f"{W}pPr")
    if properties is None:
        return None
    style = properties.find(f"{W}pStyle")
    if style is None:
        return None
    return style.get(f"{W}val")


def paragraph_kind(style: str | None) -> str:
    if style and re.search(r"heading|title", style, flags=re.IGNORECASE):
        return "heading"
    if style and re.search(r"caption", style, flags=re.IGNORECASE):
        return "caption"
    return "paragraph"


def parse_docx_part(xml_bytes: bytes, part: str, prefix: str) -> list[dict[str, Any]]:
    root = ET.fromstring(xml_bytes)
    if part == "body":
        container = root.find(f"{W}body")
        if container is None:
            return []
        nodes = [(child, {}) for child in list(container)]
    else:
        nodes = []
        for note in list(root):
            note_id = note.get(f"{W}id")
            note_type = note.get(f"{W}type")
            if note_type in {"separator", "continuationSeparator"}:
                continue
            nodes.extend(
                (child, {"note_id": note_id, "note_type": note_type})
                for child in list(note)
            )

    blocks: list[dict[str, Any]] = []
    sequence = 0
    for child, node_metadata in nodes:
        if child.tag == f"{W}p":
            text = paragraph_text(child)
            if not text.strip():
                continue
            sequence += 1
            style = paragraph_style(child)
            blocks.append(
                block(
                    f"{prefix}-p{sequence:04d}",
                    part,
                    paragraph_kind(style),
                    text,
                    style=style,
                    **node_metadata,
                )
            )
        elif child.tag == f"{W}tbl":
            for row_number, row in enumerate(child.findall(f"{W}tr"), start=1):
                for cell_number, cell in enumerate(row.findall(f"{W}tc"), start=1):
                    paragraphs = [paragraph_text(p) for p in cell.findall(f"{W}p")]
                    text = "\n".join(value for value in paragraphs if value.strip())
                    if not text.strip():
                        continue
                    sequence += 1
                    blocks.append(
                        block(
                            f"{prefix}-t{sequence:04d}",
                            part,
                            "table-cell",
                            text,
                            row=row_number,
                            cell=cell_number,
                            **node_metadata,
                        )
                    )
    return blocks


def extract_docx(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    blocks: list[dict[str, Any]] = []
    warnings = [
        "DOCX headers, footers, comments, drawings, and text boxes are not extracted by the bundled extractor.",
        "Tracked deletions are omitted; inserted text represented as normal Word text is retained.",
        "Table cells require semantic classification: prose may be reviewed, while data cells remain locked.",
    ]
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        document_name = "word/document.xml"
        if document_name not in names:
            raise ValueError("DOCX has no word/document.xml")
        blocks.extend(parse_docx_part(archive.read(document_name), "body", "body"))
        for filename, part, prefix in (
            ("word/footnotes.xml", "footnotes", "footnote"),
            ("word/endnotes.xml", "endnotes", "endnote"),
        ):
            if filename in names:
                blocks.extend(parse_docx_part(archive.read(filename), part, prefix))
    return blocks, warnings


def split_plain_paragraphs(text: str) -> list[str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return [item for item in re.split(r"\n[ \t]*\n+", normalized) if item.strip()]


def extract_txt(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    text = path.read_text(encoding="utf-8-sig")
    blocks = [
        block(f"text-p{index:04d}", "body", "paragraph", value)
        for index, value in enumerate(split_plain_paragraphs(text), start=1)
    ]
    return blocks, []


def extract_markdown(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    blocks: list[dict[str, Any]] = []
    buffer: list[str] = []
    in_fence = False
    fence_lines: list[str] = []
    sequence = 0

    def emit_buffer() -> None:
        nonlocal sequence
        if not buffer:
            return
        value = "\n".join(buffer).strip("\n")
        buffer.clear()
        if not value.strip():
            return
        sequence += 1
        first = value.lstrip().split("\n", 1)[0]
        if first.startswith("#"):
            kind = "heading"
        elif all(line.lstrip().startswith(">") for line in value.split("\n") if line.strip()):
            kind = "quotation"
        else:
            kind = "paragraph"
        blocks.append(block(f"markdown-p{sequence:04d}", "body", kind, value, locked=kind == "quotation"))

    for line in lines:
        if re.match(r"^\s*(```|~~~)", line):
            if not in_fence:
                emit_buffer()
                in_fence = True
                fence_lines = [line]
            else:
                fence_lines.append(line)
                sequence += 1
                blocks.append(
                    block(
                        f"markdown-code{sequence:04d}",
                        "body",
                        "code",
                        "\n".join(fence_lines),
                        locked=True,
                    )
                )
                in_fence = False
                fence_lines = []
            continue
        if in_fence:
            fence_lines.append(line)
        elif re.match(r"^ {0,3}#{1,6}(?:\s|$)", line):
            emit_buffer()
            buffer.append(line)
            emit_buffer()
        elif not line.strip():
            emit_buffer()
        else:
            buffer.append(line)

    if in_fence:
        sequence += 1
        blocks.append(
            block(
                f"markdown-code{sequence:04d}",
                "body",
                "code",
                "\n".join(fence_lines),
                locked=True,
            )
        )
        warning = "Markdown contains an unclosed code fence; the remaining text was locked as code."
        warnings = [warning]
    else:
        warnings = []
        emit_buffer()
    return blocks, warnings


def extract_pdf(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    reader_class = None
    try:
        from pypdf import PdfReader  # type: ignore

        reader_class = PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader  # type: ignore

            reader_class = PdfReader
        except ImportError as exc:
            raise RuntimeError("PDF extraction requires pypdf or PyPDF2") from exc

    reader = reader_class(str(path))
    blocks: list[dict[str, Any]] = []
    sequence = 0
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        for value in split_plain_paragraphs(page_text):
            sequence += 1
            blocks.append(
                block(
                    f"pdf-p{sequence:04d}",
                    f"page-{page_number}",
                    "paragraph",
                    value,
                    page=page_number,
                )
            )
    warnings = [
        "PDF extraction is degraded: columns, page headers, footnotes, ligatures, and paragraph boundaries may be wrong.",
        "Exact-quotation findings require visual verification against the PDF before adjudication.",
        "No OCR is performed; pages without extractable text remain unavailable.",
    ]
    return blocks, warnings


def extract(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        blocks, warnings = extract_docx(path)
    elif suffix in {".md", ".markdown"}:
        blocks, warnings = extract_markdown(path)
    elif suffix == ".txt":
        blocks, warnings = extract_txt(path)
    elif suffix == ".pdf":
        blocks, warnings = extract_pdf(path)
    else:
        raise ValueError(f"Unsupported input format: {suffix or '[no extension]'}")

    return {
        "schema_version": 1,
        "source_name": path.name,
        "source_path": str(path.resolve()),
        "source_sha256": sha256_file(path),
        "input_format": suffix.lstrip("."),
        "extracted_at_utc": datetime.now(timezone.utc).isoformat(),
        "warnings": warnings,
        "block_count": len(blocks),
        "blocks": blocks,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="DOCX, Markdown, TXT, or PDF input")
    parser.add_argument("--output", type=Path, help="Optional JSON output; stdout is used by default")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.expanduser()
    if not source.is_file():
        print(f"Source file not found: {source}", file=sys.stderr)
        return 2
    try:
        result = extract(source)
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"Extraction failed: {exc}", file=sys.stderr)
        return 1

    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = args.output.expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
