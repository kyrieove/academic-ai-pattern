#!/usr/bin/env python3
"""Distill the countable language baseline from two extract-JSON corpora.

Reads indexed section extracts and emits per-paper metrics and equal-weight
summaries for one section/design stratum. Only measures what the
manual already treats as a real signal: passive voice and nominalisation are
deliberately absent, because ai_pattern.md 7 rules them out as signals and
publishing them as a baseline would invite exactly that misuse.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
from pathlib import Path

from scan_all_candidates import author_prose

# Sentence splitting in academic prose dies on these; protect them first.
ABBREVIATIONS = (
    "et al.", "e.g.", "i.e.", "cf.", "vs.", "approx.", "Fig.", "Figs.",
    "Tab.", "No.", "Dr.", "Prof.", "St.", "Eq.",
)

HEDGES = (
    "may", "might", "could", "appear", "appears", "appeared", "suggest",
    "suggests", "suggested", "likely", "unlikely", "possibly", "potentially",
    "presumably", "tend", "tends", "tended", "seem", "seems", "seemed",
    "relatively", "somewhat", "arguably",
)

WORD = re.compile(r"[A-Za-z][A-Za-z'\u2019-]*")
# ponytail: a name followed by a year is narrative; everything else with a year
# inside parentheses is parenthetical.  Misses bracketed numeric styles, which
# is fine: those corpora have no narrative/parenthetical split to measure.
NARRATIVE_CITE = re.compile(
    r"(?<![(\w])[A-Z][A-Za-z'\u2019-]+"
    r"(?:\s+et\s+al\.)?(?:\s+(?:and|&)\s+[A-Z][A-Za-z'\u2019-]+)?"
    r"\s*\(\s*(?:19|20)\d{2}"
)
PAREN_CITE = re.compile(r"\([^()]*?(?:19|20)\d{2}[a-z]?[^()]*?\)")


def sentences(text: str) -> list[str]:
    guarded = text
    for i, abbreviation in enumerate(ABBREVIATIONS):
        guarded = guarded.replace(abbreviation, f"\x00{i}\x00")
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", guarded)
    restored = []
    for part in parts:
        for i, abbreviation in enumerate(ABBREVIATIONS):
            part = part.replace(f"\x00{i}\x00", abbreviation)
        if part.strip():
            restored.append(part.strip())
    return restored


def load_papers(index: Path, section: str, design: str) -> list[dict]:
    """Index paths point to section-only extract JSON, relative to the CSV."""
    papers = []
    seen = set()
    with index.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"path", "side", "section", "design", "journal", "year"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("index is missing required columns")
        for row in reader:
            if row["section"] != section or row["design"] != design:
                continue
            if row["side"] not in {"author", "field"}:
                raise ValueError(f"invalid side: {row['side']}")
            path = (index.parent / row["path"]).resolve()
            data = json.loads(path.read_text(encoding="utf-8"))
            section_names = {"introduction": "Introduction", "methods": "Methods", "method": "Methods",
                             "methodology": "Methods", "results": "Results", "discussion": "Discussion"}
            for block in data.get("blocks", []):
                heading = re.sub(r"^\s*#{1,6}\s*", "", block.get("text", "").strip())
                heading = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", heading).lower()
                if heading in section_names and section_names[heading] != section:
                    raise ValueError(f"extract contains another section; slice before indexing: {row['path']}")
            digest = data.get("source_sha256", "")
            if not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
                raise ValueError(f"missing source hash: {row['path']}")
            identity = (row["side"], digest.lower())
            if identity in seen:
                raise ValueError(f"duplicate paper in selected stratum: {row['path']}")
            seen.add(identity)
            blocks, excluded = author_prose(data.get("blocks", []))
            text = "\n\n".join(text for _, text in blocks)
            if not WORD.search(text):
                raise ValueError(f"no English author prose: {row['path']}")
            papers.append({"path": row["path"], "side": row["side"], "source_sha256": digest,
                           "block_ids": [bid for bid, _ in blocks], "excluded_blocks": excluded,
                           "metrics": measure(text, 1)})
    if not papers:
        raise ValueError("no indexed papers match section and design; full-text rows are not substituted")
    return papers


def measure(text: str, papers: int) -> dict[str, float | int | str]:
    tokens = WORD.findall(text)
    total = len(tokens)
    if not total:
        raise ValueError("cannot measure empty English prose")
    per_k = 1000 / total
    lengths = [len(WORD.findall(sentence)) for sentence in sentences(text)]
    lengths = [n for n in lengths if n]
    lowered = [token.lower() for token in tokens]
    narrative = len(NARRATIVE_CITE.findall(text))
    parenthetical = max(len(PAREN_CITE.findall(text)) - narrative, 0)
    citations = narrative + parenthetical
    return {
        "篇数": papers,
        "词数": total,
        "句长中位数": round(statistics.median(lengths), 1) if lengths else "n/a",
        "句长 p90": round(statistics.quantiles(lengths, n=10)[8], 1) if len(lengths) > 9 else "n/a",
        ">35 词句占比 %": round(100 * sum(n > 35 for n in lengths) / len(lengths), 1) if lengths else "n/a",
        "hedge /千词": round(sum(token in HEDGES for token in lowered) * per_k, 2),
        "分号 /千词": round(text.count(";") * per_k, 2),
        "破折号 /千词": round((text.count("\u2014") + text.count("--")) * per_k, 2),
        "冒号 /千词": round(text.count(":") * per_k, 2),
        "第一人称 /千词": round(sum(token in {"i", "we", "our", "us"} for token in lowered) * per_k, 2),
        "叙述式引用占比 %": round(100 * narrative / citations, 1) if citations else "n/a",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--section", choices=["Introduction", "Methods", "Results", "Discussion"], required=True)
    parser.add_argument("--design", choices=["experimental", "observational", "review", "meta", "qualitative"], required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        papers = load_papers(args.index, args.section, args.design)
    except (OSError, ValueError, KeyError) as exc:
        parser.error(str(exc))
    metrics = [m for m in papers[0]["metrics"] if m != "篇数"]
    sides = [side for side in ("author", "field") if any(p["side"] == side for p in papers)]
    lines = ["# L1 语言层", "", f"范围：{args.section} / {args.design}", "",
             "每篇等权汇总；单元格为篇间中位数 [最小值, 最大值]，n 为该指标有效篇数。",
             "这些描述统计不证明个人指纹、体裁规范或 AI 来源；无引用记 n/a，不记零。", "",
             "| 指标 | " + " | ".join(sides) + " |", "|---|" + "---|" * len(sides)]
    for metric in metrics:
        cells = []
        for side in sides:
            values = [p["metrics"][metric] for p in papers if p["side"] == side
                      and isinstance(p["metrics"][metric], (int, float))]
            cells.append(f"{round(statistics.median(values), 2)} [{min(values)}, {max(values)}]; n={len(values)}" if values else "n/a; n=0")
        lines.append("| " + metric + " | " + " | ".join(cells) + " |")
    lines.extend(["", "## 逐篇数据与出处", "",
                  "| side | 提取文件 | SHA-256 | 正文区块 | " + " | ".join(metrics) + " |",
                  "|---|---|---|---|" + "---|" * len(metrics)])
    for paper in papers:
        values = [paper["side"], paper["path"], paper["source_sha256"], ", ".join(paper["block_ids"])]
        values.extend(str(paper["metrics"][m]) for m in metrics)
        lines.append("| " + " | ".join(v.replace("|", "\\|") for v in values) + " |")
    lines.extend(["", "N/M 保护结论需另定义语义判据并列出满足判据的篇目；不能从中位数直接推得。", ""])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "papers": len(papers), "section": args.section, "design": args.design}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
