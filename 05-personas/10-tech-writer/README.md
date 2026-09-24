# Tech Writer — Copilot Kit

> **Track:** [Team Kit](../../README.md) › [Personas](../OVERVIEW.md) › **Tech Writer**

**Reference kit for the Tech Writer persona in the SIFAP modernization workshop.**

![Persona](https://img.shields.io/badge/Persona-Tech%20Writer-171717?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Person taking the Tech Writer persona in the workshop |
| **Focus** | API documentation, evolving README, `CODEMAP.md`, ADRs, changelog, and drift detection |
| **SDLC phase** | Stages 1-3: glossary, spec/ADR clarity, README, and factual run notes |
| **Expected outcome** | Glossary, discovery notes, readable spec/ADRs, README/run notes, factual PR text verified for the individual submission |

Read first: [PERSONA.md](PERSONA.md).

---

## Concept

The Tech Writer transforms decisions and code into durable project memory. In the SIFAP (Payment Inspection and Administration System) modernization, this persona maintains the glossary of Natural/Adabas legacy terms, formalizes architecture decisions as ADRs (Architecture Decision Records), and ensures that the README reflects the application's real state every hour of the workshop, not only at the end.

Why it matters: without deliberate documentation, ADRs remain empty, the README stays at "TODO: add instructions," and knowledge discovered during the workshop disappears afterward. The Tech Writer makes team learning traceable.

## Persona kit

All active artifacts live in the repository root `.github/` directory. This folder is a reference; edit the files under `.github/` when maintenance is needed.

| File | Type | Purpose |
|---|---|---|
| `PERSONA.md` | Profile | Tech Writer responsibilities, stages, prompts, and rubrics |
| `.github/skills/persona-tech-writer/SKILL.md` | Skill | API docs, README, `CODEMAP.md`, changelog, and drift detection |
| `.github/prompts/persona-tech-writer-generate-docs.prompt.md` | Prompt | `/generate-docs` |
| `.github/prompts/persona-tech-writer-update-codemap.prompt.md` | Prompt | `/update-codemap` |
| `.github/prompts/persona-tech-writer-doc-drift.prompt.md` | Prompt | `/doc-drift` |

> [!NOTE]
> Edit and review the participant's Markdown directly in the repository. This participant persona does not distribute a Pages deployment server; website publication belongs to the instructor repository.

## Where active artifacts live

- Agents: `.github/agents/`
- Prompts: `.github/prompts/persona-*.prompt.md`
- Skills: `.github/skills/`
- Instructions: `.github/instructions/`

## Best practices

- [ ] **Treat documentation as a feature.** Deliver, version, and review it with the code, not afterward.
- [ ] **Lead with the answer, then provide context.** Write for someone with 30 seconds.
- [ ] **Use Mermaid for diagrams.** Diagrams as code evolve with the system.
- [ ] **Include drift checks in CI.** Outdated documentation is worse than none.

## Apply the workflow to SIFAP

During archaeology, organize terms and findings the participants actually
established, with source links. Keep templates blank and generated team artifacts
separate. During implementation and evolution, document only real contracts,
commands, sanitized data evidence, and observed Agent outcomes. Do not supply
completed findings, invented endpoints, or a pre-approved self-check.

## References

- [Diátaxis Framework](https://diataxis.fr/)
- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Write the Docs](https://www.writethedocs.org/)
- [Mermaid — Diagramming as Code](https://mermaid.js.org/)

---

### Continue reading

| Previous | Next |
|---|---|
| [Persona overview](../OVERVIEW.md)<br/><sub>Role-by-stage checklist for the 10 personas.</sub> | [PERSONA.md](PERSONA.md)<br/><sub>Complete Tech Writer persona profile.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
