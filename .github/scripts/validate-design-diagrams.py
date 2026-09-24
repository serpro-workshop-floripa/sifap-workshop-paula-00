#!/usr/bin/env python3
"""Validate that every Mermaid block in SDD packages uses the configured theme.

Each block starts with `mermaidDirective`; graph-like diagrams in the files
named by `mermaidClassFiles` carry every `mermaidClasses` line exactly once;
state, sequence, ER, and gantt diagrams carry no `classDef`; and, with
`mermaidNeutralOnly`, no chromatic color appears. Extra paths may be passed to
scan other Markdown trees.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "mermaid-theme"
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
GRAPHLIKE = ("flowchart", "graph", "classDiagram")
NON_STYLEABLE = ("sequenceDiagram", "erDiagram", "stateDiagram", "gantt")


def is_gray(value: str) -> bool:
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    r, g, b = (int(value[i:i + 2], 16) for i in (0, 2, 4))
    return max(r, g, b) - min(r, g, b) <= 8


def kind_of(body: list[str]) -> str:
    for line in body:
        stripped = line.strip()
        if stripped and not stripped.startswith("%%"):
            return stripped.split()[0]
    return "?"


def check_file(root, config, path: Path, reporter) -> int:
    blocks = sdd.mermaid_blocks(sdd.read(path))
    where = sdd.rel(root, path)
    for start, body in blocks:
        kind = kind_of(body)
        first = next((line.strip() for line in body if line.strip()), "")
        if first != config["mermaidDirective"]:
            reporter.error(CHECK, where, start, f"{kind} diagram does not start with the configured theme directive")
        text = "\n".join(body)
        if config["mermaidNeutralOnly"]:
            chromatic = [h for h in HEX.findall(text) if not is_gray(h)]
            if chromatic:
                reporter.error(CHECK, where, start, f"{kind} diagram uses chromatic color #{chromatic[0]}")
        if kind.startswith(GRAPHLIKE) and path.name in config["mermaidClassFiles"]:
            for line in config["mermaidClasses"]:
                count = sum(1 for b in body if b.strip() == line)
                if count != 1:
                    reporter.error(CHECK, where, start, f"{kind} diagram needs `{line}` exactly once (found {count})")
        elif kind.startswith(NON_STYLEABLE) and "classDef" in text:
            reporter.error(CHECK, where, start, f"classDef is invalid in {kind}")
    return len(blocks)


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    files = [p for pkg in pkgs for p in pkg.markdown_files()]
    for extra in getattr(args, "paths", None) or []:
        target = root / extra
        files += sorted(target.rglob("*.md")) if target.is_dir() else [target]
    for path in files:
        check_file(root, config, path, reporter)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mermaid theme standard.")
    sdd.common_arguments(parser)
    parser.add_argument("paths", nargs="*", help="extra Markdown files or directories to scan")
    args = parser.parse_args()
    root, config, sroot, pkgs = sdd.context(args)
    reporter = sdd.Reporter(args.strict)
    check(root, config, sroot, pkgs, reporter, args)
    sys.exit(reporter.emit(args.format, "Mermaid theme standard"))
