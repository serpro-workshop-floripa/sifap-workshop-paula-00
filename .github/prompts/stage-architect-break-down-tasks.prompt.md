---
name: "break-down-tasks"
description: "Writes the complete stage of an architect SDD package — TASKS.md with RED/GREEN tasks, TESTING.md, and the plan-to-tasks and test-coverage checkpoints — then derives the generated files."
argument-hint: "feature=NNN-feature-name"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /break-down-tasks

## Objective

Turn the design of `.spec/<NNN>-<feature>/` into dependency-ordered, test-first work: `TASKS.md`, `TESTING.md`, `checkpoints/plan-to-tasks.yaml`, and `checkpoints/test-coverage.yaml`, then generate `TDD.md`, `SOURCE_TRACEABILITY.md`, `CHECKLIST.md`, `CROSS_ANALYSIS.md`, and `VERIFICATION.md`.

## When to Invoke

After `/design-modular-monolith` completed the design stage, before C2. For a Spec-Kit package use `/speckit.tasks`.

## Preconditions

- The design-stage gate passes for the package
- The team agreed the first increment and the test levels it needs
- The [tests instruction](../instructions/tests.instructions.md) is loaded

## Inputs the Team Must Provide

- `feature=<NNN>-<feature-name>`
- The test commands the project uses, or `PENDING` with an owner
- Any ordering constraint (data load before consultation, for example)

## What I Will Do

- Write one RED task before one GREEN task for every requirement, with `Files:` and `Acceptance:` sub-bullets
- Add data migration, consultation, and independent QA reconciliation tasks where the design needs them
- Draw the dependency graph with every task once and no cycle
- Declare every test as `TST-NNN` in the `TESTING.md` catalog with location, level, command, and status
- Map plan items to tasks and requirements to tests in the two checkpoints
- Generate the derived files and run every gate

## What I Will NOT Do

- Check a task, or claim a test ran, without evidence in `evidence/`
- Write implementation code or tests themselves; Stage 3 does that
- Mark a GREEN task before its RED task
- Hand-edit a generated file

## Output Format

```markdown
- [ ] **T001 [S] [Plan:P1.1] RED** Add a failing test for the rule. Traces REQ-001.
  - Files: `backend/src/test/java/<package>/<Rule>Test.java`.
  - Acceptance: TST-001 fails for the missing behavior.
- [ ] **T002 [S] [Plan:P1.1] GREEN** Implement the minimum behavior. Traces REQ-001.
  - Files: `backend/src/main/java/<package>/<Rule>.java`.
  - Acceptance: TST-001 passes.
```

## Definition of Done

- [ ] `TASKS.md`, `TESTING.md`, and both checkpoints exist with `mapping_status: complete`
- [ ] Every requirement has RED before GREEN and at least one `TST-NNN`
- [ ] `python3 .github/scripts/generate-sdd-support-artifacts.py --package <NNN> --include-supplements` succeeded
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --strict` passes, or its failures are reported

## Prompt Body

You are the `@architect`. Break the approved design into test-first tasks a builder can execute without guessing.

**Step 1 — Read the design.**

- Open `DESIGN.md`, `DECISIONS.md`, `checkpoints/spec-to-plan.yaml`, and `SPECIFICATION.md`.

**Step 2 — Write the tests first.**

- Declare `TST-NNN` rows in `TESTING.md` for every acceptance ID, and fill the commands, failure and measurement, evidence contract, and exit criteria sections.

**Step 3 — Write the tasks.**

- For each plan item, write a RED task then a GREEN task per requirement; mark `[P]` only for independent tasks.
- Draw the dependency graph in the neutral Mermaid theme.

**Step 4 — Checkpoint.**

- Fill `plan-to-tasks.yaml` (with a `gate` block) and `test-coverage.yaml` (requirements and tests with commands).

**Step 5 — Generate and validate.**

- Run the generator, then `python3 .github/scripts/validate-specs.py --package <NNN> --strict`; report the result verbatim.

## Invocation Example

```text
/break-down-tasks feature=001-benefit-calculation
```

Expect a complete `.spec/001-benefit-calculation/` package whose gates pass, with no task checked.
