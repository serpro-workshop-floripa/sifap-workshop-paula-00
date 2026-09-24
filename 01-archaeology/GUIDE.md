# Stage 1: Digital archaeology (50 min)

> **Path:** [Team Kit](../README.md) › [Stage 1](README.md) › **GUIDE**

**A 50-minute schedule for reading only the Natural programs and DDMs needed for the fixed consultation capability, recording traceable evidence, and preparing C1.**

| Field | Value |
|---|---|
| **Target audience** | Individual participant covering archaeology, DBA, QA, Vision, and Architecture responsibilities |
| **Prerequisites** | Read [`README.md`](README.md), access the `legacy-sifap/` directory, and complete source-data readiness pre-work before 14:00 |
| **Estimated time** | 50 min (14:00–14:50) |
| **Stage** | Stage 1: Archaeology |
| **Expected outcome** | Candidate rule catalog, measured data baseline, discovery report, and completed C1 self-check |

> [!IMPORTANT]
> **Required gate.** Before writing EARS requirements in Stage 2, the participant must read the Natural programs and DDMs needed for the fixed target capability and have evidence for every selected behavior. Each subsequent formal requirement needs a valid `source_legacy:` or a justified `[GREENFIELD]` marker. The gate is not a quantity target.

---

## Objective

Read the Natural programs and DDMs needed for the fixed target capability, record traceable evidence, and define the beneficiary consultation slice that can become a feature. The objective is not to explain the entire SIFAP Payment Inspection and Administration System, produce encyclopedic documentation, or solve open questions.

The modern system must later hold and show the legacy records of the agreed beneficiary population, not only reproduce its rules. The authorized populated Adabas source and extraction route are pre-work completed before 14:00; during Stage 1, record the measured data baseline that the Stage 3 migration starts from.

---

## Timed schedule

| Time | Activity | Minimum outcome |
|---|---|---|
| 14:00–14:05 | Start directly in `@archaeologist`; confirm the fixed target capability and the pre-work source readiness evidence. | Scope and readiness evidence or blocker recorded. |
| 14:05–14:30 | Guided reading: consultation programs, validation rules, DDMs, inputs, outputs, calls, and domain decisions needed for all-beneficiary list/search/detail. | Notes with paths and line ranges. |
| 14:30–14:40 | Record candidate rules and questions without inferring absent behavior. | Evidence in the catalog and explicit open items. |
| 14:40–14:47 | Consolidate only evidence that supports beneficiary consultation and migration readiness. | Updated catalog and discovery report. |
| 14:47–14:50 | Complete C1 self-check before switching to `@architect`. | Sources, scope, data evidence, and blockers reviewed against the C1 checklist. |

---

## Reading scope

The participant reads only the programs and DDMs needed for the fixed target capability: consult, search, and view details for **all beneficiaries migrated from Adabas to PostgreSQL**, applying the legacy validation rules discovered in the source. Focus on domain decisions and traceability. Do not try to translate every Natural command at this stage.

Start with the consultation and validation paths, then add registration, dependency, payment, program, audit, or batch members only when they provide evidence for fields, filters, validation, related records, or migration readiness. Review the required DDMs for the selected evidence. Mapping every field or proposing the complete PostgreSQL schema is not required at this stage.

The participant records the data inventory of the relevant Adabas files: measured population, keys, related records, data-quality findings, and the supported snapshot/extraction route. Record them in the [data migration records](../docs/data-migration/). The [synthetic legacy dataset](legacy-seed-data/README.md) documents the records the source was populated from; it does not prove what the source currently contains.

---

## What to record

Use the [templates](templates/) for support. For each in-scope candidate rule, record at least:

- a short description of the observed behavior;
- the `.NSN` or `.ddm` path and, when possible, the line range;
- the question that still prevents a conclusion, without turning it into a requirement;
- the rule's impact on the prioritized feature.

The `business-rules-catalog.md` file is the input to the formal specification. Use the [catalog template](templates/business-rules-catalog.template.md) if the file does not exist yet. You can enrich the glossary, dependency map, and open-question register when they help define the scope, but numeric targets do not block the handoff.

> [!IMPORTANT]
> **Exception: open questions have a fixed denominator.** SIFAP contains **20 canonical open-question slots** grouped by investigation area. Use the IDs relevant to the capability you actually read, and record them in [`mysteries-found.md`](mysteries-found.md). Findings outside the list are bonuses and do not change the denominator.

---

## Data discovery versus migration design

- **Stage 1:** record source definitions, keys, actual declarations, relationships, current measured population, and uncertainties.
- **Stage 2:** DBA and architects decide PostgreSQL mappings, snapshot/extraction, load order, reject handling, recovery, and QA acceptance in the formal plan.
- **Stage 3:** implement and execute the approved source-to-target load, reconcile it, and expose real queries.

Follow the [data lifecycle](../docs/DATA-MIGRATION.md). Stage 4 is not part of the individual challenge; judge validation after Stage 3 replaces the former post-change verification block. Source reading can continue offline, but an empty or unavailable Adabas source, or an unverified extraction route, keeps the data-readiness gate blocked. Seed files and archived FDT counts are not current database measurements. Keep restricted records outside Git.

---

## C1 self-check

In the final minutes, the participant verifies the following before switching to `@architect`:

1. the selected thin feature and what remains out of scope, without silently reducing the authorized beneficiary population;
2. the rules that can become requirements, with legacy paths;
3. the open questions that **cannot** become EARS requirements;
4. DDM and dependency references only when they affect the feature;
5. the data evidence: measured source population, agreed beneficiary population, data-quality gaps, and extraction readiness or its blocker.

If the evidence is insufficient to start `.spec/<NNN>-<feature>/spec.md`, record the blocker and reduce capability breadth without reducing the migrated beneficiary population or inventing a source.

---

## Definition of Done

- [ ] The participant read the Natural programs and DDMs needed for beneficiary consultation and legacy validation rules.
- [ ] The selected behavior has evidence in an `.NSN` or `.ddm` file, or is explicitly separated as a greenfield proposal.
- [ ] The catalog identifies the source of each candidate rule.
- [ ] The discovery report records the scope and relevant questions.
- [ ] Measured source population and extraction readiness are recorded; missing evidence remains a blocker.
- [ ] The authorized beneficiary population is confirmed; the feature does not reduce it to a sample.
- [ ] The C1 self-check is complete by 14:50.

---

## References

- [Legacy exploration checklist](LEGACY-EXPLORATION-CHECKLIST.md): C1 gate verification and fixed-capability criteria.
- [Data migration guide](../docs/DATA-MIGRATION.md): data lifecycle and acceptance gates from source readiness to reconciliation.
- [Stage 2 guide](../02-modern-spec/GUIDE.md): the next step after C1.
- [How to read Natural](legacy-sifap/HOW-TO-READ-NATURAL.md): syntax tutorial for non-developers.

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 1 README](README.md)<br/><sub>Stage overview.</sub> | [Legacy exploration checklist](LEGACY-EXPLORATION-CHECKLIST.md)<br/><sub>Required gate before Stage 2.</sub> |

<sub>[Back to the Team Kit index](../README.md)</sub>
