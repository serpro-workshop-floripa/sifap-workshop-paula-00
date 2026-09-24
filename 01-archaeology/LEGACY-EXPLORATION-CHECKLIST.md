# Legacy exploration checklist

> **Path:** [Team Kit](../README.md) › [Stage 1](README.md) › **Exploration checklist**

**Required gate before Stage 2.** This checklist ensures that the participant has read the Natural programs and DDMs needed for the fixed target capability and that candidate rules are traceable to the legacy code.

| Field | Value |
|---|---|
| **Target audience** | Individual participant, complete during Stage 1 |
| **Prerequisites** | Access to `legacy-sifap/natural-programs/` and `adabas-ddms/` |
| **Estimated time** | Completed throughout the 50-minute stage |
| **Stage** | Stage 1: Archaeology |
| **Expected outcome** | Complete capability reading matrix and verified C1 criteria |

> [!IMPORTANT]
> **Required gate before Stage 2.** No EARS requirement is accepted without a reference to a Natural program or DDM file. Greenfield requirements (with no legacy equivalent) must be marked `[GREENFIELD]` and justified in writing in the specification.

> [!WARNING]
> In the previous workshop edition, several teams skipped legacy exploration and wrote specifications based only on the modernization brief. The resulting specifications did not preserve the actual business rules from SIFAP's 29-year history as the Payment Inspection and Administration System. This gate is required.

---

## 1. The traceability rule

Every `REQ-ID` in `.spec/<NNN>-<feature>/spec.md` needs a `source_legacy:` line that points to one of these options:

- a Natural member, such as an `.NSP` or `.NSN` file, in `01-archaeology/legacy-sifap/natural-programs/` (preferably with a line range);
- a specific `.ddm` file in `01-archaeology/legacy-sifap/adabas-ddms/`;
- `[GREENFIELD]` with a one-line justification.

CI rejects PRs to `develop` when any `REQ-ID` lacks a `source_legacy:` line. Judge validation checks this after submission, and C2 self-check catches it before implementation.

---

## 2. Fixed target capability: what to read

The participant reads only the programs and DDMs needed to consult, search, and view details for **all beneficiaries migrated from Adabas to PostgreSQL**, applying discovered legacy validation rules. Every source member used as evidence must have a recorded reading interval.

| Investigation area | Typical source evidence | Open-question IDs | Why |
|---|---|---|---|
| Registration and beneficiary identity | `CADBENEF.NSP`, `CADDEPEN.NSP`, `CADPROG.NSP` when they support beneficiary fields or relationships | `SIFAP-M-01` … `M-04` | Registration logic defines central entities and identifiers. |
| Batch and migration boundaries | `BATCHPGT.NSP`, `BATCHREL.NSP`, `BATCHCON.NSP` when they affect source population or reconciliation | `SIFAP-M-05` … `M-08` | Batch flows reveal source movement and module boundaries. |
| Calculation and derived values | `CALCBENF.NSN`, `CALCCORR.NSP`, `CALCDSCT.NSP` when values must be shown or reconciled | `SIFAP-M-09` … `M-12` | Calculations explain migrated values and acceptance aggregates. |
| Validation | `VALBENEF.NSN`, `VALDOCS.NSP`, `VALELEG.NSN` | `SIFAP-M-13` … `M-16` | Validations become tests and legacy rules for beneficiary consultation. |
| Queries, reports, and audit | `CONSBENF.NSP`, `RELPGT.NSP`, `RELAUDIT.NSP` when they define list/search/detail expectations | `SIFAP-M-17` … `M-20` | Read paths feed the consultation API/UI, glossary, and runbook. |

> [!IMPORTANT]
> **There are 20 canonical open-question slots.** This is the only numeric target in Stage 1. The IDs and areas are in [`mysteries-checklist.md`](mysteries-checklist.md); record the ones relevant to the capability in [`mysteries-found.md`](mysteries-found.md). Findings outside the list count as bonuses and **do not** change the denominator.

### Checklist for each program

For each program or DDM used as evidence, record enough reading notes to confirm that you examined it:

- [ ] **Identify the program.** Record its name, author, and year of last modification.
- [ ] **Map the inputs.** Record which DDMs it reads.
- [ ] **Map the outputs.** Record which DDMs it writes.
- [ ] **Record the calls.** Record other programs called through `CALLNAT`.
- [ ] **Catalog candidate rules.** When the program contains a rule relevant to the scope, record it in `business-rules-catalog.md` with `Programa de origem` and a line range.

> [!WARNING]
> A row without `Programa de origem` does not support an EARS requirement.

---

## 3. The four DDMs: field mapping

The participant covers DBA and QA responsibilities and records evidence for the DDMs required by the consultation capability.

| DDM | Owner | Target artifact in PostgreSQL |
|---|---|---|
| `BENEFIC.ddm` | Participant | <!-- define from evidence --> |
| `PAYMENT.ddm` | Participant | <!-- define from evidence --> |
| `SOCPROG.ddm` | Participant | <!-- define from evidence --> |
| `AUDIT.ddm` | Participant | <!-- define from evidence --> |

Review the DDMs required by the selected feature. The complete PostgreSQL mapping belongs to planning and implementation; it is not a prerequisite for starting the specification.

The participant also inventories the measured population of the relevant files. Use the [data migration records](../docs/data-migration/) to distinguish current counts from historical documentation or seed definitions. Record keys, related records, data-quality findings, and the supported snapshot/extraction route. The C1 self-check confirms coverage of all authorized beneficiaries and preserves constraints for mapping and migration planning.

---

## 4. Open-question register

Use [`mysteries-checklist.md`](mysteries-checklist.md) to record open questions without anticipating answers. The register is a catalog of uncertainties, not an answer key or a source of rules.

Record only questions that affect the scope in `mysteries-found.md`. Each entry must contain:

| Field | Description |
|---|---|
| Open question | The question text, without a conclusion |
| Evidence | `path:line` |
| Impact | Effect on the scope |
| Hypothesis | Explicitly marked as unconfirmed |
| Owner | Person or area that can validate it |
| Status | `open` / `awaiting human validation` / `closed after human validation` |

A question can be closed or used as the basis for a rule only after explicit human validation supported by the recorded evidence.

---

## 5. C1 verification before starting Stage 2

At 14:50, the participant checks their own work against this matrix. A red row blocks progression to Stage 2 until recorded as a blocker or fixed.

| Check | Gate criterion |
|---|---|
| Capability reading | The participant confirmed that they read the source members needed for beneficiary consultation and validation rules. |
| Rule catalog | Every in-scope candidate rule has `Programa de origem` completed. |
| Scope | The discovery report identifies a small feature and what was deferred. |
| Open questions | Relevant uncertainties were recorded without becoming requirements. |
| Source data | Pre-work confirmed a populated, authorized Adabas source and a supported, consistent extraction route; the participant recorded baseline evidence for judge verification. |
| Population coverage | The PO confirmed all authorized beneficiaries and the necessary related data; no sample replaced the agreed population. |

---

## 6. Required Stage 2 format

Write EARS requirements only in `.spec/<NNN>-<feature>/spec.md`, using Spec-Kit. Every `REQ-ID` needs an EARS pattern, Given/When/Then criteria, and `source_legacy:`. Do not finalize a requirement until the participant has confirmed the source or greenfield justification during C2.

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 1 guide](GUIDE.md)<br/><sub>Timed schedule.</sub> | [Templates](templates/)<br/><sub>Fillable models for the stage artifacts.</sub> |

<sub>[Back to the Team Kit index](../README.md)</sub>
