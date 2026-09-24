# Stage 3 — Implementation (100 min)

> **Path:** [Team Kit](../README.md) › [Stage 3](README.md) › **GUIDE**

**This guide leads the participant through building the functional SIFAP 2.0 prototype, from the initial skeleton to features implemented with tests, migrations, and traceability to REQ-IDs.**

![Stage 3](https://img.shields.io/badge/Stage-3%20%C2%B7%20Implementation-171717?style=flat-square) ![Duration 100 min](https://img.shields.io/badge/Duration-70%20min-737373?style=flat-square) ![Time 15:30–17:10](https://img.shields.io/badge/Time-15%3A00--16%3A10-A3A3A3?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Developer responsibilities (TL + Developer) and QA responsibilities (DBA + QA) lead; the participant scaffolds CI |
| **Prerequisites** | C2 checkpoint accepted; `spec.md`, `plan.md`, and `tasks.md` ready with REQ-IDs and `source_legacy:` |
| **Estimated time** | 100 min |
| **Stage** | Stage 3 — Implementation |
| **Expected outcome** | Functional backend and frontend querying reconciled Adabas-origin data in PostgreSQL; passing tests; commits with `Implements REQ-XXX` |

> [!IMPORTANT]
> See the exact schedule in [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md). The badges show only the stage duration.

---

## Concept: Modular Monolith

A Modular Monolith is an architecture in which bounded contexts are independent Java modules within a single JVM, with explicit boundaries between them. It is the recommended starting point for modernizing SIFAP before any future microservice extraction.

**Why it matters:** the legacy SIFAP has implicit coupling between modules through shared memory (Natural/Adabas). The Modular Monolith makes this coupling explicit and controlled. Each module exposes only the interface that other modules need.

**Strangler Fig:** a migration pattern that gradually surrounds the legacy system. The Stage 3 prototype does not need to replace all of SIFAP. Modernize one bounded context at a time while keeping the legacy system active for parts that have not yet migrated.

---

## Concept: Testcontainers

Testcontainers is a Java library that starts real Docker containers during tests. Instead of simulating PostgreSQL with an in-memory database (C2), tests use the actual production database engine.

**Why it matters:** tests against C2 can pass and then fail against PostgreSQL because of differences in SQL, types, and transaction behavior. Testcontainers removes this divergence.

**Common mistake:** forgetting to start Docker Desktop before running `./mvnw test`. The error is `Could not find a valid Docker environment`.

---

## Concept: TDD (Test-Driven Development)

TDD is the practice of writing the test before the implementation. The cycle is: write a failing test (red), implement the minimum code needed to pass (green), and improve the code without breaking the test (refactor).

**Apply this to SIFAP:** choose a requirement from the participant's `spec.md` and write a
test for its approved acceptance criteria before implementing it. The test fails
until the specified logic exists; this guide supplies no completed requirement.

---

## Definition of Ready — before starting

> [!IMPORTANT]
> Confirm every item before starting this stage:

- [ ] The PO accepted the C2 checkpoint.
- [ ] The `@builder` persona is selected in Copilot Chat.
- [ ] `.spec/<NNN>-<feature>/spec.md` has REQ-IDs with valid `source_legacy:` entries.
- [ ] `.spec/<NNN>-<feature>/plan.md` contains the decisions needed for the first task.
- [ ] The participant defined the prototype's initial paths (`backend/`, `frontend/`, and, if needed, `infra/`).
- [ ] DBA and architects approved source readiness, snapshot/extraction, mappings, load order, rerun/resume, and target recovery; QA defined independent reconciliation.
- [ ] PO confirmed full authorized beneficiary coverage and the listing/search/detail acceptance criteria.
- [ ] Branch `impl/<NNN>-<feature>` was created from the updated `develop` branch.

---

## Objective

Create the first functional SIFAP 2.0 prototype from scratch and implement the features prioritized in Stage 2. The kit provides no codebase, ready-made containerization, or prototype symlink. The participant creates the structure, implements features, and writes tests. Every feature must trace to a REQ-ID.

Stage 3 is where the specification meets reality. A well-written EARS requirement from Stage 2 becomes a test that either passes or fails. Every commit includes an `Implements REQ-XXX:` reference in the message. Without it, traceability ends.

---

## First 15 minutes: creating the skeleton

### Step 1 — Create the prototype folders

```bash
mkdir -p backend frontend
```

### Step 2 — Create the minimum structure

- **Backend:** Spring Boot 3.3, Java 21, Maven Wrapper, and the base package approved in `plan.md`.
- **Frontend:** Next.js 15 App Router, strict TypeScript, and Tailwind CSS.
- **Database:** Flyway migrations in `backend/src/main/resources/db/migration/`.

Flyway creates and evolves the schema; the DBA also implements the approved
record-migration pipeline. Test fixtures may support isolated tests, but neither
fixtures nor schema-only migrations replace the source population.

> [!CAUTION]
> Do not use code or containerization from external prototypes. The workshop goal is for the participant to build the modern prototype from its reading of the legacy system.

### Step 3 — Verify that the minimum setup runs

- Backend: `cd backend && ./mvnw test` shall pass as soon as the skeleton exists.
- Frontend: `cd frontend && npm test` (or the participant-defined command) shall pass.
- Create `infra/` only when the participant starts describing IaC or local composition.

---

## Backend structure

```text
backend/src/main/java/<approved/base/package>/
└── <feature>/
    ├── domain/
    ├── application/
    └── infrastructure/
```

### Layers (inside out)

| Layer | Responsibility | Examples |
|---|---|---|
| **domain** | Pure business rules with no framework dependency | Status enums, repository interfaces, value objects |
| **application** | Use cases and orchestration | Services, request/response DTOs |
| **infrastructure** | Technical details and I/O | REST controllers, JPA entities, Spring Data repositories |

> [!IMPORTANT]
> The `domain` layer never imports classes from `infrastructure`. The flow is always Controller → Service → Repository (interface in domain, implementation in infrastructure).

---

## Step by step: add a feature

- [ ] **Reread the EARS requirement.** Open `spec.md` and reread the REQ-ID to implement.
- [ ] **Verify the legacy evidence.** Confirm `source_legacy:` and reread the corresponding `.NSN` program.
- [ ] **Review the model.** Follow the approved mapping, use cases, and REST contracts; return unresolved decisions to Architecture and DBA.
- [ ] **Write the test first.** Create the mapping/repository or behavior test before implementing the corresponding change.
- [ ] **Create the Flyway migration.** Add the reviewed schema change under `backend/src/main/resources/db/migration/`.
- [ ] **Implement the code.** Controller → Service → Repository, following the layers.
- [ ] **Run the tests.** `./mvnw test` shall pass with Docker running.
- [ ] **Commit the change.** Include `Implements REQ-XXX` in the message.

> [!CAUTION]
> Use Flyway. Never modify existing migrations. Always create new ones (`V2__`, `V3__`, and so on). Editing an old migration corrupts the schema history and breaks deployments.

---

## Flow with Copilot Plan

To implement features with traceability:

1. Select the relevant files in VS Code (Ctrl+click).
2. Open Copilot in Plan mode.
3. Describe the change in natural language and request a plan before execution:
   > "Plan the implementation of EARS `REQ-XXX`. List the files involved, risks, and required tests. Do not implement yet."
4. Review the plan against the approved architecture; Plan mode does not itself implement the change.
5. Authorize local Agent mode or implement manually, then review the diff and run the tests.

> [!TIP]
> Use Plan for design review and local Agent mode for authorized implementation.
> Stage 4 explores GitHub's separate issue-to-PR coding agent.

---

## Data migration: DBA leads, QA verifies, Developer integrates

Follow the [data migration guide](../docs/DATA-MIGRATION.md). Implement these tasks
alongside application code, not after it:

1. **Test the approved contract first.** Cover conversions, invalid inputs, preserved source identifiers, MU/PE occurrences, and failures against PostgreSQL 16.
2. **Extract the agreed Adabas snapshot.** Record source version, snapshot boundary, export format and integrity evidence. Do not write to or reset the source.
3. **Stage and load.** Preserve source lineage, validate each record, load in dependency order, and record rejects with actionable reasons. Keep raw records and credentials outside Git and public logs.
4. **Reconcile independently.** QA checks complete source-key coverage, loaded/rejected accounting, relationships, field conversions, and agreed aggregates against the same snapshot. Target child rows may outnumber source rows; explain them through mappings rather than comparing unrelated table totals.
5. **Connect real queries.** Developer implements authorized, paginated listing, search, and detail access over PostgreSQL. Verify complete beneficiary coverage across pages; no mocks or fallback seeds in the acceptance path.
6. **Exercise rerun and recovery.** Reprocessing the same snapshot must not duplicate records; interruption must have a tested resume or cleanup path. Test target recovery without changing the source.

Record sanitized results and evidence references in the
[data migration records](../docs/data-migration/). Resolve rejected beneficiaries
before claiming complete consultation; reporting a reject explains a gap but
does not make that beneficiary queryable. Do not shrink the population to pass.

---

## Tests

### Run all tests

```bash
cd backend
./mvnw test
```

**Prerequisite:** Docker must be running. The tests use Testcontainers to start a real PostgreSQL instance.

### Expected test types

| Type | Class | What it tests |
|---|---|---|
| Unit | `*ServiceTest.java` | Isolated business logic |
| Integration | `*ControllerTest.java` | Complete endpoint (HTTP → DB) |
| Repository | `*RepositoryTest.java` | Custom queries |
| Data migration | Participant-defined integration tests | Snapshot parsing, source-to-target mapping, reconciliation, rejects, rerun/resume and target recovery |
| Beneficiary consultation | API + UI acceptance tests | Authorized listing/search/detail and complete population coverage across pages |

---

## Frontend

### Run the frontend locally

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

### Frontend architecture

The frontend uses Next.js 15 with App Router and Server Components:

```text
src/app/
├── layout.tsx
├── page.tsx
└── <feature>/
    └── page.tsx
```

| Component type | When to use it |
|---|---|
| **Server Component** (default) | Server-side data fetching; no client-side JavaScript |
| **Client Component** (`"use client"`) | Interactivity: forms, modals, and local state |

---

## Traceability: requirement → code → test

Document traceability for every implemented feature:

| EARS requirement | Implementation file | Test file |
|---|---|---|
| `REQ-XXX` | `<!-- fill in -->` | `<!-- fill in -->` |

Every commit that implements specification behavior must include `Implements REQ-XXX` in the message. This closes the specification → code → test cycle and allows `/speckit.analyze` to detect drift.

---

<details>
<summary><strong>Common pitfalls — expand</strong></summary>

| If you are doing this | Do this instead |
|---|---|
| One enormous eight-hour branch | Use small commits and small PRs. One feature = one PR |
| Implementing without tests and planning to "do them later" | Write the test with the code |
| Editing an old Flyway migration | Never do this. Always create a new migration (`V5__`, `V6__`...) |
| Creating an endpoint without `@Valid` on the DTO | Always use Bean Validation in the controller |
| Mixing domain logic into the controller | The controller calls a service. Logic belongs in the service or domain |
| Importing infrastructure classes between contexts | Preserve the boundaries defined by the participant |
| Committing without `Implements REQ-XXX` | Traceability validates the work from the previous stage |

</details>

---

<details>
<summary><strong>Troubleshooting — expand</strong></summary>

| Problem | Solution |
|---|---|
| Local environment does not start | Check Java 21, Node, environment variables, and whether ports 5432/8080/3000 are free |
| Backend cannot connect to PostgreSQL | Check the configured URL and whether the participant's selected PostgreSQL instance is running |
| Frontend shows "Failed to load" | Is the backend running? Test with `curl http://localhost:8080/actuator/health` |
| Testcontainers test fails | Check Docker Desktop and the test configuration. Unit tests with Mockito do not replace the PostgreSQL migration/integration gate |
| Migration fails at startup | Never edit an existing migration. Create a new one (`V5__`, `V6__`...) |
| `mvn test-compile` import error | Verify that the package follows `domain/` → `application/` → `infrastructure/` |
| Swagger UI does not appear | Try `http://localhost:8080/swagger-ui/index.html` |

</details>

---

## Completion criteria

- [ ] The participant-prioritized flow is implemented and documented.
- [ ] The interface required for that flow is available.
- [ ] Participant-defined tests pass with `./mvnw test`.
- [ ] Local execution is documented in the prototype.
- [ ] Exposed contracts are documented with Swagger/OpenAPI.
- [ ] The prioritized Stage 1 rule is implemented and tested.
- [ ] PostgreSQL is populated from the approved Adabas snapshot, with source lineage and no unexplained record loss.
- [ ] DBA and QA reconciled keys, relationships, conversions, rejects, and agreed aggregates; no unresolved beneficiary gap is hidden.
- [ ] Authorized listing, search, and detail queries cover all beneficiaries in the agreed population, including records beyond the first page.
- [ ] Rerun/resume and target recovery were tested without changing the source; restricted extracts remain outside Git.
- [ ] Every commit includes `Implements REQ-XXX` in the message.

---

## Next step

During the C3 checkpoint (around 16:10), the participant using `@builder` and `@dba` deliver working code,
populated PostgreSQL, and QA-reviewed migration evidence to the participant (Operations).
QA responsibilities continues final data and query validation. An empty schema, test seed, or
unresolved reconciliation difference blocks data acceptance even if unit tests pass.

See [`../04-evolution/GUIDE.md`](../04-evolution/GUIDE.md) for the next stage.

---

<details>
<summary><strong>Useful prompts for Copilot Chat — expand</strong></summary>

1. "Create a REST endpoint for [feature] following the existing architecture."
2. "Write an integration test for the [endpoint] endpoint."
3. "Add Bean Validation to the [class] DTO."
4. "Create a Flyway migration to add [table/column]."
5. "Implement business rule BR-XXX: [rule description]."
6. "Create a React Server Component to list [entity]."
7. "Add error handling for [scenario]."
8. "Refactor this service to separate [responsibility] logic."

</details>

> [!TIP]
> Do not try to implement everything. Focus on quality over quantity. One well-built endpoint with tests, validation, and documentation is worth more than five broken endpoints.

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 2 — Specification](../02-modern-spec/GUIDE.md)<br/><sub>14:50–15:30 · Write EARS requirements, ADRs, and C4 diagrams.</sub> | [Stage 4 — Evolution](../04-evolution/GUIDE.md)<br/><sub>not used in the individual challenge · Copilot Agent + Terraform + CI/CD.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
