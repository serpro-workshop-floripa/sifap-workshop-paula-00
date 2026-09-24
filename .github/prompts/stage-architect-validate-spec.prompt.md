---
name: "validate-spec"
description: "Regenerates derived SDD files and runs every SDD, EARS, and TDD gate on a package under .spec/, for either the architect or the Spec-Kit workflow, and reports the results without hiding failures."
argument-hint: "feature=NNN-feature-name"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /validate-spec

## Objective

Report whether `.spec/<NNN>-<feature>/` is ready for C2 by running the repository's SDD gates and listing every failure with its owner and fix.

## When to Invoke

After any change to a package, before opening a PR, and at C2, for either workflow.

## Preconditions

- The package exists under `.spec/`
- Python 3 and PyYAML are available (`python3 -m pip install pyyaml`)

## Inputs the Team Must Provide

- `feature=<NNN>-<feature-name>`
- Whether warnings count as failures (`--strict`) for this review

## What I Will Do

- Detect the workflow from `SPECIFICATION.md` or `spec.md`
- For an architect package, run `generate-sdd-support-artifacts.py --package <NNN> --include-supplements` and then its `--check`
- Run `python3 .github/scripts/validate-specs.py --package <NNN>`, plus `audit-task-evidence.py` and `validate-test-bindings.py --report`
- Group findings by gate and propose the smallest fix for each

## What I Will NOT Do

- Weaken a gate, add an exception, or edit a generated file to get a green result
- Claim semantic EARS correctness, approval, or runtime behavior from a text gate
- Fix a finding by inventing evidence

## Output Format

```markdown
## Validation — <NNN>-<feature> (<workflow>, <stage>)

| Gate | Result | Findings |
|---|---|---|
| spec-artifacts | pass/fail | <count and first finding> |

Blocking for C2: <list or none>
```

## Definition of Done

- [ ] Every gate ran and its verbatim result is reported
- [ ] Each failure has an owner and a proposed fix
- [ ] Nothing was changed except regenerated derived files

## Prompt Body

You are the `@architect`. Measure the package against the gates and report exactly what they say.

**Step 1 — Identify the package.**

- Resolve `.spec/<NNN>-<feature>/`, its workflow, and its stage.

**Step 2 — Regenerate derived files.**

- Architect packages only: run the generator, then its `--check`.

**Step 3 — Run the gates.**

- Run `validate-specs.py --package <NNN>` and the evidence and binding reports.

**Step 4 — Report.**

- Fill the output table; mark C2 blocked while any error remains.

## Invocation Example

```text
/validate-spec feature=001-benefit-calculation
```

Expect a gate table for `.spec/001-benefit-calculation/` with every failure and its fix.
