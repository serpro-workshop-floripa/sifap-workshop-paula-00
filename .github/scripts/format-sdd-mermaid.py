#!/usr/bin/env python3
"""Apply the configured Mermaid theme to SDD package diagrams.

Replaces or inserts the `mermaidDirective` as the first line of every Mermaid
block, removes other `%%{init}` lines, and adds missing `mermaidClasses` to
graph-like diagrams in `mermaidClassFiles`. With --check, only reports which
files would change.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

BLOCK = re.compile(r"(?P<open>^(?P<fence>`{3,}|~{3,})mermaid[^\n]*\n)(?P<body>.*?)(?P<close>^(?P=fence)\s*$)",
                   re.M | re.S)
GRAPHLIKE = ("flowchart", "graph", "classDiagram")


def format_body(body: str, config: dict, needs_classes: bool) -> str:
    lines = [line for line in body.splitlines() if not line.strip().startswith("%%{")]
    kind_index = next((i for i, line in enumerate(lines) if line.strip()), None)
    result = [config["mermaidDirective"]] + lines
    if needs_classes and kind_index is not None and lines[kind_index].strip().startswith(GRAPHLIKE):
        existing = {line.strip() for line in lines}
        missing = ["  " + c for c in config["mermaidClasses"] if c not in existing]
        result = [config["mermaidDirective"], lines[kind_index]] + missing + lines[kind_index + 1:]
    return "\n".join(result) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Mermaid theme formatter.")
    sdd.common_arguments(parser)
    parser.add_argument("--check", action="store_true", help="report files that would change")
    args = parser.parse_args()
    root, config, sroot, pkgs = sdd.context(args)
    changed = []
    for pkg in pkgs:
        for path in pkg.markdown_files():
            text = sdd.read(path)
            needs = path.name in config["mermaidClassFiles"]
            new = BLOCK.sub(lambda m: m["open"] + format_body(m["body"], config, needs) + m["close"], text)
            if new != text:
                changed.append(sdd.rel(root, path))
                if not args.check:
                    path.write_text(new, encoding="utf-8")
    for name in changed:
        print(("would format " if args.check else "formatted ") + name)
    print(f"Mermaid theme formatter: {len(changed)} file(s) {'need formatting' if args.check else 'formatted'}")
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
