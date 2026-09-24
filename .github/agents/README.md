# Agents Index

This directory contains the GitHub Copilot custom agents for the workshop — **5** in total, each in its own `<name>.agent.md`.

> [!NOTE]
> Copilot discovers `*.agent.md` files in `.github/agents/`. Invoke an agent by its `name` with `@<name>` (for example `@archaeologist`). The `name` also binds prompts: a `*.prompt.md` file selects its agent through the `agent:` frontmatter key, so an agent's id is a contract, not a label.

## The two-layer model

The kit separates **when** you are working from **which role** you are covering.

| Layer | Primitive | How it loads | Why |
|---|---|---|---|
| **Stage** — the phase the participant is in | Agent, invoked with `@name` | You select it deliberately, once per stage | A stage has a start, a definition of done, and a self-checkpoint |
| **Role** — the responsibility you personally own | Skill, in [`../skills/`](../skills/) | Loads automatically from its `description` | You carry your role into every stage; nobody should have to remember to re-select it |

One exception carries a dedicated agent: **`dba`**. The data lifecycle spans all
four stages rather than sitting inside one, so it cannot be a stage agent, and it
owns tool-scoped prompts that a skill cannot bind. Every other team role is a
skill.

> [!TIP]
> Keep the stage agent selected all day and let your role skill compose into it.
> Selecting `@builder` and asking for coverage gaps loads the QA role on its own.

## Stage agents

Three challenge agents run in sequence through the `handoffs:` frontmatter key — `archaeologist -> architect -> builder`. The retained Stage 4 agent (`evolution`) is not used in the individual challenge.

| Stage | Agent | Invoke | Bound prompts | Description |
| --- | --- | --- | --- | --- |
| Stage 1 | [`archaeologist`](archaeologist.agent.md) | `@archaeologist` | 6 | Guides actual source/data reading, records coverage, dependencies and unanswered questions |
| Stage 2 | [`architect`](architect.agent.md) | `@architect` | 16 | Defines bounded contexts, writes EARS specifications, generates ADRs, and designs a Modular Monolith architecture |
| Stage 3 | [`builder`](builder.agent.md) | `@builder` | 19 | Translates Natural to Java, generates JPA from FDTs, writes equivalence tests, and builds REST + Next.js |
| Stage 4 (not used in challenge) | [`evolution`](evolution.agent.md) | `@evolution` | 16 | Retained for post-challenge workflows; the individual challenge ends at Stage 3 and judge validation |

## Cross-stage agent

| Agent | Invoke | Bound prompts | Description |
| --- | --- | --- | --- |
| [`dba`](dba.agent.md) | `@dba` | 4 | Adabas data discovery, source readiness, PostgreSQL migration and reconciliation, safe schema evolution, and evidence-based query auditing |

## Role skills that replaced persona agents

Nine persona agents and three specialist agents were converted to skills. The
slash commands did not change; only the agent that hosts them did.

| Former agent | Now this skill | Prompts moved to |
| --- | --- | --- |
| `se-ux-ui-designer` | [`ux-research-design`](../skills/ux-research-design/SKILL.md) | owned no prompts |

The rationale and the trade-offs are recorded in [ADR-0002](../../docs/adr/0002-team-roles-as-skills-not-agents.md).

## Prompt ownership

The 61 prompts in [`../prompts/`](../prompts/) bind to an agent through their `agent:` key:

- All **61** bind to one of the **5** agents above — no prompt is left on the generic built-in `agent: "agent"`. The per-agent counts are in the tables' **Bound prompts** columns.
- A prompt whose work belongs to a team role opens its body by loading that role's skill, so the role knowledge travels with the task.

Regenerate the counts with `grep -h '^agent:' ../prompts/*.prompt.md | sort | uniq -c`.

## Maintenance Rule

- Renaming an agent silently breaks **every** prompt bound to it via `agent:`; rename the agent and all its prompt bindings together, then re-run the validator.
- `description` is the only frontmatter key the gate strictly requires; `handoffs` is for challenge Stage agents only and only when a next stage exists.
- Adding a new agent needs a reason the two-layer model does not already cover. A new **role** is a skill; a new **phase** is an agent.
- The required body sections (`Mission`, `Lead Personas`, `Operating Principles`, `What This Agent Knows`, `What This Agent Does NOT Know`, `Available Prompts`, a `Definition of Done` heading, `Anti-Patterns This Agent Rejects`, `Spec-Kit Integration`) and the full schema are defined in [`../PRIMITIVE-STANDARD.md`](../PRIMITIVE-STANDARD.md) and enforced by [`../scripts/validate-copilot-primitives.py`](../scripts/validate-copilot-primitives.py).
- When you add an agent, add its row to the correct layer above and, if a prompt should invoke it, set that prompt's `agent:` to this `name`.
