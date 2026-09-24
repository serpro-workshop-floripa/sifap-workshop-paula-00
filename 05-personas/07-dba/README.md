# DBA - Copilot Kit

> **Path:** [Team Kit](../../README.md) > [Personas](../OVERVIEW.md) > **DBA**

**Lead the migration of verified Adabas records to PostgreSQL, from discovery to complete beneficiary consultation.**

| Field | Value |
|---|---|
| Audience | DBA, with QA, architects, PO/RE, Developer, and DevOps |
| Stage | Preparation and Stages 1-3 |
| Expected outcome | Source-derived records, independent reconciliation, complete query coverage, and tested recovery |

## Role

The DBA owns the data lifecycle, not only schema creation. A working schema and
test seed are supporting development artifacts; neither proves an Adabas
migration. Start with the [persona profile](PERSONA.md) and
[data migration guide](../../docs/DATA-MIGRATION.md).

## Active kit

| Artifact | Purpose |
|---|---|
| [DBA agent](../../.github/agents/dba.agent.md) | Data ownership, safe modeling, and evidence-based acceptance |
| [Source mapping prompt](../../.github/prompts/stage-archaeologist-map-source-data.prompt.md) | Guided Stage 1 source map, dictionary, and reading coverage |
| [Migration prompt](../../.github/prompts/persona-dba-migration.prompt.md) | Readiness, planning, implementation, and validation |
| [Query audit](../../.github/prompts/persona-dba-query-audit.prompt.md) | Query correctness, population coverage, authorization, and performance |
| [Database instructions](../../.github/instructions/database.instructions.md) | Schema/pipeline separation and safe repositories |
| [Blank data records](../../docs/data-migration/README.md) | Participant-owned evidence and decisions |

## First actions

- [ ] Before Stage 1, coordinate with the source owner and verify populated Adabas and extraction readiness.
- [ ] During archaeology, use `/map-source-data` with the readers; do not copy a completed mapping or answer mysteries.
- [ ] In Stage 2, co-design the migration with architects and have QA define independent validation.
- [ ] In Stage 3, load the approved snapshot and expose the resulting records through the real application.
- [ ] In final validation, verify reconciliation, replay/resume, recovery, and all-beneficiary query coverage.

## Completion criteria

- [ ] The source population and snapshot are evidenced.
- [ ] The participant produced its own source map and reviewed target decisions.
- [ ] No unresolved rejects or unexplained differences remain.
- [ ] All authorized beneficiaries are queryable through approved application flows.
- [ ] QA independently verifies evidence and PO records actual acceptance.

## References

- [PostgreSQL 16 documentation](https://www.postgresql.org/docs/16/)
- [DDM reading guide](../../01-archaeology/legacy-sifap/adabas-ddms/README.md)
- [Persona profile](PERSONA.md)
