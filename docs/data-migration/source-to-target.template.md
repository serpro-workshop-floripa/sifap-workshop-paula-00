# Template: Source-to-Target Mapping

> **Path:** [Team Kit](../../README.md) > [Data migration](../DATA-MIGRATION.md) > **Mapping**

**Complete from the team's Stage 1 data map and declaration dictionary; no SIFAP target model is supplied.**

| Field | Value |
|---|---|
| Source version / data-map and dictionary references | <!-- fill in --> |
| Feature / requirements / design reference | <!-- fill in --> |
| DBA / architect reviewer / approval state | <!-- fill in --> |

## Mapping rows

| Source file / field / evidence | Logical format and physical representation | Target owner / field / type | Conversion, null and precision policy | Source-key / relationship / occurrence lineage | Validation / reject rule |
|---|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Ambiguities requiring review

| Question | Competing evidence | Potential data loss or behavior change | Owner / required decision |
|---|---|---|---|
| <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Mapping tests

| Mapping row / REQ-ID | Scenario | Expected outcome from evidence | Test reference / status |
|---|---|---|---|
| <!-- fill in --> | <!-- fill in: boundaries, nulls, leading zeros, invalid values, MU/PE order --> | <!-- fill in --> | <!-- fill in --> |

- [ ] Every relevant source field has a destination or explicit approved treatment; no silent discard.
- [ ] Source identifiers, decimal precision, date/null semantics, and MU/PE meaning are preserved.
- [ ] Physical byte lengths are not mistaken for numeric precision.
- [ ] Normalization choices and exceptions were reviewed with architects.
- [ ] Unknown meanings remain blocked until evidence or a recorded decision resolves them.
