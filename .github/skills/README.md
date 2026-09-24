# Skills Index

This directory contains the GitHub Copilot Agent Skills for the workshop — **54** in total, each in its own `<name>/SKILL.md`.

> [!NOTE]
> Copilot discovers `SKILL.md` files under `.github/skills/<name>/` and auto-loads a skill by semantically matching your request against its `description`. That matching is invisible to people, which is what this index is for. The descriptions below are load-bearing: each states *when to use* the skill, so keep them accurate.

## Skills by area

All 54 skills, grouped by what they do. Every skill appears in exactly one group.

### Team roles (11 skills)

These carry the responsibilities that used to be persona agents. They load
automatically into whichever stage agent is active, so nobody has to re-select a
role. The reasoning is in [ADR-0002](../../docs/adr/0002-team-roles-as-skills-not-agents.md).

| Skill | Description |
| --- | --- |
| [`ux-research-design`](ux-research-design/) | Jobs-to-be-Done, user journeys, information architecture, and accessibility acceptance criteria — research, never component code. |

> [!NOTE]
> The DBA role is **not** in this list. It stays an agent (`@dba`) because the
> data lifecycle spans all four stages and owns tool-scoped prompts.

### Workshop, SDD & requirements (7 skills)

| Skill | Description |
| --- | --- |
| [`sdd-requirements-engineer`](sdd-requirements-engineer/) | Use for evidence-backed EARS authoring, validation, and checkpoint preparation with official Spec-Kit, `REQ-NNN`, `source_legacy:`, and data migration acceptance. Does not create a parallel SDD tree or prefilled exercise solutions. |
| [`user-story-refine`](user-story-refine/) | Use when refining backlog items, splitting epics, or validating INVEST criteria. Triggers include "refine story", "split epic", "acceptance criteria", "user story", and "INVEST". |
| [`code-modernization`](code-modernization/) | Use when modernizing a legacy system with a disciplined, behavior-preserving workflow. Triggers include "modernize", "legacy code", "COBOL", "business-rule extraction", and "behavior-preserving rewrite". |

### Java & Spring Boot backend (6 skills)

| Skill | Description |
| --- | --- |
| [`create-spring-boot-java-project`](create-spring-boot-java-project/) | Scaffold a Spring Boot (Java 21) project skeleton via start.spring.io with Maven, springdoc-openapi, and ArchUnit, ready to run with Docker Compose. Use when the user wants to bootstrap a new Spring Boot backend or generate a starter project. Aligns to the kit's Java 21 + Spring Boot 3.3 stack. |
| [`java-springboot`](java-springboot/) | Spring Boot application best practices — package-by-feature structure, constructor injection, DTOs and validation, service-layer transactions, Spring Data JPA, and configuration/secrets handling. Use when building or reviewing Spring Boot backend code and you want idiomatic structure and conventions. Complements the kit's Java 21 + Spring Boot 3.3 stack. |
| [`java-docs`](java-docs/) | Apply Javadoc best practices so Java types and members are documented correctly — summary sentences, @param/@return/@throws, {@code} blocks, @since, and inherited docs. Use when the user asks to write, review, or improve Javadoc or API documentation for Java code. |
| [`java-junit`](java-junit/) | JUnit 5 unit-testing best practices — test structure (Arrange-Act-Assert), lifecycle, parameterized/data-driven tests, assertions, Mockito isolation, and test organization. Use when writing or reviewing plain JUnit 5 unit tests for Java business logic. For Spring Boot slice/integration tests (@WebMvcTest, @DataJpaTest, Testcontainers), use spring-boot-testing. |
| [`spring-boot-testing`](spring-boot-testing/) | Select the right Spring Boot test technique for a scenario — test slices (@WebMvcTest, @DataJpaTest, @RestClientTest, @JsonTest, @SpringBootTest), Testcontainers, Mockito, and AssertJ. Use when writing or reviewing Spring Boot integration or slice tests. Targets the kit's Spring Boot 3.3 + JUnit 5; newer 3.4+/4.0 APIs (MockMvcTester, @MockitoBean, RestTestClient) are noted as out of scope for the kit. |

### Data & database (4 skills)

| Skill | Description |
| --- | --- |

### Frontend & testing (4 skills)

| Skill | Description |
| --- | --- |
| [`playwright-generate-test`](playwright-generate-test/) | Generate a Playwright end-to-end test in TypeScript from a described scenario by driving the Playwright MCP step by step, then run it until it passes. Use when the user asks to create or record a browser or E2E test with Playwright for a web flow. |
| [`tdd-workflow`](tdd-workflow/) | Use when practicing test-driven development, writing a failing test first, or guiding red-green-refactor. Triggers include "TDD", "red-green-refactor", "test first", "failing test", and "write a test". |
| [`test-strategy`](test-strategy/) | Use when designing a test strategy, choosing the test-pyramid shape, defining coverage targets, or evaluating testing investments across unit, integration, and E2E layers. Triggers include "test strategy", "test pyramid", "coverage target", "E2E vs integration", and "testing investment". |

### Azure, IaC & CI/CD (14 skills)

| Skill | Description |
| --- | --- |

### Documentation & diagrams (4 skills)

| Skill | Description |
| --- | --- |
| [`doc-style-lint`](doc-style-lint/) | Use when reviewing documentation for style, clarity, inclusive language, or compliance with Microsoft or Google style guides. Triggers include "doc review", "style guide", "plain language", "inclusive language", and "readability". |

### Codebase context & Copilot tooling (4 skills)

| Skill | Description |
| --- | --- |
| [`acquire-codebase-knowledge`](acquire-codebase-knowledge/) | Use this skill when the user explicitly asks to map, document, or onboard into an existing codebase. Trigger for prompts like "map this codebase", "document this architecture", "onboard me to this repo", or "create codebase docs". Do not trigger for routine feature implementation, bug fixes, or narrow code edits unless the user asks for repository-level discovery. |
| [`copilot-sdk`](copilot-sdk/) | Build agentic applications with GitHub Copilot SDK. Use when embedding AI agents in apps, creating custom tools, implementing streaming responses, managing sessions, connecting to MCP servers, or creating custom agents. Triggers on Copilot SDK, GitHub SDK, agentic app, embed Copilot, programmable agent, MCP server, custom agent. |

## Maintenance Rule

- The `name:` in a `SKILL.md` **must exactly equal its parent directory name** (lowercase letters, digits, and hyphens; 64 characters max) or Copilot silently fails to load the skill.
- Only `name` and `description` are valid frontmatter keys; any other key (for example `license`, `allowed-tools`, `compatibility`, or `metadata`) fails the `copilot-primitives` gate.
- `description` is capped at **1024 characters** and must state *when to use* the skill, because it is the only signal Copilot uses to auto-load it.
- Every skill body needs, in order: `## When to invoke`, a substantive procedure section, `## Output template`, and `## Quality gate`.
- The full schema and section contract live in [`../PRIMITIVE-STANDARD.md`](../PRIMITIVE-STANDARD.md) and are enforced by [`../scripts/validate-copilot-primitives.py`](../scripts/validate-copilot-primitives.py). When you add a skill, add its row to the matching group above and keep the total count current.
