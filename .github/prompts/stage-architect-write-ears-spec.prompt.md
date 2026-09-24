---
name: "write-ears-spec"
description: "Writes the requirements stage of an architect SDD package — FRD.md, NFRD.md, and SPECIFICATION.md — from confirmed Stage 1 rules, with EARS statements and source_legacy traceability."
argument-hint: "feature=NNN-feature-name rules=01-archaeology/business-rules-catalog.md"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /write-ears-spec

## Objective

Create or update the requirements stage of the architect package in `.spec/<NNN>-<feature>/`: `FRD.md`, `NFRD.md`, and `SPECIFICATION.md`, complete to their templates, holding only confirmed Stage 1 rules as EARS requirements. Open questions stay questions.

## When to Invoke

At the start of Stage 2, after C1, on the `spec/<NNN>-<feature>` branch, when the participant chose Option A (architect workflow). For Option B use `/speckit.specify` instead.

> [!NOTE]
> This prompt does not explore the legacy system (use `/catalog-mysteries`) or design modules (use `/design-modular-monolith`).

## Preconditions

- `01-archaeology/business-rules-catalog.md` holds the confirmed rules for the feature
- The team read each legacy source before drafting
- The [SDD skill](../skills/sdd-requirements-engineer/SKILL.md), its [EARS reference](../skills/sdd-requirements-engineer/references/ears-notation.md), and the [SDD artifacts instruction](../instructions/sdd-artifacts.instructions.md) are loaded

## Inputs the Team Must Provide

- `feature=<NNN>-<feature-name>` — the next free zero-padded number under `.spec/`
- `rules=01-archaeology/business-rules-catalog.md` — only its **Confirmed** rows may be promoted
- The subset of confirmed rules in scope, and any `[GREENFIELD]` justification the team stands behind
- DBA-reviewed data readiness and the PO-approved beneficiary consultation scope

## What I Will Do

- Scaffold the package with `python3 .github/scripts/export-spec-library.py --new-package <NNN>-<feature>` when it does not exist
- Record the workflow choice and deferrals in `02-modern-spec/scope-decisions.md`
- Verify each cited legacy line range before writing a requirement
- Write each requirement once in `SPECIFICATION.md` in the template record shape, with the next `REQ-NNN` or `NFR-NNN`
- Fill every section of `FRD.md` and `NFRD.md`, citing requirement IDs without restating them
- Copy every unvalidated item from `01-archaeology/mysteries-found.md` into the open-questions table unchanged
- Run the requirements-stage gates; derived files follow once the checkpoints exist

## What I Will NOT Do

- Create a requirement without a valid `source_legacy:` or justified `[GREENFIELD]`
- Promote a hypothesis or open question, answer it, or change its status
- Write `spec.md`, `plan.md`, or `tasks.md` in an architect package, or any file outside `.spec/`
- Leave a template section empty or a placeholder unfilled; I write `NOT APPLICABLE: <reason>` instead
- Invent SIFAP business facts, targets, or approvals

## Output Format

Each record in `.spec/<NNN>-<feature>/SPECIFICATION.md` (values are illustrative):

```markdown
- **REQ-001:** If <unwanted condition from the confirmed rule>, then the <system> shall <one observable response>.
  source_legacy: 01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSN#L<start>-L<end>
  - Priority: P0. Source: SRC-001. Status: Draft.
  - Pattern: Unwanted behavior
  - Rationale: <why the rule exists, from the evidence>
  - Acceptance: AC-REQ-001-01 Given <state>, When <trigger>, Then <observable outcome>.
  - Verification: TST-001
```

`FRD.md` and `NFRD.md` follow the [FRD](../skills/sdd-requirements-engineer/references/frd-template.md) and [NFRD](../skills/sdd-requirements-engineer/references/nfrd-template.md) templates.

## Definition of Done

- [ ] `FRD.md`, `NFRD.md`, and `SPECIFICATION.md` exist in `.spec/<NNN>-<feature>/`
- [ ] Every requirement has one EARS statement with `shall`, a CI-valid `source_legacy:`, and an `AC-<ID>-NN`
- [ ] Every section has content or `NOT APPLICABLE: <reason>`; open questions are unchanged in status
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --only validate-sdd-documents --only validate-spec-artifacts` passes, or its failures are reported
- [ ] DBA/QA and PO reviewed migration and consultation criteria

## Prompt Body

You are the `@architect`. Promote confirmed Stage 1 rules into the requirements stage of an architect package. You transcribe evidence into requirements; you never invent it. Load [sdd-requirements-engineer](../skills/sdd-requirements-engineer/SKILL.md) in `Requirements` mode first.

**Step 1 — Confirm the workflow and scope.**

- Confirm the team chose Option A; otherwise stop and point to `/speckit.specify`.
- List only **Confirmed** catalog rows assigned to the feature; record deferrals in `02-modern-spec/scope-decisions.md`.

**Step 2 — Scaffold the package.**

- Run `python3 .github/scripts/export-spec-library.py --new-package <NNN>-<feature>` if `.spec/<NNN>-<feature>/` does not exist. It never overwrites a file.

**Step 3 — Validate each source.**

- Open the cited member (`.NSP`, `.NSN`, `.NSC`, `.NSA`, `.NSL`, `.jcl`, or `.ddm`) and confirm the line range holds the logic. An unresolved citation returns to the team as an open question.

**Step 4 — Write the EARS records.**

- One record per behavior with the matching EARS pattern and exactly one `shall`.
- Put `source_legacy:` on the line after the statement, indented and not bulleted; register the source as `SRC-NNN` in the source register.
- Give every acceptance criterion an `AC-<ID>-NN` ID in Given/When/Then form.

**Step 5 — Complete FRD.md and NFRD.md.**

- Fill every section; cite requirement IDs in tables or mid-sentence; state `NOT APPLICABLE: <reason>` where a section does not apply.

**Step 6 — Carry open questions through.**

- Copy every unvalidated item from `01-archaeology/mysteries-found.md` into the open-questions table with its evidence, owner, and status unchanged.

**Step 7 — Validate.**

- Run `python3 .github/scripts/validate-specs.py --package <NNN> --stage requirements` and report its result verbatim.

## Invocation Example

```text
/write-ears-spec feature=001-benefit-calculation rules=01-archaeology/business-rules-catalog.md
```

Expect `.spec/001-benefit-calculation/` with complete `FRD.md`, `NFRD.md`, and `SPECIFICATION.md`, each requirement sourced and accepted, and open questions carried through unchanged.
