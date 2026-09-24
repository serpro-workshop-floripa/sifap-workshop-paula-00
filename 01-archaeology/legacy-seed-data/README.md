# Synthetic legacy dataset

> **Path:** [Team Kit](../../README.md) › [Stage 1](../README.md) › **Synthetic legacy dataset**

**Synthetic records for legacy SIFAP exercises.** This folder contains the fixed-width files used to populate the authorized Adabas instance before 14:00 for comparing legacy behavior with the modern system.

| Field | Value |
|---|---|
| **Target audience** | Individual participant covering DBA, QA, and implementation responsibilities |
| **Prerequisites** | Read the DDMs in [`legacy-sifap/adabas-ddms/`](../legacy-sifap/adabas-ddms/) |
| **Estimated time** | 15 min |
| **Stage** | Stage 1: Archaeology; input to Stage 3 |
| **Expected outcome** | Decoded records for validating the modern system |

> [!IMPORTANT]
> **100% synthetic data.** It contains no real personal data, no CPF or NIS assigned to a real person, and no production records. The check digits are valid only to exercise the legacy validators.

---

## Files and volumes

| File | Records | Bytes per record (excluding the line break) | Source layout |
|---|---:|---:|---|
| `beneficiary.dat` | 500 | 1739 | `layout-beneficiary.txt`, file 150 BENEFICIARY |
| `payment.dat` | 2000 | 855 | `layout-payment.txt`, file 152 PAYMENT |
| `social-program.dat` | 6 | 361 | `layout-social-program.txt`, file 151 SOCIAL-PROGRAM |
| `audit.dat` | 200 | 4995 | `layout-audit.txt`, file 153 AUDIT |

---

## Regeneration

Run from the repository root:

```bash
python3 01-archaeology/legacy-seed-data/generate_seed.py
```

The generator uses only the Python 3 standard library and a fixed seed, so its output is reproducible byte for byte. This README is generated. Translators must update the text inside `write_readme()`, not only this generated file.

---

## Layout notes

There is one physical record per line. Alphanumeric fields are ASCII padded with spaces on the right. Unpacked numeric fields are digits padded with zeros on the left.

> [!WARNING]
> Packed decimal fields are binary BCD with the scale declared in the DDM/FDT. **They are not readable as text and require decoding before any PostgreSQL load.** For the same reason, converting identifiers to numbers discards leading zeros from CPF and NIS values.

Periodic groups and MU fields are emitted with the maximum number of occurrences so that ADACMP/ADALOD scripts load deterministic, full-width records. The line break is not part of the record width.

---

## Learning fixtures

- CPF and NIS check digits use the modulo 11 algorithms from [`SUBVALCP.NSN`](../legacy-sifap/natural-programs/SUBVALCP.NSN) and [`SUBVALNI.NSN`](../legacy-sifap/natural-programs/SUBVALNI.NSN).
- Some beneficiaries have a valid CPF beginning with `000` for the government test exception path.
- Family income values cross the 300, 600, 1000, and 1500 calculation bands.
- Beneficiaries in region `99` exercise the international or diplomatic eligibility branch.
- Dependents cover none, several, inactive and terminated situations, and one record with the maximum of 10 occurrences.
- Payments include reversals, divergent reconciliation, bank returns, and rows with deliberately unbalanced gross, discount, and net values for the reporting labs.

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 1: Archaeology](../README.md)<br/><sub>Stage index and its artifacts.</sub> | [Adabas DDMs](../legacy-sifap/adabas-ddms/README.md)<br/><sub>Field definitions that describe these records.</sub> |

<sub>[Back to the Team Kit index](../../README.md)</sub>
