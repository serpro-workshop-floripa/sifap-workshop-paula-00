#!/usr/bin/env python3
"""Every test file a package names must exist once its task is checked.

Scans tasks.md and quickstart.md for inline-code paths that match `testGlobs`.
A path cited by a checked task or by quickstart.md must exist; a path cited by
an unchecked (planned) task may not exist yet and is only reported with
--report.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "testing-evidence"
CODE_RE = re.compile(r"`([^`\s]+\.[A-Za-z0-9]+)(?:#L\d+(?:-L\d+)?)?`")


def _is_test(path: str, config) -> bool:
    return sdd.matches_any(path, config["testGlobs"])


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    report = getattr(args, "report", False)
    for pkg in pkgs:
        tasks_path = pkg.role("tasks")
        if tasks_path and tasks_path.is_file():
            tasks, _, _ = sdd.parse_tasks(sdd.read(tasks_path), config)
            for task in tasks:
                for cited in CODE_RE.findall(task.text):
                    if not _is_test(cited, config) or "<" in cited:
                        continue
                    exists = (root / cited).exists()
                    if task.checked and not exists:
                        reporter.error(CHECK, sdd.rel(root, tasks_path), task.line,
                                       f"{task.id} is checked but cites missing test file {cited}")
                    elif report:
                        print(f"{pkg.name} {task.id} {cited}: {'present' if exists else 'planned'}")
        quick = pkg.role("testing")
        if quick and quick.is_file():
            for number, line in enumerate(sdd.read(quick).splitlines(), start=1):
                for cited in CODE_RE.findall(line):
                    if _is_test(cited, config) and "<" not in cited and not (root / cited).exists():
                        reporter.warning(CHECK, sdd.rel(root, quick), number, f"cites missing test file {cited}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test files named by SDD packages.")
    sdd.common_arguments(parser)
    parser.add_argument("--report", action="store_true", help="list every cited test file")
    args = parser.parse_args()
    root, config, sroot, pkgs = sdd.context(args)
    reporter = sdd.Reporter(args.strict)
    if not pkgs:
        print("No SDD packages yet; nothing to check.")
        sys.exit(0)
    check(root, config, sroot, pkgs, reporter, args)
    sys.exit(reporter.emit(args.format, "Testing evidence"))
