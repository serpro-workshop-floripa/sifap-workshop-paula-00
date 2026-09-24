---
description: "Use when reading Natural/Adabas legacy code, language patterns, FDT structure, naming conventions, and batch flows."
applyTo: "01-archaeology/legacy-sifap/**,**/*.NSP,**/*.nsp,**/*.NSN,**/*.nsn,**/*.NSS,**/*.nss,**/*.NSA,**/*.nsa,**/*.NSL,**/*.nsl,**/*.NSC,**/*.nsc,**/*.NSM,**/*.nsm,**/*.NSD,**/*.nsd,**/*.NAT,**/*.nat,**/*.CPY,**/*.cpy,**/*.DDM,**/*.ddm,**/*.jcl,**/*.JCL"
---

# Natural/Adabas Legacy Code — Reading Guide

This file activates when you open Natural programs, Adabas DDMs, JCL, copycodes, or any file within the `01-archaeology/legacy-sifap/` directory. It teaches how to read legacy code for SIFAP (Payment Inspection and Administration System): Natural program structure, CALLNAT and INCLUDE dependencies, Adabas FDTs, legacy naming, batch patterns, packed decimals, and first-pass reading strategy. It does **not** decide modern module boundaries or JPA mappings, which belong to [`modular-monolith.instructions.md`](modular-monolith.instructions.md). EARS authoring belongs to the EARS validation skill, and executable traceability rules live in [`spec-quality.yml`](../workflows/spec-quality.yml).

## Natural Program Structure

A Natural program follows this skeleton:

```
DEFINE DATA
  LOCAL
    01 #MY-VARIABLE  (A20)    /* A = alphanumeric, 20 chars */
    01 #COUNTER      (N5)     /* N = numeric, 5 digits */
    01 #AMOUNT       (P9.2)   /* P = packed decimal, 9 integer + 2 decimal digits */
    01 #RATES        (N3.4/1:27)  /* array: 27 occurrences of N3.4 */
  END-DEFINE

  /* Main logic here */

END
```

> The supplied source declarations and the kit's CI format guard use a period,
> as in `(P9.2)` and `(N3.4)`. This convention is not proof that every supplied
> program compiled or ran in an available environment. Confirm the actual
> Natural runtime and decimal-character settings with the source owner.
> Declaration formats, numeric literals, and array bounds have distinct syntax.
> Preserve the read-only corpus while recording uncertainties.

Key blocks to recognize:

| Block | Purpose |
|-------|---------|
| `DEFINE DATA LOCAL` | Variable declarations scoped to this program |
| `DEFINE DATA PARAMETER` | Input/output variables received from a caller |
| `DEFINE DATA GLOBAL` | Shared among programs in a session (rare, fragile) |
| `INPUT` | Reads from the terminal (online) or sequential file (batch) |
| `DISPLAY` / `WRITE` | Output to a screen or report |
| `MAP` | Screen layout definition (terminal UI) |

## CALLNAT vs PERFORM

- **`CALLNAT 'SUBPROG' parm1 parm2`** calls a separate subprogram. Inspect positional parameters, the callee/PDA declaration, and any value-passing modifiers. Do not infer input/output direction from parameter names or display attributes.
- **`PERFORM subroutine-name`** can invoke an internal or external subroutine. Find its actual definition before classifying the dependency.

When mapping call chains, `CALLNAT` is the important one — it crosses file boundaries.

## INCLUDE Copycodes

`INCLUDE copycode-name` inserts a shared code fragment at compile time, like a C `#include`. Copycodes typically contain:

