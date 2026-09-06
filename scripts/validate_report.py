#!/usr/bin/env python3
"""Validate an AI-pattern Markdown report against extracted source JSON."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from scan_all_candidates import generate_inventory


REQUIRED_SECTIONS = (
    "## 审查元数据",
    "## 执行摘要",
    "## S1–S16 覆盖表",
    "## 行动清单",
    "## 发现",
    "## 受保护与未触发模式",
    "## 外部证据",
    "## 限制",
    "## 源文件校验",
)
VERDICTS = {"需修改", "待作者判断", "受保护", "核查未完成"}
POSITION_PATTERN = r"\b(?:body|text|markdown|pdf|footnote|endnote)-(?:[a-z]+)?\d{4,}\b"
CANDIDATE_PATTERN = r"\bS(?:[1-9]|1[0-6])-(?:[0-9a-f]{12}|MAN-\d{3,})\b"


def validate_ledger(inventory: dict, ledger: dict, extracted: dict,
                    coverage: list, chunks: list[str], errors: list[str]) -> None:
    """Check identity and completeness; semantic judgments are author declarations."""
    source_hash = extracted.get("source_sha256")
    for label, value in (("candidate inventory", inventory), ("ledger", ledger)):
        if value.get("source_sha256") != source_hash:
            errors.append(f"{label}: source hash mismatch")
    blocks = {b["id"]: b for b in extracted.get("blocks", [])}
    scanned = inventory.get("scanned_block_ids", [])
    if not scanned or inventory.get("scanned_blocks") != len(scanned):
        errors.append("no prose scanned or inconsistent scanned block count")
    if len(scanned) != len(set(scanned)) or any(b not in blocks for b in scanned):
        errors.append("invalid scanned block IDs")
    rules = inventory.get("reviewed_rules", [])
    if not rules or len(rules) != len(set(rules)) or any(r not in {f"S{i}" for i in range(1, 17)} for r in rules):
        errors.append("invalid reviewed rules")
    if inventory != generate_inventory(extracted, rules):
        errors.append("candidate inventory differs from a deterministic rescan; regenerate it")
    raw = inventory.get("candidates", [])
    if inventory.get("candidate_count") != len(raw):
        errors.append("candidate count differs from inventory")
    for rule in rules:
        if inventory.get("counts", {}).get(rule) != sum(c.get("rule") == rule for c in raw):
            errors.append(f"{rule}: raw count differs from inventory")
    candidates = raw + ledger.get("semantic_candidates", [])
    by_id = {}
    for candidate in candidates:
        cid = candidate.get("id", "")
        if cid in by_id or not re.fullmatch(CANDIDATE_PATTERN, cid):
            errors.append(f"invalid or duplicate candidate ID: {cid}")
        by_id[cid] = candidate
        if candidate.get("rule") not in rules or not cid.startswith(candidate.get("rule", "") + "-"):
            errors.append(f"{cid}: candidate rule outside scope or inconsistent with ID")
        positions = candidate.get("block_id", "").split("+")
        fragments = candidate.get("text", "").split(" || ")
        if any(p not in scanned for p in positions):
            errors.append(f"{cid}: candidate outside scanned prose")
        normalized_sources = [" ".join(blocks.get(p, {}).get("text", "").split()) for p in positions]
        if not candidate.get("text", "").strip() or any(
            not any(" ".join(fragment.split()) in source for source in normalized_sources) for fragment in fragments
        ):
            errors.append(f"{cid}: candidate text absent from referenced blocks")
    for candidate in ledger.get("semantic_candidates", []):
        if not re.fullmatch(r"S(?:[1-9]|1[0-6])-MAN-\d{3,}", candidate.get("id", "")) or not candidate.get("signal", "").strip():
            errors.append("semantic candidate needs MAN ID and a concrete discovery reason in signal")
    findings = {chunk.splitlines()[0].strip(): chunk for chunk in chunks}
    decisions = {}
    for decision in ledger.get("decisions", []):
        cid = decision.get("candidate_id")
        if cid in decisions or cid not in by_id:
            errors.append(f"duplicate or unknown ledger candidate: {cid}")
        decisions[cid] = decision
        if decision.get("verdict") not in VERDICTS or not decision.get("reason", "").strip():
            errors.append(f"{cid}: invalid verdict or empty reason")
        fid = decision.get("finding_id")
        if decision.get("verdict") == "需修改" and not fid:
            errors.append(f"{cid}: revision decision requires a finding")
        if fid:
            chunk = findings.get(fid, "")
            links = re.search(r"(?m)^\*\*账本\*\*：(.*)$", chunk)
            if not chunk or not links or cid not in re.findall(CANDIDATE_PATTERN, links.group(1)):
                errors.append(f"{cid}: missing reverse finding link: {fid}")
            verdict = re.search(r"\*\*裁决\*\*：\s*(\S+)", chunk)
            if verdict and verdict.group(1) != decision.get("verdict"):
                errors.append(f"{cid}: finding verdict differs from ledger")
    if set(decisions) != set(by_id):
        errors.append("ledger must contain exactly one decision for every candidate")
    for fid, chunk in findings.items():
        links = re.search(r"(?m)^\*\*账本\*\*：(.*)$", chunk)
        if not links:
            errors.append(f"{fid}: missing 账本 field")
            continue
        linked = re.findall(CANDIDATE_PATTERN, links.group(1))
        if fid.startswith("AP-S") and not linked:
            errors.append(f"{fid}: pattern finding requires a candidate link")
        for cid in linked:
            if decisions.get(cid, {}).get("finding_id") != fid:
                errors.append(f"{fid}: missing reverse ledger link: {cid}")
    for number, status, count, adjudicated in coverage:
        rule = f"S{number}"
        actual = [cid for cid, c in by_id.items() if c.get("rule") == rule]
        done = sum(cid in decisions and decisions[cid].get("reason", "").strip() != "未逐条裁决" for cid in actual)
        if int(count) != len(actual) or int(adjudicated) != done:
            errors.append(f"{rule}: coverage counts differ from ledger")
        if (rule not in rules) != (status == "未审查"):
            errors.append(f"{rule}: coverage status differs from scan scope")
        if status == "已审查" and (done != len(actual) or ledger.get("semantic_review", {}).get(rule) is not True):
            errors.append(f"{rule}: complete status requires all decisions and declared semantic review")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("extract_json", type=Path)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--candidates", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True, help="Structured adjudication JSON")
    args = parser.parse_args()

    report_path = args.report.expanduser()
    extract_path = args.extract_json.expanduser()
    if not report_path.is_file() or not extract_path.is_file():
        parser.error("report and extract_json must exist")

    report = report_path.read_text(encoding="utf-8")
    extracted = json.loads(extract_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    if re.search(r"\{\{[^{}]+\}\}", report):
        fail(errors, "unresolved template placeholders")

    for section in REQUIRED_SECTIONS:
        if section not in report:
            fail(errors, f"missing section: {section}")

    section_positions = [report.find(section) for section in REQUIRED_SECTIONS]
    present_positions = [position for position in section_positions if position >= 0]
    if present_positions != sorted(present_positions):
        fail(errors, "required sections are out of order")

    for number in range(1, 17):
        if not re.search(rf"(?m)^\| S{number}(?:\s|\|)", report):
            fail(errors, f"coverage row missing: S{number}")

    coverage_rows = re.findall(
        r"(?m)^\| S(\d{1,2})\s+[^|]+\|\s*(已审查|部分审查|未审查)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|$",
        report,
    )
    if len(coverage_rows) != 16 or {r[0] for r in coverage_rows} != {str(i) for i in range(1, 17)}:
        fail(errors, f"expected 16 parseable coverage rows, found {len(coverage_rows)}")
    for rule, status, candidates, adjudicated in coverage_rows:
        if status == "未审查" and (int(candidates) or int(adjudicated)):
            fail(errors, f"S{rule}: unreviewed row must have zero counts")
        if int(adjudicated) > int(candidates):
            fail(errors, f"S{rule}: adjudicated units exceed candidates")

    finding_chunks = re.findall(r"(?ms)^### (AP-(?:S\d{2}|H|M)-\d{3}\s*\n.*?)(?=^### |^## |\Z)", report)
    ids: list[str] = []
    for chunk in finding_chunks:
        finding_id = chunk.splitlines()[0].strip()
        ids.append(finding_id)
        if not re.fullmatch(r"AP-(?:S(?:0[1-9]|1[0-6])|H|M)-\d{3}", finding_id):
            fail(errors, f"invalid finding ID: {finding_id}")
        for label in ("**位置**", "**触发片段**", "**裁决**", "**理由**", "**保护测试**", "**处理方向**"):
            if label not in chunk:
                fail(errors, f"{finding_id}: missing {label}")
        verdict_match = re.search(r"\*\*裁决\*\*：\s*(\S+)", chunk)
        if not verdict_match or verdict_match.group(1) not in VERDICTS:
            fail(errors, f"{finding_id}: invalid verdict")
        # A rewrite is the only new text this tool emits; it needs its own audit line.
        if "**候选改法**" in chunk and "**守恒核对**" not in chunk:
            fail(errors, f"{finding_id}: 候选改法 present without 守恒核对")
        if "**候选改法**" in chunk and (not verdict_match or verdict_match.group(1) != "需修改"):
            fail(errors, f"{finding_id}: only 需修改 may include a rewrite")
    if len(ids) != len(set(ids)):
        fail(errors, "duplicate finding IDs")

    # The action list is the whole set of things this round has to handle.  A
    # finding missing from it is a finding that gets forgotten.
    action_section = re.search(r"## 行动清单\n(.*?)(?=\n## )", report, re.S)
    if action_section:
        listed = re.findall(r"(?m)^\|\s*(AP-(?:S\d{2}|H|M)-\d{3})\s*\|", action_section.group(1))
        if len(listed) != len(ids):
            fail(errors, f"action list has {len(listed)} rows but {len(ids)} findings are expanded")
        missing = sorted(set(ids) - set(listed))
        if missing:
            fail(errors, f"findings missing from the action list: {', '.join(missing)}")

    known_blocks = {str(item.get("id")): str(item.get("text", "")) for item in extracted.get("blocks", [])}
    for block_id in re.findall(POSITION_PATTERN, report):
        if block_id not in known_blocks:
            fail(errors, f"unknown block id: {block_id}")

    for chunk in finding_chunks:
        finding_id = chunk.splitlines()[0].strip()
        location = re.search(r"(?m)^\*\*位置\*\*：(.*)$", chunk)
        positions = re.findall(POSITION_PATTERN, location.group(1) if location else "")
        trigger = re.search(r"\*\*触发片段\*\*：(.*?)(?=\n\*\*|\Z)", chunk, re.S)
        quotes = re.findall(r"(?m)^> (.+)$", trigger.group(1) if trigger else "")
        if not quotes:
            fail(errors, f"{finding_id}: missing exact trigger quote")
        if not positions:
            fail(errors, f"{finding_id}: no parseable block ID in position")
        for quote in quotes:
            normalized = quote.rstrip()
            if not any(normalized in known_blocks.get(block_id, "") for block_id in positions):
                fail(errors, f"{finding_id}: quote not found in its referenced blocks: {normalized[:80]}")
        # Numbers are the cheapest thing to fabricate and the most expensive to miss.
        rewrite = re.search(r"(?m)^\*\*候选改法\*\*：(.*?)(?=\n\*\*|\Z)", chunk, re.S)
        if rewrite:
            source_text = " ".join(known_blocks.get(block_id, "") for block_id in positions)
            numbers = set(re.findall(r"(?<!\w)[+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?", source_text))
            for number in sorted(set(re.findall(r"(?<!\w)[+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?", rewrite.group(1)))):
                if number not in numbers:
                    fail(errors, f"{finding_id}: 候选改法 introduces number absent from its blocks: {number}")

    expected_hash = str(extracted.get("source_sha256", "")).lower()
    if not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
        fail(errors, "missing or invalid source hash")
    if args.source:
        source = args.source.expanduser()
        if not source.is_file():
            fail(errors, f"source missing: {source}")
        elif sha256_file(source).lower() != expected_hash:
            fail(errors, "source SHA-256 differs from extraction")

    if expected_hash and expected_hash not in report.lower():
        fail(errors, "source SHA-256 missing from report")

    try:
        inventory = json.loads(args.candidates.read_text(encoding="utf-8"))
        ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
        validate_ledger(inventory, ledger, extracted, coverage_rows, finding_chunks, errors)
    except (OSError, ValueError, TypeError, AttributeError, KeyError) as exc:
        fail(errors, f"invalid candidate inventory or ledger: {exc}")

    result = {
        "ok": not errors,
        "validation_scope": "format, provenance and ledger consistency; semantic conservation requires human/agent review",
        "findings": len(ids),
        "rewrites": report.count("**候选改法**"),
        "quoted_fragments": len(re.findall(r"(?m)^> ", report)),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
