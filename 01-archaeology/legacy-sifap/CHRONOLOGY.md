# SIFAP Chronology — Canonical Source Evidence

> **Path:** [Team Kit](../../README.md) › [Stage 1](../README.md) › [SIFAP Legacy](README.md) › **Chronology**

**This file is the single source of truth for every date, author, and version claim the kit makes about SIFAP.** Every entry below is transcribed from a header line inside a read-only legacy source. Nothing here is inferred, rounded, or narrated.

| Field | Value |
|---|---|
| **Target audience** | Anyone writing or reviewing a kit document that cites a SIFAP date |
| **Prerequisites** | None |
| **Estimated time** | 5 min to consult; read once before citing any date |
| **Stage** | Stage 1 — Archaeology (consulted in all stages) |
| **Expected outcome** | You cite a date that matches its source, or you record a discrepancy |

---

## 1. Why this file exists

The corpus contains two kinds of document, and confusing them is the most common
failure in a modernization exercise.

| Layer | May it disagree with the code? | Files |
|---|---|---|
| **Evidence** — the sources themselves | It is the reference. Headers are the ground truth. | `natural-programs/*`, `adabas-ddms/*` |
| **Narrative** — period documents written *about* the system | **Yes, deliberately.** Documentation drift is the exercise. Every known divergence is registered in [declared drift](DECLARED-DRIFT.md). | `legacy-docs/*`, [`README.md`](README.md) |
| **Kit truth** — the guides that route your work | **Never.** A guide that misattributes a program breaks the exercise instead of teaching it. | This file, [`natural-programs/README.md`](natural-programs/README.md), stage guides |

A period document that contradicts a source header is a finding to record, not a
bug to report. A kit guide that contradicts a source header is a bug.

---

## 2. Reference year and arithmetic

| Anchor | Value | What it establishes |
|---|---|---|
| Earliest dated source | `BENEFIC.ddm`, 12/05/1997 | The corpus begins in 1997 |
| Latest dated source | `CONSBENF.NSP`, `RELAUDIT.NSP`, `RELPGT.NSP`, 30/05/2018 | The last recorded maintenance |
| Workshop reference year | 2026 | The year the team performs the exercise |
| Elapsed span | 1997 to 2026 = **29 calendar years** | "Approximately 30 years" is rounded scenario language |

