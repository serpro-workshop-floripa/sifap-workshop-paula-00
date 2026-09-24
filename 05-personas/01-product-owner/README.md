# Product Owner — Copilot Kit

> **Trail:** [Team Kit](../../README.md) › [Personas](../OVERVIEW.md) › **Product Owner**

**Inventory of the Copilot kit for the Product Owner persona.** Lists the active artifacts, where they live under `.github/`, and best practices specific to this role.

| Field | Value |
|---|---|
| **Target audience** | Person acting as Product Owner in the workshop |
| **Role scope** | Vision responsibility (covered by the participant) |
| **SDLC phase** | Stages 1-3 plus final judge validation: scope, acceptance criteria, and migrated-data acceptance |
| **Prerequisites** | [PERSONA.md](PERSONA.md) read |
| **Expected outcome** | Kit validated, prompts accessible in Copilot Chat |

> [!IMPORTANT]
> Read [PERSONA.md](PERSONA.md) before continuing. The profile explains the mission, self-check, and evaluation rubrics.

---

## Concept

The Product Owner is responsible for translating business needs into executable scope. In a legacy modernization process such as SIFAP (Payment Inspection and Administration System), this function is critical: legacy systems accumulate implicit rules that only make sense when someone knows "why" they exist. The PO connects every technical decision to business evidence.

---

## Persona kit

| **Artifact** | Type | Purpose |
|---|---|---|
| `PERSONA.md` | Profile | Responsibilities, self-check, prompts, and rubric |
| `.github/skills/persona-product-owner/SKILL.md` | Skill | Product Owner role guidance for specification, backlog, and acceptance |
| `.github/prompts/persona-product-owner-spec.prompt.md` | Prompt | `/spec` — writes a section of `.spec/<NNN>-<feature>/spec.md` from user stories in EARS |
| `.github/prompts/persona-product-owner-update-spec.prompt.md` | Prompt | `/update-spec` — updates the specification when a feature changes |
| `.github/prompts/persona-product-owner-acceptance-check.prompt.md` | Prompt | `/acceptance-check` — checks whether the code meets the acceptance criteria |
| [Optional integration guidance](../README.md#how-to-activate-your-persona) | Reference | Verify real configured tools; no persona manifest is installed |

---

## Where the artifacts live

The active artifacts are consolidated under the root `.github/` directory:

| **Type** | Path |
|---|---|
| Agents | `.github/agents/` |
| Prompts | `.github/prompts/persona-*.prompt.md` |
| Skills | `.github/skills/` |
| Instructions | `.github/instructions/` |

Use this directory as the reference. Active files live only under the root `.github/` directory — edit them there when maintenance is needed.

Optional integrations follow the [persona setup guidance](../README.md#how-to-activate-your-persona); never copy a descriptive manifest as executable configuration.

---

## Best practices

- Write requirements in EARS so that every sentence is testable.
- Keep every user story tied to a measurable outcome.
- Mark assumptions explicitly — a hidden assumption becomes a production bug.
- Treat `.specify/memory/constitution.md` as the source of truth for non-negotiable items.

---

## References

- [EARS Notation — Alistair Mavin](https://alistairmavin.com/ears/)
- [Spec-Driven Development (Spec-Kit)](https://github.com/github/spec-kit)
- [User Story Mapping — Jeff Patton](https://www.jpattonassociates.com/user-story-mapping/)
- [GitHub Copilot for PMs](https://docs.github.com/en/copilot)

---

### Continue reading

| Previous | Next |
|---|---|
| [OVERVIEW](../OVERVIEW.md)<br/><sub>Table of the 10 personas.</sub> | [PERSONA.md](PERSONA.md)<br/><sub>Profile for this persona.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
