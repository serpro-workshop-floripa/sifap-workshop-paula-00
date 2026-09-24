# Documentation

> **Path:** [Individual challenge kit](../README.md) › **Docs**

**Language:** English (`main`). Use the [language selector](../README.md#repository-languages) for translated documentation and branch-specific Copilot instructions.

Cross-cutting documentation used during the individual challenge.

| Field | Value |
|---|---|
| **Target audience** | Individual participant |
| **Prerequisites** | Read [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) |
| **Estimated time** | 5 min |
| **Expected outcome** | Know where to find decisions, data migration guidance, status tracking, and troubleshooting |

---

## How to use this folder

- [ ] **Before 14:00** — read [STATUS.md](STATUS.md) and [DATA-MIGRATION.md](DATA-MIGRATION.md).
- [ ] **During Stage 1** — update the [Stage 1 glossary](../01-archaeology/glossary.md) and record legacy sources.
- [ ] **During Stage 2** — create ADRs in [adr/](adr/) for non-trivial design decisions.
- [ ] **During Stage 3** — record migration, reconciliation, and validation evidence without sensitive data.
- [ ] **Before submission** — complete the PR checklist and STATUS C3 section.

## Structure

| Path | Purpose |
|---|---|
| [`adr/`](adr/) | Architecture decision records, including challenge-format ADR-0003 |
| [`../01-archaeology/glossary.md`](../01-archaeology/glossary.md) | Domain glossary completed during Stage 1 |
| [`DATA-MIGRATION.md`](DATA-MIGRATION.md) | Source readiness, discovery, migration, reconciliation, and beneficiary consultation |
| [Scenario chronology](../README.md#scenario-chronology-and-evidence) | Approximately 30 years of history, original source dates, and the 2026 workshop reference year |
| [Canonical chronology](../01-archaeology/legacy-sifap/CHRONOLOGY.md) | Dates, authors, and name index transcribed from source headers |
| [Declared drift](../01-archaeology/legacy-sifap/DECLARED-DRIFT.md) | Deliberate contradictions between period documents and code |
| [Mystery evidence and difficulty](../01-archaeology/mysteries-checklist.md) | Investigation levels, source comparison, escalation, and honest unresolved outcomes |
| [`data-migration/`](data-migration/) | Blank records for your own data evidence and decisions |
| [`4-agents-explained.md`](4-agents-explained.md) | Explanation of the stage agents and role skills |
| [`persona-agent-matrix.md`](persona-agent-matrix.md) | Role responsibilities across stages |
| [`sdlc-flow-guide.md`](sdlc-flow-guide.md) | Extended process reference; [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) remains the challenge schedule source of truth |
| [`STATUS.md`](STATUS.md) | Individual progress, C1/C2/C3, and judge submission tracker |
| [`runbook.md`](runbook.md) | How to run the system locally, in CI, and on Azure if built |

## Conventions

- Use one ADR per durable decision. Number them sequentially: `0001-title.md`, `0002-title.md`.
- Keep glossary terms alphabetical with citations to the legacy source where each term originated.
- Every important decision becomes an ADR. A chat conversation is not a sufficient record.
- Every glossary term originating in the legacy system needs a source (`.NSN`, `.ddm`, or historical document).
- Never record credentials, CPF, NIS, benefit amounts, or source administration details in Git.

## Documentation definition of done

- [ ] Glossary includes legacy sources.
- [ ] ADRs include context, options, decision, and consequences.
- [ ] Migration records link to sanitized readiness, load, reconciliation, and consultation evidence.
- [ ] Internal links point to the correct files.
- [ ] Documents explain the reason before the procedure.

## Quick links

- [Challenge flow](../00-TEAM-FLOW.md)
- [Role responsibilities](../05-personas/)
- [Stage 1 guide](../01-archaeology/GUIDE.md)
- [Git workflow](../00-GIT-WORKFLOW.md)

---

### Continue reading

| Previous | Next |
|---|---|
| [Reference Cards](../09-cheat-sheets/README.md)<br/><sub>Quick Copilot, Spec-Kit, and model references.</sub> | [Visual Glossary](../07-concepts/03-visual-glossary.md)<br/><sub>Domain and technical terms from SIFAP.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
