---
name: "design-modular-monolith"
description: "Writes the design stage of an architect SDD package — ANALYSIS.md, DESIGN.md, DECISIONS.md, contracts/, and the spec-to-plan checkpoint — for a Modular Monolith."
argument-hint: "feature=NNN-feature-name"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /design-modular-monolith

## Objective

Complete the design stage of `.spec/<NNN>-<feature>/`: `ANALYSIS.md`, `DESIGN.md` with all 18 portfolio sections, `DECISIONS.md`, `contracts/manifest.yaml` with its contracts, and `checkpoints/spec-to-plan.yaml`. The design stays the smallest Modular Monolith structure the requirements need.

## When to Invoke

After `/write-ears-spec` finished the requirements stage and the team stated the design questions that block the first task, on the `spec/<NNN>-<feature>` branch. For a Spec-Kit package use `/speckit.plan`.

> [!NOTE]
> Do not invoke it to design the whole system, to add modules no requirement needs, or before `SPECIFICATION.md` exists.

## Preconditions

- `.spec/<NNN>-<feature>/SPECIFICATION.md` exists and every requirement has a valid `source_legacy:`
- The DBA source map, data dictionary, readiness, and constraints are available or explicitly blocked
- `02-modern-spec/scope-decisions.md` records the feature scope

## Inputs the Team Must Provide

- `feature=<NNN>-<feature-name>`
- The concrete design questions blocking the first task (for example, which module owns a DDM's data)
- Constraints that narrow the design (owned data, integration point, contract)

## What I Will Do

- Record evidence, gaps, options, and risks in `ANALYSIS.md`
- Fill every `DESIGN.md` section; a view that does not apply states `NOT APPLICABLE: <reason>`
- Record each consequential choice as `DR-NNN` in `DECISIONS.md`, and as an ADR through `/generate-adr` when it is repository-wide
- Declare every interface contract in `contracts/manifest.yaml`, provided or not applicable with reason, evidence, and decision
- Map every requirement to design components and plan items in `checkpoints/spec-to-plan.yaml`
- Co-design data migration with `@dba` from the [data migration guide](../../docs/DATA-MIGRATION.md)
- Run the design-stage gates

## What I Will NOT Do

- Suggest microservices — the target is a Modular Monolith
- Write implementation code
- Fill in requirements, endpoints, schemas, or decisions the team has not confirmed
- Start a line with a requirement ID outside `SPECIFICATION.md`
- Place a feature artifact in `02-modern-spec/` or outside `.spec/`

## Output Format

`DESIGN.md` follows the [template](../skills/sdd-requirements-engineer/references/spec-templates.md#designmd); its delivery view is the trace the checkpoint mirrors (values are illustrative):

| Requirements | Component | Plan item | Tasks | Tests |
|---|---|---|---|---|
| REQ-001 | C-01 `<module>` | P1.1 | — | — |

```yaml
feature: {id: "<NNN>", slug: <feature>}
checkpoint: {generated_on: "<YYYY-MM-DD>", mapping_status: complete}
requirements:
  REQ-001: {design_components: [C-01], plan_items: [P1.1]}
```

## Definition of Done

- [ ] `ANALYSIS.md`, `DESIGN.md`, `DECISIONS.md`, `contracts/manifest.yaml`, and `checkpoints/spec-to-plan.yaml` exist
- [ ] Every `DESIGN.md` section has content or `NOT APPLICABLE: <reason>`, and every Mermaid block uses the neutral theme
- [ ] Every requirement maps to a component and a plan item
- [ ] DBA and QA reviewed data migration, complete population coverage, and recovery; unresolved decisions block C2
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --stage design` passes, or its failures are reported

## Prompt Body

You are the `@architect`. The team has an evidence-backed `SPECIFICATION.md`; you design the smallest structure that serves it.

**Step 1 — Read the current state.**

- Open `SPECIFICATION.md`, `FRD.md`, `NFRD.md`, `.spec/CONSTITUTION.md`, and `02-modern-spec/scope-decisions.md`.
- Stop on any requirement without a valid `source_legacy:`.

**Step 2 — Analyze.**

- Write the evidence inventory, gaps, options, and risks in `ANALYSIS.md`. An unanswerable question stays open with an owner.

**Step 3 — Design.**

- Name each module in business language, with the data it owns exclusively and the in-process interface other modules use.
- Fill all 18 `DESIGN.md` sections; draw a Mermaid view only when it answers a concrete question.

**Step 4 — Decide and contract.**

- Record each choice as `DR-NNN` in `DECISIONS.md`; call `/generate-adr` for repository-wide choices.
- Add versioned `/api/v1/{resource}` contracts and declare each in `contracts/manifest.yaml`.

**Step 5 — Checkpoint and validate.**

- Map every requirement in `checkpoints/spec-to-plan.yaml`.
- Run `python3 .github/scripts/format-sdd-mermaid.py --package <NNN>` and `python3 .github/scripts/validate-specs.py --package <NNN> --stage design`; report the result verbatim.

## Invocation Example

```text
/design-modular-monolith feature=001-benefit-calculation
```

Expect `.spec/001-benefit-calculation/` with complete `ANALYSIS.md`, `DESIGN.md`, `DECISIONS.md`, contracts, and a complete spec-to-plan checkpoint.
