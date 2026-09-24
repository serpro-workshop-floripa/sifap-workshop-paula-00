# @archaeologist — Stage 1: Archaeology

> **Path:** [Team Kit](../../README.md) › [Stage Agents](../README.md) › **@archaeologist**

**The `@archaeologist` agent guides the participant through a systematic reading of legacy Natural/Adabas code, extracting traceable business rules and mapping dependencies to define the Stage 2 scope.**

| Field | Value |
|---|---|
| **Target audience** | Entire participant during Stage 1, with all participants working in parallel |
| **Prerequisites** | `01-archaeology/legacy-sifap/` available in the workspace |
| **Estimated time** | 11:00–12:00 + 13:30–14:00 |
| **Stage** | Stage 1 — Archaeology |
| **Expected outcome** | Rule catalog with sources, mapped DDMs, open questions, and defined feature scope |

![Stage 1](https://img.shields.io/badge/Stage-1%20%C2%B7%20Archaeology-171717?style=flat-square)
![Investigative approach](https://img.shields.io/badge/Approach-Investigative-404040?style=flat-square)

---

## When to use

Use this agent while the participant reads legacy code. `@archaeologist` helps the participant observe, catalog, and formulate questions. It does not write modern code or invent business rules.

- **Lead:** Requirements Engineer
- **Data lead:** DBA, with independent QA evidence review
- **Strong support:** Tech Writer and Enterprise Architect
- **Hard-gate prerequisite:** read the assigned Natural programs before writing any specification

---

## What the agent does

- Guides line-by-line reading of `.NSN` programs and Adabas DDM structures
- Identifies inputs, processing, outputs, and business rules in each program
- Maps dependencies between programs through `CALLNAT`
- Guides DDM/FDT and declaration reading with DBA; source mapping belongs here, PostgreSQL design belongs in Stage 2
- Records evidence with file paths and line references
- Identifies open questions without inventing answers

---

## What the agent does NOT do

- It does not read legacy code unless the participant opens the file
- It does not turn a hypothesis into a confirmed requirement
- It does not suggest modern architecture (that is the `@architect` role in Stage 2)
- It does not edit files in `01-archaeology/legacy-sifap/` (read-only)

---

## Inputs

| Input | Location |
|---|---|
| Assigned Natural programs | `01-archaeology/legacy-sifap/natural-programs/*.NSN` |
| Adabas DDMs | `01-archaeology/legacy-sifap/adabas-ddms/*.ddm` |
| Exploration checklist | `01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md` |

---

## Expected outputs

| Artifact | Location |
|---|---|
| Business-rule catalog | `01-archaeology/business-rules-catalog.md` |
| Dependency map (Mermaid) | `01-archaeology/dependency-map.md` |
| Source data map and declaration dictionary | `01-archaeology/data-map.md`, `program-data-dictionary.md` (generated through `/map-source-data`) |
| Actual reading coverage | `01-archaeology/reading-coverage.md` |
| Open-question list | `01-archaeology/mysteries-found.md`: four investigation slots per pair, 20 per participant, using the [difficulty/evidence checklist](../../01-archaeology/mysteries-checklist.md) |
| Selected feature scope | Recorded before the 14:00 checkpoint |

Use the [blank templates](../../01-archaeology/templates/) and
[data lifecycle](../../docs/DATA-MIGRATION.md). The participant generates these
documents during archaeology; no complete source analysis or approval is supplied.

---

## How to select the agent in Copilot Chat

- [ ] **Open Copilot Chat** in VS Code (`Ctrl+Alt+I` / `Cmd+Alt+I`).
- [ ] **Select `@archaeologist`** from the agent selector.
- [ ] **Open the first assigned Natural program** in the editor before sending the first prompt.
- [ ] **Paste the opening prompt** below and press Enter.

```text
I am starting Stage 1 — Archaeology.
We have Natural/Adabas code in 01-archaeology/legacy-sifap/.
Help the participant examine the assigned programs and record only evidence
and open questions for the scope we will select. Do not infer answers.
```

---

## Example prompts

| Situation | Useful prompt |
|---|---|
| Unknown Natural program | "Read this program with me and separate input, processing, output, and business rules." |
| Adabas DDM | "/map-source-data: read the selected DDM/FDT and declarations with me; record evidence and unknowns, not PostgreSQL decisions." |
| Ambiguous rule | "Do not invent an answer. Record it as a mystery with a hypothesis, evidence, and impact." |
| CALLNAT | "Map who calls whom and generate a simple Mermaid diagram." |

---

## Definition of Done

- [ ] The pair read every assigned Natural program in full.
- [ ] Every rule considered for the scope has `source_legacy:` with a file and line.
- [ ] The participant consulted DDMs and dependencies when they affect the selected feature.
- [ ] Open questions are recorded without invented answers.
- [ ] The discovery report is ready for the 14:00 checkpoint.
- [ ] Source map, dictionary, and actual reading ledger were generated from participant evidence.
- [ ] DBA/QA verified populated-source and extraction readiness; missing evidence blocks C1 data acceptance.

---

## Common mistakes

| Symptom | Cause | Correction |
|---|---|---|
| Copilot gives vague generalizations | No file is open in the editor | Open the `.NSN` file and cite the specific section in the prompt |
| Business rule has no source | The participant accepted a hypothesis as fact | Mark it as a mystery until code evidence exists |
| Time is lost detailing out-of-scope areas | No scope decision was made | Select the thin feature before 12:00 and limit reading to it |
| Legacy files are edited | Confusion about the stage's role | `01-archaeology/legacy-sifap/` is read-only |

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage Agents — overview](../README.md)<br/><sub>The 4 agents, schedule, and responsibility matrix.</sub> | [@architect](../02-architect/README.md)<br/><sub>Stage 2: transform evidence into a modern specification.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
