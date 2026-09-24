#!/usr/bin/env python3
"""Validate that declared statuses never exceed their evidence.

A package or requirement may claim Implemented only when tasks.md exists and
every task is checked and in the verification ledger; Verified additionally
needs every active requirement bound to at least one test file. Unknown status
values are errors, and an Approved claim needs a recorded approver.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "spec-status"


def _evidence(pkg, config) -> tuple[bool, str]:
    path = pkg.role("tasks")
    if not path or not path.is_file():
        return False, "tasks.md does not exist"
    tasks, ledger, _ = sdd.parse_tasks(sdd.read(path), config)
    if not tasks:
        return False, "tasks.md has no tasks"
    open_tasks = [t.id for t in tasks if not t.checked or t.id not in ledger]
    if open_tasks:
        return False, "tasks without ledger evidence: " + ", ".join(open_tasks[:8])
    return True, ""


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    _, reference = sdd.requirement_patterns(config)
    tests = sdd.test_files(root, config)
    bound: set[str] = set()
    for name in tests:
        bound |= set(reference.findall(sdd.read(root / name)))
    for pkg in pkgs:
        spec = pkg.role("requirements")
        if not spec or not spec.is_file():
            continue
        where = sdd.rel(root, spec)
        text = sdd.read(spec)
        status, line = sdd.document_status(text)
        if line and status is None:
            reporter.error(CHECK, where, line, "unrecognized status value")
        if status is None and line is None:
            reporter.warning(CHECK, where, None, "no document Status declared")
        reqs = sdd.parse_requirements(spec, config)
        claims = [(status, line, "package")] + [(r.status, r.line, r.id) for r in reqs]
        complete, why = _evidence(pkg, config)
        for value, at, who in claims:
            rank = sdd.STATUS_RANK.get(value or "draft", 0)
            if rank >= sdd.STATUS_RANK["implemented"] and not complete:
                reporter.error(CHECK, where, at, f"{who} claims {value} but {why}")
            if value == "verified":
                ids = [r.id for r in reqs if r.status != "retired"] if who == "package" else [who]
                unbound = [i for i in ids if i not in bound]
                if unbound:
                    reporter.error(CHECK, where, at, f"{who} claims verified but no test references " + ", ".join(unbound))
            if value == "approved" and not re.search(r"(Approved by|Aprovado por|Aprobado por|Approver|Aprovador)", text, re.I):
                reporter.warning(CHECK, where, at, f"{who} claims approved without a recorded approver")


if __name__ == "__main__":
    sdd.run_main(check, "Honest specification status.")
