---
description: "Use when writing database repositories, Flyway schema changes, Adabas-to-PostgreSQL data migration, reconciliation, SQL queries, indexes, and recovery-safe data changes."
applyTo: "backend/src/main/java/**/infrastructure/**,backend/src/main/resources/db/migration/**"
---
# Database Conventions - Schema, Data Migration, and Repositories

This file governs persistence code and schema migrations in PostgreSQL 16.
It covers source-derived loads, migration safety, queries, and recovery.
Entity boundaries belong to [modular-monolith.instructions.md](modular-monolith.instructions.md);
legacy interpretation belongs to [natural-adabas.instructions.md](natural-adabas.instructions.md).
The [DBA data lifecycle](../../docs/DATA-MIGRATION.md) defines stage ownership and acceptance.

## Schema Evolution and Record Migration

Flyway migrations are versioned, forward, and immutable after application to a
shared database. Name them `V<n>__<snake_case_description>.sql`, following the
existing sequence. One logical schema change per file; never edit an applied
checksum or disguise drift with blanket `IF NOT EXISTS`.

Schema history is not a record-migration log. Loading Adabas data additionally
requires a reviewed source snapshot, mappings, source-key lineage, run manifest,
checkpoint/resume, duplicate prevention, record accounting, and recovery.
Keep large data transfers separate from schema migrations.

- Start from a verified populated, authorized source; do not substitute generated PostgreSQL seeds.
- Preserve immutable restricted input and use dependency-aware, bounded transactions.
- Validate records at boundaries; explicitly report rejects and errors rather than dropping, truncating, coercing, or defaulting them silently.
- Define how replay/resume works for the same snapshot and how unrelated target data is protected.
- QA independently verifies key sets, fields, relationships, MU/PE occurrences, and agreed aggregates before C3.

## Monetary Values, Identifiers, and Source Fidelity

Money and packed decimal values map to PostgreSQL `NUMERIC(precision, scale)`
and Java `BigDecimal`, never `float`, `double`, `real`, or `money`.
Establish integer digits, fractional digits, sign, and physical encoding from
actual DDM/FDT, program, and runtime evidence. Physical bytes are not SQL
precision. Preserve leading zeros in identifiers and record date, time-zone,
null/suppression, and empty-value semantics explicitly.

Normalize structured MU/PE data into related tables unless measured evidence
and a reviewed decision justify another representation. Preserve occurrence
identity and ordering when required by source behavior.

## Repositories and Consultation

Use Spring Data derived queries or JPQL `@Query` with named bound parameters.
Native queries also bind values; identifiers and sort choices require explicit
allow-lists. Never concatenate user input into SQL.

- Keep application transaction boundaries in services, not repository annotations.
- Return `Optional<T>` for potentially absent single records.
- Use projections where appropriate and avoid unnecessary sensitive fields.
- Provide stable bounded pagination and authorization for listing, search, and detail.
- Test coverage of all beneficiaries in the approved source population, not only a sample or first page.
- Preserve append-only audit history; no audit deletion as a migration shortcut.

## Indexes and Constraints

Declare reviewed constraints and indexes in versioned schema migrations.
Uniqueness, foreign keys, and `CHECK` constraints require source or approved
specification evidence; they must not hide unresolved legacy contradictions.

Choose indexes using the actual query shape, selectivity, plan, and write cost.
A `WHERE`/`JOIN` column or sequential scan is not sufficient justification.
For large live tables, evaluate concurrent index creation and lock duration;
`CREATE INDEX CONCURRENTLY` cannot run inside a transaction block, so document
the required Flyway transaction configuration and failure recovery.

## Recovery-Safe Changes

Use the safe-migration expand/backfill/contract
procedure when compatibility requires it:

| Phase | Work | Safety condition |
|---|---|---|
| Expand | Add compatible nullable structures | Existing application still operates |
| Backfill / migrate | Transfer records in resumable batches | Explicit validation, accounting, and checkpointing |
| Contract | Retire obsolete structures only after verification | Readers migrated and rollback/recovery window reviewed |

Do not promise every destructive change is reversible. Record a tested recovery
or forward-correction strategy using the tooling actually installed. Do not
assume `flyway undo` is available or put an unrecognized `.undo.sql` file in the
forward-migration location.

Test data recovery independently of schema evolution in an isolated target.
Never reset or modify the source to make reconciliation pass.

## Query Performance and Execution Safety

Use query-optimization for plan analysis.
Investigate N+1 with actual calling loops and fetch behavior; collection fetch
joins can change pagination semantics and must be verified.

`EXPLAIN ANALYZE` executes the statement. Use authorized read-only queries on
isolated representative data; it is not a safe inspection wrapper for arbitrary
writes or side-effecting functions. Keep plans and logs sanitized.

## Convenções

| Rule | Rationale |
|---|---|
| Immutable `V<n>__snake_case.sql` | Auditable schema history |
| Separate schema and data-run evidence | Flyway does not establish record migration success |
| `NUMERIC` / `BigDecimal` with evidence-backed precision | Exact financial values |
| Parameter binding and service transactions | Safe queries and explicit transaction boundaries |
| Measured indexes and reviewed constraints | Preserve meaning without speculative performance changes |
| Replay/resume and isolated recovery tests | Reliable data movement without source mutation |

## Faça / Não faça

| Do | Do not |
|---|---|
| Create a new forward migration | Edit an applied schema migration |
| Load the approved source snapshot | Call a new test seed a migration |
| Account for every source record | Silently drop rejects or narrow the population |
| Verify query coverage and authorization | Accept a mocked or sample-only screen |
| Test recovery with actual tools | Assume schema rollback restores the dataset |

## Checklist antes de abrir um PR

- [ ] Source definitions and approved mappings trace to actual evidence.
- [ ] Applied Flyway files remain unchanged; schema and record pipelines are distinct.
- [ ] Identifiers, exact decimals, null/date semantics, and MU/PE meaning are preserved.
- [ ] Queries bind parameters, use reviewed indexes, and respect access boundaries.
- [ ] Independent reconciliation has no unresolved differences or beneficiary gaps.
- [ ] All authorized beneficiaries are queryable through the real application.
- [ ] Replay/resume and target recovery were tested without changing the source.
- [ ] Sensitive records, extracts, credentials, and detailed rejects remain outside Git.
