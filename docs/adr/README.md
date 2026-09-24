# Architecture Decision Records (ADRs)

> **Path:** [Individual challenge kit](../../README.md) › [Docs](../README.md) › **ADRs**

Index of architecture decision records — one decision per file, numbered sequentially.

| Field | Value |
|---|---|
| **Target audience** | Individual participant, especially when acting as architect or technical lead |
| **When to create** | For every decision that is difficult to revisit later (more than one hour to reverse) |
| **Expected outcome** | Auditable history of decisions made under time pressure |

---

## Why write ADRs

An ADR preserves the context and trade-offs of a decision for later review. Its value depends on evidence and clarity; this kit does not claim a measured writing-time or rework-saving ratio.

## When to write an ADR

Write one when:

- A decision will be difficult to revisit later (more than one hour to reverse).
- Reasonable maintainers could choose different options.
- A decision affects more than one bounded context, data migration path, or deployment concern.

Do not write an ADR for variable names, formatting configuration, or minor library versions.

---

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| 0000 | [Template](0000-template.md) | template | 2026-04-29 |
| 0001 | [Agent instructions single source of truth](0001-agent-instructions-single-source-of-truth.md) | accepted | 2026-08-17 |
| 0002 | [Team roles as skills, not agents](0002-team-roles-as-skills-not-agents.md) | accepted | 2026-09-15 |
| 0003 | [Individual challenge format](0003-individual-challenge-format.md) | accepted | 2026-09-24 |

> [!NOTE]
> Add new ADRs to this table as they are created, first with status `proposed` and then `accepted` after accountable review.
> ADRs 0001-0003 govern maintenance of the kit and challenge format. They are not completed SIFAP exercise decisions or approval of a participant's architecture.

---

## How to add an ADR

- [ ] **Open an issue** using the [ADR issue template](../../.github/ISSUE_TEMPLATE/adr.yml), if time allows.
- [ ] **Copy the template** — `0000-template.md` → `NNNN-your-title.md` (next sequential number).
- [ ] **Complete every section** — context, decision, alternatives, consequences, and status.
- [ ] **Link it from the relevant spec, plan, task, or PR.**
- [ ] **Record the actual review state** in this index. A proposed ADR may remain a draft; acceptance needs accountable review.

---

### Continue reading

| Previous | Next |
|---|---|
| [Cross-cutting Documentation](../README.md)<br/><sub>Glossary, data migration, STATUS, and runbook.</sub> | [Stage 2 — Modern Specification](../../02-modern-spec/GUIDE.md)<br/><sub>Write EARS, ADRs, and design artifacts.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
