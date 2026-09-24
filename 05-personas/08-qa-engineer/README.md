# QA Engineer — Copilot Kit

> **Track:** [Team Kit](../../README.md) › [Personas](../OVERVIEW.md) › **QA Engineer**

**Reference kit for the QA Engineer persona in the SIFAP modernization workshop.**

![Persona](https://img.shields.io/badge/Persona-QA%20Engineer-171717?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Person taking the QA Engineer persona in the workshop |
| **Focus** | Generating tests from EARS specs, covering critical behavior, and keeping the pipeline green |
| **SDLC phase** | Stages 1-3 plus final judge validation: test design, reconciliation, and evidence checks |
| **Expected outcome** | Passing test suite, green CI pipeline, and guaranteed spec-to-test traceability |

Read first: [PERSONA.md](PERSONA.md).

---

## Concept

The QA Engineer transforms EARS requirements into executable tests. In the SIFAP (Payment Inspection and Administration System) modernization, this persona validates functional equivalence between the Natural legacy behavior and the modern Java 21 code, ensuring that every REQ-ID has at least one verifiable test and that the GitHub Actions CI pipeline remains green.

Why it matters: missing or fragile tests leave the participant blind to regressions. In legacy modernization, functional equivalence between old and new behavior can only be proven by tests traceable to requirements.

## Persona kit

All active artifacts live in the repository root `.github/` directory. This folder is a reference; edit the files under `.github/` when maintenance is needed.

| File | Type | Purpose |
|---|---|---|
| `PERSONA.md` | Profile | QA Engineer responsibilities, stages, prompts, and rubrics |
| `.github/skills/persona-qa-engineer/SKILL.md` | Skill | Test generation, coverage analysis, and quality gates |
| `.github/prompts/persona-qa-engineer-create-tests.prompt.md` | Prompt | `/create-tests` |
| `.github/prompts/persona-qa-engineer-coverage-gaps.prompt.md` | Prompt | `/coverage-gaps` |
| `.github/prompts/persona-qa-engineer-test-strategy.prompt.md` | Prompt | `/test-strategy` |
| `.github/instructions/tests.instructions.md` | Instructions | Testing conventions |

> [!TIP]
> Verify optional tools through the [persona setup guidance](../README.md#how-to-activate-your-persona). Sample hooks and descriptive manifests are not passing test evidence.

## Where active artifacts live

- Agents: `.github/agents/`
- Prompts: `.github/prompts/persona-*.prompt.md`
- Skills: `.github/skills/`
- Instructions: `.github/instructions/`

## Best practices

- [ ] **Follow the test pyramid.** Prioritize more unit tests, a moderate number of integration tests, and fewer end-to-end tests.
- [ ] **Treat a flaky test as a bug.** Isolate, fix, or remove it; never ignore it.
- [ ] **Ensure every assertion proves behavior.** Line coverage without a meaningful assertion does not validate the domain.
- [ ] **Trace tests to requirements.** Every test must reference a REQ-ID in an inline comment.

## Apply the workflow to SIFAP

During archaeology, independently verify the DBA's source baseline and actual
reading evidence. In Stage 2, derive tests from the participant's reviewed REQ-IDs and
data mappings. In Stages 3-4, use PostgreSQL integration tests and independent
reconciliation to verify complete source-key/field/relationship coverage, real
beneficiary queries, and recovery. A copied expected result or a test seed is
not proof of migration. Use the [data lifecycle](../../docs/DATA-MIGRATION.md);
the kit supplies no completed test outcomes.

## References

- [Google Testing Blog](https://testing.googleblog.com/)
- [xUnit Test Patterns — Gerard Meszaros](http://xunitpatterns.com/)
- [Software Testing ISTQB](https://www.istqb.org/)
- [Property-Based Testing — jqwik/fast-check](https://jqwik.net/)

---

### Continue reading

| Previous | Next |
|---|---|
| [Persona overview](../OVERVIEW.md)<br/><sub>Role-by-stage checklist for the 10 personas.</sub> | [PERSONA.md](PERSONA.md)<br/><sub>Complete QA Engineer persona profile.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
