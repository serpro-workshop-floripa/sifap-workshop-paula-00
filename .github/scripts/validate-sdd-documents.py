#!/usr/bin/env python3
"""Validate requirement records: EARS wording, sources, acceptance, and trace.

For every package: IDs are unique and declared only in spec.md; each record
states one EARS response with a recognized pattern; a source line sits within
the configured window and resolves; acceptance IDs exist; every active
requirement is referenced by frd.md/nfrd.md (kit), plan.md, and tasks.md when
those files exist; no document references an undeclared ID.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "ears-traceability"
PATTERNS = [
    ("complex", r"^(while|enquanto|mientras)\b.*\b(when|quando|cuando)\b"),
    ("unwanted", r"^(if|se|si)\b"),
    ("event-driven", r"^(when|quando|cuando)\b"),
    ("state-driven", r"^(while|enquanto|mientras|during|durante)\b"),
    ("optional", r"^(where|onde|donde|caso)\b"),
    ("ubiquitous", r"^(the|o|a|os|as|el|la|los|las)\b"),
]
VAGUE = r"\b(fast|quick|user[- ]friendly|intuitive|robust|scalable|efficient|easy|appropriate|adequate|r[aá]pid[oa]|intuitiv[oa]|robust[oa]|f[aá]cil|adequad[oa])\b"


def ears_statement(req: sdd.Requirement, keywords: list[str]) -> tuple[int, str] | None:
    kw = "|".join(re.escape(k) for k in keywords)
    first = re.sub(rf"^.*?{re.escape(req.id)}(?:\*\*)?\s*:?(?:\*\*)?\s*", "", req.body[0]).strip()
    for offset, line in enumerate([first] + req.body[1:]):
        text = re.sub(r"^\s*(?:>\s*|[-*]\s+)?", "", line).strip()
        if re.search(rf"\b({kw})\b", text, re.I) and not re.match(r"^\s*(?:\*\*)?[A-Za-z _-]+(?:\*\*)?\s*:", text):
            return req.line + offset, text
    return None


def classify(statement: str) -> str | None:
    lowered = statement.lower()
    for name, pattern in PATTERNS:
        if re.match(pattern, lowered):
            return name
    return None


def _check_record(root, config, req, sources, reporter, seen) -> None:
    where = sdd.rel(root, req.file)
    if req.id in seen:
        reporter.error(CHECK, where, req.line, f"{req.id} is declared twice (first at line {seen[req.id]})")
        return
    seen[req.id] = req.line
    if req.status == "retired":
        return
    found = ears_statement(req, config["earsKeywords"])
    if not found:
        reporter.error(CHECK, where, req.line, f"{req.id} has no EARS statement with {'/'.join(config['earsKeywords'])}")
    else:
        line, statement = found
        count = len(re.findall(rf"\b({'|'.join(config['earsKeywords'])})\b", statement, re.I))
        if count > 1:
            reporter.error(CHECK, where, line, f"{req.id} states {count} responses; split it into atomic requirements")
        pattern = classify(statement)
        if not pattern:
            reporter.error(CHECK, where, line, f"{req.id} does not start with an EARS pattern keyword")
        elif pattern == "unwanted" and not re.search(r"\b(then|então|entonces)\b", statement, re.I):
            reporter.error(CHECK, where, line, f"{req.id} unwanted-behavior pattern needs 'then'")
        declared = re.search(r"(?:Pattern|Padr[aã]o|Patr[oó]n)\s*:\s*([A-Za-z -]+)", req.text, re.I)
        if pattern and declared and pattern.split("-")[0] not in declared.group(1).lower():
            reporter.warning(CHECK, where, line, f"{req.id} declares '{declared.group(1).strip()}' but reads as {pattern}")
        if re.search(VAGUE, statement, re.I):
            reporter.warning(CHECK, where, line, f"{req.id} uses a vague term; state a measurable response")
    src = sdd.source_lines(req, config)
    if not src:
        reporter.error(CHECK, where, req.line,
                       f"{req.id} has no {'/'.join(config['sourceKeys'][:1])}: line within {config['sourceWindow']} lines")
    for line, value, bulleted in src:
        if bulleted and config["sourceLineMustBeUnbulleted"]:
            reporter.error(CHECK, where, line, f"{req.id} source line must not be a list item")
        problem = sdd.source_value_problem(value, root, config, sources)
        if problem:
            reporter.error(CHECK, where, line, f"{req.id} source: {problem}")
    if config["requireAcceptanceIds"]:
        ac = re.compile(config["acceptanceIdPattern"].replace("{id}", re.escape(req.id)))
        if not ac.search(req.text):
            reporter.error(CHECK, where, req.line, f"{req.id} has no acceptance ID matching {config['acceptanceIdPattern']}")


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    _, reference = sdd.requirement_patterns(config)
    seen_global: dict[str, str] = {}
    all_ids = set(sdd.all_requirements(pkgs, config))
    for pkg in pkgs:
        spec = pkg.role("requirements")
        if not spec or not spec.is_file():
            continue
        spec_text = sdd.read(spec)
        sources = sdd.registered_source_ids(spec_text)
        reqs = sdd.parse_requirements(spec, config)
        seen: dict[str, int] = {}
        for req in reqs:
            if req.id in seen_global and seen_global[req.id] != pkg.name:
                reporter.error(CHECK, sdd.rel(root, spec), req.line, f"{req.id} is already declared in package {seen_global[req.id]}")
            seen_global.setdefault(req.id, pkg.name)
            _check_record(root, config, req, sources, reporter, seen)
        declared = {r.id for r in reqs}
        active = {r.id for r in reqs if r.status != "retired"}
        for path in pkg.markdown_files():
            if path == spec:
                continue
            text = sdd.read(path)
            for index, rid in sdd.declarations(text, config):
                reporter.error(CHECK, sdd.rel(root, path), index + 1,
                               f"{rid} starts a line outside {spec.name}; cite it mid-sentence or in a table cell")
            for rid in sorted(set(reference.findall(text)) - declared - all_ids):
                reporter.error(CHECK, sdd.rel(root, path), None, f"references undeclared {rid}")
        coverage = {name: active for name in sdd.COVERAGE.get(pkg.workflow, sdd.COVERAGE["spec-kit"])}
        if pkg.workflow == "kit":
            coverage["FRD.md"] = {r for r in active if r.startswith("REQ-")}
            coverage["NFRD.md"] = {r for r in active if r.startswith("NFR-")}
        for name, ids in coverage.items():
            path = pkg.path / name
            if path and path.is_file():
                missing = sorted(ids - set(reference.findall(sdd.read(path))))
                if missing:
                    reporter.error(CHECK, sdd.rel(root, path), None, "does not reference " + ", ".join(missing))


if __name__ == "__main__":
    sdd.run_main(check, "EARS requirements and traceability.")
