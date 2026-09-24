#!/usr/bin/env python3
"""Scaffold an architect SDD package, or export the unapproved template library.

    python3 .github/scripts/export-spec-library.py --new-package 002-benefit-query
    python3 .github/scripts/export-spec-library.py --export <new-directory>

`--new-package` writes every authored artifact of an architect (kit) package
into `<spec root>/<NNN>-<slug>/` from the templates in the
sdd-requirements-engineer skill, fills the feature id and slug, and never
overwrites an existing file. Generated artifacts (CHECKLIST, CROSS_ANALYSIS,
VERIFICATION, SOURCE_TRACEABILITY, TDD) are produced afterwards by
generate-sdd-support-artifacts.py once the checkpoints are complete.

`--export` copies the templates and references into a new, versioned directory
for another repository. Nothing is published, approved, or overwritten.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

REFERENCES = Path(__file__).resolve().parents[1] / "skills/sdd-requirements-engineer/references"
AUTHORED = (
    "SPECIFICATION.md", "ANALYSIS.md", "DESIGN.md", "DECISIONS.md", "TASKS.md", "TESTING.md",
    "checkpoints/spec-to-plan.yaml", "checkpoints/plan-to-tasks.yaml", "checkpoints/test-coverage.yaml",
    "contracts/manifest.yaml", "evidence/README.md",
)
GENERATED = ("CHECKLIST.md", "CROSS_ANALYSIS.md", "VERIFICATION.md", "SOURCE_TRACEABILITY.md", "TDD.md")
SEPARATE = {"FRD.md": "frd-template.md", "NFRD.md": "nfrd-template.md"}


def extract(text: str, heading: str | None = None) -> str:
    if heading:
        marker = f"\n## {heading}\n"
        if marker not in text:
            raise ValueError(f"missing template section '## {heading}'")
        text = text.split(marker, 1)[1]
    match = re.search(r"^(`{3,})(markdown|yaml)\n", text, re.M)
    if match is None:
        raise ValueError(f"missing template fence for {heading}")
    end = re.search(r"^" + re.escape(match[1]) + r"$", text[match.end():], re.M)
    if end is None:
        raise ValueError(f"unterminated template for {heading}")
    return text[match.end():match.end() + end.start()].rstrip() + "\n"


def templates(include_generated: bool) -> dict[str, str]:
    source = (REFERENCES / "spec-templates.md").read_text(encoding="utf-8")
    names = list(AUTHORED) + (list(GENERATED) + ["CONSTITUTION.md"] if include_generated else [])
    files = {name: extract(source, name) for name in names}
    for name, reference in SEPARATE.items():
        files[name] = extract((REFERENCES / reference).read_text(encoding="utf-8"))
    return files


def new_package(name: str) -> int:
    match = re.fullmatch(r"(\d{3,})-([a-z0-9]+(?:-[a-z0-9]+)*)", name)
    if not match:
        print("package name must be <NNN>-<kebab-slug>", file=sys.stderr)
        return 2
    feature_id, slug = match.groups()
    root = sdd.repo_root()
    config = sdd.load_config(root)
    target = sdd.spec_root(root, config) / name
    written = []
    for relative, content in templates(include_generated=False).items():
        content = content.replace("<NNN>-<feature>", name).replace('"<NNN>"', f'"{feature_id}"')
        content = content.replace("slug: <feature>", f"slug: {slug}")
        path = target / relative
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        written.append(sdd.rel(root, path))
    constitution = sdd.spec_root(root, config) / "CONSTITUTION.md"
    if not any((root / p).is_file() for p in config["constitutionPaths"]):
        constitution.write_text(extract((REFERENCES / "spec-templates.md").read_text(encoding="utf-8"),
                                        "CONSTITUTION.md"), encoding="utf-8")
        written.append(sdd.rel(root, constitution))
    for path in written:
        print(f"created {path}")
    print(f"Scaffolded {name}: {len(written)} file(s). Fill every placeholder, then run "
          f"generate-sdd-support-artifacts.py --package {feature_id} --include-supplements.")
    return 0


def export(destination: Path) -> int:
    if destination.exists():
        print("destination exists; choose a new versioned directory", file=sys.stderr)
        return 2
    warning = "> UNAPPROVED AUTHORING TEMPLATE. Replace every placeholder with project evidence.\n\n"
    files = {k: (warning + v if k.endswith(".md") else v) for k, v in templates(include_generated=True).items()}
    for path in sorted(REFERENCES.glob("*.md")):
        files[f"references/{path.name}"] = path.read_text(encoding="utf-8")
    files["template-manifest.json"] = json.dumps({
        "schema_version": "1.0",
        "status": "unapproved_authoring_template",
        "files": {p: hashlib.sha256(c.encode("utf-8")).hexdigest() for p, c in sorted(files.items())},
    }, indent=2, sort_keys=True) + "\n"
    for name, content in files.items():
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Exported {len(files)} template file(s) to {destination}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--new-package", metavar="NNN-slug")
    group.add_argument("--export", type=Path, metavar="DIRECTORY")
    args = parser.parse_args()
    try:
        return new_package(args.new_package) if args.new_package else export(args.export)
    except ValueError as exc:
        print(f"template error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
