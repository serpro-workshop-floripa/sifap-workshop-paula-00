# Template: Migration Plan Support

> **Path:** [Team Kit](../../README.md) > [Data migration](../DATA-MIGRATION.md) > **Migration plan**

**The participant completes this in Stage 2 with `/migration phase=plan`; link it from the feature's formal `plan.md`.**

| Field | Participant decision |
|---|---|
| Feature / REQ-IDs / formal spec and plan | <!-- fill in --> |
| Covered roles (DBA / Architecture / QA / Developer / PO) | <!-- fill in --> |
| Source readiness and archaeology evidence | <!-- fill in --> |
| Authorized population and consultation scope | <!-- fill in --> |
| Approval status and blockers | <!-- fill in: do not pre-approve --> |

## Extraction contract

| Property | Decision / evidence / missing information |
|---|---|
| Source version, snapshot boundary, related files and concurrent writes | <!-- fill in --> |
| Supported extraction interface, format and version | <!-- fill in --> |
| Layout, encoding, source keys, manifest, and integrity checks | <!-- fill in --> |
| Completeness validation and authorized restricted storage | <!-- fill in --> |

## Migration and recovery design

| Concern | Planned approach | Governing requirement / evidence | Owner |
|---|---|---|---|
| Source-to-target mapping and lineage | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Schema version and module ownership | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Staging, validation and dependency-aware load order | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Rejects and approved remediation | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Batch/transaction boundaries and duplicate prevention | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Checkpoints, interruption, replay and resume | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Target recovery and unrelated data protection | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Application compatibility and cutover boundary | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

## Verification planned before implementation

| Check | Test / inspection method | Expected acceptance rule | Task / self-check |
|---|---|---|---|
| Full source-key coverage and record accounting | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Field/relationship/occurrence preservation | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Agreed financial aggregates | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Authorized listing/search/detail across all beneficiaries | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |
| Rerun/resume and target recovery | <!-- fill in --> | <!-- fill in --> | <!-- fill in --> |

- [ ] Formal requirements retain `REQ-NNN`, acceptance criteria, and `source_legacy:`.
- [ ] DBA, Architecture, QA, and PO responsibilities were reviewed during the C2 data self-check.
- [ ] Missing extraction, mapping, or acceptance decisions remain blockers.
