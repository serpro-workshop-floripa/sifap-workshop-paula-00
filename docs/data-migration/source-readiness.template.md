# Template: Source Data Readiness

> **Path:** [Team Kit](../../README.md) > [Data migration](../DATA-MIGRATION.md) > **Source readiness**

**Complete during pre-work before 14:00 and confirm during Stage 1 using `/migration phase=readiness`.**

| Field | Participant evidence |
|---|---|
| Participant / source owner / DBA-QA evidence | <!-- fill in --> |
| Authorized environment identity, without access address or credentials | <!-- fill in --> |
| Source version and synthetic population provenance | <!-- fill in --> |
| Population action performed by authorized owner / evidence | <!-- fill in or BLOCKED --> |
| Measurement time and read method | <!-- fill in --> |
| Approved beneficiary population and required related data | <!-- fill in --> |

## Measured population

| Source file | Seed expectation reference, if known | Current measured count | Integrity / quality observation | Restricted evidence reference |
|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in: recipe only --> | <!-- fill in or unknown --> | <!-- fill in --> | <!-- fill in --> |

## Extraction readiness

| Concern | Evidence / decision / blocker |
|---|---|
| Supported read-only extraction method and owner | <!-- fill in --> |
| Consistent snapshot across related files and concurrent writes | <!-- fill in --> |
| Format, layout, encoding, and source-key availability | <!-- fill in --> |
| Coverage, truncation and integrity checks | <!-- fill in --> |
| Authorized restricted storage, retention, and cleanup | <!-- fill in --> |
| Missing access, capability, or source definitions | <!-- fill in --> |

## Review

| Gate | Result / evidence | Owner / next action |
|---|---|---|
| Populated source verified | <!-- fill in --> | <!-- fill in --> |
| Extractable consistent population | <!-- fill in --> | <!-- fill in --> |
| Baseline evidence check | <!-- fill in --> | <!-- fill in --> |
| Population coverage | <!-- fill in --> | <!-- fill in --> |
| C1 readiness | <!-- fill in: pending / blocked / accepted with evidence --> | <!-- fill in --> |

- [ ] No current count is inferred from a seed recipe or archived FDT.
- [ ] Source administration and sensitive records remain outside this kit.
- [ ] Unavailable source or extraction is an explicit blocker.
