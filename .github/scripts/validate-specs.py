#!/usr/bin/env python3
"""Run every SDD gate, plus checkpoint and contract closure for architect packages.

    python3 .github/scripts/validate-specs.py [--package 001] [--strict]

Architect (kit) packages must close their identifiers across artifacts:
SPECIFICATION.md requirements equal the requirement maps in
checkpoints/spec-to-plan.yaml and test-coverage.yaml; tasks declared in TASKS.md
equal the tasks in plan-to-tasks.yaml; tests in test-coverage.yaml are declared
in TESTING.md; checkpoint feature.id/slug match the folder; and
contracts/manifest.yaml accounts for every contract file, each either provided
(present and well-formed) or not_applicable (with a reason, evidence path, and
a DR-NNN recorded in DECISIONS.md).

The umbrella then runs structure, EARS/traceability, task graph/TDD, status,
test bindings, testing evidence, and Mermaid checks. Spec-Kit packages get
every gate except checkpoint closure.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sdd_lib as sdd  # noqa: E402

CHECK = "checkpoints"
GATES = [
    "validate-spec-artifacts",
    "validate-sdd-documents",
    "validate-task-graph",
    "validate-spec-status",
    "validate-test-bindings",
    "validate-testing-evidence",
    "validate-design-diagrams",
]
TASK_DECL = re.compile(r"^\s*[-*]\s+\[[ xX]\]\s+(?:\*\*)?(T\d{3,})\b|^#{2,6}\s+(T\d{3,})\b", re.M)
TEST_DECL = re.compile(r"^\|\s*(TST-[A-Z]*\d{3,})\s*\|", re.M)
DECISION_ID = re.compile(r"DR-\d{3,}")
WAIVER_REASON_MIN = 40


def _load(module: str):
    spec = importlib.util.spec_from_file_location(module.replace("-", "_"), HERE / f"{module}.py")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def _contracts(root, pkg, reporter, prefix, slug) -> None:
    where = sdd.rel(root, pkg.path / "contracts/manifest.yaml")
    manifest = sdd.load_yaml(pkg.path / "contracts/manifest.yaml", reporter, CHECK, where)
    if manifest is None:
        return
    feature = manifest.get("feature") or {}
    if (str(feature.get("id")), feature.get("slug")) != (prefix, slug):
        reporter.error(CHECK, where, None, f"feature id/slug must be {prefix}/{slug}")
    declared = manifest.get("contracts")
    if not isinstance(declared, dict) or not declared:
        reporter.error(CHECK, where, None, "'contracts' must map each contract file name to a declaration")
        return
    files = {p.name for p in (pkg.path / "contracts").iterdir() if p.is_file() and p.name not in {"manifest.yaml", "README.md"}}
    for name in sorted(files - set(declared)):
        reporter.error(CHECK, where, None, f"contracts/{name} is not declared in the manifest")
    decisions = pkg.text("DECISIONS.md")
    statuses = []
    for name, entry in declared.items():
        entry = entry or {}
        status = entry.get("status")
        statuses.append(status)
        path = pkg.path / "contracts" / name
        if status == "provided":
            if not path.is_file():
                reporter.error(CHECK, where, None, f"{name} is provided but absent")
                continue
            _contract_shape(root, path, reporter)
        elif status == "not_applicable":
            if path.is_file():
                reporter.error(CHECK, where, None, f"{name} is not_applicable but the file is present")
            if len(str(entry.get("reason", "")).strip()) < WAIVER_REASON_MIN:
                reporter.error(CHECK, where, None, f"{name} needs a reason of at least {WAIVER_REASON_MIN} characters")
            evidence = str(entry.get("evidence", "")).strip()
            if not evidence or not (root / evidence).exists():
                reporter.error(CHECK, where, None, f"{name} needs an existing repository 'evidence' path")
            decision = str(entry.get("decision", "")).strip()
            if not DECISION_ID.fullmatch(decision) or decision not in decisions:
                reporter.error(CHECK, where, None, f"{name} needs a DR-NNN 'decision' recorded in DECISIONS.md")
        else:
            reporter.error(CHECK, where, None, f"{name} status must be provided or not_applicable")
    if statuses and all(s == "not_applicable" for s in statuses) and len(statuses) > 1:
        reporter.warning(CHECK, where, None, "every contract is waived; confirm the feature exposes no interface")


def _contract_shape(root, path, reporter) -> None:
    where = sdd.rel(root, path)
    if path.suffix == ".json":
        try:
            doc = json.loads(sdd.read(path))
        except json.JSONDecodeError as exc:
            reporter.error(CHECK, where, None, f"invalid JSON: {exc}")
            return
        if path.name.endswith(".schema.json") and not any(k in doc for k in ("properties", "$defs", "oneOf", "type")):
            reporter.error(CHECK, where, None, "not an object schema")
    elif path.suffix in {".yaml", ".yml"}:
        doc = sdd.load_yaml(path, reporter, CHECK, where)
        if isinstance(doc, dict) and "openapi" in doc:
            for key in ("info", "paths"):
                if key not in doc:
                    reporter.error(CHECK, where, None, f"OpenAPI document lacks '{key}'")


def _closure(root, config, pkg, reporter) -> None:
    m = re.match(r"^(\d{3,})-(.+)$", pkg.name)
    if not m:
        return
    prefix, slug = m.groups()
    docs = {}
    for name in ("spec-to-plan", "plan-to-tasks", "test-coverage"):
        path = pkg.path / "checkpoints" / f"{name}.yaml"
        if not path.is_file():
            return
        doc = sdd.load_yaml(path, reporter, CHECK, sdd.rel(root, path))
        if not isinstance(doc, dict):
            return
        docs[name] = doc
        feature = doc.get("feature") or {}
        if (str(feature.get("id")), feature.get("slug")) != (prefix, slug):
            reporter.error(CHECK, sdd.rel(root, path), None, f"feature id/slug must be {prefix}/{slug}")
        if (doc.get("checkpoint") or {}).get("mapping_status") != "complete":
            reporter.warning(CHECK, sdd.rel(root, path), None, "mapping_status is not 'complete'")
    spec = pkg.role("requirements")
    reqs = {r.id for r in sdd.parse_requirements(spec, config)} if spec else set()
    tasks = {a or b for a, b in TASK_DECL.findall(pkg.text("TASKS.md"))}
    tests = set(TEST_DECL.findall(pkg.text("TESTING.md")))
    sp = set((docs["spec-to-plan"].get("requirements") or {}))
    tc = docs["test-coverage"].get("requirements") or {}
    items = (docs["plan-to-tasks"].get("plan_items") or {}).values()
    pt_reqs = {r for item in items for r in (item or {}).get("requirements", [])}
    pt_tasks = {t for item in items for t in (item or {}).get("tasks", [])}
    tc_tests = {t for entry in tc.values() for t in (entry or {}).get("tests", [])}
    where = sdd.rel(root, pkg.path / "checkpoints")
    for label, diff in (
        ("spec-to-plan names undeclared requirements", sp - reqs),
        ("requirements missing from spec-to-plan", reqs - sp),
        ("requirements missing from test-coverage", reqs - set(tc)),
        ("test-coverage names undeclared requirements", set(tc) - reqs),
        ("plan-to-tasks names undeclared requirements", pt_reqs - reqs),
        ("plan-to-tasks names tasks absent from TASKS.md", pt_tasks - tasks),
        ("tasks never mapped by plan-to-tasks", tasks - pt_tasks),
        ("test-coverage names tests absent from TESTING.md", tc_tests - tests),
    ):
        if diff:
            reporter.error(CHECK, where, None, f"{label}: {', '.join(sorted(diff))}")
    if "gate" not in docs["plan-to-tasks"]:
        reporter.warning(CHECK, where, None, "plan-to-tasks.yaml has no 'gate' block")
    _contracts(root, pkg, reporter, prefix, slug)


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    for pkg in pkgs:
        if pkg.workflow == "kit" and pkg.name not in config.get("ignorePackages", []):
            _closure(root, config, pkg, reporter)


def main() -> int:
    parser = argparse.ArgumentParser(description="All SDD gates.")
    sdd.common_arguments(parser)
    parser.add_argument("--only", action="append", choices=GATES + ["checkpoints"], help="run only these gates")
    args = parser.parse_args()
    args.paths, args.report = [], False
    root, config, sroot, pkgs = sdd.context(args)
    pkgs = [p for p in pkgs if p.name not in config.get("ignorePackages", [])]
    if not pkgs:
        print(f"No SDD packages under {sdd.rel(root, sroot)}/ yet; nothing to validate.")
        return 0
    reporter = sdd.Reporter(args.strict)
    selected = args.only or GATES + ["checkpoints"]
    for gate in GATES:
        if gate in selected:
            _load(gate).check(root, config, sroot, pkgs, reporter, args)
    if "checkpoints" in selected:
        check(root, config, sroot, pkgs, reporter, args)
    kinds = ", ".join(f"{p.name} ({p.workflow})" for p in pkgs)
    print(f"Packages: {kinds}")
    return reporter.emit(args.format, "SDD gates")


if __name__ == "__main__":
    sys.exit(main())
