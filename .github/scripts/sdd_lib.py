"""Shared, repository-agnostic model of Spec-Driven Development packages.

Every SDD script imports this module. It discovers the repository root from the
current working directory, loads an optional `.github/sdd.json` (or `.sdd.json`)
configuration, finds feature packages under the specification root, and parses
requirements, tasks, statuses, and Mermaid blocks. Defaults work in any
repository; the configuration only narrows them.

Two package workflows are recognized:

* kit (architect prompts and skill): FRD.md, NFRD.md, SPECIFICATION.md,
  SOURCE_TRACEABILITY.md, ANALYSIS.md, DESIGN.md, DECISIONS.md, TASKS.md,
  TDD.md, TESTING.md, CHECKLIST.md, CROSS_ANALYSIS.md, VERIFICATION.md,
  checkpoints/, contracts/, evidence/;
* spec-kit (GitHub Spec-Kit commands): spec.md, plan.md, tasks.md,
  research.md, data-model.md, contracts/, quickstart.md, checklists/.
"""

from __future__ import annotations

import fnmatch
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_CONFIG: dict = {
    "specRoot": None,
    "specRootCandidates": [".spec", ".specs", "specs"],
    "requirementIdPattern": r"(?:REQ|NFR)-\d{3,}",
    "acceptanceIdPattern": r"AC-{id}-\d{2}",
    "sourceKeys": ["source_legacy", "source", "origem", "origen"],
    "sourceLineMustBeUnbulleted": True,
    "sourcePathPatterns": [],
    "sourceWindow": 20,
    "greenfieldMarker": "[GREENFIELD]",
    "earsKeywords": ["shall", "deve", "debe"],
    "requireAcceptanceIds": True,
    "tdd": "auto",
    "testGlobs": [
        "**/src/test/**",
        "**/*.test.*",
        "**/*.spec.*",
        "**/test_*.py",
        "**/*_test.*",
        "**/tests/**",
        "**/__tests__/**",
    ],
    "ignoreGlobs": ["**/node_modules/**", "**/.git/**", "**/target/**", "**/.venv/**", "**/dist/**"],
    "constitutionPaths": [".spec/CONSTITUTION.md", ".specify/memory/constitution.md"],
    "stage": "complete",
    "mermaidDirective": (
        "%%{init: {'theme':'neutral','themeVariables':{'fontFamily':'ui-sans-serif, system-ui, sans-serif',"
        "'primaryColor':'#F5F5F5','primaryTextColor':'#171717','primaryBorderColor':'#171717',"
        "'lineColor':'#525252','secondaryColor':'#FFFFFF','tertiaryColor':'#FAFAFA','background':'#FFFFFF'}}}%%"
    ),
    "mermaidClasses": [
        "classDef default fill:#F5F5F5,stroke:#171717,color:#171717",
        "classDef zone fill:#FFFFFF,stroke:#525252,color:#171717",
        "classDef external fill:#FAFAFA,stroke:#A3A3A3,color:#404040",
    ],
    "mermaidClassFiles": ["DESIGN.md", "TASKS.md", "TDD.md", "plan.md", "tasks.md"],
    "mermaidNeutralOnly": True,
    "notApplicableMarkers": ["NOT APPLICABLE:", "NÃO APLICÁVEL:", "NO APLICA:"],
    "workflows": ["kit", "spec-kit"],
    "ignorePackages": [],
    "generatedAuthor": "Specification team",
    # Section order of the architect templates in the sdd-requirements-engineer skill.
    "requiredSections": {
        "kit": {
            "FRD.md": ["Document control", "Problem and outcomes", "Scope", "Actors and permissions",
                       "Domain model and lifecycle", "Functional requirements", "External interactions",
                       "Requirement summary", "Delivery increments", "Open questions", "Review record"],
            "NFRD.md": ["Document control", "Applicability", "Deployment and measurement contexts",
                        "Quality requirements", "Security and compliance decisions", "Technology constraints",
                        "Requirement summary", "Blockers and open questions", "Review record"],
            "SPECIFICATION.md": ["Problem and outcome", "Scope and non-goals", "Actors and dependencies",
                                 "Source register", "Requirements", "Assumptions, blockers, and open questions",
                                 "Dispositions", "Review record"],
            "ANALYSIS.md": ["Evidence inventory", "Gap analysis", "Options and trade-offs", "Risk register"],
            "DESIGN.md": ["Architecture Overview", "System Context", "Component Map", "Deployment View",
                          "State Model", "Critical Sequences", "Data Flow and Lifecycle", "Data Model",
                          "Interfaces and Contracts", "Error Model", "Security Design", "Threat Model",
                          "Observability Design", "Testing Strategy", "Implementation Surface",
                          "Delivery and Traceability View", "Risks and Trade-Offs", "Phased Development"],
            "TASKS.md": ["Pre-Implementation Gate", "Execution Rules", "Dependency Graph", "Completion Gate",
                         "Execution log"],
            "TESTING.md": ["Test catalog", "Commands", "Failure and measurement", "Evidence contract",
                           "Exit criteria"],
        },
        "spec-kit": {},
    },
}

