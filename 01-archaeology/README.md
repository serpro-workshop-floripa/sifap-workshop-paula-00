# Stage 1 — Archaeology

> **Track:** [Team Kit](../README.md) › **Stage 1 — Archaeology**

**Stage 1 overview.** Read this page before opening the GUIDE; it presents the objective, expected artifacts, and participants.

| Field | Value |
|---|---|
| **Target audience** | Individual participant covering all Stage 1 responsibilities |
| **Prerequisites** | Local legacy corpus; source-data readiness pre-work completed before 14:00 |
| **Estimated time** | 50 min (14:00–14:50) |
| **Stage** | Stage 1 — Archaeology |
| **Expected outcome** | Rules catalog, dependency map, glossary, discovery report, and C1 self-check evidence |

![Stage 1](https://img.shields.io/badge/Stage-1%20%C2%B7%20Archaeology-171717?style=flat-square) ![Mandatory gate](https://img.shields.io/badge/Gate-Hard%20Gate-404040?style=flat-square) ![Individual challenge](https://img.shields.io/badge/Format-Individual%20challenge-737373?style=flat-square)

> [!IMPORTANT]
> **Read first:** [`LEGACY-EXPLORATION-CHECKLIST.md`](LEGACY-EXPLORATION-CHECKLIST.md) — mandatory gate before starting Stage 2. No EARS requirement is accepted without traceability to legacy code.

> [!TIP]
> **Use both source and data evidence.** Natural sources, DDMs, the FDT and historical documents are in [`legacy-sifap/`](legacy-sifap/). Code reading can proceed offline; the data-readiness gate additionally needs an authorized populated Adabas source and a supported extraction route. Offline files do not prove current record counts.

---

## What Stage 1 is

**Software archaeology** is the practice of extracting knowledge from legacy systems by systematically reading source code without modifying it. In this workshop, archaeology has a precise objective: gather enough evidence to write traceable requirements in Stage 2.

The SIFAP scenario spans approximately 30 years; see the
[chronology and evidence policy](../README.md#scenario-chronology-and-evidence).
Code and dated documents can disagree. Investigate both before specifying
behavior. The dates and authors the kit stands behind are transcribed from the
source headers in [`legacy-sifap/CHRONOLOGY.md`](legacy-sifap/CHRONOLOGY.md),
and the divergences period documents carry on purpose are listed in
[declared drift](legacy-sifap/DECLARED-DRIFT.md). CI checks source-reference
structure and file existence; human review must establish whether the cited
evidence actually supports the requirement.

---

## Where this fits in the workshop flow

See [Challenge flow](../00-TEAM-FLOW.md) for the 14:00-17:40 schedule, C1/C2/C3 self-checkpoints, and judge validation.

---

## Who works here

The participant starts directly in `@archaeologist` at 14:00 and reads only the Natural programs and DDMs needed for the fixed target capability: consult, search, and view details for all migrated beneficiaries with discovered legacy validation rules. See [`GUIDE.md`](GUIDE.md) for the Stage 1 sequence.

The participant covers DBA, QA, Vision, and Architecture responsibilities themselves. The authorized Adabas source and extraction route are pre-work; Stage 1 records only the evidence needed for C1 and later judge verification.

---

## Stage 1 artifacts

| File | Purpose |
|---|---|
| [`LEGACY-EXPLORATION-CHECKLIST.md`](LEGACY-EXPLORATION-CHECKLIST.md) | **Mandatory gate.** Fixed capability reading scope and completion criteria before Stage 2. |
| [`GUIDE.md`](GUIDE.md) | Step-by-step guide with a timed schedule. |
| [`glossary.md`](glossary.md) | Glossary of SIFAP domain terms and abbreviations. |
| [`business-rules-catalog.md`](business-rules-catalog.md) | Catalog of extracted business rules with mandatory `Source Program`. |
| [`dependency-map.md`](dependency-map.md) | Dependency map between programs and DDMs. |
| [`discovery-report.md`](discovery-report.md) | Discovery report consolidating the stage evidence. |
| [`mysteries-checklist.md`](mysteries-checklist.md) | Traceability checklist for open questions. |
| [`mysteries-found.md`](mysteries-found.md) | Detailed record of open questions with evidence and owner. |
| [Data-map template](templates/data-map.md) | `/map-source-data` generates the team's `data-map.md` during source reading. |
| [Declaration dictionary template](templates/program-data-dictionary.md) | `/map-source-data` generates `program-data-dictionary.md` from examined members. |
| [Reading coverage template](templates/reading-coverage.md) | Kickoff initializes the ledger; readers and QA record actual intervals, not copied completion. |
| [C1 review template](templates/LEGACY-EXPLORATION-CHECKLIST.md) | Unfilled self-check evidence and approval record; the stage checklist remains authoritative. |
| [Data migration records](../docs/data-migration/) | Blank records for source readiness, measured population, mapping, and reconciliation. |

The legacy code is in [`legacy-sifap/`](legacy-sifap/) (shared by the kit).

These documents are generated **during archaeology** through guided prompts and
human review. Templates remain unfilled; only the generated team artifacts
receive findings. The kit contains no worked source map, declaration dictionary,
completed reading ledger, or pre-approved C1 report.

Legacy files under `legacy-sifap/` are read-only exercise inputs. Do not modify them or use them to provision a lab; record findings in the stage artifacts.

---

### Continue reading

| Previous | Next |
|---|---|
| [Team Kit](../README.md)<br/><sub>Main repository hub.</sub> | [Stage 1 GUIDE](GUIDE.md)<br/><sub>50-minute timed schedule for reading the legacy system and cataloging rules.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
