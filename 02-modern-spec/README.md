# Stage 2 — Specification

> **Path:** [Team Kit](../README.md) › **Stage 2 — Specification**

**In this stage, the participant uses `@architect` to transform legacy discoveries into traceable requirements, a technical plan, and implementable tasks using GitHub Spec-Kit.**

![Stage 2](https://img.shields.io/badge/Stage-2%20%C2%B7%20Specification-171717?style=flat-square) ![Led by architect](https://img.shields.io/badge/Lead-%40architect-404040?style=flat-square) ![Deliverable Spec-Kit](https://img.shields.io/badge/Deliverable-Spec--Kit-737373?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Participant using `@architect`, with `@dba` for migration design |
| **Prerequisites** | Stage 1 completed; C1 checkpoint accepted by the PO |
| **Estimated time** | 40 min (14:50–15:30) |
| **Stage** | Stage 2 — Specification |
| **Expected outcome** | Traceable `spec.md`, `plan.md`, and `tasks.md`, including DBA-owned data migration and consultation acceptance |

> [!IMPORTANT]
> Formal requirements, plans, and tasks live in `.spec/<NNN>-<feature>/spec.md`, `plan.md`, and `tasks.md`.
> This folder contains only Stage 2 supporting material, templates and scope decisions, and does not replace the Spec-Kit artifacts.

---

## Where this fits in the day's flow

See the challenge schedule in [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md). Stage 2 runs 14:50–15:30 and ends at checkpoint C2.

## Responsibilities covered here

The participant covers architecture, requirements, product, QA, and documentation responsibilities personally; `@dba` supports migration design.

## Contents of this folder

DBA co-designs the source-to-target mappings, snapshot, load, and recovery plan
with Architecture. Vision approves beneficiary coverage and QA defines
reconciliation and query checks before implementation. Use the
[data migration guide](../docs/DATA-MIGRATION.md) as the C2 checklist.

| File | Purpose |
|---|---|
| [`GUIDE.md`](GUIDE.md) | Timed guide and artifact location rule |
| [`scope-decisions.md`](scope-decisions.md) | Record of scope selection, deferrals, and open questions |
| [`ADR-TEMPLATE.md`](ADR-TEMPLATE.md) | Support for an architectural decision that blocks the plan |
| [`templates/ADR.template.md`](templates/ADR.template.md) | ADR template for use through `/generate-adr` |
| [`templates/bounded-contexts.template.md`](templates/bounded-contexts.template.md) | Bounded context map template |

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 1 — Archaeology](../01-archaeology/README.md)<br/><sub>Archaeology summary and links to the detailed GUIDE.</sub> | [Stage 2 — GUIDE](GUIDE.md)<br/><sub>14:50–15:30 · Create spec.md, plan.md, and tasks.md for the beneficiary consultation slice.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
