# Developer — Copilot Kit

> **Track:** [Team Kit](../../README.md) › [Personas](../OVERVIEW.md) › **Developer**

**Reference kit for the Developer persona in the SIFAP modernization workshop.**

![Persona](https://img.shields.io/badge/Persona-Developer-171717?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Person taking the Developer persona in the workshop |
| **Focus** | Java 21 + Next.js 15 implementation, TDD, bug fixing |
| **SDLC phase** | Stage 3: Java/TypeScript implementation, tests, and integration |
| **Expected outcome** | Backend + frontend for the prioritized slice with passing tests |

Read first: [PERSONA.md](PERSONA.md).

---

## Concept

The Developer transforms EARS specifications into executable code. In the SIFAP (Payment Inspection and Administration System) modernization, this persona translates Natural programs and DDM/Adabas models into Java 21 with Spring Boot 3.3, JPA/Hibernate, and PostgreSQL 16, while also implementing the frontend in Next.js 15 with TypeScript.

Why it matters: without the Developer, requirements remain text. This persona turns the proof of concept into tested, mergeable software.

## Persona kit

All active artifacts live in the repository root `.github/` directory. This folder is a reference; edit the files under `.github/` when maintenance is needed.

| File | Type | Purpose |
|---|---|---|
| `PERSONA.md` | Profile | Developer responsibilities, stages, prompts, and rubrics |
| `.github/skills/persona-developer/SKILL.md` | Skill | Implementation, TDD, and bug fixing |
| `.github/prompts/persona-developer-implement.prompt.md` | Prompt | `/implement` |
| `.github/prompts/persona-developer-fix-bug.prompt.md` | Prompt | `/fix-bug` |
| `.github/prompts/persona-developer-tdd.prompt.md` | Prompt | `/tdd` |
| `.github/prompts/persona-developer-refactor.prompt.md` | Prompt | `/refactor` |

> [!TIP]
> Optional tools follow the [persona setup guidance](../README.md#how-to-activate-your-persona). No executable MCP configuration ships in this persona folder.

## Where active artifacts live

- Agents: `.github/agents/`
- Prompts: `.github/prompts/persona-*.prompt.md`
- Skills: `.github/skills/`
- Instructions: `.github/instructions/`

## Best practices

- [ ] **Write tests before or alongside the code.** When the design is clear, write the test first. Every commit includes tests.
- [ ] **Keep PRs small.** One topic per PR, reviewable in about 20 minutes.
- [ ] **Separate refactoring from behavior changes.** Use distinct commits for each intent.
- [ ] **Comment why, not what.** The code describes what it does; the comment explains the reason.

## Apply the workflow to SIFAP

Select a task from the participant's approved `tasks.md`, reread its actual
`source_legacy:`, and write the governing acceptance tests before implementation.
Work with DBA and QA on the [data lifecycle](../../docs/DATA-MIGRATION.md):
the real API/UI must query migrated PostgreSQL records, including all authorized
beneficiaries across pages. No endpoint behavior or completed requirement is
provided by this kit.

## References

- [Clean Code — Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Refactoring — Martin Fowler](https://refactoring.com/)
- [Test-Driven Development — Kent Beck](https://www.oreilly.com/library/view/test-driven-development/0321146530/)
- [GitHub Copilot Best Practices](https://docs.github.com/en/copilot)

---

### Continue reading

| Previous | Next |
|---|---|
| [Persona overview](../OVERVIEW.md)<br/><sub>Role-by-stage checklist for the 10 personas.</sub> | [PERSONA.md](PERSONA.md)<br/><sub>Complete Developer persona profile.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
