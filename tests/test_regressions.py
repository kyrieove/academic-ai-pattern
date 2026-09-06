"""Regression checks for extraction, audit completeness and corpus provenance."""
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from extract_document import extract
from scan_all_candidates import author_prose
from next_report_path import next_report_path
from distill_baseline import load_papers, measure


class RegressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)

    def write(self, name, text):
        path = self.directory / name
        path.write_text(text, encoding="utf-8")
        return path

    def run_script(self, script, *args):
        return subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts" / script), *map(str, args)],
                              capture_output=True, text=True, encoding="utf-8")

    def test_headingless_text_is_prose(self):
        data = extract(self.write("paper.txt", "This important framework needs evidence.\n\nA short claim"))
        self.assertEqual(len(author_prose(data["blocks"])[0]), 2)

    def test_heading_without_blank_line_preserves_body(self):
        data = extract(self.write("paper.md", "# Introduction\nThis important claim needs evidence."))
        self.assertEqual([b["kind"] for b in data["blocks"]], ["heading", "paragraph"])
        self.assertEqual(len(author_prose(data["blocks"])[0]), 1)

    def test_locked_and_references_excluded(self):
        data = extract(self.write("paper.md", "# Introduction\nBody prose.\n\n```python\nLOCKED\n```\n\n# References\nREFERENCE_ENTRY"))
        self.assertEqual([text for _, text in author_prose(data["blocks"])[0]], ["Body prose."])

    def audit_inputs(self):
        source = self.write("paper.md", "# Introduction\nThis result from 12 trials is important.")
        data = extract(source)
        extracted = self.write("extract.json", json.dumps(data))
        candidates = self.directory / "candidates.json"
        result = self.run_script("scan_all_candidates.py", extracted, "--json", candidates)
        self.assertEqual(result.returncode, 0, result.stderr)
        inventory = json.loads(candidates.read_text(encoding="utf-8"))
        ledger_data = {"source_sha256": data["source_sha256"], "semantic_candidates": [],
                       "semantic_review": {f"S{i}": True for i in range(1, 17)},
                       "decisions": [{"candidate_id": c["id"], "reason": "Important has no stated comparison; author must clarify its function.",
                                      "verdict": "待作者判断", "finding_id": None} for c in inventory["candidates"]]}
        ledger = self.write("ledger.json", json.dumps(ledger_data))
        report = (ROOT / "assets/report-template.md").read_text(encoding="utf-8")
        import re
        report = re.sub(r"\{\{[^{}]+\}\}", "无", report)
        for rule in range(1, 17):
            count = inventory["counts"][f"S{rule}"]
            report = re.sub(rf"(?m)^(\| S{rule} [^|]+\|).*", rf"\1 已审查 | {count} | {count} |", report)
        report += "\n" + data["source_sha256"]
        return source, extracted, candidates, ledger, self.write("report.md", report), ledger_data

    def validate(self, inputs):
        source, extracted, candidates, ledger, report, _ = inputs
        return self.run_script("validate_report.py", report, extracted, "--source", source,
                               "--candidates", candidates, "--ledger", ledger)

    def test_complete_no_finding_report_passes(self):
        result = self.validate(self.audit_inputs())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_decision_fails(self):
        inputs = self.audit_inputs()
        inputs[5]["decisions"] = []
        inputs[3].write_text(json.dumps(inputs[5]), encoding="utf-8")
        self.assertNotEqual(self.validate(inputs).returncode, 0)

    def test_placeholder_fails(self):
        inputs = self.audit_inputs()
        with inputs[4].open("a", encoding="utf-8") as handle:
            handle.write("\n{{UNFILLED}}")
        self.assertNotEqual(self.validate(inputs).returncode, 0)

    def test_zero_prose_fails_scan(self):
        extracted = self.write("empty.json", json.dumps({"blocks": []}))
        self.assertNotEqual(self.run_script("scan_all_candidates.py", extracted).returncode, 0)

    def test_missing_semantic_review_fails(self):
        inputs = self.audit_inputs()
        inputs[5]["semantic_review"]["S10"] = False
        inputs[3].write_text(json.dumps(inputs[5]), encoding="utf-8")
        self.assertNotEqual(self.validate(inputs).returncode, 0)

    def test_candidate_inventory_cannot_be_trimmed(self):
        inputs = self.audit_inputs()
        inventory = json.loads(inputs[2].read_text(encoding="utf-8"))
        inventory["candidates"] = []
        inventory["candidate_count"] = 0
        inventory["counts"] = {f"S{i}": 0 for i in range(1, 17)}
        inputs[2].write_text(json.dumps(inventory), encoding="utf-8")
        result = self.validate(inputs)
        self.assertIn("deterministic rescan", result.stdout)
        self.assertEqual(result.returncode, 1)

    def test_duplicate_decision_fails(self):
        inputs = self.audit_inputs()
        inputs[5]["decisions"].append(inputs[5]["decisions"][0])
        inputs[3].write_text(json.dumps(inputs[5]), encoding="utf-8")
        self.assertIn("duplicate", self.validate(inputs).stdout)

    def test_semantic_candidate_is_included_in_coverage(self):
        inputs = self.audit_inputs()
        data = inputs[5]
        data["semantic_candidates"] = [{"id": "S3-MAN-001", "rule": "S3", "block_id": "markdown-p0002",
                                         "text": "This result from 12 trials is important.",
                                         "signal": "The result itself has not been described."}]
        data["decisions"].append({"candidate_id": "S3-MAN-001", "reason": "The result needs context from the author.",
                                  "verdict": "待作者判断", "finding_id": None})
        inputs[3].write_text(json.dumps(data), encoding="utf-8")
        report = inputs[4].read_text(encoding="utf-8").replace("| S3 抽象到不知所言 | 已审查 | 0 | 0 |",
                                                             "| S3 抽象到不知所言 | 已审查 | 1 | 1 |")
        inputs[4].write_text(report, encoding="utf-8")
        result = self.validate(inputs)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rewrite_number_requires_exact_token(self):
        inputs = self.audit_inputs()
        decision = inputs[5]["decisions"][0]
        decision.update(verdict="需修改", finding_id="AP-S08-001")
        inputs[3].write_text(json.dumps(inputs[5]), encoding="utf-8")
        report = inputs[4].read_text(encoding="utf-8")
        report = report.replace("## 发现", "| AP-S08-001 | 评价 | 需修改 | markdown-p0002 | 删评价。 |\n\n## 发现", 1)
        finding = f"""### AP-S08-001

**位置**：markdown-p0002

**触发片段**：

> This result from 12 trials is important.

**裁决**：需修改

**理由**：评价没有比较维度。

**保护测试**：important 没有定义其依据。

**处理方向**：删除评价。

**候选改法**：This result is from 2 trials.

**守恒核对**：测试一个伪造的数值。

**账本**：{decision['candidate_id']}

"""
        report = report.replace("## 受保护与未触发模式", finding + "## 受保护与未触发模式")
        inputs[4].write_text(report, encoding="utf-8")
        result = self.validate(inputs)
        self.assertEqual(result.returncode, 1)
        self.assertIn("introduces number", result.stdout)
        inputs[4].write_text(report.replace("from 2 trials.", "from 12 trials."), encoding="utf-8")
        result = self.validate(inputs)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_revision_without_finding_fails(self):
        inputs = self.audit_inputs()
        inputs[5]["decisions"][0]["verdict"] = "需修改"
        inputs[3].write_text(json.dumps(inputs[5]), encoding="utf-8")
        self.assertIn("requires a finding", self.validate(inputs).stdout)

    def test_source_change_fails(self):
        inputs = self.audit_inputs()
        inputs[0].write_text("Changed source", encoding="utf-8")
        self.assertIn("source SHA-256 differs", self.validate(inputs).stdout)

    def test_version_checks_companion_files(self):
        source = self.write("paper.md", "Body.")
        self.write("paper-ai-pattern-ledger.json", "{}")
        self.assertEqual(next_report_path(source).name, "paper-ai-pattern-report-v2.md")

    def test_sample_report_and_reverse_links(self):
        source = ROOT / "examples/sample_paper.md"
        extracted = self.write("sample.json", json.dumps(extract(source)))
        candidates = self.directory / "sample_candidates.json"
        scan = self.run_script("scan_all_candidates.py", extracted, "--rules", "S1", "S13", "--output", candidates)
        self.assertEqual(scan.returncode, 0, scan.stderr)
        report = ROOT / "examples/sample_report.md"
        ledger = ROOT / "examples/sample_ledger.json"
        result = self.run_script("validate_report.py", report, extracted, "--source", source,
                                 "--candidates", candidates, "--ledger", ledger)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        broken = json.loads(ledger.read_text(encoding="utf-8"))
        for decision in broken["decisions"]:
            if decision["finding_id"]:
                decision["finding_id"] = "AP-S01-999"
                break
        broken_path = self.write("broken.json", json.dumps(broken))
        result = self.run_script("validate_report.py", report, extracted, "--source", source,
                                 "--candidates", candidates, "--ledger", broken_path)
        self.assertEqual(result.returncode, 1)
        self.assertIn("reverse", result.stdout)

    def test_baseline_respects_index_and_exclusions(self):
        paper = self.write("paper.json", json.dumps({"source_sha256": "a" * 64, "blocks": [
            {"id": "text-p0001", "kind": "paragraph", "text": "We may observe changes."},
            {"id": "text-p0002", "kind": "code", "locked": True, "text": "LOCKED_CODE"},
            {"id": "text-p0003", "kind": "heading", "text": "References"},
            {"id": "text-p0004", "kind": "paragraph", "text": "REFERENCE_ENTRY"}]}))
        index = self.directory / "index.csv"
        with index.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["path", "side", "journal", "year", "section", "design", "n", "is_author", "notes"])
            writer.writerow([paper.name, "author", "Test", "2020", "Introduction", "experimental", "", "true", ""])
        output = self.directory / "baseline.md"
        result = self.run_script("distill_baseline.py", "--index", index, "--section", "Introduction",
                                 "--design", "experimental", "--output", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        rendered = output.read_text(encoding="utf-8")
        self.assertIn("250.0", rendered)  # one hedge / four words, no locked/reference words
        self.assertIn("paper.json", rendered)
        result = self.run_script("distill_baseline.py", "--index", index, "--section", "Methods",
                                 "--design", "experimental", "--output", output)
        self.assertNotEqual(result.returncode, 0)

    def test_no_citations_is_not_zero_narrative_share(self):
        self.assertEqual(measure("We observed changes.", 1)["叙述式引用占比 %"], "n/a")

    def test_baseline_rejects_full_text_labeled_as_one_section(self):
        self.write("paper.json", json.dumps({"source_sha256": "b" * 64, "blocks": [
            {"id": "text-p0001", "kind": "heading", "text": "Introduction"},
            {"id": "text-p0002", "kind": "paragraph", "text": "We may observe changes."},
            {"id": "text-p0003", "kind": "heading", "text": "Methods"},
            {"id": "text-p0004", "kind": "paragraph", "text": "We ran an experiment."}]}))
        index = self.write("index.csv", "path,side,journal,year,section,design\npaper.json,author,Test,2020,Introduction,experimental\n")
        with self.assertRaisesRegex(ValueError, "another section"):
            load_papers(index, "Introduction", "experimental")

    def test_baseline_rejects_duplicate_papers(self):
        self.write("paper.json", json.dumps({"source_sha256": "c" * 64, "blocks": [
            {"id": "text-p0001", "kind": "paragraph", "text": "We may observe changes."}]}))
        row = "paper.json,author,Test,2020,Introduction,experimental\n"
        index = self.write("index.csv", "path,side,journal,year,section,design\n" + row + row)
        with self.assertRaisesRegex(ValueError, "duplicate paper"):
            load_papers(index, "Introduction", "experimental")


if __name__ == "__main__":
    unittest.main()
