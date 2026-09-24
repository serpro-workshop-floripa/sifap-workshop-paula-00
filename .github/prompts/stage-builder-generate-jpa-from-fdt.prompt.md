---
name: "generate-jpa-from-fdt"
description: "Implements DBA-reviewed source-to-target mappings as JPA entities and Flyway schema changes, preserving source semantics and leaving data-load acceptance to the migration workflow."
argument-hint: "ddm=01-archaeology/legacy-sifap/adabas-ddms/<DDM>.ddm context=<context> package=<java.package> dateformat=<format>"
agent: "builder"
tools: ["read", "search", "edit", "execute"]
---
# /generate-jpa-from-fdt

## Objective

Implement the approved mapping from source DDM/FDT and program evidence into JPA
entities and corresponding Flyway schema changes. Do not decide a new data model
or default MU/PE data to JSONB during code generation.

## When to Invoke

At the beginning of Stage 3, when the team is setting up the data layer for a bounded context.

## Preconditions

- The feature's `.spec/<NNN>-<feature>/spec.md`, `plan.md`, and `tasks.md` contain the approved data ownership, mappings, and requirements
- The DDM file is accessible in `01-archaeology/legacy-sifap/adabas-ddms/`
- The team selected the target package based on the modular monolith design
- DBA and architects reviewed source-key lineage, precision, null/date semantics, and MU/PE treatment; unresolved mappings remain blockers

## Inputs the Team Must Provide

- The path to the DDM file (for example, `01-archaeology/legacy-sifap/adabas-ddms/DDMXXXXX.ddm`)
- The bounded context and target Java package
- The date format used in the legacy system (for example, packed `YYYYMMDD` or alpha `YYYY-MM-DD`)
- The actual source map, declaration dictionary, reviewed source-to-target record, and governing REQ-IDs

## What I Will Do

- Read the DDM and available physical FDT as distinct sources, alongside program declarations
- Map each field to the appropriate Java/JPA type
- Handle MU fields using the reviewed normalized mapping; use JSONB only with an approved evidence-backed exception
- Handle PE groups as embedded `@OneToMany` entities
- Generate the Flyway migration that creates the PostgreSQL table
- Return unknown field semantics to DBA/Architecture rather than generating guessed production fields

## What I Will NOT Do

- Invent business meaning for cryptic field names - unresolved semantics return to DBA/Architecture
- Assume date formats — the team must confirm them
- Create stored procedures — all business logic remains in Java
- Skip MU/PE fields — they are the most difficult part and must be handled explicitly

## Output Format

Two files:

1. JPA entity under the owning backend module's approved persistence package.
2. Flyway migration under `backend/src/main/resources/db/migration/`.

These outputs create schema, not migrated records. Follow
/migration phase=implement and QA reconciliation
for source-to-target population and complete beneficiary consultation.

## Definition of Done

- [ ] The entity compiles without errors
- [ ] Every mapped source field has its approved target or explicit treatment; no silent loss
- [ ] MU fields follow the reviewed normalized mapping; any JSONB exception has evidence and an ADR
- [ ] PE groups use `@OneToMany` with a separate entity class
- [ ] The Flyway migration is valid PostgreSQL 16 DDL
- [ ] No unresolved semantics were replaced by guessed field names, lengths, or types
- [ ] Cryptic fields are referred for human recording as open questions when necessary

## Prompt Body

You are the `@builder`. The team needs to create a JPA entity from an Adabas DDM.

**Step 1 — Review source definitions and the approved mapping.**
Open the specified DDM, available FDT, program declarations, and reviewed
source-to-target record. Extract the mapped definitions without confusing their formats:

- Level number (01 = top-level, 02+ = children)
- Short name (two-character Adabas name)
- Long name (if present in comments or documentation)
- Format: A (alpha), N (numeric), P (packed), B (binary), D (date), T (time)
- Length
- Descriptor type: DE (searchable), MU (multi-value), PE (periodic group), SU (super-descriptor)

Confirm these definitions with the DBA before generating code. If the planned
mapping or source semantics is unresolved, stop that field's implementation and
record the blocker; do not create a guessed column with a FIXME.

**Step 2 — Map types.**
Apply these mapping rules:

| Adabas | Java | JPA | Notes |
|--------|------|-----|-------|
| A(n) | `String` | `@Column(length = n)` | |
| Numeric quantity | Reviewed integer type | `@Column` | Identifiers may require strings to preserve leading zeros |
| Numeric decimal | `BigDecimal` | Reviewed precision and scale | Verify integer and fractional digits |
| Packed decimal | `BigDecimal` | Reviewed precision and scale | Physical byte length is not numeric precision |
| D | `LocalDate` | `@Column` | Ask the team for the source format |
| T | `LocalDateTime` | `@Column` | |
| B(n) | `byte[]` | `@Lob` | Rare |
| MU field | Reviewed collection type | Related table by default | JSONB only with a reviewed exception |
| PE group | `List<EmbeddedEntity>` | `@OneToMany` | Separate entity class |

Implement the Stage 2 choice. If alternatives remain undecided, return to
`/migration phase=plan` rather than making an implicit architecture decision.

**Step 3 — Handle PE groups.**
For each PE group, create a separate `@Entity` class with:

- Its own table
- A `@ManyToOne` back-reference to the parent entity
- All fields within the PE group mapped as in Step 2
- An index field that tracks the occurrence number

**Step 4 — Handle super-descriptors.**
Implement only indexes justified by the approved query pattern. A source
superdescriptor does not automatically imply an equivalent PostgreSQL index:

```java
@Table(indexes = @Index(columnList = "field_a, field_b"))
```

**Step 5 — Preserve unresolved questions.**
For any unclear field, return its source evidence and ambiguity to DBA and the
architects. Do not invent its English meaning, length, or type.

If the field is not yet in `01-archaeology/mysteries-found.md`, tell the team
that a person must record it as an open question with `path:line` evidence. Do not
describe an answer, confirm a hypothesis, or change the catalog status.

**Step 6 — Generate the Flyway migration.**
Write a PostgreSQL 16 DDL script:

- Table name derived from the entity name (snake_case)
- Column types corresponding to the JPA mappings
- JSONB columns for MU fields (if JSONB was selected)
- Separate table for PE groups with a foreign key
- Reviewed keys, relationships, and evidence-backed indexes
- Constraints approved in the plan; null suppression or a comment alone does not establish `NOT NULL`

Number the migration: `V[NNN]__create_[table_name].sql`.

**Step 7 — Verify compilation.**
Ensure that the entity class compiles. Report any problems.

Run the existing targeted mapping/repository tests against PostgreSQL. Keep
source population, record migration, independent reconciliation, and real
beneficiary queries as separate required checks in the [data lifecycle](../../docs/DATA-MIGRATION.md).

## Invocation Example

```
/generate-jpa-from-fdt ddm=01-archaeology/legacy-sifap/adabas-ddms/<DDM>.ddm context=<context> package=<java.package> dateformat=<format>
```