# Architect (kit) packages: every file and directory below is mandatory.
KIT_STAGES = {
    "requirements": ["FRD.md", "NFRD.md", "SPECIFICATION.md"],
    "design": ["ANALYSIS.md", "DESIGN.md", "DECISIONS.md", "contracts/manifest.yaml",
               "checkpoints/spec-to-plan.yaml"],
    "complete": ["TASKS.md", "TDD.md", "TESTING.md", "SOURCE_TRACEABILITY.md", "CHECKLIST.md", "CROSS_ANALYSIS.md",
                 "VERIFICATION.md", "checkpoints/plan-to-tasks.yaml",
                 "checkpoints/test-coverage.yaml", "evidence/"],
}
KIT_DERIVED = ["SOURCE_TRACEABILITY.md", "CROSS_ANALYSIS.md", "VERIFICATION.md", "CHECKLIST.md"]
SPEC_KIT_STAGES = {
    "requirements": ["spec.md"],
    "design": ["plan.md", "research.md", "quickstart.md"],
    "complete": ["tasks.md"],
}
STAGE_ORDER = ["requirements", "design", "complete"]
ROLES = {
    "kit": {"requirements": "SPECIFICATION.md", "plan": "DESIGN.md", "tasks": "TASKS.md",
            "testing": "TESTING.md", "frd": "FRD.md", "nfrd": "NFRD.md"},
    "spec-kit": {"requirements": "spec.md", "plan": "plan.md", "tasks": "tasks.md",
                 "testing": "quickstart.md"},
}
# Every active requirement must be cited by these files, per workflow.
COVERAGE = {
    "kit": ["DESIGN.md", "TASKS.md", "TDD.md", "TESTING.md", "SOURCE_TRACEABILITY.md",
            "CROSS_ANALYSIS.md", "VERIFICATION.md"],
    "spec-kit": ["plan.md", "tasks.md"],
}
UPPERCASE_ARTIFACT_RE = re.compile(r"^[A-Z][A-Z_]+\.md$")
PACKAGE_NAME_RE = re.compile(r"^\d{3,}-[a-z0-9]+(?:-[a-z0-9]+)*$")
TEST_ROW_RE = re.compile(r"^\|\s*(TST-[A-Z]*\d{3,})\s*\|(.*)$")


def stage_files(workflow: str, stage: str = "complete") -> list[str]:
    stages = KIT_STAGES if workflow == "kit" else SPEC_KIT_STAGES
    files: list[str] = []
    for name in STAGE_ORDER[: STAGE_ORDER.index(stage) + 1]:
        files += stages[name]
    return files


STATUS_ALIASES = {
    "draft": "draft", "rascunho": "draft", "borrador": "draft",
    "ready for review": "ready", "pronto para revisão": "ready", "listo para revisión": "ready",
    "approved": "approved", "aprovado": "approved", "aprobado": "approved",
    "implemented": "implemented", "implementado": "implemented",
    "verified": "verified", "verificado": "verified",
    "retired": "retired", "aposentado": "retired", "retirado": "retired",
    "superseded": "retired", "substituído": "retired", "sustituido": "retired",
    "planned": "draft", "planejado": "draft", "planificado": "draft",
    "blocked": "blocked", "bloqueado": "blocked",
}
STATUS_RANK = {"draft": 0, "blocked": 0, "ready": 1,
               "approved": 2, "implemented": 3, "verified": 4, "retired": -1}


