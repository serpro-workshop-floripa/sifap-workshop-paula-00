---
name: "ux-research-design"
description: "Use when establishing who uses the modernized SIFAP interface and what they need — Jobs-to-be-Done, user journeys, information architecture, and accessibility requirements that feed the frontend build. Produces research documents, never component code. Triggers include \"user journey\", \"jobs to be done\", \"UX research\", \"accessibility spec\", and \"who uses this screen\"."
---
# UX research and design intent

## When to invoke

- "Who actually uses this screen, and to do what?"
- "Map the journey before we design the page."
- "What are the accessibility requirements for this flow?"
- "Is this information architecture right?"

## Role boundary

| This produces | This never produces |
|---|---|
| Research documents in Markdown | `.tsx` files or Tailwind classes |
| Job statements and journeys | Component implementations |
| Accessibility acceptance criteria | Visual design assets |
| Information architecture | Framework or library choices |

Hand the output to the react-nextjs-frontend skill or the developer skill to
build it.

## Procedure

**Step 1 — Establish the user before the screen.**

- A wireframe without a job statement is rejected.
- For the SIFAP domain, name the actual operator: who opens this, from where, under what time pressure, and what happens if they get it wrong.
- Ground the role in evidence where it exists. The legacy 3270 transaction codes and screen flows describe real work; cite them rather than inventing a persona.

**Step 2 — Write the job, not the feature.**

- Shape: `When <situation>, I want to <motivation>, so I can <expected outcome>`.
- A job survives a redesign. A feature does not.

**Step 3 — Map the journey end to end.**

| Stage | What the user does | What they need | Where it fails today |
|---|---|---|---|

- Include the unhappy paths: not found, ambiguous match, stale data, partial permission.
- The legacy failure modes are evidence. A modern design that silently repeats them has not improved anything.

**Step 4 — Make accessibility a requirement, not a review.**

- Keyboard path for every action, visible focus, and a logical tab order.
- Semantic structure and labels, not ARIA patched over a `div`.
- Contrast and target sizes meeting WCAG 2.2 AA.
- Error messages that state what to do next, not just what failed.
- Write these as acceptance criteria so they can fail a test.

**Step 5 — Respect the data rules.**

- Sensitive data such as CPF and benefit amounts is masked by default, revealed only by an explicit authorized action.
- A screen that shows everything to everybody is a security finding, not a convenience.

## Anti-patterns to reject

| Request | Response |
|---|---|
| "Design the screen" with no user named | Establish the job first. |
| An invented persona with invented pain | Cite the legacy flow, or mark it as an assumption. |
| Accessibility as a final review pass | Write it as acceptance criteria up front. |
| A happy path only | Map not-found, ambiguous, and partial-permission paths. |
| A layout proposal written as component code | This skill produces research; hand it off to build. |

## Output template

```markdown
## Job statements

- When <situation>, I want to <motivation>, so I can <expected outcome>.

## Journey — <flow name>

| Stage | User action | Needs | Failure mode today | Evidence |
|---|---|---|---|---|

## Information architecture

<What is grouped, what is primary, what is progressive disclosure.>

## Accessibility acceptance criteria

- Given <context>, when <action> by keyboard only, then <observable result>.

## Data exposure rules

| Field | Default state | Reveal requires |
|---|---|---|
```

## Quality gate

- [ ] Every screen traces to at least one job statement.
- [ ] Each journey includes its unhappy paths.
- [ ] Accessibility is written as testable acceptance criteria, not as a principle.
- [ ] Sensitive fields have an explicit default state and reveal rule.
- [ ] Claims about current behavior cite the corpus or are labelled assumptions.
- [ ] The deliverable is a research document, not component code.
