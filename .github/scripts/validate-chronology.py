#!/usr/bin/env python3
"""Validate that kit documents agree with the SIFAP legacy source headers.

Why this gate exists
--------------------
The corpus has two layers. Period documents about SIFAP are *allowed* to
contradict the code: documentation drift is the lesson of Stage 1, and every
deliberate divergence is registered in DECLARED-DRIFT.md. The kit's own guides
are *not* allowed to contradict the code: a guide that misattributes a program
sends a pair to the wrong evidence and breaks the exercise it is supposed to
teach.

This script turns that distinction into a build gate. It reads the `* AUTHOR:`
and `* DATE:` headers straight out of the read-only corpus, then checks the
tables in the kit-truth documents against them.

What it checks
--------------
1. Every Natural member, JCL, and DDM carries a parseable AUTHOR and DATE header.
2. The canonical tables in 01-archaeology/legacy-sifap/CHRONOLOGY.md match those
   headers exactly (author and full creation date).
3. The pair-assignment table in natural-programs/README.md matches them
   (author and creation year).
4. The corpus span asserted in CHRONOLOGY.md equals the span actually present.
5. DECLARED-DRIFT.md has unique IDs and every document it names exists.

Design constraints
------------------
Python 3.11+, standard library only, so CI needs no `pip install`. Only tables
sitting under a named heading are checked, which keeps prose and derived
narrative tables out of scope by construction.

Exit status
-----------
Non-zero when any error is found, with a `::error` annotation per finding.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CORPUS = REPO_ROOT / "01-archaeology" / "legacy-sifap"
PROGRAMS = CORPUS / "natural-programs"
DDMS = CORPUS / "adabas-ddms"
CHRONOLOGY = CORPUS / "CHRONOLOGY.md"
DRIFT = CORPUS / "DECLARED-DRIFT.md"
PROGRAMS_README = PROGRAMS / "README.md"

MEMBER_SUFFIXES = (".NSP", ".NSN", ".NSC", ".NSA", ".NSL", ".jcl")

# Natural members use `* AUTHOR:`; JCL uses `//* AUTHOR...:`. One pattern covers
# both because everything before the keyword is comment punctuation.
AUTHOR_RE = re.compile(
    r"^\s*(?://)?\*\s*AUTHOR\.*:\s*(.+?)\s*$", re.IGNORECASE)
DATE_RE = re.compile(
    r"^\s*(?://)?\*\s*DATE\.*:\s*(\d{2}/\d{2}/\d{4})\s*$", re.IGNORECASE)
HEADER_SCAN_LINES = 20

YEAR_RE = re.compile(r"\b(19[89]\d|20[0-2]\d)\b")
FULL_DATE_RE = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
DRIFT_ID_RE = re.compile(r"`(DRIFT-\d{2})`")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)")

# The elapsed-span assertion is the one prose string this gate reads, so it needs
# the wording of the branch it runs on. Paths, section numbers and table data are
# identical in every edition.
SPAN_PHRASE = {
    "en": "{n} calendar years",
    "pt-br": "{n} anos civis",
    "es": "{n} años naturales",
}


def branch_language() -> str:
    metadata = REPO_ROOT / ".github" / "language.json"
    if not metadata.is_file():
        return "en"
    try:
        return json.loads(metadata.read_text(encoding="utf-8")).get("language", "en")
    except json.JSONDecodeError:
        return "en"


class Reporter:
    """Collects findings and prints GitHub Actions annotations."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, file: Path | str, message: str) -> None:
        rel = file if isinstance(
            file, str) else file.relative_to(REPO_ROOT).as_posix()
        self.errors.append(f"{rel}: {message}")
        print(f"::error file={rel}::{message}")