class Reporter:
    """Collect findings and print them as GitHub annotations or JSON."""

    def __init__(self, strict: bool = False) -> None:
        self.strict = strict
        self.findings: list[dict] = []

    def add(self, level: str, check: str, path: Path | str | None, line: int | None, message: str) -> None:
        if level == "warning" and self.strict:
            level = "error"
        self.findings.append({"level": level, "check": check, "file": str(path) if path else None,
                              "line": line, "message": message})

    def error(self, check: str, path, line, message: str) -> None:
        self.add("error", check, path, line, message)

    def warning(self, check: str, path, line, message: str) -> None:
        self.add("warning", check, path, line, message)

    @property
    def errors(self) -> int:
        return sum(1 for f in self.findings if f["level"] == "error")

    def emit(self, fmt: str = "text", title: str = "SDD validation") -> int:
        if fmt == "json":
            print(json.dumps(
                {"errors": self.errors, "findings": self.findings}, indent=2, ensure_ascii=False))
        else:
            for f in self.findings:
                location = f["file"] or "."
                if f["line"]:
                    location += f",line={f['line']}"
                print(
                    f"::{f['level']} file={location}::[{f['check']}] {f['message']}")
            warnings = len(self.findings) - self.errors
            print(f"{title}: {self.errors} error(s), {warnings} warning(s)")
        return 1 if self.errors else 0


def repo_root(start: Path | None = None) -> Path:
    if os.environ.get("SDD_REPO_ROOT"):
        return Path(os.environ["SDD_REPO_ROOT"]).resolve()
    start = start or Path.cwd()
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=start,
                             capture_output=True, text=True, check=True)
        return Path(out.stdout.strip())
    except (OSError, subprocess.CalledProcessError):
        return start.resolve()


def load_config(root: Path, override: str | None = None) -> dict:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    candidates = [Path(override)] if override else [
        root / ".github/sdd.json", root / ".sdd.json"]
    for candidate in candidates:
        path = candidate if candidate.is_absolute() else root / candidate
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            data.pop("$comment", None)
            for key, value in data.items():
                if isinstance(value, dict) and isinstance(config.get(key), dict):
                    config[key].update(value)
                else:
                    config[key] = value
            config["_configPath"] = str(path)
            break
    return config


def spec_root(root: Path, config: dict, override: str | None = None) -> Path:
    if override:
        return (root / override).resolve() if not Path(override).is_absolute() else Path(override)
    if config.get("specRoot"):
        return root / config["specRoot"]
    for candidate in config["specRootCandidates"]:
        if (root / candidate).is_dir():
            return root / candidate
    return root / config["specRootCandidates"][0]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def matches_any(relpath: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(relpath, g) or fnmatch.fnmatch("/" + relpath, g) for g in globs)


