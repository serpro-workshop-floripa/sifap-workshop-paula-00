# ADR-0002: Team roles are skills; only stages and the data lifecycle are agents

> **Path:** [Team Kit](../../README.md) › [Docs](../README.md) › [ADRs](README.md) › **ADR-0002**

| Field | Value |
|---|---|
| **Status** | accepted |
| **Date** | 2026-09-15 |
| **Authors** | Kit maintainers |
| **Supersedes** | N/A |

---

## Context

The kit shipped **17 agents**: 4 stage agents, 10 persona agents, and 3 depth
specialists. Two of those groups were doing different jobs under one primitive.

A **stage** is a phase the whole team enters and leaves together. It has a start,
a definition of done, and a handoff to the next stage. Selecting it deliberately
is the point — the selection *is* the ritual.

A **role** is a responsibility one person carries through every stage. The
Product Owner does not stop being the Product Owner when Stage 3 begins. Yet the
persona-agent design required that person to re-select `@product-owner` in every
conversation, and to re-select the stage agent afterwards to get stage context
back. The two layers competed for a single selector instead of composing.

Three concrete costs followed:

1. **Selector load.** Seventeen entries for a five-person, eight-hour workshop.
2. **Teaching load.** Three separate documents existed to explain why two layers
   are "not duplicates" — a reliable sign that the abstraction, not the
   documentation, was wrong.
3. **Dead weight.** The three specialist agents owned **zero** prompts. They were
   pure knowledge already, wearing an agent's frontmatter.

Skills solve the role half directly: they load from their `description` through
semantic matching, so the knowledge arrives without a selection step and composes
with whatever agent is active.

One role does not fit the rule. The **DBA** owns the data lifecycle, which the
persona matrix marks as `Data lead` in **all four** stages, and which owns
tool-scoped prompts (`persona-dba-migration`, `persona-dba-query-audit`,
`postgresql-code-review`, `postgresql-optimization`). It is cross-stage by
definition, so it cannot be folded into a stage agent, and its prompts need a
binding target that only an agent provides.

## Decision

Keep **five agents**: the four stage agents (`archaeologist`, `architect`,
`builder`, `evolution`) plus `dba`.

Convert the nine remaining persona agents and the three specialists to skills
under `.github/skills/`. Rebind each orphaned prompt to the stage agent that owns
the moment when that prompt is used, and open each rebound prompt's body by
loading the role skill that carries its boundary, procedure, and quality gate.

The governing rule for future primitives: **a new phase is an agent; a new role
is a skill.**

## Alternatives considered

| Alternative | Why it was rejected |
|---|---|
| Keep all 17 agents | Preserves every cost above and keeps two primitives competing for one selector. |
| Hide personas with `user-invocable: false` | Cheap and reversible, and it does declutter the selector — but the knowledge still fails to compose into the active agent, which is the actual defect. Useful as a trial, not as the destination. |
| Convert the DBA too, and drop its agent | The data lifecycle spans all four stages and owns four tool-scoped prompts. Folding it into one stage agent would misrepresent when the work happens. |
| Merge persona prompts into the stage agents' bodies | Destroys the slash commands, which are the part participants actually use. |

## Consequences

- **Easier:** five entries in the selector; role knowledge arrives without being requested; the two-layer model needs one table instead of three documents; twelve fewer primitives to keep in sync.
- **Harder:** a participant who wants a role's full context on demand must name it (`persona-qa-engineer`) rather than `@`-mention it. Skill matching is semantic, so a `description` that drifts silently degrades loading — descriptions now carry more weight and are reviewed accordingly.
- **Risks:** 37 prompts changed their `agent:` binding in one commit. A partial application would fail the `copilot-primitives` gate, which is the intended safety net.
- **Mitigations:** the gate validates `prompt -> agent` integrity and skill `name`-to-directory equality on every PR; [`.github/agents/README.md`](../../.github/agents/README.md) carries the former-agent-to-skill mapping so a stale reference is traceable.


## 2026-09-24 note

[ADR-0003](0003-individual-challenge-format.md) moves the workshop to an individual challenge format. This decision still holds: one participant switches stage agents across the challenge while all role skills remain available and load as the work requires them.

## Related

- REQ-IDs: N/A
- ADRs: [ADR-0001](0001-agent-instructions-single-source-of-truth.md)
- Instruction files: [`.github/PRIMITIVE-STANDARD.md`](../../.github/PRIMITIVE-STANDARD.md), [`.github/instructions/agent-skills.instructions.md`](../../.github/instructions/agent-skills.instructions.md)

## References

- GitHub Docs — About customizing GitHub Copilot responses: <https://docs.github.com/en/copilot/concepts/response-customization>
- GitHub Docs — Support for different types of custom instructions: <https://docs.github.com/en/copilot/reference/custom-instructions-support>

---

### Continue reading

| Previous | Next |
|---|---|
| [ADR-0001](0001-agent-instructions-single-source-of-truth.md)<br/><sub>Single source of truth for agent instructions.</sub> | [ADRs — Index](README.md)<br/><sub>Index of recorded decisions.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
