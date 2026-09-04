#!/usr/bin/env python3
"""Validate an AI-pattern Markdown report against extracted source JSON."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


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
POSITION_PATTERN = r"\b(?:body|text|markdown|pdf|footnote|endnote)-[a-z]?\d{4}\b"


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
    parser.add_argument("--source", type=Path)
    args = parser.parse_args()

    report_path = args.report.expanduser()
    extract_path = args.extract_json.expanduser()
    if not report_path.is_file() or not extract_path.is_file():
        parser.error("report and extract_json must exist")

    report = report_path.read_text(encoding="utf-8")
    extracted = json.loads(extract_path.read_text(encoding="utf-8"))
    errors: list[str] = []

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
    if len(coverage_rows) != 16:
        fail(errors, f"expected 16 parseable coverage rows, found {len(coverage_rows)}")
    for rule, status, candidates, adjudicated in coverage_rows:
        if status == "未审查" and (int(candidates) or int(adjudicated)):
            fail(errors, f"S{rule}: unreviewed row must have zero counts")
        if int(adjudicated) > int(candidates):
            fail(errors, f"S{rule}: adjudicated units exceed candidates")

    finding_chunks = re.split(r"(?m)^### (?=AP-(?:S\d{2}|H|M)-\d{3}\s*$)", report)[1:]
    ids: list[str] = []
    for chunk in finding_chunks:
        finding_id = chunk.splitlines()[0].strip()
        ids.append(finding_id)
        for label in ("**位置**", "**触发片段**", "**裁决**", "**理由**", "**保护测试**", "**处理方向**"):
            if label not in chunk:
                fail(errors, f"{finding_id}: missing {label}")
        verdict_match = re.search(r"\*\*裁决\*\*：\s*(\S+)", chunk)
        if not verdict_match or verdict_match.group(1) not in VERDICTS:
            fail(errors, f"{finding_id}: invalid verdict")
        # A rewrite is the only new text this tool emits; it needs its own audit line.
        if "**候选改法**" in chunk and "**守恒核对**" not in chunk:
            fail(errors, f"{finding_id}: 候选改法 present without 守恒核对")
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
        positions = re.findall(POSITION_PATTERN, chunk)
        quotes = re.findall(r"(?m)^> (.+)$", chunk)
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
            for number in sorted(set(re.findall(r"\d+(?:\.\d+)?", rewrite.group(1)))):
                if number not in source_text:
                    fail(errors, f"{finding_id}: 候选改法 introduces number absent from its blocks: {number}")

    expected_hash = str(extracted.get("source_sha256", "")).lower()
    if args.source:
        source = args.source.expanduser()
        if not source.is_file():
            fail(errors, f"source missing: {source}")
        elif sha256_file(source).lower() != expected_hash:
            fail(errors, "source SHA-256 differs from extraction")

    if expected_hash and expected_hash not in report.lower():
        fail(errors, "source SHA-256 missing from report")

    result = {
        "ok": not errors,
        "findings": len(ids),
        "rewrites": report.count("**候选改法**"),
        "quoted_fragments": len(re.findall(r"(?m)^> ", report)),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
