#!/usr/bin/env python3
"""Print the first unused AI-pattern report path beside a source file."""

from __future__ import annotations

import argparse
from pathlib import Path


def next_report_path(source: Path) -> Path:
    version = 1
    while True:
        suffix = "" if version == 1 else f"-v{version}"
        companions = [source.with_name(f"{source.stem}-ai-pattern-{kind}{suffix}.{extension}")
                      for kind, extension in (("report", "md"), ("ledger", "json"),
                                              ("ledger", "md"), ("candidates", "json"))]
        if not any(path.exists() for path in companions):
            return companions[0]
        version += 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_file():
        parser.error(f"source file not found: {source}")
    print(next_report_path(source))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

