#!/usr/bin/env python3
"""Audit the evidence behind checked tasks; reference integrity only.

A checked task must carry an `Evidence:` line that cites at least one existing
file (usually under the package `evidence/` folder) or an https URL, and every
repository path in its `Files:` line must exist. Evidence files under
`evidence/` must be referenced by some task. This proves that claimed evidence
is present and linked, not that the recorded run actually passed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "task-evidence"
CODE = re.compile(r"`([^`\s]+)`")
LINK = re.compile(r"\]\(([^)\s]+)\)")
URL = re.compile(r"https://\S+")
LABEL = re.compile(r"^(Evidence|Evidência|Evidencia|Files|Arquivos|Archivos)\s*:\s*(.*)$", re.I)


def _cited(value: str) -> list[str]:
    return CODE.findall(value) + LINK.findall(value)


def _exists(root: Path, pkg: sdd.Package, ref: str) -> bool:
    target = ref.split("#", 1)[0]
    return (pkg.path / target).exists() or (root / target).exists()


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    for pkg in pkgs:
        tasks_path = pkg.role("tasks")
        if not tasks_path:
            continue
        where = sdd.rel(root, tasks_path)
        tasks, _, _ = sdd.parse_tasks(sdd.read(tasks_path), config)
        referenced: set[str] = set()
        for task in tasks:
            fields: dict[str, str] = {}
            for line in task.text.splitlines()[1:]:
                m = LABEL.match(line.lstrip("-* ").strip())
                if m:
                    key = m.group(1).lower()
                    fields["evidence" if key.startswith("evid") else "files"] = m.group(2)
            evidence = fields.get("evidence", "")
            for ref in _cited(evidence):
                referenced.add(ref.split("#", 1)[0])
            if not task.checked:
                continue
            refs = _cited(evidence)
            if not refs and not URL.search(evidence):
                reporter.error(CHECK, where, task.line, f"{task.id} is checked without an Evidence: line citing a file or URL")
            for ref in refs:
                if "://" not in ref and not _exists(root, pkg, ref):
                    reporter.error(CHECK, where, task.line, f"{task.id} cites missing evidence {ref}")
            for ref in _cited(fields.get("files", "")):
                if "<" not in ref and not _exists(root, pkg, ref):
                    reporter.error(CHECK, where, task.line, f"{task.id} is checked but its file {ref} does not exist")
        folder = pkg.path / "evidence"
        if folder.is_dir():
            for item in sorted(p for p in folder.rglob("*") if p.is_file() and p.name != "README.md"):
                local = item.relative_to(pkg.path).as_posix()
                if local not in referenced and sdd.rel(root, item) not in referenced:
                    reporter.warning(CHECK, sdd.rel(root, item), None, "evidence file is not cited by any task")


if __name__ == "__main__":
    sdd.run_main(check, "Task evidence audit.")
