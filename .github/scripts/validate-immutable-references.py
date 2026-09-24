#!/usr/bin/env python3
"""Enforce immutable cross-repository references.

A reference into another repository must resolve to an immutable tag or commit;
a mutable branch such as `main` changes what this repository resolves without a
recorded upgrade. The gate inspects GitHub blob/tree/raw URLs, Terraform Git
module sources, and GitHub Actions `uses:` steps, which must pin a full commit
SHA. References into this repository (detected from `origin`) are exempt.

Usage:
    validate-immutable-references.py [PATH ...]   (default: .github, infra, terraform)

Exit code 0 means every cross-repository reference is immutable.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import subprocess  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

ROOT = sdd.repo_root()


def _self_repository() -> str:
    try:
        url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""
    match = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", url)
    return match.group(1) if match else ""


SELF_REPOSITORY = _self_repository()
ACTION_USES = re.compile(r"^\s*-?\s*uses:\s*['\"]?(?P<repo>[\w.-]+/[\w.-]+)(?:/[^@\s]*)?@(?P<ref>[^\s'\"#]+)")
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")

EXCLUDED_PARTS = {
    ".git",
    ".terraform",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    "__pycache__",
    ".test-results",
}

# A GitHub blob or tree URL carrying the ref it resolves.
GITHUB_REF_URL = re.compile(
    r"https://github\.com/(?P<repo>[\w.-]+/[\w.-]+)/(?:blob|tree|raw)/(?P<ref>[^/\s\"']+)"
)

# A Terraform module sourced from Git, optionally pinned with ?ref=.
TERRAFORM_GIT_SOURCE = re.compile(
    r'source\s*=\s*"(?:git::)?(?P<url>[^"]*github\.com[^"]*)"'
)

# A 40- or 7-plus-character hexadecimal commit, or a version-like tag.
COMMIT_REF = re.compile(r"^[0-9a-f]{7,40}$")
TAG_REF = re.compile(r"^v?\d+\.\d+")

MUTABLE_REFS = {"main", "master", "develop", "HEAD", "trunk"}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    repository: str
    ref: str

    def render(self, root: Path) -> str:
        try:
            location = self.path.relative_to(root)
        except ValueError:
            location = self.path
        return (
            f"{location}:{self.line}: mutable-cross-repository-reference: "
            f"{self.repository} is referenced at {self.ref!r}. Use an immutable "
            "tag or commit so the resolved content cannot change without a "
            "recorded upgrade."
        )


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def is_immutable(ref: str) -> bool:
    if ref in MUTABLE_REFS:
        return False
    return bool(COMMIT_REF.fullmatch(ref) or TAG_REF.match(ref))


def scan_line(path: Path, number: int, line: str) -> list[Finding]:
    findings: list[Finding] = []

    for match in GITHUB_REF_URL.finditer(line):
        repository = match.group("repo")
        ref = match.group("ref")
        if repository == SELF_REPOSITORY:
            continue
        if not is_immutable(ref):
            findings.append(Finding(path, number, repository, ref))

    action = ACTION_USES.match(line)
    if action and action.group("repo") != SELF_REPOSITORY and not FULL_SHA.fullmatch(action.group("ref")):
        findings.append(Finding(path, number, action.group("repo"), action.group("ref") + " (pin a full commit SHA)"))

    for match in TERRAFORM_GIT_SOURCE.finditer(line):
        url = match.group("url")
        if SELF_REPOSITORY and SELF_REPOSITORY in url:
            continue
        if "?ref=" not in url:
            findings.append(Finding(path, number, url, "<unpinned>"))
            continue
        ref = url.split("?ref=", 1)[1].split("&", 1)[0]
        if not is_immutable(ref):
            findings.append(Finding(path, number, url, ref))

    return findings


def scan(paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    suffixes = {".yaml", ".yml", ".tf"}
    for target in paths:
        candidates = [target] if target.is_file() else list(target.rglob("*"))
        for path in candidates:
            if not path.is_file() or is_excluded(path) or path.suffix not in suffixes:
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (OSError, UnicodeDecodeError):
                continue
            for number, line in enumerate(lines, 1):
                findings.extend(scan_line(path, number, line))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args(argv)

    targets = args.paths or [ROOT / ".github", ROOT / "infra", ROOT / "terraform"]
    resolved = [p if p.is_absolute() else ROOT / p for p in targets]
    existing = [p for p in resolved if p.exists()]
    if not existing:
        print("No inspectable path exists; nothing to check.")
        return 0

    findings = scan(existing)
    for finding in findings:
        print(finding.render(ROOT), file=sys.stderr)

    print(f"Summary: mutable cross-repository references {len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
