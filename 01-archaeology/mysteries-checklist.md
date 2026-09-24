# Open-question checklist: Stage 1

> **Path:** [Team Kit](../README.md) › [Stage 1](README.md) › **Open-question checklist**

**Trace uncertainties before Stage 2.** This checklist ensures that every open question is recorded with evidence, a hypothesis marked as unconfirmed, and an identified owner.

| Field | Value |
|---|---|
| **Target audience** | Individual participant, complete during Stage 1 |
| **Prerequisites** | Read the programs and DDMs needed for the fixed target capability |
| **Stage** | Stage 1: Archaeology |
| **Expected outcome** | A list of unanswered questions with traceability and an owner |

> [!IMPORTANT]
> **Traceability gate.** A question remains open until it receives explicit human validation supported by evidence. It cannot become an answer, rule, or requirement without that validation.

---

## The denominator is 20

SIFAP, the Payment Inspection and Administration System, contains **20 canonical open-question slots**: business rules, contradictions, and decisions that were never documented and exist only in the code. They are grouped by investigation area and difficulty so an individual participant can use the IDs relevant to the fixed consultation capability.

| Rule | Value |
|---|---|
| Total canonical open questions for the group | **20** (`SIFAP-M-01` … `SIFAP-M-20`) |
| Per investigation area | **4** |
| Capability scope | IDs relevant to consulted beneficiary list/search/detail and validation rules |
| Complete challenge record | Relevant IDs recorded, with blockers explicit for unread areas |

> [!NOTE]
> **Why use a fixed number.** Without a denominator, participants report different quantities after reading the same material, depending on aggregation granularity and how many artifacts they open. The denominator **does not change**: findings outside the list are **bonuses** recognized in the debrief, but they do not replace a missing canonical open question, and facilitators do not create canonical IDs during the workshop.

Eight of the 20 are **two-sided**: they count only with both pieces of evidence (code **and** DDM, or code **and** legacy document). Comparing sources is required.

### Where to look by investigation area

The labels indicate the open question's **area**, never the finding.

| Area | Domain | IDs | Programs |
|---|---|---|---|
| Registration | Registration | `M-01` … `M-04` | `CADBENEF`, `CADDEPEN`, `CADPROG` |
| Batch | Batch | `M-05` … `M-08` | `BATCHPGT`, `BATCHREL`, `BATCHCON` |
| Calculation | Calculation | `M-09` … `M-12` | `CALCBENF`, `CALCCORR`, `CALCDSCT`\* |
| Validation | Validation | `M-13` … `M-16` | `VALBENEF`, `VALDOCS`, `VALELEG` |
| Queries and reports | Queries and reports | `M-17` … `M-20` | `CONSBENF`, `RELPGT`, `RELAUDIT` |

\* `CALCDSCT.NSP` is supporting reading for calculation evidence. It contains no canonical open question, but it is worth asking why it exists.

> [!TIP]
> **If you are stuck for more than 20 minutes, ask workshop support and record the blocker.** A hint does not cost points; remaining stuck takes you out of the exercise.

---

## For each open question

- [ ] The question is recorded without an answer or conclusion.
- [ ] The evidence contains `path:line`.
- [ ] The impact is recorded.
- [ ] The hypothesis is explicitly marked as **unconfirmed**.
- [ ] An accountable person or area is identified.
- [ ] The status is recorded.

---

## Record structure

| Open question | Evidence (`path:line`) | Impact | Hypothesis (unconfirmed) | Accountable person/area | Status |
|---|---|---|---|---|---|
| <!-- fill in --> | <!-- fill in: path:line --> | <!-- fill in --> | <!-- fill in: unconfirmed --> | <!-- fill in --> | <!-- fill in: open / awaiting human validation / closed after human validation --> |

---

## Capability scorecard

Complete this table with the IDs relevant to the source members you read for the fixed capability.

| Canonical ID | Found | Recorded in `mysteries-found.md` |
|---|---|---|
| `SIFAP-M-__` | [ ] | [ ] |
| `SIFAP-M-__` | [ ] | [ ] |
| `SIFAP-M-__` | [ ] | [ ] |
| `SIFAP-M-__` | [ ] | [ ] |

**Additional findings (bonus):** <!-- liste aqui; não mudam o denominador -->

---

## Methods for finding open questions

None of these tips reveals a finding. They are all reusable legacy-code reading techniques.

1. **Read comments before code.** In 29-year-old code, a comment is often the only place where someone tried to explain *why*. A comment with a name and date is especially valuable.
2. **Read the program header.** Lines such as `* CHANGED: yyyy-mm-dd - NAME - reason` tell the system's story in chronological order.
3. **Compare code with documentation.** When `legacy-docs/` and the code disagree, you have found something.
4. **Compare code with the DDM.** Type, size, and value domain must agree between the program and `adabas-ddms/`, but they do not always agree.
5. **Look for numeric literals.** Every unexplained number in a calculation raises questions: where did it come from, who decided it, and what breaks if it changes?
6. **Ask, "Who writes to this field?"** Choose a DDM field and find every program that writes to it. Sometimes the answer is none.
7. **Read commented-out code.** Disabled blocks reveal what the system once did and why it stopped.
8. **Question `ESCAPE`, an `IF` without `ELSE`, and unconditional assignment.** Early exits and rules that always apply hide decisions that nobody recorded.
9. **Cross-check the relevant programs and DDMs.** Several open questions appear only when you compare two files.

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 1 guide](GUIDE.md)<br/><sub>Step-by-step schedule.</sub> | [Open-question register](mysteries-found.md)<br/><sub>Detailed register with evidence and an owner.</sub> |

<sub>[Back to the Team Kit index](../README.md)</sub>