def tracked_files(root: Path) -> list[str]:
    try:
        out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=root,
                             capture_output=True, text=True, check=True)
        return [line for line in out.stdout.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        return [rel(root, p) for p in root.rglob("*") if p.is_file()]


def fence_mask(lines: list[str]) -> list[bool]:
    """True for lines inside fenced code blocks (the fence lines included)."""
    mask, fence = [], None
    for line in lines:
        stripped = line.lstrip()
        marker = re.match(r"(`{3,}|~{3,})", stripped)
        if fence is None and marker:
            fence = marker.group(1)[0] * len(marker.group(1))
            mask.append(True)
        elif fence is not None:
            mask.append(True)
            if stripped.startswith(fence) and stripped.strip(fence[0]).strip() == "":
                fence = None
        else:
            mask.append(False)
    return mask


def headings(text: str) -> list[tuple[int, int, str]]:
    """Return (line_number, level, normalized title) for ATX headings outside fences."""
    lines = text.splitlines()
    mask = fence_mask(lines)
    result = []
    for number, (line, fenced) in enumerate(zip(lines, mask), start=1):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if m and not fenced:
            title = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", m.group(2)).strip()
            result.append((number, len(m.group(1)), title))
    return result


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[`*_]", "", title)).strip().lower()


@dataclass
class Requirement:
    id: str
    file: Path
    line: int
    body: list[str]
    status: str | None = None

    @property
    def text(self) -> str:
        return "\n".join(self.body)


@dataclass
class Task:
    id: str
    line: int
    checked: bool
    text: str
    phase: str | None
    parallel: bool
    traces: set[str] = field(default_factory=set)
    depends: set[str] = field(default_factory=set)


@dataclass
class Package:
    path: Path
    workflow: str
    files: dict[str, Path]

    @property
    def name(self) -> str:
        return self.path.name

    def text(self, name: str) -> str:
        path = self.path / name
        return read(path) if path.is_file() else ""

    def role(self, role: str) -> Path | None:
        name = ROLES.get(self.workflow, ROLES["spec-kit"]).get(role)
        path = self.path / name if name else None
        return path if path and path.is_file() else None

    def markdown_files(self) -> list[Path]:
        return sorted(p for p in self.path.rglob("*.md") if p.is_file())


def detect_workflow(path: Path) -> str:
    names = {p.name for p in path.iterdir()}
    if "SPECIFICATION.md" in names and "spec.md" in names:
        return "mixed"
    if "SPECIFICATION.md" in names:
        return "kit"
    if "spec.md" in names:
        return "spec-kit"
    if names & {"FRD.md", "NFRD.md", "DESIGN.md", "TASKS.md"}:
        return "kit"
    if names & {"plan.md", "tasks.md", "research.md", "quickstart.md"}:
        return "spec-kit"
    return "undetermined"


def packages(root_dir: Path, only: str | None = None) -> list[Package]:
    if not root_dir.is_dir():
        return []
    result = []
    for child in sorted(root_dir.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        if only and child.name != only and not child.name.startswith(only + "-"):
            continue
        files = {p.name: p for p in child.iterdir()}
        result.append(Package(child, detect_workflow(child), files))
    return result


def requirement_patterns(config: dict) -> tuple[re.Pattern, re.Pattern]:
    rid = config["requirementIdPattern"]
    declaration = re.compile(
        rf"^\s*(?:#{{1,6}}\s+(?P<heading>{rid})(?=\s|:|$)|"
        rf"(?:[-*]\s+)?(?:\*\*)?(?P<key>{rid})(?:\*\*)?(?:\s+\([^)]+\))?(?:\s*:|\s+-|\s*$))"
    )
    reference = re.compile(rf"(?<![A-Za-z0-9-])({rid})(?![0-9])")
    return declaration, reference


def declarations(text: str, config: dict) -> list[tuple[int, str]]:
    declaration, _ = requirement_patterns(config)
    lines = text.splitlines()
    mask = fence_mask(lines)
    found = []
    for index, (line, fenced) in enumerate(zip(lines, mask)):
        if fenced or line.lstrip().startswith("|"):
            continue
        m = declaration.match(line)
        if m:
            found.append((index, m.group("heading") or m.group("key")))
    return found


def parse_requirements(path: Path, config: dict) -> list[Requirement]:
    text = read(path)
    lines = text.splitlines()
    decls = declarations(text, config)
    result = []
    for position, (index, rid) in enumerate(decls):
        end = decls[position + 1][0] if position + \
            1 < len(decls) else len(lines)
        body = lines[index:end]
        # A later heading of the same or higher level closes the record.
        level = len(re.match(r"^\s*(#*)", lines[index]).group(1)) or 7
        for offset, line in enumerate(body[1:], start=1):
            h = re.match(r"^(#{1,6})\s", line)
            if h and len(h.group(1)) <= level:
                body = body[:offset]
                break
        status = None
        for line in body:
            m = re.match(
                r"^\s*[-*]?\s*(?:\*\*)?(?:Status|Estado)(?:\*\*)?\s*:\s*(.+?)\s*$", line, re.I)
            if m:
                status = normalize_status(m.group(1))
                break
        result.append(Requirement(rid, path, index + 1, body, status))
    return result


def normalize_status(value: str) -> str | None:
    cleaned = re.sub(r"[`*_\"']", "", value).strip().lower()
    cleaned = re.split(r"\s+[—–-]\s+|\s*\(|,|;", cleaned)[0].strip()
    for alias in sorted(STATUS_ALIASES, key=len, reverse=True):
        if cleaned.startswith(alias):
            return STATUS_ALIASES[alias]
    return None


def document_status(text: str) -> tuple[str | None, int | None]:
    """First document-level status: `Status: X` line or `| Status | X |` row before requirements."""
    for number, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^\s*#{1,6}\s", line) and re.search(r"(?:REQ|NFR)-\d", line):
            break
        m = (re.match(r"^\s*[-*]?\s*(?:\*\*)?(?:Status|Estado)(?:\*\*)?\s*:\s*(.+?)\s*$", line, re.I)
             or re.match(r"^\s*\|\s*(?:\*\*)?(?:Status|Estado)(?:\*\*)?\s*\|\s*([^|]+?)\s*\|", line, re.I))
        if m:
            return normalize_status(m.group(1)), number
    return None, None


TASK_RE = re.compile(
    r"^\s*[-*]\s+\[(?P<mark>[ xX])\]\s+(?:\*\*)?(?P<id>T\d{3,})\b(?P<rest>.*)$")
PHASE_RE = re.compile(r"\b(RED|GREEN|REFACTOR)\b")
DEPENDS_RE = re.compile(
    r"\b(?:depends(?: on)?|depende(?: de)?|deps?)\s*:?\s*((?:T\d{3,}(?:\s*(?:,|;|&|and|e|y)\s*)?)+)", re.I)
EDGE_RE = re.compile(r"\b(T\d{3,})\b[^\n]*?-->(?:\|[^|]*\|)?\s*(T\d{3,})\b")
LEDGER_RE = re.compile(
    r"(?:Marked complete by verification sweep|Marcadas? como conclu[ií]das? pela varredura de verifica[cç][aã]o|"
    r"Marcadas? como completadas? por el barrido de verificaci[oó]n)\s*:\s*(.+)", re.I)


def parse_tasks(text: str, config: dict) -> tuple[list[Task], set[str], list[tuple[str, str]]]:
    """Return tasks, the ledger task ids, and Mermaid dependency edges."""
    _, reference = requirement_patterns(config)
    lines = text.splitlines()
    mask = fence_mask(lines)
    tasks: list[Task] = []
    current: Task | None = None
    for number, (line, fenced) in enumerate(zip(lines, mask), start=1):
        if fenced:
            current = None
            continue
        m = TASK_RE.match(line)
        if m:
            rest = m.group("rest")
            phase = PHASE_RE.search(rest)
            current = Task(m.group("id"), number, m.group("mark") != " ", rest,
                           phase.group(1) if phase else None, bool(re.search(r"\[P\]", rest)))
            current.traces |= set(reference.findall(rest))
            for dep in DEPENDS_RE.findall(rest):
                current.depends |= set(re.findall(r"T\d{3,}", dep))
            tasks.append(current)
            continue
        if current and (line.startswith("  ") or line.startswith("\t")) and line.strip():
            current.text += "\n" + line.strip()
            current.traces |= set(reference.findall(line))
            for dep in DEPENDS_RE.findall(line):
                current.depends |= set(re.findall(r"T\d{3,}", dep))
        elif line.strip() and not line.startswith(" "):
            current = None
    ledger: set[str] = set()
    for m in LEDGER_RE.finditer(text):
        ledger |= set(re.findall(r"T\d{3,}", m.group(1)))
    edges = []
    in_mermaid = False
    for line in lines:
        if line.strip().startswith("```mermaid"):
            in_mermaid = True
            continue
        if in_mermaid and line.strip().startswith("```"):
            in_mermaid = False
            continue
        if in_mermaid:
            chain = re.findall(r"\b(T\d{3,})\b", line)
            if "-->" in line and len(chain) >= 2:
                edges.extend(zip(chain, chain[1:]))
    return tasks, ledger, edges


def source_lines(req: Requirement, config: dict) -> list[tuple[int, str, bool]]:
    """(line, value, bulleted) for every source key within the configured window."""
    keys = "|".join(re.escape(k) for k in config["sourceKeys"])
    pattern = re.compile(
        rf"^(\s*[-*]\s+)?\s*(?:\*\*)?(?:{keys})(?:\*\*)?\s*:\s*(.+?)\s*$", re.I)
    found = []
    for offset, line in enumerate(req.body[1:config["sourceWindow"] + 1], start=1):
        m = pattern.match(line)
        if m:
            found.append((req.line + offset, m.group(2), bool(m.group(1))))
    return found


def source_value_problem(value: str, root: Path, config: dict, registered_sources: set[str]) -> str | None:
    """None when the source value is acceptable, otherwise the reason."""
    value = value.strip()
    if value[:1] in "\"'":
        if len(value) < 2 or value[-1] != value[0]:
            return "unbalanced quotes"
        value = value[1:-1].strip()
    if "`" in value:
        return "remove backticks; CI parsers read the raw value"
    marker = config["greenfieldMarker"]
    if value.startswith(marker):
        return None if value[len(marker):].strip() else f"{marker} needs a one-line justification"
    patterns = config.get("sourcePathPatterns") or []
    parts = [p.strip() for p in re.split(r"\s*[,;]\s*", value) if p.strip()]
    for part in parts:
        if re.fullmatch(r"SRC-\d{3,}", part):
            if part not in registered_sources:
                return f"{part} is not in the spec.md source register"
            continue
        if patterns and not any(re.fullmatch(p, part) for p in patterns):
            return f"'{part}' does not match the configured source path patterns"
        target = part.split("#", 1)[0]
        if not (root / target).exists():
            return f"'{target}' does not exist in the repository"
        anchor = re.fullmatch(r"L(\d+)(?:-L(\d+))?",
                              part.split("#", 1)[1]) if "#" in part else None
        if "#" in part and not anchor:
            return f"'{part}' uses an invalid line anchor; use #L<start>-L<end>"
        if anchor and (root / target).is_file():
            length = len(read(root / target).splitlines())
            start, end = int(anchor.group(1)), int(
                anchor.group(2) or anchor.group(1))
            if start > end or end > length:
                return f"'{part}' points beyond the {length} lines of {target}"
    return None


def registered_source_ids(text: str) -> set[str]:
    return set(re.findall(r"^\s*(?:\|\s*)?(SRC-\d{3,})\b", text, re.M))


def mermaid_blocks(text: str) -> list[tuple[int, list[str]]]:
    blocks, current, start = [], None, 0
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if current is None and re.match(r"^(`{3,}|~{3,})\s*mermaid\b", stripped):
            current, start = [], number
        elif current is not None and re.match(r"^(`{3,}|~{3,})\s*$", stripped):
            blocks.append((start, current))
            current = None
        elif current is not None:
            current.append(line)
    return blocks


def test_files(root: Path, config: dict) -> list[str]:
    return [f for f in tracked_files(root)
            if matches_any(f, config["testGlobs"]) and not matches_any(f, config["ignoreGlobs"])
            and not f.endswith(".md")]


def all_requirements(pkgs: list[Package], config: dict) -> dict[str, Requirement]:
    reqs: dict[str, Requirement] = {}
    for pkg in pkgs:
        spec = pkg.role("requirements")
        if spec:
            for req in parse_requirements(spec, config):
                reqs.setdefault(req.id, req)
    return reqs


def parse_tests(text: str, config: dict) -> list[dict]:
    """Rows of a test catalog table whose first cell is a TST-### ID."""
    _, reference = requirement_patterns(config)
    rows = []
    for number, line in enumerate(text.splitlines(), start=1):
        m = TEST_ROW_RE.match(line)
        if m:
            cells = [c.strip() for c in m.group(2).strip().strip("|").split("|")]
            code = re.findall(r"`([^`]+)`", m.group(2))
            rows.append({"id": m.group(1), "line": number, "cells": cells,
                         "requirements": set(reference.findall(m.group(2))),
                         "paths": [c for c in code if "/" in c and " " not in c],
                         "status": normalize_status(cells[-1]) if cells else None})
    return rows


def load_yaml(path: Path, reporter: "Reporter", check: str, where: str):
    try:
        import yaml  # PyYAML is the only third-party dependency, needed for checkpoints.
    except ImportError:
        reporter.error(check, where, None, "PyYAML is required to read checkpoints (pip install pyyaml)")
        return None
    try:
        return yaml.safe_load(read(path)) or {}
    except yaml.YAMLError as exc:
        reporter.error(check, where, None, f"invalid YAML: {exc}")
        return None


def common_arguments(parser) -> None:
    parser.add_argument(
        "--spec-root", help="specification root (default: config or auto-detected)")
    parser.add_argument(
        "--package", help="validate one package by NNN or NNN-slug")
    parser.add_argument(
        "--config", help="path to an SDD config file (default: .github/sdd.json)")
    parser.add_argument("--strict", action="store_true",
                        help="treat warnings as errors")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--stage", choices=STAGE_ORDER, default=None,
                        help="package stage to require (default: complete, or config 'stage')")


def context(args) -> tuple[Path, dict, Path, list[Package]]:
    root = repo_root()
    config = load_config(root, getattr(args, "config", None))
    sroot = spec_root(root, config, getattr(args, "spec_root", None))
    return root, config, sroot, packages(sroot, getattr(args, "package", None))


def run_main(check, description: str) -> None:
    """Standard CLI wrapper: parse common args, run `check(root, config, sroot, pkgs, reporter, args)`."""
    import argparse

    parser = argparse.ArgumentParser(description=description)
    common_arguments(parser)
    args = parser.parse_args()
    root, config, sroot, pkgs = context(args)
    reporter = Reporter(strict=args.strict)
    if not pkgs:
        print(
            f"No SDD packages under {rel(root, sroot)}/ yet; nothing to validate.")
        sys.exit(0)
    check(root, config, sroot, pkgs, reporter, args)
    sys.exit(reporter.emit(args.format, description.split(".")[0]))


os.environ.setdefault("PYTHONIOENCODING", "utf-8")
