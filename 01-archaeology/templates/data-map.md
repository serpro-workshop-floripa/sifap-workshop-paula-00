# Template: Source Data Map

> **Path:** [Team Kit](../../README.md) > [Stage 1](../README.md) > **Templates** > **Data map**

**DBA-owned record of the data definitions and population the team actually investigates in Stage 1.**

> [!NOTE]
> Use `/map-source-data` with `@archaeologist` and the DBA after guided source reading.
> Write findings to `01-archaeology/data-map.md`, not into this template.
> No field mapping, count, interpretation, or approval is supplied here.

| Field | Team evidence |
|---|---|
| Participant / DBA-QA review evidence / date | <!-- fill in --> |
| Source version and authorized reading scope | <!-- fill in --> |
| DDM/FDT coverage and missing definitions | <!-- fill in --> |
| Population evidence reference | <!-- fill in: measured source or BLOCKED; not a seed estimate --> |
| Status | <!-- fill in: draft / awaiting evidence / ready for review --> |

## Source files and identifiers

| DDM / FDT | Observed file binding | Declared keys / descriptors | Code access evidence | Open question |
|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in: actual path:line --> | <!-- fill in --> |

## Field-level evidence

Duplicate rows for the fields actually examined. Keep logical format, physical
storage, and program declarations separate. Do not infer SQL precision from an
ambiguous packed length or treat null suppression as a required-value rule.

| Source field / logical name | Format / length / scale as declared | Storage / descriptor markers | Group / occurrence bounds | Observed meaning and evidence | Uncertainty |
|---|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in: source path:line --> | <!-- fill in --> |

## Relationships and access

| Source relationship | Reader / writer evidence | Declared or observed? | Integrity not established | Owner |
|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in: path:line --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Population and quality

Use the [source readiness template](../../docs/data-migration/source-readiness.template.md)
for authorization, measured counts, snapshot/extraction capability, and restricted
evidence references. Never copy beneficiary records into this document.

| Source population | Measurement method / time | Count / coverage | Quality observation | Evidence reference / blocker |
|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Cross-source questions

| Question | Code evidence | DDM/FDT or historical evidence | Impact / owner | Mystery record reference |
|---|---|---|---|---|
| <!-- fill in: question, not answer --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in: reader-assigned ID or BONUS --> |

## C1 self-check for architecture

| Evidence or blocker | Effect on later migration planning | Responsible role | Self-check result |
|---|---|---|---|
| <!-- fill in --> | <!-- fill in: no approved target design here --> | <!-- fill in --> | <!-- fill in only after actual self-check --> |

## Completion checks

- [ ] Every populated row cites evidence from actual reading or measurement.
- [ ] Unread fields and missing physical definitions remain explicit.
- [ ] Seed recipes, archived FDT statistics, and current population measurements are distinguished.
- [ ] MU/PE occurrences, identifiers, numeric/date semantics, and data-quality gaps are recorded without silently choosing a resolution.
- [ ] DBA and QA responsibilities were reviewed against evidence; no PostgreSQL model or C1 approval was fabricated.

## References

- [Stage 1 guide](../GUIDE.md)
- [Data migration lifecycle](../../docs/DATA-MIGRATION.md)
- [Declaration dictionary template](program-data-dictionary.md)
