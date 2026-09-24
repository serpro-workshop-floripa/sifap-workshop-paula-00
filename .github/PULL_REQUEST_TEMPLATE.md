# Pull Request

## Description

<!-- Describe what was implemented in this PR. -->

## Stage

- [ ] Stage 1 - Archaeology evidence
- [ ] Stage 2 - Modern specification
- [ ] Stage 3 - Implementation and data migration
- [ ] Submission PR: `impl/<NNN>-<feature>` -> `develop`

## Responsible participant

<!-- Your name or GitHub handle. You cover all role responsibilities yourself in the individual challenge. -->

## REQ-IDs Addressed

<!-- Example: REQ-001, REQ-003 -->

## Submission checklist

- [ ] CI is green, including `legacy-traceability` and test jobs.
- [ ] Every requirement has a REQ-ID, EARS wording, and `source_legacy:`.
- [ ] Backend `mvn verify` passes.
- [ ] Frontend tests pass, if a frontend was built.
- [ ] Data reconciliation proves source count = loaded + explained rejects.
- [ ] Source keys and agreed aggregates reconcile with no unexplained losses.
- [ ] Migration rerun completes without duplicates.
- [ ] Listing covers the complete migrated beneficiary population, not a sample or first page.
- [ ] Search covers the complete migrated beneficiary population.
- [ ] Detail view works for migrated beneficiaries selected from the full population.
- [ ] No sensitive data is exposed in logs, screenshots, commits, or the PR body.
- [ ] Workflow changes, if any, use least-privilege permissions and actions pinned by SHA.

## How to validate

<!-- List the exact commands and evidence locations the judge should use. -->
