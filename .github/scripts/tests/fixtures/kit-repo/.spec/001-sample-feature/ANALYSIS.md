# Analysis: Sample Feature

## Evidence inventory

| Source ID | Evidence | Relevance | Confidence |
| --- | --- | --- | --- |
| SRC-001 | `docs/requirements.md` | Governs both requirements | High |

## Gap analysis

| Finding | Affected | Resolution |
| --- | --- | --- |
| Nominal load undefined | NFR-001 | Question Q-001 |

## Options and trade-offs

| Option | Decision |
| --- | --- |
| Validate in the service | Selected in DR-001 |

## Risk register

| Risk | Mitigation |
| --- | --- |
| RISK-001 checksum rule differs by document type | Cover each type in TST-001 |
