# Template: Reconciliation and Consultation Evidence

> **Path:** [Team Kit](../../README.md) > [Data migration](../DATA-MIGRATION.md) > **Reconciliation**

**DBA records the actual run; QA verifies independently and PO accepts observed outcomes. Leave results unfilled until executed.**

| Field | Run evidence |
|---|---|
| Source version / snapshot / manifest integrity | <!-- fill in --> |
| Pipeline run / mapping version / target schema version | <!-- fill in --> |
| Authorized population | <!-- fill in --> |
| DBA / QA reviewer / execution date | <!-- fill in --> |
| Restricted evidence reference | <!-- fill in: no raw records or access credentials --> |

## Record accounting

| Source file / population unit | Source records | Staged records | Accepted source records | Rejected source records | Unexplained difference / disposition |
|---|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

Compare source dispositions, not unrelated target table counts. Explain any
one-to-many row expansion through the approved mapping and source-key lineage.

## Independent reconciliation

| Check | Source expectation / method | Actual target result | Evidence / reviewer | Pass, fail, or not run |
|---|---|---|---|---|
| Complete key sets, duplicates and source lineage | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Required fields, types, precision, dates, nulls and leading zeros | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Benefit and payment values, statuses and reference periods, record by record | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Relationships and MU/PE occurrences/order | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Agreed aggregate checks, such as totals by program, status and reference period | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Application consultation

| Flow / REQ-ID | Authorized scenario | Complete population or page coverage | Observed outcome / evidence | Gap / owner |
|---|---|---|---|---|
| Listing, including subsequent pages | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Search | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Detail and required related data | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Legacy-to-modern comparison of ordinary and edge-case beneficiaries | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Unauthorized access / sensitive data handling | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Rerun, resume and recovery

| Scenario | Isolated test context | Observed result | Evidence / reviewer |
|---|---|---|---|
| Same snapshot rerun without duplicates | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Interrupted load resume or controlled restart | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Target recovery without changing source or unrelated data | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Acceptance

| Decision | Result / evidence / owner |
|---|---|
| Unresolved rejects or differences | <!-- fill in --> |
| Unqueryable beneficiaries | <!-- fill in --> |
| DBA and independent QA review | <!-- fill in --> |
| PO acceptance or blocking items | <!-- fill in --> |
| Restricted evidence retention and cleanup | <!-- fill in --> |

- [ ] Every source record is accounted for and unexplained differences are zero.
- [ ] Required legacy values, including benefit and payment amounts, match the source record by record, not only in totals.
- [ ] Unresolved rejects and beneficiary gaps were resolved before claiming complete migration.
- [ ] All authorized beneficiaries are queryable, not only samples.
- [ ] Rerun/resume and target recovery were tested.
- [ ] Review and acceptance reflect actual evidence, not copied approvals.
