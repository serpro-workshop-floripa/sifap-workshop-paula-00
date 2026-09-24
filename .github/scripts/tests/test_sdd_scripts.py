"""Regression tests for the portable SDD, EARS, and TDD gates.

Each test copies the reference fixture into a scratch repository, applies one
mutation, and asserts the gate that owns the rule fails (or that the untouched
fixture passes every gate).

    python3 -m unittest discover -s .github/scripts/tests -v
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "kit-repo"
PACKAGE = ".spec/001-sample-feature"


class GateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.repo = self.tmp / "repo"
        shutil.copytree(FIXTURE, self.repo)
        self.pkg = self.repo / PACKAGE

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_script(self, name: str, *args: str) -> subprocess.CompletedProcess:
        env = dict(os.environ, SDD_REPO_ROOT=str(self.repo))
        return subprocess.run([sys.executable, str(SCRIPTS / name), *args], cwd=self.repo, env=env,
                              capture_output=True, text=True, check=False)

    def edit(self, name: str, old: str, new: str) -> None:
        path = self.pkg / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture drifted: {old!r} not in {name}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assertFails(self, result: subprocess.CompletedProcess, fragment: str) -> None:
        self.assertNotEqual(0, result.returncode,
                            result.stdout + result.stderr)
        self.assertIn(fragment, result.stdout + result.stderr)

    def test_reference_fixture_passes_every_gate(self) -> None:
        result = self.run_script("validate-specs.py", "--strict")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        for script in ("audit-task-evidence.py", "validate-test-bindings.py"):
            self.assertEqual(0, self.run_script(script).returncode, script)
        check = self.run_script(
            "generate-sdd-support-artifacts.py", "--include-supplements", "--check")
        self.assertEqual(0, check.returncode, check.stdout + check.stderr)

    def test_missing_architect_artifact_fails(self) -> None:
        (self.pkg / "DESIGN.md").unlink()
        self.assertFails(self.run_script(
            "validate-spec-artifacts.py"), "missing DESIGN.md")

    def test_missing_evidence_folder_fails(self) -> None:
        shutil.rmtree(self.pkg / "evidence")
        self.assertFails(self.run_script(
            "validate-spec-artifacts.py"), "missing evidence/")

    def test_spec_kit_file_inside_architect_package_fails(self) -> None:
        (self.pkg / "plan.md").write_text("# Plan\n\nText.\n", encoding="utf-8")
        self.assertFails(self.run_script(
            "validate-spec-artifacts.py"), "Spec-Kit file inside")

    def test_empty_section_fails(self) -> None:
        self.edit("DESIGN.md", "NOT APPLICABLE: validation is stateless.\n", "")
        self.assertFails(self.run_script(
            "validate-spec-artifacts.py"), "section 'State Model' is empty")

    def test_compound_ears_statement_fails(self) -> None:
        self.edit("SPECIFICATION.md", "shall reject it with error code DOC-01.",
                  "shall reject it and shall log the attempt.")
        self.assertFails(self.run_script(
            "validate-sdd-documents.py"), "split it into atomic requirements")

    def test_missing_ears_trigger_fails(self) -> None:
        self.edit("SPECIFICATION.md", "When a clerk submits", "Clerks submit")
        self.assertFails(self.run_script(
            "validate-sdd-documents.py"), "EARS pattern keyword")

    def test_unresolvable_source_fails(self) -> None:
        self.edit("SPECIFICATION.md",
                  "docs/requirements.md#L3", "docs/missing.md")
        self.assertFails(self.run_script(
            "validate-sdd-documents.py"), "does not exist")

    def test_line_anchor_beyond_file_fails(self) -> None:
        self.edit("SPECIFICATION.md", "docs/requirements.md#L3",
                  "docs/requirements.md#L90")
        self.assertFails(self.run_script(
            "validate-sdd-documents.py"), "points beyond")

    def test_declaration_outside_specification_fails(self) -> None:
        self.edit("DESIGN.md", "## Architecture Overview\n",
                  "## Architecture Overview\n\nREQ-001: duplicated.\n")
        self.assertFails(self.run_script(
            "validate-sdd-documents.py"), "starts a line outside")

    def test_missing_acceptance_id_fails(self) -> None:
        self.edit("SPECIFICATION.md", "AC-REQ-001-01", "Scenario")
        self.assertFails(self.run_script(
            "validate-sdd-documents.py"), "no acceptance ID")

    def test_green_before_red_fails(self) -> None:
        text = (self.pkg / "TASKS.md").read_text(encoding="utf-8")
        text = text.replace("[Plan:P1.1] RED", "[Plan:P1.1] XRED").replace(
            "[Plan:P1.1] GREEN", "[Plan:P1.1] RED")
        (self.pkg / "TASKS.md").write_text(text.replace("XRED", "GREEN"), encoding="utf-8")
        self.assertFails(self.run_script(
            "validate-task-graph.py"), "precedes its RED task")

    def test_checked_task_without_ledger_fails(self) -> None:
        self.edit("TASKS.md", "- [ ] **T001", "- [x] **T001")
        self.assertFails(self.run_script(
            "validate-task-graph.py"), "missing from the")

    def test_checked_task_without_evidence_fails(self) -> None:
        self.edit("TASKS.md", "- [ ] **T001", "- [x] **T001")
        self.assertFails(self.run_script(
            "audit-task-evidence.py"), "without an Evidence")

    def test_status_beyond_evidence_fails(self) -> None:
        self.edit("SPECIFICATION.md", 'status: "Draft"',
                  'status: "Implemented"')
        self.assertFails(self.run_script(
            "validate-spec-status.py"), "claims implemented")

    def test_checkpoint_gap_fails(self) -> None:
        self.edit("checkpoints/spec-to-plan.yaml",
                  "  NFR-001: {design_components: [C-01], plan_items: [P1.2]}\n", "")
        self.assertFails(self.run_script("validate-specs.py",
                         "--only", "checkpoints"), "missing from spec-to-plan")

    def test_undeclared_contract_file_fails(self) -> None:
        (self.pkg / "contracts/extra.schema.json").write_text("{}", encoding="utf-8")
        self.assertFails(self.run_script("validate-specs.py",
                         "--only", "checkpoints"), "not declared")

    def test_chromatic_mermaid_color_fails(self) -> None:
        self.edit("DESIGN.md", "classDef zone fill:#FFFFFF",
                  "classDef zone fill:#FF0000")
        self.assertFails(self.run_script(
            "validate-design-diagrams.py"), "chromatic color")

    def test_stale_generated_artifact_fails(self) -> None:
        self.edit("SPECIFICATION.md", "Invalid documents corrupt",
                  "Invalid documents damage")
        result = self.run_script(
            "generate-sdd-support-artifacts.py", "--include-supplements", "--check")
        self.assertFails(result, "stale")

    def test_test_citing_undeclared_requirement_fails(self) -> None:
        (self.repo / "tests/test_orphan.py").write_text(
            "def test_x():  # REQ-999\n    pass\n", encoding="utf-8")
        self.assertFails(self.run_script(
            "validate-test-bindings.py"), "REQ-999")

    def test_spec_kit_package_is_recognized(self) -> None:
        pkg = self.repo / ".spec/002-spec-kit-feature"
        pkg.mkdir()
        (pkg / "spec.md").write_text(
            "# Spec\n\n## Requirements\n\n### REQ-201\n\nWhen a user asks, the service shall answer.\n\n"
            "source_legacy: docs/requirements.md\n\n- AC-REQ-201-01: Given x, When y, Then z.\n",
            encoding="utf-8")
        result = self.run_script(
            "validate-spec-artifacts.py", "--package", "002")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        (pkg / "DESIGN.md").write_text("# Design\n\nText.\n", encoding="utf-8")
        self.assertFails(self.run_script(
            "validate-spec-artifacts.py", "--package", "002"), "architect (kit) file")
        (pkg / "SPECIFICATION.md").write_text("# Specification\n\nText.\n", encoding="utf-8")
        self.assertFails(self.run_script(
            "validate-spec-artifacts.py", "--package", "002"), "mixes")

    def test_scaffold_creates_every_authored_file(self) -> None:
        result = self.run_script(
            "export-spec-library.py", "--new-package", "003-new-feature")
        self.assertEqual(0, result.returncode, result.stderr)
        created = self.repo / ".spec/003-new-feature"
        for name in ("FRD.md", "NFRD.md", "SPECIFICATION.md", "ANALYSIS.md", "DESIGN.md", "DECISIONS.md",
                     "TASKS.md", "TESTING.md", "checkpoints/spec-to-plan.yaml", "contracts/manifest.yaml",
                     "evidence/README.md"):
            self.assertTrue((created / name).is_file(), name)
        self.assertFails(self.run_script("validate-spec-artifacts.py", "--package", "003", "--stage", "complete"), "SOURCE_TRACEABILITY.md")

    def test_red_phase_requires_a_real_failure(self) -> None:
        failing = self.run_script(
            "validate-red-phase.py", "--", sys.executable, "-c", "import sys; sys.exit(1)")
        self.assertEqual(0, failing.returncode, failing.stderr)
        passing = self.run_script(
            "validate-red-phase.py", "--", sys.executable, "-c", "pass")
        self.assertFails(passing, "tests passed")
        runner = self.run_script(
            "validate-red-phase.py", "--", sys.executable, "-c", "import sys; sys.exit(5)")
        self.assertFails(runner, "runner error")


if __name__ == "__main__":
    unittest.main()
