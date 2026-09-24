# Technical Lead — Copilot Kit

> **Trail:** [Team Kit](../../README.md) › [Personas](../OVERVIEW.md) › **Technical Lead**

**Inventory of the Copilot kit for the Technical Lead persona.** Lists the active artifacts, where they live under `.github/`, and best practices specific to this role.

| Field | Value |
|---|---|
| **Target audience** | Person acting as Technical Lead in the workshop |
| **Role scope** | Technical leadership responsibility (covered by the participant) |
| **SDLC phase** | Stages 2-3: sequencing, standards, self-review, and submission readiness |
| **Prerequisites** | [PERSONA.md](PERSONA.md) read |
| **Expected outcome** | Kit validated, prompts accessible in Copilot Chat |

> [!IMPORTANT]
> Read [PERSONA.md](PERSONA.md) before continuing. The profile explains the mission, self-check, and evaluation rubrics.

---

## Concept

The Technical Lead connects architecture to everyday code. This role defines implementation standards, unblocks the participant when someone gets stuck on a technical detail, and ensures that the application created by the participant actually runs end to end by the end of Stage 3. In SIFAP (Payment Inspection and Administration System), the TL maintains execution speed without compromising quality by choosing which technical battles are worth fighting.

---

## Persona kit

| **Artifact** | Type | Purpose |
|---|---|---|
| `PERSONA.md` | Profile | Responsibilities, self-check, prompts, and rubric |
| `.github/skills/persona-technical-lead/SKILL.md` | Skill | Technical governance |
| `.github/prompts/persona-technical-lead-setup-project.prompt.md` | Prompt | `/setup-project` |
| `.github/prompts/persona-technical-lead-routing-table.prompt.md` | Prompt | `/routing-table` |
| `.github/prompts/persona-technical-lead-audit-context.prompt.md` | Prompt | `/audit-context` |
| [CI conventions](../../.github/instructions/cicd.instructions.md) | Validation | Use real scoped test/build checks; do not suppress failures through sample hooks |

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

Optional integrations follow the [persona setup guidance](../README.md#how-to-activate-your-persona); preserve existing configuration and verify permissions.

---

## Best practices

- Block bad changes, not people; review the PR and protect reviewers' time.
- `CODEMAP.md` is the participant's working memory; if it is outdated, the participant works without visibility.
- Model routing matters: Opus for discovery, Sonnet for implementation, Haiku for mechanical transformations.
- Cost per feature is an engineering metric; track it alongside coverage.

---

## References

- [Staff Engineer — Will Larson](https://staffeng.com/)
- [The Manager's Path — Camille Fournier](https://www.oreilly.com/library/view/the-managers-path/9781491973882/)
- [Accelerate — Forsgren, Humble, Kim](https://itrevolution.com/product/accelerate/)
- [GitHub Copilot Best Practices](https://docs.github.com/en/copilot)

---

### Continue reading

| Previous | Next |
|---|---|
| [OVERVIEW](../OVERVIEW.md)<br/><sub>Table of the 10 personas.</sub> | [PERSONA.md](PERSONA.md)<br/><sub>Profile for this persona.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
