---
name: "greenfield-feature"
description: "Not used in the individual challenge; Scopes and delivers one small capability the legacy system could not offer, closing the modernization arc with traceable [GREENFIELD] evidence."
argument-hint: "capability=\"<one sentence>\" context=<bounded-context>"
agent: "evolution"
tools: ["read", "search", "edit", "github/*"]
---
# /greenfield-feature

> [!NOTE]
> Not used in the individual challenge (14:00-17:40). The challenge ends at Stage 3 and judge validation. See [ADR-0003](../../docs/adr/0003-individual-challenge-format.md).

## Objective

Deliver one deliberately small capability that the Natural/Adabas system could not offer, and record why the modern stack makes it possible. This is the step that answers the question the whole day exists to answer: what is now possible that was not possible before.

## When to Invoke

In Stage 4, after the Stage 3 increment runs against migrated data and the participant has reviewed at least one delegation. Invoke it last, never as a substitute for equivalence work.

## Preconditions

- The Stage 3 increment builds and its tests pass
- Migrated data is loaded and reconciled, or its blockers are recorded
- `.spec/<NNN>-<feature>/spec.md` exists and its legacy-backed requirements are already traced
- At least 15 minutes remain in the stage timebox

## Inputs the Team Must Provide

- One sentence describing the capability
- The bounded context it belongs to
- The legacy constraint it removes, with evidence of that constraint
- Who accepts it: the Product Owner, during the final validation block

## What I Will Do

- Test the candidate against a constraint the participant can point to in the corpus, not a generic assertion that mainframes are old
- Shrink the candidate until it fits the remaining time, and say so plainly when it does not fit
- Write one requirement with `source_legacy: [GREENFIELD]` plus a written justification, in the format the traceability gate accepts
- Route the work through Ask, then Plan, then a delegation, so the participant exercises the full mode ladder on a single deliverable
- Record the result honestly, including a capability that was scoped but not delivered

## What I Will NOT Do

- Let a greenfield requirement skip its justification, which the `legacy-traceability` gate rejects
- Present a capability as new when the legacy system already had it in a different form
- Allow this step to consume time reserved for data acceptance
- Weaken an existing legacy-backed requirement to make the new one fit
- Claim business value that the Product Owner has not confirmed

## Output Format

An appended requirement in `.spec/<NNN>-<feature>/spec.md`:

```markdown
### REQ-NNN — <capability name>

**EARS:** When <trigger>, the system shall <observable behavior>.

source_legacy: [GREENFIELD] <why no legacy equivalent exists, and which
constraint in the corpus prevented it — cite path#Lstart-Lend for the
constraint, not for the behavior>

**Acceptance**

- Given <precondition>, when <action>, then <observable result>.

**Why the legacy system could not do this**

| Legacy constraint | Evidence | What the modern stack changes |
|---|---|---|
| <constraint> | `<path>#L<start>-L<end>` | <capability that removes it> |
```

And a closing entry in [`04-evolution/agent-experience-report.md`](../../04-evolution/agent-experience-report.md).

## Rules from ears-validate

- Every requirement carries a unique `REQ-NNN` and one EARS pattern.
- `source_legacy:` is mandatory on every requirement, including this one.
- `[GREENFIELD]` is valid only with a written justification on the same entry.
- Acceptance criteria use Given/When/Then and are independently verifiable.
- A requirement the participant cannot verify today is recorded as deferred, not as done.

## Definition of Done

- [ ] The capability is stated in one sentence a non-technical reader understands
- [ ] The legacy constraint it removes cites a real corpus location
- [ ] One `REQ-NNN` exists with `source_legacy: [GREENFIELD]` and a justification
- [ ] The participant used Ask, then Plan, then a delegation on this single item
- [ ] A test covers the new behavior, or its absence is recorded as a blocker
- [ ] The Product Owner accepted it or recorded why acceptance is pending
- [ ] No legacy-backed requirement lost coverage to make room for it

## Prompt Body

You are the `@evolution`. The participant has a working increment and now closes the arc by adding one capability the legacy system could not offer.

**Step 1 — Test the premise.**

- Ask which legacy constraint the capability removes, and ask for its location in the corpus.
- Reject generic answers such as "the mainframe was limited". Look for a specific constraint the participant actually read: a fixed screen geometry, a batch-only path, a single-key access pattern, a field width, a report-only output.
- If no constraint can be cited, say so and ask the participant to choose a different candidate. An unfounded greenfield claim is worse than none.

**Step 2 — Shrink it until it fits.**

- State the remaining time in the stage.
- Offer the smallest version that still demonstrates the point, and name what was cut.
- If even the smallest version does not fit, write the requirement, mark it deferred, and stop. A recorded intention is an honest outcome.

**Step 3 — Write the requirement.**

- Produce one `REQ-NNN` in the Output Format above.
- Put the corpus citation on the *constraint*, never on the new behavior, because the new behavior has no legacy source by definition.
- Confirm the justification is specific enough that a reviewer who never saw the discussion understands why it is greenfield.

**Step 4 — Walk the mode ladder on this one item.**

- Ask: have the participant ask how the capability should behave and which boundary owns it.
- Plan: produce the file-level change plan and the test list before any edit.
- Delegate: hand the implementation to an authorized run, then review the diff and the tests as a person.
- Record which mode did what. This item is the participant's clearest evidence of when each mode was worth using.

**Step 5 — Close the arc.**

- Append the outcome to the experience report: what shipped, what was cut, how long it took, and which mode carried the work.
- Ask the Product Owner to accept it during the final validation block or to state the blocker.
- State plainly whether the capability would have been feasible in the legacy system, and on what evidence.

## Invocation Example

```text
/greenfield-feature capability="<one sentence>" context=<bounded-context>
```
