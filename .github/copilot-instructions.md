# GitHub Copilot Instructions — Legacy Modernization Workshop

> These instructions tell Copilot what the participant is building, which stack to use,
> which conventions to follow, and what NOT to do. They apply to each participant's entire
> repository.

## Approved Tools — These Only

This workshop uses a **fixed toolchain**: VS Code, GitHub Copilot (Ask + Plan + Agent modes), GitHub Spec-Kit, GitHub, Docker / Docker Compose, and Terraform. Other AI assistants, IDEs, web chat UIs, and SDD frameworks are not permitted because mixing tools breaks specification → code → test traceability. Full table: [`README.md`](../README.md).

## Project Context

Modernization of the approximately 30-year-old Natural/Adabas **SIFAP** system (Payment Inspection and Administration System) to Java 21 + Next.js 15; [chronology](../01-archaeology/legacy-sifap/CHRONOLOGY.md) is transcribed from source headers and starts in 1997, with a 2026 workshop reference year. Preserve source dates and cite that file rather than restating a date. [`01-archaeology/legacy-sifap/`](../01-archaeology/legacy-sifap/) contains 24 Natural/JCL members, 4 `.ddm` DDMs, and 1 FDT listing; [assignments](../01-archaeology/legacy-sifap/natural-programs/README.md) cover 15 assigned and 9 supporting members.

The workshop is an **individual challenge** (14:00-17:40): each participant does Stages 1-3 alone, starting in `@archaeologist`, and the first two submissions that pass judge validation win; Stage 4 and parallel sub-agent orchestration are not part of it. See [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) and [ADR-0003](../docs/adr/0003-individual-challenge-format.md).

The kit uses **two layers**: a stage agent per phase (the challenge uses `archaeologist`, `architect`, `builder`, and the cross-stage `dba`; `evolution` is kept but unused) and a role skill for each of the 10 roles the participant covers. Roles are skills so they load automatically and compose into whichever stage agent is active; see [`06-stage-agents/README.md`](../06-stage-agents/README.md) and [ADR-0002](../docs/adr/0002-team-roles-as-skills-not-agents.md). A new phase is an agent; a new role is a skill.

Use the skills in [`.github/skills/`](skills/) for specialized workflows. Copilot selects the relevant skill from its description; do not duplicate specialized workflows in these global instructions.

## Repository languages

