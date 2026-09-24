---
description: "Use when creating, editing, or reviewing Spec-Driven Development packages under .spec/ — the architect package (FRD, NFRD, SPECIFICATION, ANALYSIS, DESIGN, DECISIONS, TASKS, TDD, TESTING, derived files, checkpoints, contracts, evidence) or a Spec-Kit package — plus the constitution, EARS records, traceability, and status."
applyTo: ".spec/**,.specify/memory/**"
---

# Spec-Driven Development Artifacts — Guide

This file opens for every file under `.spec/` and for the Spec-Kit constitution. It owns the package layout and file contracts. The [sdd-requirements-engineer](../skills/sdd-requirements-engineer/SKILL.md) skill owns the procedure and the [templates](../skills/sdd-requirements-engineer/references/spec-templates.md); the `@architect` agent and its prompts write the files; the scripts in `.github/scripts/` and [spec-quality.yml](../workflows/spec-quality.yml) enforce them. A [worked package](../scripts/tests/fixtures/kit-repo/.spec/001-sample-feature/SPECIFICATION.md) passes every gate.

## Choose One Workflow per Package

| | Option A — architect workflow | Option B — Spec-Kit workflow |
|---|---|---|
| Driven by | `@architect` prompts and the SDD skill | Installed `/speckit.*` commands |
| Folder | `.spec/<NNN>-<feature>/` | `.spec/<NNN>-<feature>/` (moved from Spec-Kit's `specs/` output) |
| Files | Uppercase architect package below | `spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`, `tasks.md`, `checklists/` |
| Detected by | `SPECIFICATION.md` | `spec.md` |

Record the choice in `02-modern-spec/scope-decisions.md`. A package with both `SPECIFICATION.md` and `spec.md` fails the gates.

## Architect Package Layout

```text
.spec/
├── CONSTITUTION.md
└── <NNN>-<feature>/
    ├── checkpoints/   spec-to-plan.yaml, plan-to-tasks.yaml, test-coverage.yaml
    ├── contracts/     manifest.yaml + contract files
    ├── evidence/      README.md + dated run evidence
    ├── ANALYSIS.md
    ├── CHECKLIST.md             generated
    ├── CROSS_ANALYSIS.md        generated
    ├── DECISIONS.md
    ├── DESIGN.md
    ├── FRD.md
    ├── NFRD.md
    ├── SOURCE_TRACEABILITY.md   generated
    ├── SPECIFICATION.md
    ├── TASKS.md
    ├── TDD.md                   generated unless hand-authored
    ├── TESTING.md
    └── VERIFICATION.md          generated
```

| Stage | Files that must exist | Prompt |
|---|---|---|
| Requirements | `FRD.md`, `NFRD.md`, `SPECIFICATION.md` | `/write-ears-spec` |
| Design | + `ANALYSIS.md`, `DESIGN.md`, `DECISIONS.md`, `contracts/manifest.yaml`, `checkpoints/spec-to-plan.yaml` | `/design-modular-monolith`, `/generate-adr` |
| Complete | + `TASKS.md`, `TDD.md`, `TESTING.md`, `SOURCE_TRACEABILITY.md`, `CHECKLIST.md`, `CROSS_ANALYSIS.md`, `VERIFICATION.md`, the other two checkpoints, `evidence/` | `/break-down-tasks`, `/validate-spec` |

Start a package with `python3 .github/scripts/export-spec-library.py --new-package <NNN>-<feature>`; it writes every authored template and never overwrites. Derive the generated files with `python3 .github/scripts/generate-sdd-support-artifacts.py --package <NNN> --include-supplements`; never edit them by hand.

## Completeness

- Every authored file contains every H2 section of its template, in template order.
- A section without applicable content holds `NOT APPLICABLE: <reason>`; an unknown value is `PENDING` or `BLOCKED` with an owner. An empty section or an unfilled `<placeholder>` fails the gate.
- Completeness never licenses invention: no target, actor, rule, diagram, decision, or approval is created to fill a section.

## Requirement Records

`SPECIFICATION.md` is the only home of a normative statement:

```markdown
- **REQ-001:** When <trigger>, the <system> shall <one observable response>.
  source_legacy: 01-archaeology/legacy-sifap/natural-programs/<MEMBER>.NSN#L<start>-L<end>
  - Priority: P0. Source: SRC-001. Status: Draft.
  - Pattern: Event-driven
  - Rationale: <why>
  - Acceptance: AC-REQ-001-01 Given <state>, When <trigger>, Then <outcome>.
  - Verification: TST-001
```

- `REQ-NNN` is functional and `NFR-NNN` non-functional; both are unique across `.spec/`.
- One EARS pattern and exactly one `shall` per record; the unwanted pattern needs `If … then`.
- `source_legacy:` sits within 20 lines of the declaration, is not a list item, has no backticks, and cites a real legacy path with a valid line range or `[GREENFIELD] <justification>`. `SRC-###` in the metadata line points at the source register.
- Outside `SPECIFICATION.md`, cite IDs mid-sentence or in table cells; a line that starts with an ID is read as a second declaration.
- Every active ID appears in `FRD.md` or `NFRD.md`, `DESIGN.md`, `TASKS.md`, `TESTING.md`, and all three checkpoints; tests cite it in a comment (`// REQ-001`).

## Tasks, Tests, and Evidence

- One checkbox per task: `- [ ] **T001 [S] [Plan:P1.1] RED** <action>. Traces REQ-001.` with `Files:` and `Acceptance:` sub-bullets. RED precedes GREEN for every requirement; `[P]` never depends directly on another `[P]`.
- The Mermaid dependency graph names only real tasks; dependencies form no cycle.
- A task is checked only with an `Evidence:` sub-bullet citing a file in `evidence/` and its ID in the `Marked complete by verification sweep:` ledger. `validate-red-phase.py -- <test command>` proves the RED step.
- `TESTING.md` declares each `TST-NNN` in its catalog table; `test-coverage.yaml` maps every requirement to tests.
- Status never exceeds evidence: `Implemented` needs every task checked and in the ledger; `Verified` also needs a test citing every requirement.

## Spec-Kit Packages

Spec-Kit's templates in `.specify/templates/` own the lowercase files. `/speckit.specify` writes to Spec-Kit's dot-less `specs` folder; move the feature folder into `.spec/` with `git mv` and point `.specify/feature.json` at it. The shared requirement, source, TDD, status, and Mermaid rules above still apply. If both constitutions exist, `.specify/memory/constitution.md` is a symlink to `.spec/CONSTITUTION.md`.

## Executable Gates

| Command | Proves |
|---|---|
| `python3 .github/scripts/validate-specs.py [--package NNN] [--strict]` | Runs every gate below plus checkpoint and contract closure |
| `validate-spec-artifacts.py` | Layout per workflow and stage, required sections, empty sections, placeholders, one constitution |
| `validate-sdd-documents.py` | EARS shape, sources, acceptance IDs, single declaration, cross-file coverage |
| `validate-task-graph.py` | Task IDs, dependencies, cycles, RED before GREEN, ledger |
| `validate-spec-status.py` | Status never exceeds evidence |
| `validate-test-bindings.py`, `validate-testing-evidence.py`, `audit-task-evidence.py` | Tests cite requirements; cited tests and evidence exist |
| `validate-design-diagrams.py`, `format-sdd-mermaid.py` | Neutral Mermaid theme and classes |
| `generate-sdd-support-artifacts.py --include-supplements --check` | Generated files are current |

Text gates do not prove EARS meaning, human approval, rendering, or behavioral equivalence; review those explicitly.

## Convenções

| Rule | Rationale |
|---|---|
| Packages are `.spec/<NNN>-<kebab-slug>/`, zero-padded and never renumbered | Stable references and branch names |
| One workflow per package | The gates and generators rely on one layout |
| Generated files are regenerated, never edited | Derived views cannot drift from their sources |
| Stable IDs: `REQ-`, `NFR-`, `AC-<ID>-NN`, `SRC-`, `RISK-`, `DR-`, `T`, `TST-`, `CON-` | Cross-file references survive edits |
| Evidence is dated and redacts CPF, NIS, benefit amounts, and secrets | Security rule for every artifact |

## Faça / Não faça

| Do | Do not |
|---|---|
| Scaffold with `export-spec-library.py` and fill every section | Leave a template section or placeholder unfilled |
| Keep each EARS statement only in `SPECIFICATION.md` | Copy or reword a normative statement elsewhere |
| Regenerate derived files after any source change | Hand-edit `CHECKLIST.md`, `CROSS_ANALYSIS.md`, `VERIFICATION.md`, or `SOURCE_TRACEABILITY.md` |
| State `NOT APPLICABLE: <reason>` | Delete a section that does not apply |
| Report failing gates as failing | Mark planned work done or simulate approval |

## Checklist antes de abrir um PR

- [ ] The package follows one workflow and has every file its stage requires.
- [ ] Every section has content or a justified `NOT APPLICABLE`, and no placeholder remains.
- [ ] Every requirement has one EARS statement, a valid `source_legacy:`, and an acceptance ID.
- [ ] RED precedes GREEN, and checked tasks carry evidence and ledger entries.
- [ ] Generated files are current.
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --strict` passes, or its failures are listed in the PR.
