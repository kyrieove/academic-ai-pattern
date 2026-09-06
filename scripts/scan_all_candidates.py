#!/usr/bin/env python3
"""Generate a high-recall S1-S16 candidate inventory from extracted blocks.

This scanner locates candidates; it does not adjudicate them.  Its purpose is to
make full-audit recall observable instead of allowing an unsupported zero count.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\"'])")
CITATION = re.compile(r"\([^()]*?(?:19|20)\d{2}[a-z]?[^()]*?\)")
PAREN = re.compile(r"\([^()]*\)")
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")


# Markdown marks its headings; a DOCX that never applied heading styles does
# not, so a bare short line has to be recognised as a heading too.
SECTION_NAME = (
    r"(references|reference list|bibliography|works cited|"
    r"acknowledge?ments?|declarations?|declaration of ai use|conflicts? of interest|"
    r"competing interests?|funding|author contributions?|data availability|"
    r"supplementary|supporting information|appendix|appendices|notes|"
    r"参考文献|致谢|附录|声明)"
)
TRAILING_SECTION = re.compile(rf"^#{{1,6}}\s*[\d.]*\s*{SECTION_NAME}\b", re.I)
BARE_TRAILING = re.compile(rf"^[\d.\s]*{SECTION_NAME}\s*[:：]?$", re.I)
# Only recognized section names are inferred as bare headings; short prose is kept.
BARE_HEADING = re.compile(
    rf"^(?:\d+(?:\.\d+)*\.?\s+)?(?:abstract|introduction|background|methods?|"
    rf"methodology|results|discussion|conclusions?|{SECTION_NAME})\s*[:：]?$", re.I
)
# A front-matter block: most of its lines are "Label: value" pairs (cover page,
# title block, submission metadata).  These are not author prose.
METADATA_LINE = re.compile(r"^\s*(?:\*\*|__)?[^:：\n]{1,40}(?:\*\*|__)?\s*[:：]\s*\S")


def is_front_matter(text: str) -> bool:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines or len(lines) > 12:
        return False
    hits = sum(1 for line in lines if METADATA_LINE.match(line))
    return hits >= max(2, (len(lines) * 3 + 4) // 5)


def author_prose(items: list[dict]) -> tuple[list[tuple[str, str]], list[dict]]:
    """Keep author body prose only.  Every exclusion is recorded, never silent."""
    kept: list[tuple[str, str]] = []
    dropped: list[dict] = []
    trailing = False
    for item in items:
        block_id = str(item.get("id"))
        text = str(item.get("text", ""))
        stripped = " ".join(text.split())
        if item.get("locked"):
            dropped.append({"id": block_id, "reason": "locked-material"})
            continue
        heading = item.get("kind") == "heading" or (
            BARE_HEADING.match(stripped) and len(stripped.split()) <= 8
        )

        if TRAILING_SECTION.match(stripped) or (heading and BARE_TRAILING.match(stripped)):
            trailing = True
        if trailing:
            dropped.append({"id": block_id, "reason": "trailing-section"})
            continue
        if not stripped:
            dropped.append({"id": block_id, "reason": "empty"})
            continue
        if heading:
            dropped.append({"id": block_id, "reason": "heading"})
            continue
        if not kept and is_front_matter(text):
            dropped.append({"id": block_id, "reason": "front-matter"})
            continue
        if item.get("kind") != "paragraph":
            dropped.append({"id": block_id, "reason": f"kind:{item.get('kind')}"})
            continue
        kept.append((block_id, text))
    return kept, dropped


def sentences(text: str) -> list[str]:
    return [item.strip() for item in SENTENCE_SPLIT.split(" ".join(text.split())) if item.strip()]


def prose_without_citations(text: str) -> str:
    return CITATION.sub("", text)


def add(rows: list[dict], seen: set[tuple], rule: str, block_id: str, text: str, signal: str) -> None:
    key = (rule, block_id, text)
    if key not in seen:
        seen.add(key)
        fingerprint = hashlib.sha256(json.dumps(key, ensure_ascii=False).encode("utf-8")).hexdigest()[:12]
        rows.append({"id": f"{rule}-{fingerprint}", "origin": "scanner", "rule": rule,
                     "block_id": block_id, "text": text, "signal": signal})


def generate_inventory(extracted: dict, reviewed_rules: list[str] | None = None) -> dict:
    blocks, excluded = author_prose(extracted.get("blocks", []))

    rows: list[dict] = []
    seen: set[tuple] = set()
    all_sentences: list[tuple[str, str]] = []
    for block_id, paragraph in blocks:
        for sentence in sentences(paragraph):
            all_sentences.append((block_id, sentence))
            clean = prose_without_citations(sentence)
            lower = clean.lower()

            # S1: retain a broad comma-list scan and separate verb-chain signals.
            comma_count = clean.count(",")
            if comma_count >= 3 and re.search(r",\s*(?:and|or)\s", clean, re.I):
                add(rows, seen, "S1", block_id, sentence, f"comma-list:{comma_count}")
            if re.search(r"\b(?:has|have|had) to\s+\w+[^.]{0,220},\s*\w+[^.]{0,160},\s*(?:and\s+)?\w+", clean, re.I):
                add(rows, seen, "S1", block_id, sentence, "governed-verb-chain")
            if len(re.findall(r"\b\w+(?:ing|s|es)\b(?=[^.;]{0,55}(?:,|\band\b))", lower)) >= 4:
                add(rows, seen, "S1", block_id, sentence, "coordinated-actions")

            # S2: explicit or compressed reason/count scaffolds.
            if re.search(r"\b(?:two|three|four) (?:reasons|features|things|points|considerations)\b|\bfor (?:two|three|four) reasons\b", lower):
                add(rows, seen, "S2", block_id, sentence, "numbered-reasons")
            if re.search(r"\bfocus(?:es|ed)? on\b[^.]{0,80}\bbecause\b[^.]{0,140}\band\b", lower):
                add(rows, seen, "S2", block_id, sentence, "stacked-selection-rationale")

            # S3: abstract labels and payoff shells from the full manual.
            if re.search(r"\b(?:helps? (?:to )?explain|helps? (?:to )?show|their contribution is to show|is to show what|"
                         r"this view (?:helps|accommodates)|the implication is|what matters|the point is|"
                         r"process-oriented views?|provides? (?:a )?(?:basis|insight|constraints?))\b", lower):
                add(rows, seen, "S3", block_id, sentence, "abstract-or-payoff-shell")
            if re.search(r",\s*(?:clarifying|highlighting|suggesting|leaving|supporting|showing)\b", lower):
                add(rows, seen, "S3", block_id, sentence, "ing-payoff")

            # S4: every prose colon is a candidate; URLs and metadata are already excluded.
            if ":" in clean and not re.search(r"https?://", clean):
                add(rows, seen, "S4", block_id, sentence, "colon-expansion")

            # S5: demonstrative distance, excluding ordinary that-clauses later in adjudication.
            if re.search(r"(?:^|[.!?]\s+)That\b|\bthat (?:view|result|pattern|literature|account|claim|difference|effect|comparison|component|framework|level|possibility|conclusion)\b", sentence):
                add(rows, seen, "S5", block_id, sentence, "demonstrative-that")

            # S8: complete historical author list plus generic evaluation shells.
            if re.search(r"\b(?:easy to understate|hard to miss|honest position|not a peripheral rival|"
                         r"plainly|instructive|straightforward|useful|crucial|important|clear(?:est)?|"
                         r"strongest|best supported|better-behaved|serious|informative part)\b", lower):
                add(rows, seen, "S8", block_id, sentence, "author-evaluation")

            # S9: broad contrast inventory; adjudication checks both sides.
            contrast = re.findall(r"\b(?:rather than|instead of|not merely|not simply|not only|"
                                  r"does not mean|should not be taken|although|though|whereas|despite|"
                                  r"while|whether|but)\b", lower)
            if contrast:
                add(rows, seen, "S9", block_id, sentence, "contrast:" + ",".join(sorted(set(contrast))))
            if re.search(r"\b(?:from|ranging from)\s+[^,.;]{1,55}\s+to\s+[^,.;]{1,55}", lower):
                add(rows, seen, "S9", block_id, sentence, "range-frame")

            # S11: strong claims, stacked hedges, and universal boundary language.
            if re.search(r"\b(?:prove[sd]?|demonstrat(?:e|es|ed)|establish(?:es|ed)?|confirm(?:s|ed)?|"
                         r"cannot|never|every|all|universal|exactly|clearly|plainly|settle[sd]?|"
                         r"remains? debatable|much less|at least as|best supported)\b", lower):
                add(rows, seen, "S11", block_id, sentence, "claim-strength")
            if re.search(r"\b(?:may|might|could|appears? to|seems? to|suggests?)\b[^.]{0,70}\b(?:may|might|could|appears? to|seems? to|suggests?)\b", lower):
                add(rows, seen, "S11", block_id, sentence, "stacked-hedge")

            # S12: vague agents/trends and citation stacks.
            if re.search(r"\b(?:studies|researchers|research|the literature|developmental accounts|"
                         r"previous work|evidence)\s+(?:increasingly |consistently )?(?:show|shows|suggest|suggests|"
                         r"argue|argues|report|reports|identify|identifies|describe|describes)\b", lower):
                add(rows, seen, "S12", block_id, sentence, "vague-attribution")
            citations = CITATION.findall(sentence)
            semicolons = sum(item.count(";") for item in citations)
            if semicolons >= 2:
                add(rows, seen, "S12", block_id, sentence, f"citation-stack:{semicolons + 1}")

            # S13: portable scaffolds and generic future/limitation gestures.
            if re.search(r"\b(?:future research should|further research is needed|to the best of our knowledge|"
                         r"despite (?:these|the) limitations|remains largely unexplored|warrants caution|"
                         r"provides? (?:a )?(?:basis|starting point|evidence|constraints?)|"
                         r"the present (?:paper|study|article|investigation) (?:argues|focuses|considers|examines))\b", lower):
                add(rows, seen, "S13", block_id, sentence, "portable-scaffold")

            # S14: author-confirmed metaphors plus generic dramatic compression.
            if re.search(r"\b(?:mental [\"']?brake|isolated hardware vacuum|swallow the construct|background noise|"
                         r"speed measured under another name|closeness to the brain|causal chain|"
                         r"how wide a net|sits? at the centre|hunt for|poor stand-in|"
                         r"not a tool but a mirror|becomes? a trap)\b", lower):
                add(rows, seen, "S14", block_id, sentence, "metaphor-or-personification")

            # S15 and S16.
            if "?" in sentence:
                add(rows, seen, "S15", block_id, sentence, "question")
            if re.search(r"\bSection \d+(?:\.\d+)?\b|\b(?:a further|the next) (?:question|issue|qualification|limitation)\b|"
                         r"\b(?:is|are) taken up\b|\bthe discussion (?:below|considers|is organized)\b", sentence, re.I):
                add(rows, seen, "S16", block_id, sentence, "navigation-or-metadiscourse")

    # S6: repeated six-grams, preserving locations and excluding citation/name noise.
    grams: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for block_id, sentence in all_sentences:
        plain = PAREN.sub(" ", sentence.lower())
        words = WORD.findall(plain)
        for index in range(len(words) - 5):
            gram = " ".join(words[index:index + 6])
            if not re.search(r"\bet al\b|\bsection\b", gram):
                grams[gram].append((block_id, sentence))
    for gram, occurrences in grams.items():
        unique_blocks = sorted({block_id for block_id, _ in occurrences})
        if len(unique_blocks) >= 2:
            for block_id, sentence in dict.fromkeys(occurrences):
                add(rows, seen, "S6", block_id, sentence, f"repeated-6gram:{gram}")

    # S7: make every prose paragraph boundary observable for manual adjudication.
    for index in range(len(blocks) - 1):
        left_id, left = blocks[index]
        right_id, right = blocks[index + 1]
        left_s = sentences(left)
        right_s = sentences(right)
        if left_s and right_s:
            text = left_s[-1] + " || " + right_s[0]
            add(rows, seen, "S7", f"{left_id}+{right_id}", text, "paragraph-boundary")

    # S10: term-family occurrences are all candidates until their identity is adjudicated.
    families = {
        "latency": ("response latency", "processing delay", "execution lag", "response delay"),
        "accuracy": ("recognition accuracy", "detection precision", "classification accuracy", "recognition rate"),
        "redundancy": ("sensory redundancy", "crossmodal duplication", "multimodal overlap"),
    }
    for family, terms in families.items():
        for block_id, paragraph in blocks:
            for term in terms:
                if re.search(rf"\b{re.escape(term)}(?:s)?\b", paragraph, re.I):
                    add(rows, seen, "S10", block_id, paragraph, f"term-family:{family}:{term}")
                    break

    rows.sort(key=lambda row: (int(row["rule"][1:]), row["block_id"], row["text"]))
    reviewed_rules = reviewed_rules or [f"S{i}" for i in range(1, 17)]
    rows = [row for row in rows if row["rule"] in reviewed_rules]
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["rule"]] += 1
    result = {
        "schema_version": 2,
        "source_name": extracted.get("source_name"),
        "source_sha256": extracted.get("source_sha256"),
        "scope": "author body prose only; front matter, locked material and trailing sections excluded",
        "scanned_blocks": len(blocks),
        "scanned_block_ids": [block_id for block_id, _ in blocks],
        "input_blocks": len(extracted.get("blocks", [])),
        "reviewed_rules": reviewed_rules,
        "warnings": ([] if blocks else ["No author prose scanned; review cannot be completed."])
                    + ["Lexical signals are not exhaustive; each reviewed rule needs a semantic review."],
        "excluded_blocks": excluded,
        "candidate_count": len(rows),
        "counts": {f"S{number}": counts.get(f"S{number}", 0) for number in range(1, 17)},
        "candidates": rows,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("extract_json", type=Path)
    parser.add_argument("--output", "--json", type=Path)
    parser.add_argument("--rules", nargs="+", choices=[f"S{i}" for i in range(1, 17)],
                        help="Rules included in a focused review; default: all")
    parser.add_argument("--markdown", type=Path, help="Optional human-readable candidate ledger")
    args = parser.parse_args()

    extracted = json.loads(args.extract_json.read_text(encoding="utf-8"))
    result = generate_inventory(extracted, args.rules)
    rows = result["candidates"]
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    if args.markdown:
        lines = [
            f"# AI-pattern 全量原始候选账：{result['source_name']}",
            "",
            f"- 源文件 SHA-256：`{result['source_sha256']}`",
            f"- 范围：{result['scope']}",
            f"- 原始规则信号：{result['candidate_count']}",
            "- 说明：这是高召回定位结果，不等于自动定罪；任何筛除都必须在主报告中说明。",
            "",
            "## 扫描计数",
            "",
            "| 规则 | 原始候选 |",
            "|---|---:|",
        ]
        for number in range(1, 17):
            rule = f"S{number}"
            lines.append(f"| {rule} | {result['counts'][rule]} |")
        for number in range(1, 17):
            rule = f"S{number}"
            lines.extend(["", f"## {rule}", ""])
            for row in rows:
                if row["rule"] != rule:
                    continue
                safe = row["text"].replace("\n", " ").replace("|", "\\|")
                lines.append(f"### {row['id']}")
                lines.append("")
                lines.append(f"- 位置：`{row['block_id']}`")
                lines.append(f"- 信号：`{row['signal']}`")
                lines.append(f"- 原文：{safe}")
        args.markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0 if result["scanned_blocks"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
