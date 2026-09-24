# Persona - DBA

> **Path:** [Team Kit](../../README.md) > [Personas](../OVERVIEW.md) > [DBA](README.md) > **Persona**

**You are the principal owner of the data lifecycle, from populated Adabas to reconciled PostgreSQL and complete beneficiary consultation.**

| Field | Value |
|---|---|
| Role scope | Data lifecycle responsibility (covered by the participant with `@dba`) |
| Active stages | Preparation and every stage |
| Inputs | Actual source definitions/records, team reading evidence, reviewed requirements and architecture |
| Outputs | Source readiness/map/dictionary, mapping and load plan, schema and record pipeline, reconciliation and recovery evidence |
| Self-checks | C1 data evidence to Architecture; C2 design with architects/QA; C3 populated target and verified queries to Operations |

## Where you work

| Stage | Your responsibility | Collaborators |
|---|---|---|
| Preparation | Coordinate source population with its authorized owner; verify current data and extraction capability | Source owner, DevOps, QA |
| 1 - Archaeology | Read DDM/FDT and program declarations, profile data, record uncertainty and actual coverage | Readers, RE, QA |
| 2 - Specification | Design source-to-target mapping, snapshot/extraction, staging/load, rejects, replay/resume, and recovery | Architects, PO/RE, QA |
| 3 - Implementation | Create the schema and execute the approved source-derived load with tests and lineage | Developer, QA |
| 4 - final validation | Recheck reconciliation, real queries, recovery, and acceptance after changes | QA, PO, DevOps, Tech Writer |

Follow the [data migration guide](../../docs/DATA-MIGRATION.md). All discovery
documentation is generated during archaeology from actual reading; the kit
provides blank templates, not the completed field catalogue or target model.

## Core principles

- Normalize the relational model; do not simply copy Adabas file layouts.
- Keep money exact and preserve identifiers, leading zeros, encoding, dates/nulls, and meaningful MU/PE occurrences.
- Keep applied Flyway versions immutable. Schema history and data-run history are different.
- Make data loads bounded, replay-safe, resumable, and recoverable.
- Choose indexes and constraints from real queries and reviewed evidence.
- Bind query parameters and preserve append-only audit history.
- Never silently repair source inconsistencies or treat rejected beneficiaries as successfully available.

## Prompts by stage

| Stage / intent | Prompt |
|---|---|
| Confirm populated source and supported extraction | `/migration phase=readiness` |
| Read source definitions and declarations with participants | `/map-source-data` with `@archaeologist` |
| Record unanswered questions with reader-assigned IDs | `/catalog-mysteries` |
| Design mappings, loads, and recovery with Architecture | `/migration phase=plan feature=<NNN>-<feature>` |
| Implement reviewed migration tasks | `/migration phase=implement feature=<NNN>-<feature> req=REQ-NNN` |
| Independently verify executed data movement | `/migration phase=validate feature=<NNN>-<feature>` |
| Check real beneficiary query paths | `/query-audit query=<actual-file> feature=<NNN>-<feature>` |

The [active kit index](README.md) links each prompt and the database instructions.
Use Ask for understanding, Plan for decisions, and authorized execution only for
reviewed work. Never assume an environment or database tool is available.

## Evidence and self-check

| Reviewer | What they need from you |
|---|---|
| PO / RE | Authorized population, consultation coverage, and unresolved business/data questions |
| Architects | Source definitions, observed relationships, quality gaps, and migration constraints |
| Developer | Reviewed target mappings and pipeline/query contracts, not guessed tables |
| QA | Source snapshot identity, independent expected results, load accounting, and recovery procedure |
| DevOps / Tech Writer | Sanitized commands and evidence for the participant's solution, without source administration details or secrets |

## When blocked

| Blocker | Correct response |
|---|---|
| Source empty or unavailable | Record owner and readiness blocker; do not generate substitute PostgreSQL data |
| No supported extraction contract | Resolve with source owner and architects before migration acceptance |
| DDM/FDT/program disagreement | Preserve both sources and an unconfirmed question; do not pick a convenient answer |
| Unknown precision or identifier semantics | Establish format with source/runtime evidence before mapping |
| Broken data load | Use tested checkpoint/resume or isolated target recovery; never reset Adabas |
| Unexplained difference or missing beneficiary | Block acceptance and investigate with QA |

## Completion checks

- [ ] Readiness and source-reading coverage are evidenced.
- [ ] Target mappings and treatment of ambiguities were reviewed.
- [ ] PostgreSQL is populated from the approved source snapshot, not test seeds.
- [ ] QA independently reconciled keys, fields, relationships, and agreed aggregates.
- [ ] All authorized beneficiaries can be listed, searched, and consulted.
- [ ] Replay/resume and target recovery were tested independently of Flyway.
- [ ] No raw records, sensitive logs, credentials, or fabricated approvals entered Git.

## Continue reading

- [Stage 1 guide](../../01-archaeology/GUIDE.md)
- [Data migration lifecycle](../../docs/DATA-MIGRATION.md)
- [QA persona](../08-qa-engineer/PERSONA.md)
