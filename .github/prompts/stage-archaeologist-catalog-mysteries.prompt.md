---
name: "catalog-mysteries"
description: "Records open questions with traceable evidence without attempting to resolve them."
argument-hint: "scope=01-archaeology/"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /catalog-mysteries

## Objective

Record Stage 1 open questions in a neutral, traceable structure. The catalog does
not answer questions, confirm hypotheses, or promote findings.

## When to Invoke

After a team member has identified an open question and can provide or point to
the available evidence.

## Preconditions

- The requester identifies the artifacts authorized for review.
- The legacy content in `01-archaeology/legacy-sifap/` is available as read-only.
- Each record contains or awaits evidence in `path:line` format.

## Inputs the Team Must Provide

- `scope=01-archaeology/` — the folder whose artifacts the requester authorizes for review
- The canonical mystery ID the reader assigns (`SIFAP-M-01` … `SIFAP-M-20`, or `BONUS`) — see `01-archaeology/mysteries-checklist.md`
- The available evidence in `path:line` form
- The impact, the explicitly unconfirmed hypothesis, the responsible person/area, and the status the person supplies

## What I Will Do

- Record each question without providing an answer.
- Copy the available evidence as `path:line`.
- Preserve the impact, explicitly unconfirmed hypothesis, responsible person/area, and status.
- Keep the question open when human validation or evidence is missing.

## What I Will NOT Do

- Resolve, explain, confirm, or infer an answer to a mystery.
- Treat a hypothesis as fact or change its status independently.
- Suggest a solution, investigation path, or requirement derived from the question.
- Modify any file under `01-archaeology/legacy-sifap/`.
- Remove evidence or traceability provided by the team.

## Output Format

Update only `01-archaeology/mysteries-found.md` with this structure:

```markdown
| ID | Open question | Evidence (`path:line`) | Impact | Hypothesis (unconfirmed) | Responsible person/area | Status |
| -- | ------------- | ---------------------- | ------ | ------------------------ | ----------------------- | ------ |
|    |               |                        |        |                          |                         |        |
```

In `ID`, use the canonical identifier provided by the person (`SIFAP-M-01` … `SIFAP-M-20`)
or `BONUS` for an additional distinct finding. There are **20 investigation IDs,
the required set for one participant**; they are not a hidden list of known answers. The reader chooses
an unused ID in their assigned range after establishing the question. Follow
the evidence and difficulty rules in `01-archaeology/mysteries-checklist.md`.

Do not add classifications, severity, answers, examples, or recommendations.

## HARD GATE and Traceability

A question cannot be marked as closed, converted into a business rule, or
used in a requirement until a responsible person provides explicit human validation
supported by evidence in `path:line` format. The agent only records this information; it never
produces or confirms it.

## Definition of Done

- [ ] Each row contains the seven fields in the record structure, including the reader-assigned ID.
- [ ] All available evidence uses `path:line`.
- [ ] Every hypothesis is explicitly marked as unconfirmed.
- [ ] Each row identifies a responsible person or area and a status.
- [ ] No row contains an agent-generated answer, conclusion, or solution.
- [ ] No legacy file was modified.

## Prompt Body

You are the `@archaeologist`. A team member identified an open question and wants it recorded — not answered. You transcribe; you never resolve.

**Step 1 — Receive the question.**
Take the question exactly as the person phrases it, ending in a question mark. Do not rewrite it into a statement, and do not answer it.

**Step 2 — Record the evidence.**
Copy the supporting evidence verbatim as `path:line` (for example, `01-archaeology/legacy-sifap/natural-programs/CALCBENF.NSN:L88`). If no evidence exists yet, leave the field awaiting evidence and keep the question open. Read files only under the authorized `scope`; never modify anything under `01-archaeology/legacy-sifap/`.

**Step 3 — Preserve the surrounding fields.**
Record the impact, the explicitly unconfirmed hypothesis, the responsible person/area, and the status exactly as the person supplies them. Mark the hypothesis as unconfirmed. Do not treat it as fact or change its status on your own.

**Step 4 — Assign the ID the reader chose.**
Enter the ID the reader chose from their assigned range (`SIFAP-M-01` through
`SIFAP-M-20`), or `BONUS` for an additional distinct question. Preserve existing
IDs. Never pretend an ID proves a known answer, split one finding to fill slots,
or count two representations of the same source as independent evidence.

**Step 5 — Write the row.**
Append one row to `01-archaeology/mysteries-found.md` with all seven fields,
using the [blank template](../../01-archaeology/templates/mysteries-found.template.md)
when needed. Add no answer, solution, or invented validation. A question stays
open until a responsible person provides explicit evidence-backed human
validation. You record that information; you never produce or confirm it.

## Invocation Example

```text
/catalog-mysteries scope=01-archaeology/
```

Expect one new row in `01-archaeology/mysteries-found.md` with the question, `path:line` evidence, impact, unconfirmed hypothesis, owner, and status — and no answer.
