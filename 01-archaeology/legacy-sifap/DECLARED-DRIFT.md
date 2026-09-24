# Declared Drift — Contradictions That Are Deliberate

> **Path:** [Team Kit](../../README.md) › [Stage 1](../README.md) › [SIFAP Legacy](README.md) › **Declared Drift**

**A register of every place where a narrative document about SIFAP knowingly disagrees with the source it describes.** Documentation drift is the central lesson of Stage 1, so these divergences are preserved on purpose. This file records that they are intentional; it never records which side is correct.

| Field | Value |
|---|---|
| **Target audience** | Kit maintainers, facilitators, and the chronology CI gate |
| **Prerequisites** | [Chronology](CHRONOLOGY.md) |
| **Estimated time** | 5 min |
| **Stage** | Stage 1 — Archaeology (maintenance artifact) |
| **Expected outcome** | You can tell a designed divergence from a kit defect |

> [!IMPORTANT]
> This register answers one question only: **"is this contradiction on purpose?"**
> It does not say which document is right, what the code actually does, or which
> business rule applies. Reading it removes no discovery work, because every
> entry still requires the team to open the source and decide what the
> difference means.

---

## 1. Why a register is necessary

Without it, three failures are indistinguishable from each other:

| Situation | Without the register | With the register |
|---|---|---|
| A period document misstates a date | Looks like a kit typo; someone "fixes" it and deletes the exercise | Preserved and cited as a finding |
| A kit guide misstates a date | Looks like a designed puzzle; nobody fixes it and the map stays wrong | Fails CI immediately |
| A team finds a real inconsistency | No way to tell whether it was known | Unregistered finding, recorded as a discovery |

The rule that follows from the table:

- **Narrative layer** (`legacy-docs/`, [`README.md`](README.md)) may drift, and every known drift appears below.
- **Kit-truth layer** ([`CHRONOLOGY.md`](CHRONOLOGY.md), [`natural-programs/README.md`](natural-programs/README.md), stage guides) may never drift.

---

## 2. Register

`Claim` is what the narrative document states. `Source` is the artifact that
records something different. Read both before concluding anything.

| ID | Narrative document | Claim it makes | Source that differs | Why it is preserved |
|---|---|---|---|---|
| `DRIFT-01` | [`README.md`](README.md) §2.1 | The reconciliation program arrived with the 2002 SIAFI integration | `BATCHCON.NSP` header | A retro-fitted timeline groups a program with the project that later justified it |
| `DRIFT-02` | [`README.md`](README.md) §2.1 | The audit DDM was created during the 2005 platform migration | `AUDIT.ddm` header | A file can be defined years before the module that finally uses it |
| `DRIFT-03` | [`README.md`](README.md) §2.1 | The audit report is part of the 2005 release | `RELAUDIT.NSP` header | Release notes written afterwards absorb earlier work |
| `DRIFT-04` | [`README.md`](README.md) §2.1 | The deduction module is the 2015 "last significant feature" | `CALCDSCT.NSP` header and its change lines | A large change to an old program is often remembered as a new program |
| `DRIFT-05` | [`README.md`](README.md) §3 | Names an original team roster | `* AUTHOR:` lines across the corpus | Institutional memory and code attribution diverge over three decades |
| `DRIFT-06` | [`README.md`](README.md) §5 | Attributes an author, a year, and a last-change year per program | Member headers | An inventory compiled during a later documentation effort inherits its own errors |
| `DRIFT-07` | [`README.md`](README.md) §5.6 | Lists shared subprograms and copycode by name | The members actually present in `natural-programs/` | A partial inventory is the most dangerous kind of inventory |
| `DRIFT-08` | [`README.md`](README.md) §7.3 | Attributes a recovery procedure review to a named DBA | `* AUTHOR:` line in the four DDMs | Operational memory is rarely written down by the person who owns the artifact |
| `DRIFT-09` | [`README.md`](README.md) §6 | States record volumes for a stated reference date | `FDT-150-BENEFICIARY.txt` run date | A printed report is a historical observation, never a current measurement |
| `DRIFT-10` | [`legacy-docs/ORIGINAL-ARCHITECTURE-1997.md`](legacy-docs/ORIGINAL-ARCHITECTURE-1997.md) | Carries annotations describing events after its issue date | Its own front matter date | Long-lived documents accumulate later margin notes |
| `DRIFT-11` | [`legacy-docs/TECHNICAL-MANUAL-SIFAP-2008.md`](legacy-docs/TECHNICAL-MANUAL-SIFAP-2008.md) | Describes behavior as of its publication | Change lines dated after it | A manual freezes; the code does not |
| `DRIFT-12` | [`legacy-docs/BUSINESS-RULES-2012.md`](legacy-docs/BUSINESS-RULES-2012.md) | Documents business rules as of 2012, incompletely | Change lines dated after it | An abandoned discovery effort leaves a partial and aging record |

---

## 3. What a team does with a drift it finds

- [ ] **Record it as a question, not a correction.** Use [`mysteries-found.md`](../mysteries-found.md) with evidence, impact, owner, and status.
- [ ] **Cite both sides.** `path#Lstart-Lend` for the source and the section for the narrative claim.
- [ ] **Mark the hypothesis as unconfirmed.** Only explicit human validation closes it.
- [ ] **Never edit the legacy source.** The corpus is read-only, including the documents that are wrong.
- [ ] **Never quietly align a period document to the code.** That deletes evidence.

---

## 4. Adding or removing an entry

- [ ] **Add an entry** when a new divergence is introduced on purpose into the narrative layer. State the document, the claim, and the differing source — never the resolution.
- [ ] **Remove an entry** only when the underlying narrative document is removed from the corpus.
- [ ] **Never add a kit guide to this register.** Kit truth is fixed, not declared.
- [ ] **Re-run the gate** with `python3 .github/scripts/validate-chronology.py` after any change.

---

### Continue reading

| Previous | Next |
|---|---|
| [Chronology](CHRONOLOGY.md)<br/><sub>Canonical dates, authors, and the name index.</sub> | [Natural Programs](natural-programs/README.md)<br/><sub>The 15 assigned members and 9 supporting members.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
