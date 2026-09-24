---
name: "map-source-data"
description: "Guides Stage 1 reading of DDM/FDT and Natural declarations, recording source data and actual reading coverage without supplying a target schema or mystery answers."
argument-hint: "scope=<source-paths> team=<team-name>"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /map-source-data

## Objective

Help the team and DBA discover the source data model through shared reading.
Generate the Stage 1 data map, declaration dictionary, and reading ledger from
the evidence examined in this session, not a prefilled analysis.

## When to Invoke

After `/archaeology-kickoff`, while the participant reads the assigned programs and
the DBA reviews the relevant DDMs and FDT. Continue incrementally as supporting
members are examined.

## Preconditions

- The team selected actual paths under `01-archaeology/legacy-sifap/`.
- The [legacy reading guide](../instructions/natural-adabas.instructions.md) and [Stage 1 guide](../../01-archaeology/GUIDE.md) are available.
- Existing team artifacts are inspected before any update; legacy sources and templates remain unchanged.

## Inputs the Team Must Provide

- `scope` - source paths the participant authorizes for guided reading.
- Team, reader, and DBA identities, or unfilled identity fields.
- Observations and questions the readers have already recorded.
- Measured source-data evidence, if available; otherwise retain a readiness blocker and route to `/migration phase=readiness`.

## What I Will Do

- Open the selected source intervals with the team and ask readers to identify declarations, access patterns, and evidence.
- Record field names, logical formats, physical lengths, keys/descriptors, MU/PE structures, parameter order, and view subsets only from actual source reading.
- Separate declared semantics, comments, measured data, and unresolved interpretations.
- Update `data-map.md`, `program-data-dictionary.md`, and `reading-coverage.md` under `01-archaeology/` using their [blank templates](../../01-archaeology/templates/).
- Cross-link verified access relationships to `/map-dependencies` and reader-identified uncertainties to `/catalog-mysteries`.

## What I Will NOT Do

- Load a completed catalogue or instructor/reference solution as evidence of the team's work.
- Generate all SIFAP findings or mystery answers before the participants read the sources.
- Invent field meanings, SQL precision, runtime counts, signatures, or acceptance.
- Approve PostgreSQL mappings, constraints, indexes, or a migration design in Stage 1.
- Modify source files, populate/reset a database, or copy raw records into Markdown.

## Output Format

| Generated team artifact | Template | Contents |
|---|---|---|
| `01-archaeology/data-map.md` | [Data map](../../01-archaeology/templates/data-map.md) | Evidence-backed source definitions, relationships, population references, and questions |
| `01-archaeology/program-data-dictionary.md` | [Dictionary](../../01-archaeology/templates/program-data-dictionary.md) | Declarations and caller/view context from examined members |
| `01-archaeology/reading-coverage.md` | [Coverage](../../01-archaeology/templates/reading-coverage.md) | Actual intervals, readers, unread scope, and review state |

```markdown
### Reading update
- Sources and intervals examined: <actual paths and intervals>
- Team observations recorded: <references>
- Unread scope and blockers: <explicit gaps>
- Next authorized reading step: <scope agreed with the team>
```

## Definition of Done

- [ ] All three team artifacts exist, without overwriting previous findings.
- [ ] Every populated field or interpretation cites its source.
- [ ] Partial reading and missing runtime evidence remain explicit.
- [ ] Mystery hypotheses remain unconfirmed and IDs remain reader-assigned.
- [ ] No target decision, source count, or human acceptance was fabricated.

## Prompt Body

You are the `@archaeologist`, working with the DBA and participants.

**Step 1 - Establish the reading boundary.**

- Read the inventory and existing team findings. Confirm the next source member or interval.
- Ask the reader what the declaration or access pattern establishes before recording a conclusion.

**Step 2 - Capture source definitions.**

- Use the data-map template for DDM/FDT fields, descriptors, repeating groups, and relationships.
- Distinguish logical declarations from physical bytes and current measurements; do not infer the latter from seed recipes or archived statistics.

**Step 3 - Capture program declarations.**

- Use the dictionary template for local, parameter, imported, view, and copycode-required fields.
- Preserve names, sizes, dimensions, ordering, and source references. Mark unknown meanings as unknown.

**Step 4 - Record coverage and questions.**

- Update only intervals actually read; do not equate file enumeration with completed reading.
- For a reader-identified uncertainty, preserve evidence and an unconfirmed hypothesis. Use `/catalog-mysteries` to record the reader's canonical ID or `BONUS`; do not solve or silently close it.

**Step 5 - Prepare the data checkpoint.**

- Write sanitized findings to the three generated paths, using relative links valid at their output locations.
- Point the DBA to the [data lifecycle](../../docs/DATA-MIGRATION.md) for readiness and Stage 2 planning.
- Leave target design, unresolved questions, and C1 completion to the accountable human reviewers.

## Invocation Example

```text
/map-source-data scope=<DDM-and-program-paths-selected-by-the-team> team=<team-name>
```
