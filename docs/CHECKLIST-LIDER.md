# Participant Self-Checklist

![Checklist](https://img.shields.io/badge/Type-Checklist-171717?style=flat-square)
![Participant](https://img.shields.io/badge/Scope-Individual%20challenge-737373?style=flat-square)
![Duration](https://img.shields.io/badge/Duration-14%3A00%E2%80%9317%3A40-A3A3A3?style=flat-square)

> **Path:** [Team Kit](../README.md) › [Docs](README.md) › **Participant Self-Checklist**

**Chronological checklist for one participant** — use it at C1, C2, C3, and the finish line. The full schedule lives in [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md).

| Field | Value |
|---|---|
| **Target audience** | Individual workshop participant |
| **Prerequisites** | Setup complete before 14:00; read [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) |
| **Expected outcome** | Submission PR is ready for judge validation with honest evidence |

---

## Before 14:00 — pre-work only

- [ ] Git, VS Code, Copilot, Spec-Kit, Java 21, Node, Docker, and repository access are ready.
- [ ] The repository is cloned and `develop` is available.
- [ ] The authorized, populated Adabas source route or extraction is ready for Stage 1 discovery.
- [ ] You have skimmed the [persona overview](../05-personas/OVERVIEW.md) and know that you cover all 10 roles yourself.
- [ ] You can select `@archaeologist`, `@architect`, `@builder`, and `@dba` in Copilot Chat.

---

## Stage 1 — Archaeology (`@archaeologist` + `@dba`)

- [ ] Read the legacy programs and DDM/FDT evidence needed for the fixed beneficiary consultation capability.
- [ ] Record business rules with source citations; leave unproven interpretations as questions.
- [ ] Record glossary terms and legacy field meanings.
- [ ] Profile the complete authorized beneficiary population and document the source facts needed for migration.
- [ ] Apply the 20-minute rule: if blocked, ask workshop support and record the blocker.

### C1 self-check — before switching to `@architect`

- [ ] Discovery artifacts identify the legacy files actually read.
- [ ] Candidate rules are backed by cited evidence or explicitly marked unconfirmed.
- [ ] Data discovery includes source population, keys, fields, anomalies, and extraction assumptions.
- [ ] The scope candidate is thin enough for Stage 3 but does not reduce the migrated population or verification standard.

---

## Stage 2 — Specification (`@architect` + `@dba`)

- [ ] Write EARS requirements with unique `REQ-NNN` IDs.
- [ ] Include a `source_legacy:` line for every requirement.
- [ ] Define scope/out-of-scope for listing, search, and detail over all migrated beneficiaries.
- [ ] Document architecture/module decisions and ADRs only where a real choice exists.
- [ ] Design source-to-target mapping, reject handling, reconciliation, rerun/resume, and recovery.
- [ ] Define tests and acceptance checks before implementation starts.

### C2 self-check — before switching to `@builder`

- [ ] Every formal requirement has REQ-ID, EARS wording, acceptance criteria, and `source_legacy:`.
- [ ] Tasks are small enough to execute during Stage 3.
- [ ] Data acceptance can prove source count = loaded + explained rejects.
- [ ] Listing, search, and detail checks cover the complete migrated population, not a sample.
- [ ] No Stage 3 task depends on unpublished instructor assets or hidden answers.

---

## Stage 3 — Implementation and data migration (`@builder` + `@dba`)

- [ ] Implement the scoped backend and frontend only as needed for the beneficiary consultation capability.
- [ ] Keep tests tied to REQ-IDs through inline comments or clear names.
- [ ] Load PostgreSQL from the approved source route; do not replace migration with seed data.
- [ ] Reconcile source records, rejects, keys, and agreed aggregates.
- [ ] Verify rerun safety: no duplicates and no unexplained losses.
- [ ] Update README/run notes with real commands and outcomes.
- [ ] Keep the required CI jobs green for the submission PR.

### C3 self-check — before opening the PR

- [ ] Backend `mvn verify` passes.
- [ ] Frontend tests pass if a frontend was built.
- [ ] CI is green, including `legacy-traceability` and test jobs.
- [ ] Every requirement remains traceable to legacy evidence.
- [ ] Data reconciles: source count = loaded + explained rejects, with no unexplained losses.
- [ ] Listing, search, and detail reach all migrated beneficiaries, including records beyond the first page.
- [ ] The PR branch is `impl/<NNN>-<feature>` and targets `develop`.

---

## Finish line — judge validation

- [ ] Open the submission PR and fill in the checklist honestly.
- [ ] Notify the judge before the submission deadline.
- [ ] If rejected, fix the reported issue and resubmit; the new PR update timestamp counts.
- [ ] Preserve evidence for any unfinished work or blocker. An honest verified increment is better than an unproven claim.

The first two participants whose submission passes judge validation win. The judge's verification replaces cross-review and uses private validation assets that are not published in this kit.

---

## Three questions to ask yourself every 20 minutes

```text
1. Am I blocked, guessing, or missing evidence?
2. Is the next C1/C2/C3 self-check still achievable?
3. Are CI, tests, and data reconciliation getting safer or riskier?
```

If the answer reveals a blocker, ask workshop support and record the issue instead of hiding it.

---

## Emergency responses

| Situation | Participant action |
|---|---|
| You lack direction for 15 minutes | Restate the current stage objective and choose the smallest evidence-backed next step. |
| CI fails | Stop feature expansion and fix the required check. |
| New evidence requires a scope change after C2 | Update spec/plan/tasks and repeat the affected self-check; never hide data loss by shrinking scope. |
| You want to refactor without an existing test | Stop. Add or identify the test first. |
| Thirty minutes remain and reconciliation fails | Record the blocker, prioritize the defect, and do not claim migration success. |
| Copilot is unavailable | Use Plan B in [troubleshooting.md](troubleshooting.md#plan-b--copilot-outage). |

---

### Continue reading

| Previous | Next |
|---|---|
| [Challenge Flow](../00-TEAM-FLOW.md)<br/><sub>Complete 14:00–17:40 schedule.</sub> | [Lessons Learned](lessons-learned.md)<br/><sub>Common mistakes.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
