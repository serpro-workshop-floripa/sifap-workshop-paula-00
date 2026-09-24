# Discovery Report — Stage 1: Digital Archaeology

> **Track:** [Team Kit](../README.md) › [Stage 1](README.md) › **Discovery Report**

**Artifact completed by the participant at the end of Stage 1.** Consolidates the archaeology findings and is the primary input for Stage 2.

| Field | Value |
|---|---|
| **Target audience** | Individual participant—consolidation at the end of Stage 1 |
| **Prerequisites** | Completed rules catalog, dependency map, and glossary |
| **Stage** | Stage 1 — Archaeology |
| **Expected outcome** | Document of up to 3 pages with a summary, carving hypotheses, and source artifacts |

> [!IMPORTANT]
> This document consolidates all Stage 1 findings. Complete each section with the participant's evidence-backed conclusions. Without it, the Stage 2 specification has no evidence base.

> [!NOTE]
> Step-by-step guide: [`GUIDE.md`](GUIDE.md).

**Participant**: <!-- fill in -->
**Date**: <!-- fill in: YYYY-MM-DD -->
**Edition**: <!-- fill in -->
**Responsibilities covered**: <!-- fill in: 10 roles covered by the participant -->

---

## 1. Executive summary

<!-- fill in: maximum 5 sentences—what SIFAP, the Payment Inspection and Administration System, is; what it does; and the state of the code -->

---

## 2. What we know (confirmed)

### 2.1 Business rules

<!-- fill in: confirmed rules with EARS candidates—reference business-rules-catalog.md -->

### 2.2 Dependencies

<!-- fill in: edge counts from the dependency map—reference dependency-map.md -->

### 2.3 Data structures

<!-- fill in: summary of data-map.md and program-data-dictionary.md from actual reading -->

### 2.4 Source population and readiness

<!-- fill in: DBA/QA measurements, authorized population, supported extraction evidence, or explicit blockers; not counts assumed from a seed -->

---

## 3. What is risky

### 3.1 Open questions awaiting human validation

| Open question | Evidence (`path:line`) | Impact | Hypothesis (unconfirmed) | Responsible person/area | Status |
|---|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in: path:line --> | <!-- fill in --> | <!-- fill in: unconfirmed --> | <!-- fill in --> | <!-- fill in --> |

### 3.2 Rules with weak evidence

<!-- fill in: rules classified as "Inferred" that require validation -->

---

## 4. Recommended carving hypotheses

> [!NOTE]
> Record only hypotheses supported by the participant's findings, for Architecture to evaluate in Stage 2. Do not invent a fixed number or approve a target model here.

### Hypothesis 1: <!-- fill in: business name -->

- Programs: <!-- fill in -->
- DDMs: <!-- fill in -->
- Rationale: <!-- fill in -->

### Hypothesis 2: <!-- fill in -->

- Programs: <!-- fill in -->
- DDMs: <!-- fill in -->
- Rationale: <!-- fill in -->

### Hypothesis 3: <!-- fill in -->

- Programs: <!-- fill in -->
- DDMs: <!-- fill in -->
- Rationale: <!-- fill in -->

---

## 5. Source artifacts

| Artifact | Path | Status |
|---|---|---|
| Inventory | [inventory.md](inventory.md) | <!-- fill in --> |
| Reading coverage | `reading-coverage.md` (generated from its [template](templates/reading-coverage.md)) | <!-- fill in --> |
| Source data map | `data-map.md` (generated from its [template](templates/data-map.md)) | <!-- fill in --> |
| Declaration dictionary | `program-data-dictionary.md` (generated from its [template](templates/program-data-dictionary.md)) | <!-- fill in --> |
| Source readiness | `docs/data-migration/source-readiness.md` (see [template](../docs/data-migration/source-readiness.template.md)) | <!-- fill in --> |
| Business Rules | [business-rules-catalog.md](business-rules-catalog.md) | <!-- fill in --> |
| Dependencies | [dependency-map.md](dependency-map.md) | <!-- fill in --> |
| Open questions | [mysteries-found.md](mysteries-found.md) | <!-- fill in --> |
| Glossary | [glossary.md](glossary.md) | <!-- fill in --> |

---

## 6. Team approval

- Reviewed by: <!-- fill in -->
- Confidence: <!-- fill in: High / Medium / Low -->
- DBA / QA data-readiness review: <!-- fill in or pending -->
- PO scope and beneficiary population: <!-- fill in -->
- C1 self-check outcome: <!-- fill in: actual evidence or pending -->

Use the [C1 evidence-review template](templates/LEGACY-EXPLORATION-CHECKLIST.md).
No approval is implied by the presence of this file.

---

## Definition of done

- [ ] Summary with no more than 5 sentences.
- [ ] Only evidence-backed boundary hypotheses are recorded.
- [ ] All artifacts have actual status; unfilled fields or missing evidence are not complete.
- [ ] Source map, dictionary, reading coverage, readiness, and mystery gaps are linked.
- [ ] Document is no longer than 3 pages.

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 1 GUIDE](GUIDE.md)<br/><sub>Step-by-step schedule.</sub> | [Stage 2 — Modern Spec](../02-modern-spec/README.md)<br/><sub>C1 self-check and start of EARS.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