- Keep documentation and all Copilot primitive prose (agents, prompts, instructions, skills, and hooks) on `main` and `develop` in English; publish Brazilian Portuguese on `portugues-br` and Spanish on `espanol`.
- Follow the target branch's language, not the conversation language. Never merge the translated documentation tree into `main`.
- Preserve technical paths, identifiers, and legacy sources. Keep the [language selector](../README.md#repository-languages) linked to existing language branches and their instructions.

## Participant-only scope

- Keep only exercise guides, templates, Copilot primitives and local source inputs in this kit.
- The website, Pages publication, instructor demos, answer keys and reference solutions belong in the private instructor repository.
- Do not publish access addresses, credentials or administration instructions for instructor environments. Teams build and document their own solution.

## Target Stack

- **Backend:** Java 21 + Spring Boot 3.3 + JPA/Hibernate + PostgreSQL 16
- **Frontend:** Next.js 15 (App Router) + TypeScript 5 (strict) + Tailwind CSS + shadcn/ui
- **Containers:** Docker + Docker Compose created by the participant in Stage 3 when necessary
- **IaC:** Terraform (Azure provider ~> 3.x)
- **CI/CD:** GitHub Actions
- **Testing:** JUnit 5 + Testcontainers (backend); Vitest + Testing Library (frontend)

## Cross-Cutting Implementation Rules

Detailed Java, TypeScript, database, security, infrastructure, and test rules live in [`.github/instructions/`](instructions/) and load automatically for matching paths.

- Use English class names and comments.
- Path REST APIs as `/api/v1/{resource}`.
- Validate inputs at every system boundary.
- Never hardcode secrets, API keys, or credentials.
- Never expose sensitive data (CPF, benefit amounts) in logs — mask it.
- Configure CORS explicitly — no `*` wildcard in production.
- Use Managed Identity for Azure service-to-service authentication.
- Write tests during implementation, not after the fact.

## Spec-Driven Development (Spec-Kit)

- Every requirement uses **EARS notation** (Easy Approach to Requirements Syntax)
- Every requirement has a unique **REQ-ID** in the `REQ-NNN` format
- **Every requirement includes a `source_legacy:` line** pointing to legacy files or `[GREENFIELD] + justification.`
  Use `01-archaeology/legacy-sifap/natural-programs/*.{NSP,NSN,NSS,NSA,NSL,NSC,NSM,jcl}` or `01-archaeology/legacy-sifap/adabas-ddms/*.{NSD,ddm,txt}` for legacy-backed requirements.
  The `legacy-traceability` CI job rejects PRs that violate this rule. See [`01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md`](../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md).
- Tests trace to REQ-IDs through inline comments
- Branch strategy: one repository per participant; each prefix is cut from `develop` (never from `spec/*`) and merged back `develop` → `main`; there is no `stage` branch.
  - `spec/<NNN>-<feature>` — Stage 2
  - `impl/<NNN>-<feature>` — Stage 3; the submission PR is `impl/<NNN>-<feature>` → `develop`
  - `docs/<topic>` — documentation-only changes
  - `infra/<component>` and `agent/<issue-NN>` are not used in the challenge
  - Do not collapse `impl/` — or any other prefix — into `spec/`.
  - Full table: [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md)
- Before writing EARS requirements in Stage 2, the participant MUST have read the Natural programs and DDMs for the target capability (HARD GATE — see the checklist above)

## Strict Rules — Do Not Do This

- ❌ Do not assume a pre-existing application prototype, inherited containerization, or workshop infrastructure. `backend/`, `frontend/`, and `infra/` do not exist yet — the participant creates only what the slice requires during Stage 3. The local legacy sources are read-only exercise inputs, not a lab to provision or administer.
- ❌ Do not write an EARS requirement without `source_legacy:` — CI will reject the PR
- ❌ Do not add dependencies without justification in an ADR
- ❌ Do not write tests after the fact — write them during implementation
- ❌ Do not expose secrets in commit messages, logs, or PR descriptions
- ❌ Do not merge into `main` without review; in the challenge, the judge reviews the submission PR
- ❌ Do not skip the self-checkpoints C1, C2, and C3 at stage transitions (see [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md))
- ❌ Do not run parallel sub-agent orchestration (Copilot CLI fan-out or worker harnesses) during the challenge
- ❌ Do not create a root `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. This file is the single source of truth for repo-wide agent instructions; every Copilot surface that reads `AGENTS.md` also reads this file, and this file outranks it in precedence — a second file only adds drift risk. See [`docs/adr/0001-agent-instructions-single-source-of-truth.md`](../docs/adr/0001-agent-instructions-single-source-of-truth.md).
- ❌ Do not add or edit a Copilot primitive (agent, prompt, instruction, skill, or hook) that does not follow [`PRIMITIVE-STANDARD.md`](PRIMITIVE-STANDARD.md); the `copilot-primitives` CI job enforces its structure.

## References

- Schedule, checkpoints, and finish line: [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md)
- Git workflow: [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md)
- Copilot's 3 modes (Ask · Plan · Agent): [`09-cheat-sheets/copilot-3-modes.md`](../09-cheat-sheets/copilot-3-modes.md)
- Role kits (the participant covers all 10; active artifacts are already consolidated in `.github/`): [`05-personas/`](../05-personas/)
- Stage agents: [`06-stage-agents/`](../06-stage-agents/)
- SIFAP legacy system: [`01-archaeology/legacy-sifap/`](../01-archaeology/legacy-sifap/)
- Spec-Kit SDD: <https://github.com/github/spec-kit>

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->
