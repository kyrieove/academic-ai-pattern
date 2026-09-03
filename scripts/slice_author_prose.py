#!/usr/bin/env python3
"""Slice extracted blocks to the actual manuscript prose.

Useful for DOCX files with a cover page and a table of contents whose entries
repeat section names before the real body.  The output retains original block
IDs and source metadata, but includes only blocks from the exact Introduction
heading through the block before the exact AI-use declaration or References.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def heading_text(text: str) -> str:
    return re.sub(r"^#{1,6}\s+", "", " ".join(text.split())).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.source.read_text(encoding="utf-8"))
    blocks = data.get("blocks", [])

    starts = [
        i for i, block in enumerate(blocks)
        if re.match(r"^(?:1\.?\s*)?introduction\b", heading_text(str(block.get("text", ""))).lower())
    ]
    if not starts:
        raise SystemExit("Introduction heading not found")
    start = starts[-1]
    stop = len(blocks)
    for i in range(start + 1, len(blocks)):
        normalized = heading_text(str(blocks[i].get("text", ""))).lower()
        if normalized in {"declaration of ai use", "references"}:
            stop = i
            break

    sliced = dict(data)
    sliced_blocks = []
    for block in blocks[start:stop]:
        copied = dict(block)
        # The bundled DOCX extractor currently reports Word headings as
        # paragraphs.  Preserve them for traceability but keep scanners from
        # treating them as prose, matching Markdown extraction behavior.
        if str(copied.get("style")) in {"1", "2", "3", "4", "Heading 1", "Heading 2", "Heading 3", "Heading 4"}:
            copied["kind"] = "heading"
        sliced_blocks.append(copied)
    sliced["blocks"] = sliced_blocks
    sliced["block_count"] = len(sliced["blocks"])
    sliced["slice"] = {
        "start_id": blocks[start].get("id"),
        "stop_before_id": blocks[stop].get("id") if stop < len(blocks) else None,
    }
    args.output.write_text(json.dumps(sliced, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(sliced["slice"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
