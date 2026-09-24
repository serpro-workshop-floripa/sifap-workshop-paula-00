# Persona-Agent Matrix

![Reference Type](https://img.shields.io/badge/Type-Reference-171717?style=flat-square)
![Use Who does what](https://img.shields.io/badge/Use-Who%20does%20what-737373?style=flat-square)

> **Path:** [Team Kit](../README.md) › [Docs](README.md) › **Persona-Agent Matrix**

**Maps each role persona to the stage agents used in the individual challenge.** One participant covers every role; this matrix is a role-by-stage checklist, not an assignment chart.

| Field | Value |
|---|---|
| **Target audience** | Individual workshop participants |
| **When to consult** | At the start of each stage and before each self-checkpoint |
| **Expected outcome** | You know which responsibility to emphasize while using the current stage agent |

---

## How to read this matrix

1. Start the stage agent listed for the current challenge stage.
2. Read down the column and apply the relevant role responsibilities yourself.
3. Use `@dba` whenever data discovery, mapping, migration, reconciliation, or rerun/recovery evidence is involved.
4. Stop at C1, C2, and C3 to verify the artifacts before moving on.

> [!NOTE]
> **Rows are skills; columns are agents.** You select the column once per stage with `@name`. Role rows load automatically from skill descriptions and compose into whichever stage agent is active. The DBA is also an agent because its data lifecycle spans every stage. See [ADR-0002](adr/0002-team-roles-as-skills-not-agents.md) and [ADR-0003](adr/0003-individual-challenge-format.md).

---

## The challenge matrix

| # | Persona | Stage 1 `@archaeologist` | Stage 2 `@architect` | Stage 3 `@builder` | Final judge validation |
|---|---|---|---|---|---|
| 01 | Product Owner | Confirm business meaning and target beneficiary population | Decide v1 scope and acceptance criteria | Validate real migrated-data behavior | Accept or record blockers |
| 02 | Requirements Engineer | Capture candidate rules with evidence | Write EARS requirements with REQ-IDs and `source_legacy:` | Keep code/tests tied to requirements | Verify traceability |
| 03 | Enterprise Architect | Identify external systems, batch sources, and constraints | Validate context and integration decisions | Check implementation still fits context | Review unresolved architecture blockers |
| 04 | Software Architect | Observe boundaries emerging from legacy evidence | Define module boundaries, ADRs, and implementation plan | Guard boundaries during code generation | Confirm deviations are documented |
| 05 | Technical Lead | Track risks and sequence | Keep tasks small and implementable | Enforce standards and self-review before PR | Confirm C3 submission readiness |
| 06 | Developer | Understand legacy behavior before coding | Estimate implementation path from tasks | Implement Java/Next.js slice and tests | Fix judge-reported defects if rejected |
| 07 | DBA | Profile DDM/FDT fields and source population | Design source-to-target mapping and recovery | Load PostgreSQL, reconcile, and prove rerun safety | Prove no unexplained losses |
| 08 | QA Engineer | Define evidence needed for acceptance | Define tests and reconciliation checks | Run happy/error paths and data checks | Verify all required tests and data evidence |
| 09 | DevOps Engineer | Confirm local tools and pre-work readiness | Review execution constraints | Keep required CI jobs green for submission | Provide CI evidence |
| 10 | Tech Writer | Maintain glossary and discovery notes | Keep spec/ADRs readable and consistent | Update README/run notes from real commands | Ensure checklist and PR text are clear |

---

## Stage checklists

### Stage 1 — `@archaeologist` + `@dba`

- Read the Natural/Adabas sources for the fixed capability.
- Capture rules, glossary terms, data fields, relationships, and open questions with source citations.
- Agree the complete authorized beneficiary population for migration and consultation.
- Do not write requirements without evidence; record unknowns honestly.

**C1 self-check:** discovery artifacts cite sources, data facts are recorded, and no rule is promoted without evidence.

### Stage 2 — `@architect` + `@dba`

- Convert confirmed rules into EARS requirements with REQ-IDs and `source_legacy:`.
- Define scope, out-of-scope, module boundaries, and ADRs only for real decisions.
- Design migration, reject handling, reconciliation, rerun/resume, and recovery.
- Define tests for listing, search, detail, and data reconciliation before coding.

**C2 self-check:** formal artifacts are traceable, implementation tasks are small, and data acceptance is testable.

### Stage 3 — `@builder` + `@dba`

- Implement only the scoped consultation capability.
- Populate PostgreSQL from the approved source route; do not replace migration with sample seed data.
- Run backend `mvn verify` and frontend tests if a frontend exists.
- Keep required CI green and document real commands/results.

**C3 self-check:** CI green, tests pass, every requirement is traceable, source count = loaded + explained rejects, rerun has no duplicates, and listing/search/detail cover the complete migrated beneficiary population.

---

## Suggested reading order

- [ ] Read [OVERVIEW.md](../05-personas/OVERVIEW.md) to see the one-person role checklist.
- [ ] Read the `PERSONA.md` files most relevant to the current stage.
- [ ] Open the current stage agent README in [`06-stage-agents/`](../06-stage-agents/).
- [ ] Activate the stage agent in Copilot Chat and begin working.

## References

- [Agent kits](../06-stage-agents/README.md)
- [Agent architecture](4-agents-explained.md)
- [Challenge flow](../00-TEAM-FLOW.md)
- [Persona kits](../05-personas/README.md)

---

### Continue reading

| Previous | Next |
|---|---|
| [Four Agents Explained](4-agents-explained.md)<br/><sub>Why the challenge uses stage agents plus `@dba`.</sub> | [Challenge Flow](../00-TEAM-FLOW.md)<br/><sub>Schedule and self-checkpoints.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