def normalize(text: str) -> str:
    """Fold case, punctuation, and accents-free spacing so names compare equal."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def read_header(path: Path) -> tuple[str | None, str | None]:
    author = date = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[:HEADER_SCAN_LINES]:
        if author is None and (match := AUTHOR_RE.match(line)):
            author = match.group(1)
        if date is None and (match := DATE_RE.match(line)):
            date = match.group(1)
    return author, date


def collect_corpus(reporter: Reporter) -> dict[str, tuple[str, str]]:
    """Map every corpus artifact name to its declared (author, dd/mm/yyyy)."""
    canon: dict[str, tuple[str, str]] = {}
    sources = [p for p in sorted(PROGRAMS.iterdir())
               if p.suffix in MEMBER_SUFFIXES]
    sources += sorted(DDMS.glob("*.ddm"))
    for path in sources:
        author, date = read_header(path)
        if author is None or date is None:
            reporter.error(
                path, "header is missing a parseable '* AUTHOR:' or '* DATE:' line")
            continue
        canon[path.name] = (author, date)
    return canon


def table_under_heading(path: Path, heading_pattern: str) -> list[tuple[int, str]]:
    """Return the first Markdown table that follows a heading, as (line_no, row)."""
    heading_re = re.compile(heading_pattern)
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[tuple[int, str]] = []
    in_section = seen_table = False
    for index, line in enumerate(lines, start=1):
        if line.startswith("#"):
            if in_section and seen_table:
                break
            in_section = bool(heading_re.search(line))
            continue
        if not in_section:
            continue
        if line.lstrip().startswith("|"):
            seen_table = True
            rows.append((index, line))
        elif seen_table and line.strip():
            break
    return rows


def check_table(
    path: Path,
    heading_pattern: str,
    canon: dict[str, tuple[str, str]],
    reporter: Reporter,
    *,
    full_date: bool,
) -> int:
    """Assert every artifact row in one table matches the corpus headers."""
    checked = 0
    other_authors = {normalize(author) for author, _ in canon.values()}
    for line_no, row in table_under_heading(path, heading_pattern):
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        named = [name for name in canon if f"`{name}`" in row]
        if len(named) != 1:
            continue
        name = named[0]
        author, date = canon[name]
        haystack = normalize(row)
        location = f"{path.relative_to(REPO_ROOT).as_posix()}:{line_no}"

        if normalize(author) not in haystack:
            wrong = sorted(o for o in other_authors if o !=
                           normalize(author) and o in haystack)
            detail = f" (row names '{wrong[0]}')" if wrong else ""
            reporter.error(
                location, f"{name} is authored by '{author}' in its header{detail}")

        expected = date if full_date else date[-4:]
        found = FULL_DATE_RE.findall(
            row) if full_date else YEAR_RE.findall(row)
        if expected not in found:
            kind = "creation date" if full_date else "creation year"
            reporter.error(
                location, f"{name} has {kind} {expected} in its header, row states {found or 'none'}")
        checked += 1
    return checked


def check_corpus_span(canon: dict[str, tuple[str, str]], reporter: Reporter) -> None:
    """The stated span must equal the span the corpus actually covers."""
    years = sorted(date[-4:] for _, date in canon.values())
    text = CHRONOLOGY.read_text(encoding="utf-8")
    section = text.split("## 2.")[1].split("## 3.")[
        0] if "## 2." in text else ""
    if years[0] not in section:
        reporter.error(
            CHRONOLOGY, f"earliest dated source is {years[0]}, which section 2 does not state")
    elapsed = 2026 - int(years[0])
    template = SPAN_PHRASE.get(branch_language(), SPAN_PHRASE["en"])
    phrase = template.format(n=elapsed)
    if phrase not in section:
        reporter.error(
            CHRONOLOGY, f"span from {years[0]} to reference year 2026 is '{phrase}'")


def check_drift_register(reporter: Reporter) -> None:
    text = DRIFT.read_text(encoding="utf-8")
    ids = DRIFT_ID_RE.findall(text)
    if len(ids) != len(set(ids)):
        reporter.error(DRIFT, "duplicate DRIFT- identifier in the register")
    for target in {t for t in LINK_RE.findall(text) if not t.startswith(("http", "mailto"))}:
        if not (DRIFT.parent / target).resolve().exists():
            reporter.error(
                DRIFT, f"register links to a missing file: {target}")


def main() -> int:
    reporter = Reporter()
    canon = collect_corpus(reporter)
    if not canon:
        reporter.error("01-archaeology/legacy-sifap",
                       "no legacy sources found to validate against")
        return 1

    checked = check_table(CHRONOLOGY, r"3\.1\.", canon,
                          reporter, full_date=True)
    checked += check_table(CHRONOLOGY, r"3\.2\.", canon,
                           reporter, full_date=True)
    checked += check_table(CHRONOLOGY, r"^## 4\.",
                           canon, reporter, full_date=True)
    checked += check_table(PROGRAMS_README, r"^## 1\.",
                           canon, reporter, full_date=False)
    check_corpus_span(canon, reporter)
    check_drift_register(reporter)

    print(
        f"\nChronology gate: {len(canon)} legacy artifacts parsed, {checked} kit table rows checked.")
    if reporter.errors:
        print(f"FAIL: {len(reporter.errors)} chronology error(s).")
        for finding in reporter.errors:
            print(f"  - {finding}")
        return 1
    print("PASS: every kit table agrees with the source headers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
