#!/usr/bin/env python3
"""Validate the structure and completeness of every SDD package.

Checks package naming, the file set required by each workflow (kit or
Spec-Kit) and stage, forbidden uppercase or empty artifacts, required sections
from `.github/sdd.json`, empty sections, justified NOT APPLICABLE markers,
leftover clarification markers, and a single repository constitution.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "spec-artifacts"
PLACEHOLDER = re.compile(r"<(?!!--)[A-Za-z][^<>\n]{0,60}>")


def _stage(pkg: sdd.Package, requested: str | None) -> str:
    if requested:
        return requested
    stages = sdd.KIT_STAGES if pkg.workflow == "kit" else sdd.SPEC_KIT_STAGES
    for stage in reversed(sdd.STAGE_ORDER):
        if any((pkg.path / name.rstrip("/")).exists() for name in stages[stage]):
            return stage
    return "requirements"


def _check_sections(root, config, pkg, reporter) -> None:
    required = config["requiredSections"].get(pkg.workflow, {})
    for name, sections in required.items():
        path = pkg.path / name
        if not path.is_file():
            continue
        found = [sdd.normalize_title(t) for _, level, t in sdd.headings(sdd.read(path)) if level == 2]
        positions = []
        for section in sections:
            wanted = sdd.normalize_title(section)
            index = next((i for i, t in enumerate(found) if t.startswith(wanted)), None)
            if index is None:
                reporter.error(CHECK, sdd.rel(root, path), None, f"missing required section '{section}'")
            else:
                positions.append(index)
        if positions != sorted(positions):
            reporter.warning(CHECK, sdd.rel(root, path), None, "required sections are out of template order")


def _check_bodies(root, config, path, reporter) -> None:
    text = sdd.read(path)
    lines = text.splitlines()
    heads = sdd.headings(text)
    for position, (number, level, title) in enumerate(heads):
        end = heads[position + 1][0] - 1 if position + 1 < len(heads) else len(lines)
        body = [line for line in lines[number:end] if line.strip() and not line.strip().startswith("<!--")]
        next_level = heads[position + 1][1] if position + 1 < len(heads) else 0
        if not body and (next_level == 0 or next_level <= level) and level > 1:
            reporter.error(CHECK, sdd.rel(root, path), number,
                           f"section '{title}' is empty; add content or a NOT APPLICABLE: <reason> line")
    fenced = sdd.fence_mask(lines)
    for number, line in enumerate(lines, start=1):
        prose = re.sub(r"`[^`]*`", "", line)
        if not fenced[number - 1] and PLACEHOLDER.search(prose):
            reporter.warning(CHECK, sdd.rel(root, path), number, f"unfilled template placeholder {PLACEHOLDER.search(prose).group(0)}")
        for marker in config["notApplicableMarkers"]:
            if marker.lower() in line.lower():
                tail = line.lower().split(marker.lower(), 1)[1].strip(" *_`.")
                if not tail:
                    reporter.error(CHECK, sdd.rel(root, path), number, f"'{marker}' needs a reason")
        if "[NEEDS CLARIFICATION" in line:
            reporter.warning(CHECK, sdd.rel(root, path), number, "unresolved [NEEDS CLARIFICATION] marker")


def check_constitution(root: Path, config: dict, reporter: sdd.Reporter) -> None:
    existing = [root / p for p in config["constitutionPaths"] if (root / p).is_file()]
    if not existing:
        reporter.warning(CHECK, None, None, "no constitution found at " + ", ".join(config["constitutionPaths"]))
        return
    contents = {p.resolve(): sdd.read(p) for p in existing}
    if len(set(contents.values())) > 1:
        reporter.error(CHECK, sdd.rel(root, existing[1]), None,
                       "two different constitutions exist; keep one file or symlink the other to it")


def _check_file_set(root, pkg, stage, reporter) -> None:
    where = sdd.rel(root, pkg.path)
    for name in sdd.stage_files(pkg.workflow, stage):
        target = pkg.path / name.rstrip("/")
        present = target.is_dir() if name.endswith("/") else target.is_file()
        if not present:
            reporter.error(CHECK, where, None, f"missing {name} for the {pkg.workflow} workflow at the {stage} stage")
    spec_kit_names = {"spec.md", "plan.md", "tasks.md", "research.md", "data-model.md", "quickstart.md"}
    for name, path in pkg.files.items():
        if pkg.workflow == "kit" and name in spec_kit_names:
            reporter.error(CHECK, sdd.rel(root, path), None, "Spec-Kit file inside an architect (kit) package; keep one workflow per package")
        if pkg.workflow == "spec-kit" and sdd.UPPERCASE_ARTIFACT_RE.match(name) and name != "README.md":
            reporter.error(CHECK, sdd.rel(root, path), None, "architect (kit) file inside a Spec-Kit package; keep one workflow per package")
    if pkg.workflow == "kit":
        for name in sdd.KIT_DERIVED:
            path = pkg.path / name
            if path.is_file() and "GENERATED BY" not in sdd.read(path)[:600]:
                reporter.warning(CHECK, sdd.rel(root, path), None,
                                 "derived artifact lacks the generator marker; regenerate it with generate-sdd-support-artifacts.py")
    if pkg.workflow == "spec-kit" and (pkg.path / "plan.md").is_file():
        if not (pkg.path / "data-model.md").is_file():
            reporter.warning(CHECK, where, None, "data-model.md is absent; add it or state NOT APPLICABLE in plan.md")
        if not (pkg.path / "contracts").is_dir():
            reporter.warning(CHECK, where, None, "contracts/ is absent; add contracts or contracts/README.md")


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    check_constitution(root, config, reporter)
    requested = getattr(args, "stage", None)
    for pkg in pkgs:
        where = sdd.rel(root, pkg.path)
        if pkg.name in config.get("ignorePackages", []):
            continue
        if not sdd.PACKAGE_NAME_RE.match(pkg.name):
            reporter.error(CHECK, where, None, "package folder must be <NNN>-<kebab-slug>")
        if pkg.workflow == "mixed":
            reporter.error(CHECK, where, None, "package mixes SPECIFICATION.md (architect) and spec.md (Spec-Kit); keep one workflow")
            continue
        if pkg.workflow == "undetermined":
            reporter.error(CHECK, where, None, "package has neither SPECIFICATION.md (architect) nor spec.md (Spec-Kit)")
            continue
        _check_file_set(root, pkg, _stage(pkg, requested), reporter)
        for path in pkg.markdown_files():
            if not sdd.read(path).strip():
                reporter.error(CHECK, sdd.rel(root, path), None, "file is empty")
                continue
            _check_bodies(root, config, path, reporter)
        _check_sections(root, config, pkg, reporter)


if __name__ == "__main__":
    sdd.run_main(check, "SDD artifact structure and completeness.")
