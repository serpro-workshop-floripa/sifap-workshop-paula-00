#!/usr/bin/env python3
"""Bind requirements to automated tests in both directions.

Every active requirement should be cited (`// REQ-NNN`) by at least one test
file matched by `testGlobs`; every ID a test cites must be declared in a
package. Missing bindings are warnings until implementation starts (a checked
task exists) and errors afterwards. Use --report to list each binding.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "test-bindings"


def bindings(root, config) -> dict[str, set[str]]:
    _, reference = sdd.requirement_patterns(config)
    result: dict[str, set[str]] = {}
    for name in sdd.test_files(root, config):
        for rid in reference.findall(sdd.read(root / name)):
            result.setdefault(rid, set()).add(name)
    return result


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    found = bindings(root, config)
    declared = sdd.all_requirements(pkgs, config)
    for rid, files in sorted(found.items()):
        if rid not in declared:
            for name in sorted(files):
                reporter.error(CHECK, name, None, f"cites {rid}, which no package declares")
    for pkg in pkgs:
        tasks_path = pkg.role("tasks")
        started = False
        if tasks_path and tasks_path.is_file():
            started = any(t.checked for t in sdd.parse_tasks(sdd.read(tasks_path), config)[0])
        spec = pkg.role("requirements")
        if not spec or not spec.is_file():
            continue
        for req in sdd.parse_requirements(spec, config):
            if req.status == "retired" or req.id in found:
                continue
            level = "error" if started else "warning"
            reporter.add(level, CHECK, sdd.rel(root, spec), req.line, f"{req.id} is not cited by any test file")
    if getattr(args, "report", False):
        for rid in sorted(declared):
            print(f"{rid}: {', '.join(sorted(found.get(rid, []))) or '(none)'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Requirement-to-test bindings.")
    sdd.common_arguments(parser)
    parser.add_argument("--report", action="store_true", help="print every requirement and its test files")
    args = parser.parse_args()
    root, config, sroot, pkgs = sdd.context(args)
    reporter = sdd.Reporter(args.strict)
    if not pkgs:
        print("No SDD packages yet; nothing to bind.")
        sys.exit(0)
    check(root, config, sroot, pkgs, reporter, args)
    sys.exit(reporter.emit(args.format, "Requirement-to-test bindings"))
