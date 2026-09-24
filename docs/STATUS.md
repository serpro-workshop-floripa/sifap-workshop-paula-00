# Challenge STATUS — Progress Dashboard

> **Path:** [Individual challenge kit](../README.md) › [Docs](README.md) › **STATUS**

Use this one-page template to track your own progress, self-checkpoints, evidence, and blockers during the 14:00-17:40 individual challenge.

![Dashboard](https://img.shields.io/badge/Dashboard-Challenge%20status-171717?style=flat-square) ![Update](https://img.shields.io/badge/Update-at%20C1%2FC2%2FC3-737373?style=flat-square) ![Owner](https://img.shields.io/badge/Owner-Participant-A3A3A3?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Individual participant |
| **Update frequency** | At C1, C2, C3, and whenever blocked |
| **Expected outcome** | Clear record of what is ready, in progress, blocked, and submitted |

---

## Overall status

| Indicator | Status | Notes |
|---|---|---|
| Laptop tools validated | — | Git, gh, VS Code, Copilot, Java, Node, pnpm, Docker, Spec-Kit |
| `develop` ready | — | Branch exists and can receive PRs |
| Stage agents available | — | `@archaeologist`, `@architect`, `@builder`, `@dba` |
| Adabas source readiness verified | — | Authorized populated source and extraction route |
| CI green on submission PR | — | Include `legacy-traceability` and test jobs |
| PostgreSQL population reconciled | — | Source count = loaded + explained rejects |
| Complete beneficiary consultation verified | — | Listing, search, and detail across full migrated population |

---

## Progress across the challenge

| Step | Status | Agent | Time budget | Self-check complete? | Notes |
|---|---|---|---|---|---|
| **Stage 1 — Archaeology** | Not started | `@archaeologist` + `@dba` | 14:00-14:50 | No | — |
| **C1 — Discovery self-check** | Not started | Participant | before Stage 2 | No | — |
| **Stage 2 — Specification** | Not started | `@architect` + `@dba` | 14:50-15:30 | No | — |
| **C2 — Spec self-check** | Not started | Participant | before Stage 3 | No | — |
| **Stage 3 — Implementation and migration** | Not started | `@builder` + `@dba` | 15:30-17:10 | No | — |
| **C3 — Submission PR** | Not started | Participant | by 17:10 | No | — |
| **Judge validation** | Waiting | Judge | 17:10-17:40 | No | — |

**Status legend:** Not started · In progress · Complete · Delayed · Blocked · Submitted · Accepted · Rejected

---

## Self-checkpoint record

### C1 — end of Stage 1

| Check | Status | Evidence / notes |
|---|---|---|
| Legacy programs/DDMs for the target capability read | — | — |
| Business rules cited with file and line evidence | — | — |
| Data questions, source population, and extraction blockers captured | — | — |
| Ready to write requirements in Stage 2 | — | — |

### C2 — end of Stage 2

| Check | Status | Evidence / notes |
|---|---|---|
| `spec/<NNN>-<feature>` created from `develop` | — | — |
| Every requirement has REQ-ID, EARS, and `source_legacy:` | — | — |
| Plan, tasks, ADRs, and migration design are traceable | — | — |
| Tests planned before implementation tasks | — | — |
| Ready to implement in Stage 3 | — | — |

### C3 — submission readiness

| Check | Status | Evidence / notes |
|---|---|---|
| `impl/<NNN>-<feature>` created from `develop` | — | — |
| Backend `mvn verify` passes | — | — |
| Frontend tests pass, if a frontend was built | — | — |
| Data source count = loaded + explained rejects | — | — |
| Source keys and agreed aggregates reconcile | — | — |
| Rerun completes without duplicates | — | — |
| Listing covers complete migrated beneficiary population | — | — |
| Search covers complete migrated beneficiary population | — | — |
| Detail covers migrated beneficiaries from the full population | — | — |
| Submission PR opened: `impl/<NNN>-<feature>` -> `develop` | — | — |

---

## Metrics

| Metric | Target | Current |
|---|---|---|
| Legacy-backed requirements | Every REQ-ID | — |
| `[GREENFIELD]` requirements | Only with justification | — |
| Backend tests | `mvn verify` passes | — |
| Frontend tests | Pass if frontend exists | — |
| Source records accounted for | Complete agreed snapshot; no unexplained loss | — |
| Beneficiaries queryable through modern app | All authorized beneficiaries | — |
| Data rerun and recovery checks | Passed with recorded evidence | — |
| Submission timestamp | Before or at 17:10 | — |

---

## Active alerts

> [!WARNING]
> Add an entry below whenever a blocker or risk appears. If blocked for 20 minutes, ask workshop support and record the blocker.

- [ ] (no current alerts)

---

## Submission outcome

| Item | Value |
|---|---|
| Submission PR | — |
| Submitted at | — |
| Judge status | Waiting / Accepted / Rejected |
| Rejection reason, if any | — |
| Resubmission timestamp, if any | — |

---

### Continue reading

| Previous | Next |
|---|---|
| [Data Migration](DATA-MIGRATION.md)<br/><sub>Source-to-target evidence and acceptance.</sub> | [Git workflow](../00-GIT-WORKFLOW.md)<br/><sub>Submission branch and PR rules.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
