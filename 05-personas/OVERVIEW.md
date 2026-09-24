# Overview of the 10 Personas

> **Track:** [Team Kit](../README.md) › [Personas](README.md) › **OVERVIEW**

**One-page comparison of the 10 role personas.** In the individual challenge, one participant covers every role as a responsibility checklist while switching stage agents.

| Field | Value |
|---|---|
| **Target audience** | Individual workshop participants |
| **Prerequisites** | None |
| **Estimated time** | 5 min |
| **Expected outcome** | You understand which responsibility to apply in each stage |

> [!IMPORTANT]
> The challenge is individual. You cover all 10 roles yourself; roles load as skills automatically. Select only the current stage agent (`@archaeologist`, `@architect`, `@builder`) and call on `@dba` for data discovery, migration design, and reconciliation.

---

## The 10 role responsibilities

![Distribution of persona responsibilities: vision, architecture, implementation, quality, and operations](../assets/personas-team.svg)

| **#** | Persona | Challenge focus | Most active stage(s) | Supports | Default when stuck |
|---|---|---|---|---|---|
| 01 | [Product Owner](01-product-owner/PERSONA.md) | Scope, value, and migrated-data acceptance | 1, 2, final validation | 3 | One thin feature; preserve data and verification gates |
| 02 | [Requirements Engineer](02-requirements-engineer/PERSONA.md) | EARS requirements and traceability | 1, 2 | 3 | Trace every requirement to legacy evidence |
| 03 | [Enterprise Architect](03-enterprise-architect/PERSONA.md) | External dependencies and scope decisions | 1, 2 | 3 | Record alternatives and assumptions explicitly |
| 04 | [Software Architect](04-software-architect/PERSONA.md) | Module boundaries, technical plan, ADRs | 2 | 3 | Validate design assumptions against evidence |
| 05 | [Technical Lead](05-technical-lead/PERSONA.md) | Standards, sequencing, and self-review | 3 | 1, 2 | Implement the prioritized EARS requirement |
| 06 | [Developer](06-developer/PERSONA.md) | Java/TypeScript code, tests, and integration | 3 | 2 | Complete one end-to-end capability with tests |
| 07 | [DBA](07-dba/PERSONA.md) | Source readiness, migration, reconciliation, recovery | 1, 2, 3 | All stages | Reconcile source records; never replace migration with a seed |
| 08 | [QA Engineer](08-qa-engineer/PERSONA.md) | Tests, independent data checks, quality gates | 2, 3 | 1 | Happy path + error path for critical REQ-IDs |
| 09 | [DevOps Engineer](09-devops-engineer/PERSONA.md) | Local execution and CI green for submission | 3 | 1, 2 | Fix the failing required check before adding scope |
| 10 | [Tech Writer](10-tech-writer/PERSONA.md) | Glossary, README clarity, ADR/spec readability | 1, 2, 3 | All stages | Record the decision now, with evidence |

---

## Role-by-stage checklist

Use this as a one-person checklist. Budgets are summarized in [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md), the source of truth for the 14:00–17:40 challenge schedule.

| Stage | Agent | Responsibility checklist |
|---|---|---|
| **1 · Archaeology** | `@archaeologist` + `@dba` | Read the legacy sources for the target capability; capture rules, glossary terms, open questions, data fields, and source-population evidence. |
| **C1 self-check** | — | Verify the discovery artifacts have cited legacy evidence and enough data facts to support requirements. |
| **2 · Specification** | `@architect` + `@dba` | Convert evidence into EARS requirements with REQ-IDs and `source_legacy:`, define scope, architecture, data migration design, tests, and tasks. |
| **C2 self-check** | — | Verify every formal requirement is traceable and implementation tasks are small enough for Stage 3. |
| **3 · Implementation and data migration** | `@builder` + `@dba` | Implement the thin slice, migrate all agreed beneficiary data, reconcile source-to-target counts, run tests, and keep CI green. |
| **C3 self-check / submission** | — | Verify CI, tests, traceability, data reconciliation, and listing/search/detail coverage before opening the PR to `develop`. |

---

## Emergency defaults (summary)

Each `PERSONA.md` details a "When stuck" section. Here is one line per role:

- **PO:** Choose one thin capability and protect the migrated population and verification standard.
- **RE:** Trace each EARS requirement to evidence and record gaps for clarification.
- **EA:** Use an ADR only for real choices; record alternatives and consequences.
- **SA:** Keep module boundaries simple and validate assumptions before coding.
- **TL:** Stop refactoring without tests; focus on the submission gate.
- **Dev:** One complete endpoint and test path is better than several broken partials.
- **DBA:** Follow the [data lifecycle](../docs/DATA-MIGRATION.md); reconcile source records and rerun behavior.
- **QA:** Verify one happy path and one error path for each critical REQ-ID.
- **DevOps:** Keep the required CI jobs green for the submission PR.
- **TW:** Ask yourself: "What decision or term did I just use that is not written down yet?"

---

### Continue reading

| Previous | Next |
|---|---|
| [SETUP](../00-SETUP.md)<br/><sub>Pre-work setup before 14:00.</sub> | [Stage 1 — Archaeology](../01-archaeology/GUIDE.md)<br/><sub>Read the legacy system and catalog business rules.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
