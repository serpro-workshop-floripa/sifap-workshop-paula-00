# Start here: individual challenge pre-work

> **Track:** [Individual challenge kit](README.md) › **Start here**

Use this page before the 14:00 start. The challenge starts directly in `@archaeologist`; there is no opening block during the timed exercise.

![Start](https://img.shields.io/badge/Start-00-171717?style=flat-square) ![When: before 14:00](https://img.shields.io/badge/When-Before%2014%3A00-737373?style=flat-square) ![Audience: individual participant](https://img.shields.io/badge/Audience-Individual-A3A3A3?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | One participant working alone |
| **Prerequisites** | Git, VS Code, Copilot, Spec-Kit, Java, Node, Docker, repository clone, and authorized populated Adabas source/extraction route ready before 14:00 |
| **Estimated time** | 15 minutes of reading after setup |
| **Expected result** | You know what to open at 14:00, how to self-check C1/C2/C3, and how to submit |

---

## Pre-work checklist (complete before 14:00)

- [ ] Follow [`00-SETUP.md`](00-SETUP.md) and verify your laptop tools.
- [ ] Clone your own private repository and create or pull `develop`.
- [ ] Confirm Copilot Ask, Plan, Agent, and the stage agents load in VS Code.
- [ ] Install and verify official Spec-Kit (`specify version`).
- [ ] Confirm the local legacy sources are present under [`01-archaeology/legacy-sifap/`](01-archaeology/legacy-sifap/).
- [ ] Confirm the authorized, populated Adabas source and supported extraction route are ready; keep credentials out of Git.
- [ ] Read the challenge flow in [`00-TEAM-FLOW.md`](00-TEAM-FLOW.md) and Git rules in [`00-GIT-WORKFLOW.md`](00-GIT-WORKFLOW.md).
- [ ] Open the visual glossary: [`07-concepts/03-visual-glossary.md`](07-concepts/03-visual-glossary.md).
- [ ] Skim all 10 role responsibilities in [`05-personas/`](05-personas/). You cover them yourself; roles are skills, not teammates.

> [!IMPORTANT]
> Do not run parallel sub-agent orchestration, worker harnesses, or Copilot CLI fan-out during the challenge. Use Copilot Ask, Plan, and Agent modes with the active stage agent.

---

## At 14:00: open `@archaeologist`

At 14:00, open Copilot Chat in VS Code and select `@archaeologist`.

Use the first prompt to begin Stage 1:

```text
@archaeologist Start Stage 1 for the individual SIFAP challenge. Help me discover the legacy rules for listing, searching, and viewing all beneficiaries migrated from Adabas to PostgreSQL. Keep every finding tied to legacy files and lines, and prepare me for checkpoint C1.
```

Use `@dba` when data-source discovery, DDM/FDT interpretation, extraction, or reconciliation questions appear.

---

## Challenge schedule

Reference budgets are in [`00-TEAM-FLOW.md`](00-TEAM-FLOW.md):

| Time | Step | Agent | Checkpoint |
|---|---|---|---|
| 14:00-14:50 | Stage 1 — Archaeology | `@archaeologist` + `@dba` as needed | C1 |
| 14:50-15:30 | Stage 2 — Specification | `@architect` + `@dba` as needed | C2 |
| 15:30-17:10 | Stage 3 — Implementation and data migration | `@builder` + `@dba` | C3 submission |
| 17:10-17:40 | Final judge validation | Judge | Acceptance or rejection |

The fixed target capability is to consult — list, search, and detail — **all** beneficiaries migrated from Adabas to PostgreSQL, applying the validation rules you discover from the legacy system.

---

## Self-checkpoints

C1, C2, and C3 replace handoffs. Before switching agents, check your own artifacts against the same definition of done.

- **C1 (end of Stage 1):** legacy programs/DDMs read, business rules recorded with evidence, data questions and blockers captured.
- **C2 (end of Stage 2):** EARS requirements, REQ-IDs, `source_legacy:`, plan, tasks, ADRs, and migration design are traceable.
- **C3 (end of Stage 3):** implementation, tests, data load, reconciliation, rerun behavior, and consultation coverage are ready for the submission PR.

If you are stuck for 20 minutes, ask workshop support and record the blocker. Reduce capability breadth if needed, never the migrated population or verification standard.

---

## Finish line

Your submission is accepted only if all of these pass:

1. CI is green, including `legacy-traceability` and test jobs.
2. Every requirement has a REQ-ID, EARS wording, and `source_legacy:`.
3. Tests pass: backend `mvn verify`; frontend tests if a frontend was built.
4. Data is reconciled: source count = loaded + explained rejects; source keys and agreed aggregates reconcile; no unexplained losses; rerun without duplicates.
5. Listing, search, and detail cover the complete migrated beneficiary population, not a sample or first page.

---

## How to submit

1. Work in your own repository.
2. Create `spec/<NNN>-<feature>` from `develop` during Stage 2.
3. Create `impl/<NNN>-<feature>` from `develop` during Stage 3.
4. Open the submission PR from `impl/<NNN>-<feature>` to `develop`.
5. Complete the PR checklist in [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).
6. Notify the judge.

The PR creation time is the submission timestamp. The first two participants whose submissions pass judge validation win. The submission deadline is 17:10; rejected submissions may be fixed and resubmitted with a new timestamp.

---

### Continue reading

| Previous | Next |
|---|---|
| [Individual challenge kit](README.md)<br/><sub>Main hub for this repository.</sub> | [Challenge flow](00-TEAM-FLOW.md)<br/><sub>14:00-17:40 schedule, C1/C2/C3, finish line.</sub> |

<sub>[Back to the kit index](README.md)</sub>