- Shared data area definitions (Natural's "struct")
- Common validation routines
- Standard error-handling blocks

When you see `INCLUDE`, find the corresponding copycode to understand the complete data layout.

### Member Extensions

A Natural library is **flat**: there are no subdirectories, and each member is resolved by name, not by path. The extension indicates the type:

| Extension | Type | Called by |
|----------|------|-------------|
| `.NSP` | Program | invoked by the Natural session or batch input |
| `.NSN` | Subprogram | `CALLNAT` |
| `.NSA` | Parameter Data Area (PDA) | `PARAMETER USING` |
| `.NSL` | Local Data Area (LDA) | `LOCAL USING` |
| `.NSC` | Copycode | `INCLUDE` |
| `.NSM` | Map (3270 screen layout) | `INPUT USING MAP` |
| `.jcl` | Job Control Language | batch scheduler |

`CALLNAT`, `INCLUDE`, `PARAMETER USING`, and `LOCAL USING` **MUST NOT be ignored**: each pulls code or declarations from another file. A program read in isolation is incomplete.

Natural member names are limited to 8 characters. In this corpus, the Natural DDM/member names are `BENEFIC`, `SOCPROG`, `PAYMENT`, and `AUDIT`. The Adabas file can still be described conceptually as the Beneficiary or Social Program file, and the DDM field names keep their long names.

## Adabas FDT (Field Definition Table)

Every Adabas file has an FDT that defines its fields. Think of it as the schema:

| Column | Meaning |
|--------|---------|
| Level | Hierarchical depth (01 = top level, 02+ = children) |
| Name | Two-character short name (AA, AB, AC...) |
| Format | Physical Adabas notation, such as `A`, `U`, `P`, or `B`; do not substitute Natural/DDM logical format meanings |
| Length | Field size in bytes |
| Descriptor | `DE` = searchable index, `MU` = multi-value (array), `PE` = periodic group (repeating group) |

### MU (Multiple-Value) Fields

A field marked `MU` can contain multiple values. In Natural, it is accessed by
occurrence, such as `FIELD(1)`. Distinguish the bounds declared in a view from
physical/source-runtime limits; do not assume they are interchangeable.

**Stage boundary:** record source structure and occurrence semantics here.
The DBA and architects decide a normalized target in Stage 2; JSONB needs an
evidence-backed exception, not a default mapping.

### PE (Periodic Groups)

A `PE` group is a repeating group of related fields — like a row in an embedded table. For example, an address history in which each occurrence has a street, city, and date.

**Stage boundary:** record the repeated fields together and their occurrence
order. Do not approve an `@OneToMany`, embedded type, or JSONB representation
during source discovery.

### Super-Descriptors

A super-descriptor combines multiple fields into a single searchable key (composite index). Notation such as `SU = AA + AB(1-4)` means "concatenate field AA with the first 4 bytes of AB."

**Stage boundary:** a source descriptor suggests an access pattern, not an
automatic PostgreSQL index. Verify query shape, selectivity, and target design.

## 1990s Naming Conventions

Legacy Natural codebases use prefix-based names. Common patterns include:

| Prefix Pattern | Typical Meaning |
|---|---|
| `BN-` or `BATCH-` | Batch program or batch-related variable |
| `PG-` or `PROG-` | Main program |
| `PS-` or `SUB-` | Subprogram (called via CALLNAT) |
| `AU-` or `AUT-` | Related to authorization or audit |
| `#` prefix on variables | Local working variable (Natural convention) |
| `+` prefix on variables | Context-independent variable; inspect the declaration and runtime use |

These are conventions, not rules — verify by reading the code rather than assuming.

## Batch Job Patterns

Batch Natural programs typically follow this structure:

```
READ WORK FILE 1 record
  /* process each record */
  AT END OF DATA
    /* final totals / cleanup */
  END-ENDDATA
END-WORK
```

Control-break reports use:

```
READ logical-file BY descriptor
  AT BREAK OF descriptor
    /* subtotal when descriptor value changes */
  BEFORE BREAK PROCESSING
    /* detail line for each record */
  END-BREAK
END-READ
```

## Packed Decimal Handling

Packed decimal (`P` format) stores digits efficiently: each byte holds two digits, and the final nibble is the sign (C=positive, D=negative). It is common in financial calculations.

When mapping to Java: ALWAYS use `BigDecimal`, NEVER `double` or `float`. Packed fields with the `P9.2` format mean 9 integer digits plus 2 decimal places → `BigDecimal` with `scale(2)`.

Both unpacked and packed numeric declarations can represent financial values;
`N` alone does not prove a defect. Compare the actual program, DDM, physical
storage and operations. Natural `(P9.2)` describes nine integer and two
fractional digits, whereas physical byte length is a different measurement.
Verify the supplied notation and runtime before selecting target precision.

## Reading Strategy

When approaching a legacy program for the first time:

1. **Start with DEFINE DATA** — understand the variables and their types
2. **Find the main READ or FIND** — this reveals which data the program processes
3. **Trace CALLNAT calls** — these are the dependencies
4. **Look for INCLUDE copycodes** — they expand the data definitions
5. **Check AT BREAK / AT END OF DATA** — they reveal reporting or processing logic
6. **Note every ESCAPE or ON ERROR** — these are error-handling paths
7. **Check `IF NO RECORDS FOUND` and record-buffer state.** Trace initialization, successful reads, no-record paths and resets. View-buffer contents do not disappear merely because a `FIND`/`READ` block ends; do not infer lexical scope or freshness.
8. **Check the actual selection/access form and DDM markers.** Distinguish search selection from descriptor-ordered access. Read all markers in the supplied listing and verify statement/runtime constraints; do not declare compilation or runtime failure from a generic descriptor rule alone.

## Convenções

| Rule | Rationale |
|---|---|
| Supplied declarations use period decimal notation such as `(P9.2)` | The CI guard checks this text convention; actual runtime compatibility is verified separately |
| Trace `CALLNAT`, `INCLUDE`, `PARAMETER USING`, and `LOCAL USING` | A Natural member read in isolation is incomplete |
| Compare program field formats with the matching DDM | Type and size mismatches can cause silent truncation or overflow |
| Map packed money fields to `BigDecimal` | `double` and `float` lose financial precision |
| Verify statement form, descriptors and runtime assumptions | Selection validity and ordered access are not interchangeable, and static reading does not prove execution |
| Treat prefixes as clues, not proof | Legacy naming conventions vary and must be verified in code |

## Faça / Não faça

| Do | Do not |
|---|---|
| Start with `DEFINE DATA` to understand variables and types | Interpret business rules before knowing the data layout |
| Find the main `READ` or `FIND` to identify processed data | Assume the program's primary file from its name alone |
| Trace every `CALLNAT` dependency and `INCLUDE` copycode | Ignore external subprograms, PDAs, LDAs, copycodes, or maps |
| Check `AT BREAK`, `AT END OF DATA`, `ESCAPE`, and `ON ERROR` paths | Read only the happy path through the program |
| Trace view-buffer initialization, reads and no-record paths | Assume the buffer is cleared or out of scope when a block ends |
| Inspect selection, descriptor ordering and actual listing markers | Assert universal compile/runtime behavior without evidence |

## Checklist antes de abrir um PR

- [ ] `DEFINE DATA` variables, arrays, parameters, and relevant formats were captured before summarizing behavior
- [ ] Main `READ`, `FIND`, work-file, report, and control-break paths were identified
- [ ] Every `CALLNAT`, `INCLUDE`, `PARAMETER USING`, `LOCAL USING`, map, and JCL dependency was traced or noted as open
- [ ] Program field formats were compared with the DDM for type, size, descriptor, MU, PE, and super-descriptor semantics
- [ ] Packed decimal and monetary values were mapped or documented as `BigDecimal` candidates, never floating-point values
- [ ] Error, escape, no-records, end-of-data, and silent-default paths were included in the extracted business rules