> [!IMPORTANT]
> Write "approximately 30 years" or "approximately three decades" in prose, and
> **29 years** wherever a number is stated as a measurement. Never move a source
> date to make the arithmetic rounder. See the
> [chronology policy](../../README.md#scenario-chronology-and-evidence).

---

## 3. Canonical member chronology

Transcribed from the `* AUTHOR:` and `* DATE:` header lines of each member. The
"Last recorded change" column is the final `* CHANGED:` line in the same header.

### 3.1. The 15 assigned members

| Member | Type | Author in header | Created | Last recorded change |
|---|---|---|---|---|
| `CADBENEF.NSP` | Program | CARLOS ROBERTO DA SILVA | 15/03/1997 | 12/09/2012 |
| `CALCBENF.NSN` | Subprogram | CARLOS ROBERTO DA SILVA | 18/04/1997 | 14/06/2016 |
| `BATCHPGT.NSP` | Program | CARLOS ROBERTO DA SILVA | 22/06/1997 | 18/03/2016 |
| `CADPROG.NSP` | Program | MARCOS ANTONIO RIBEIRO | 10/09/1997 | 18/11/2012 |
| `VALBENEF.NSN` | Subprogram | MARCIA HELENA OLIVEIRA | 08/01/1998 | 18/08/2011 |
| `VALDOCS.NSP` | Program | ANA LUCIA PEREIRA | 14/05/1998 | 18/08/2011 |
| `CADDEPEN.NSP` | Program | ANA LUCIA PEREIRA | 20/06/1998 | 12/09/2012 |
| `CONSBENF.NSP` | Program | MARCIA HELENA OLIVEIRA | 28/09/1998 | 30/05/2018 |
| `VALELEG.NSN` | Subprogram | JOSE FERREIRA DOS SANTOS | 03/02/1999 | 05/04/2013 |
| `CALCDSCT.NSP` | Program | ROBERTO MENDES JUNIOR | 25/08/1999 | 14/06/2016 |
| `BATCHREL.NSP` | Program | PATRICIA GOMES DE SOUZA | 10/11/1999 | 05/06/2014 |
| `RELPGT.NSP` | Program | ANA LUCIA PEREIRA | 17/12/1999 | 30/05/2018 |
| `BATCHCON.NSP` | Program | MARCOS ANTONIO RIBEIRO | 05/03/2000 | 11/05/2017 |
| `CALCCORR.NSP` | Program | PATRICIA GOMES DE SOUZA | 12/07/2001 | 14/06/2016 |
| `RELAUDIT.NSP` | Program | ROBERTO MENDES JUNIOR | 20/08/2002 | 30/05/2018 |

### 3.2. The 9 supporting members

| Member | Type | Author in header | Created | Last recorded change |
|---|---|---|---|---|
| `CCVALCPF.NSC` | Copycode | CARLOS ROBERTO DA SILVA | 15/03/1997 | 07/06/2011 |
| `PDACALC.NSA` | PDA | CARLOS ROBERTO DA SILVA | 22/06/1997 | 30/09/2015 |
| `SIFAPJ01.jcl` | JCL | CARLOS ROBERTO DA SILVA | 22/06/1997 | 10/07/2015 |
| `LDASIFAP.NSL` | LDA | CARLOS ROBERTO DA SILVA | 10/09/1997 | 30/09/2015 |
| `PDAVALID.NSA` | PDA | MARCIA HELENA OLIVEIRA | 12/03/1998 | 07/06/2011 |
| `SUBVALCP.NSN` | Subprogram | MARCIA HELENA OLIVEIRA | 12/03/1998 | 07/06/2011 |
| `SIFAPJ02.jcl` | JCL | PATRICIA GOMES DE SOUZA | 10/11/1999 | 14/02/2013 |
| `CCAUDIT.NSC` | Copycode | ADILSON BATISTA | 15/04/2005 | 10/07/2015 |
| `SUBVALNI.NSN` | Subprogram | ROBERTO MENDES JUNIOR | 07/06/2011 | 30/09/2015 |

---

## 4. Canonical data-layer chronology

| Artifact | Adabas file | Author in header | Created | Last recorded change |
|---|---|---|---|---|
| `BENEFIC.ddm` | FNR 150 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 12/05/1997 | see header |
| `SOCPROG.ddm` | FNR 151 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 12/05/1997 | see header |
| `PAYMENT.ddm` | FNR 152 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 15/05/1997 | see header |
| `AUDIT.ddm` | FNR 153 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 20/05/1997 | see header |

`FDT-150-BENEFICIARY.txt` is an ADAREP listing, not a definition. It states three
distinct dates, and conflating them is a documented trap:

| Date in the listing | What it means |
|---|---|
| `ADACMP FDT AS LOADED 1997-05-12` | When the field definition table was first loaded |
| `LAST FDT CHANGE 2015-11-19` | The last structural change to the table |
| `RUN DATE 2018-03-14` | When somebody printed this report |

> [!WARNING]
> The run date is when the report was produced. It is not a measurement of the
> database today, and it does not authorize any record-count claim in 2026. The
> DBA measures the live population during source-readiness checks.

---

## 5. Canonical release chronology

Derived strictly from section 3. Each row cites the evidence that dates it.

| Year | What the sources show | Evidence |
|---|---|---|
| 1997 | Four DDMs defined (May); first registration, calculation, and batch members created (Mar–Sep) | `BENEFIC.ddm`, `CADBENEF.NSP`, `CALCBENF.NSN`, `BATCHPGT.NSP`, `CADPROG.NSP` |
| 1998 | Validation and query members created; Y2K century window introduced 12/08/1998 | `VALBENEF.NSN`, `VALDOCS.NSP`, `CADDEPEN.NSP`, `CONSBENF.NSP`, `BATCHPGT.NSP` change line |
| 1999 | Eligibility, deduction, reporting members and the reporting job | `VALELEG.NSN`, `CALCDSCT.NSP`, `BATCHREL.NSP`, `RELPGT.NSP`, `SIFAPJ02.jcl` |
| 2000 | Bank-return reconciliation created | `BATCHCON.NSP` |
| 2001 | Retroactive correction created; 13th-salary change to the benefit calculation | `CALCCORR.NSP`, `CALCBENF.NSN` change line |
| 2002 | Audit-trail report created | `RELAUDIT.NSP` |
| 2005 | Shared audit copycode created; CPF validation adjusted across members | `CCAUDIT.NSC`, `CCVALCPF.NSC` and `VALBENEF.NSN` change lines |
| 2011 | `CALLNAT` refactor — validation and calculation converted to subprograms; NIS subprogram created | Ticket 6210 change lines, `SUBVALNI.NSN` |
| 2016 | Ticket 7210 — DDM standardization across the calculation family | `CALCBENF.NSN`, `CALCCORR.NSP`, `CALCDSCT.NSP` change lines |
| 2018 | Last recorded maintenance — views aligned with the DDMs on 30/05/2018 | `CONSBENF.NSP`, `RELAUDIT.NSP`, `RELPGT.NSP` change lines |

> [!NOTE]
> A creation date is not a production release date, and a change line is not a
> deployment record. The corpus contains no deployment evidence. Any claim about
> when a change reached production is a hypothesis for the team to mark as such.

---

## 6. Canonical name index

Header `* AUTHOR:` lines use full names; `* CHANGED:` lines use short forms. The
same person therefore appears under two spellings, and two different people can
share a first name. Resolve a name here before attributing a rule to anybody.

| Full name as authored | Short form in change lines | Earliest evidence | Latest evidence |
|---|---|---|---|
| CARLOS ROBERTO DA SILVA | `CARLOS SILVA` | 15/03/1997 | 30/11/2001 |
| ROBERTO CARLOS FERREIRA | `ROBERTO C. FERREIRA` | 12/05/1997 | 11/08/2003 |
| MARCOS ANTONIO RIBEIRO | `MARCOS RIBEIRO` | 10/09/1997 | 18/09/2005 |
| MARCIA HELENA OLIVEIRA | `MARCIA HELENA` | 08/01/1998 | 12/04/2007 |
| ANA LUCIA PEREIRA | `ANA LUCIA` | 14/05/1998 | 25/03/2004 |
| (change lines only) | `R.SOUZA` | 12/08/1998 | 12/08/1998 |
| (change lines only) | `MARCIA A. SOUZA` | 10/01/1999 | 08/03/2001 |
| JOSE FERREIRA DOS SANTOS | `JOSE FERREIRA` | 03/02/1999 | 10/01/2011 |
| ROBERTO MENDES JUNIOR | `ROBERTO MENDES` | 25/08/1999 | 09/04/2013 |
| PATRICIA GOMES DE SOUZA | `PATRICIA GOMES` | 10/11/1999 | 30/05/2018 |
| ADILSON BATISTA | `ADILSON BATISTA` | 15/04/2005 | 22/06/2010 |
| (change lines only) | `FERNANDA OLIVEIRA` | 09/02/2012 | 09/02/2012 |
| (change lines only) | `FERNANDA COSTA` | 11/10/2009 | 15/09/2014 |
| (change lines only) | `ANDERSON LIMA` | 30/04/2011 | 22/07/2016 |
| (collective) | `SUPDE TEAM`, `SIFAP TEAM` | 09/05/2011 | 11/05/2017 |

> [!TIP]
> Three name traps are already visible in this table. `CARLOS ROBERTO DA SILVA`
> and `ROBERTO CARLOS FERREIRA` invert the same two given names. `MARCIA HELENA
> OLIVEIRA` and `MARCIA A. SOUZA` are distinct people. `FERNANDA OLIVEIRA` and
> `FERNANDA COSTA` are distinct people who both touched audit-related code.
> Confirm the member and the date before attributing a change to a person.

---

## 7. How to cite a date

- [ ] **Quote the artifact, not a summary.** Cite `CADBENEF.NSP#L5`, never "the docs say 1997".
- [ ] **State which representation you read.** A Word export and a Markdown export of the same document are one source, not two.
- [ ] **Separate creation, change, and observation.** A header date, a change line, and a report run date answer three different questions.
- [ ] **Record disagreement instead of resolving it silently.** Add it to [`mysteries-found.md`](../mysteries-found.md) with evidence and an owner.
- [ ] **Never edit a legacy source to fix an inconsistency.** The corpus is read-only.

---

## 8. How this file is enforced

The `chronology` job in [`spec-quality.yml`](../../.github/workflows/spec-quality.yml)
runs [`validate-chronology.py`](../../.github/scripts/validate-chronology.py), which:

1. Parses `* AUTHOR:` and `* DATE:` from every member and DDM in the corpus.
2. Compares them against the tables in this file and in [`natural-programs/README.md`](natural-programs/README.md).
3. Fails when a kit document attributes a member to the wrong author or year.
4. Ignores divergences that are registered in [declared drift](DECLARED-DRIFT.md), because those are the exercise.

Adding an undeclared contradiction to a kit guide fails the build. That is the
point: coherence is enforced, not promised.

---

### Continue reading

| Previous | Next |
|---|---|
| [SIFAP Legacy — overview](README.md)<br/><sub>System context and history.</sub> | [Declared drift](DECLARED-DRIFT.md)<br/><sub>The contradictions that are deliberate.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
