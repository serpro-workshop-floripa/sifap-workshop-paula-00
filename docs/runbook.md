# Participant Runbook Template

![Runbook Type](https://img.shields.io/badge/Type-Runbook-171717?style=flat-square)
![Owner DevOps](https://img.shields.io/badge/Owner-DevOps-737373?style=flat-square)

> **Path:** [Team Kit](../README.md) › [Docs](README.md) › **Runbook**

**Template for documenting how to run, verify and diagnose the participants' own solution.**
Fill it in with the participant's commands and evidence; it does not describe or grant access to instructor environments.

| Field | Value |
|---|---|
| **Target audience** | Participant, especially when covering DevOps responsibilities |
| **Prerequisites** | Local setup completed according to [`00-SETUP.md`](../00-SETUP.md) |
| **Expected outcome** | Working local environment, readable CI, and correct escalation |

---

## Initial checks (first use)

- [ ] **Verify prerequisites** — run each line and confirm that no errors occur:

```bash
git --version
java -version
node --version
docker --version
specify version
```

> [!NOTE]
> The kit does not include a ready-made prototype. When you create `backend/`, `frontend/`, and, if needed after the challenge, `infra/`, record the actual execution commands here.

After creating the prototype, document:

| Service | URL / Command |
|---|---|
| Backend health | — |
| Swagger UI | — |
| Local frontend | — |
| How to configure local authentication, without recording passwords | — |

---

## Daily routine

- [ ] **Check repository state:**

```bash
git status
```

- [ ] **Run backend tests** (when `backend/` exists):

```bash
(cd backend && ./mvnw test)
```

- [ ] **Run frontend tests** (when `frontend/` exists):

```bash
(cd frontend && pnpm test)
```

---

## Data migration operations (DBA owns, QA verifies)

Complete this table using your [data migration records](data-migration/)
and [approved lifecycle](DATA-MIGRATION.md). These are unfilled participant
instructions, not commands for administering the source environment.

| Item | Participant-owned command or sanitized evidence reference |
|---|---|
| Authorized source version, measured population, and snapshot identifier | — |
| Supported extraction and integrity verification | — |
| Target schema version and staging/load execution | — |
| Record accounting, rejects, and independent reconciliation | — |
| Complete beneficiary listing/search/detail checks | — |
| Same-snapshot rerun/resume without duplicates | — |
| Target recovery without changing the source | — |
| Restricted evidence retention and cleanup | — |
| DBA owner, QA reviewer, and PO acceptance or blockers | — |

Do not commit source records, personal data, secrets, or access addresses.
Unresolved data differences block acceptance; test seeds and passing builds do
not substitute for the migrated population.

---

## CI — Understand the workflows

Use the actual workflow definitions as the source of truth for triggers and
commands. Application jobs are path-filtered; a green docs-only run does not
prove that a backend, frontend, or migration was tested.

| Workflow file | What it verifies | When it runs |
|---|---|---|
| [`ci.yml`](../.github/workflows/ci.yml) | Natural-format guard; conditional backend `./mvnw -B verify`, pnpm frontend checks, Terraform validation | Configured branch pushes and PRs; application jobs depend on changed paths |
| [`spec-quality.yml`](../.github/workflows/spec-quality.yml) | Markdown/primitive validation, blocking source-reference gate, non-blocking test-reference report | Configured branch pushes and path-filtered PRs |

- [ ] **When CI fails** — open the Actions tab on GitHub, select the failed run, and read the log.
- [ ] **Fix locally** — reproduce the error with the commands for the prototype you created before pushing again.

---

## Participant-created infrastructure — post-challenge Stage 4

> [!NOTE]
> Not used in the individual challenge (14:00-17:40). The challenge ends at Stage 3 and judge validation. See [ADR-0003](../docs/adr/0003-individual-challenge-format.md).

The kit does not include provisioned resources, state files or a configured subscription. If post-challenge scope includes infrastructure, follow the [Stage 4 guide](../04-evolution/GUIDE.md) and document only what you create.

- [ ] Record the modules and configuration files that actually exist.
- [ ] Record validation commands and the plan review outcome.
- [ ] Record planning permissions and limits; do not deploy or provision during this workshop.
- [ ] Describe authentication without committing secrets, tokens or state files.
- [ ] If nothing was deployed, state that limitation instead of presenting an environment as ready.

---

## Common problems

| Symptom | Likely cause | Fix | How to confirm |
|---|---|---|---|
| Local environment hangs | A required port may be in use | Identify the process owner and approved port configuration; do not stop another participant's process | The selected service starts without a port error |
| `mvn verify` fails in Testcontainers | Docker is not running | Start Docker Desktop | Tests pass on the next run |
| `pnpm test` fails on snapshots | An intentional behavior change or a regression | Compare with the approved requirement; update only reviewed expectations, never bulk-accept to force green | Tests and review confirm the intended behavior |
| Infrastructure plan is rejected | Configuration does not meet the authorized limits or policies | Read the diagnostic and review the plan before deploying | The reviewed plan passes validation |
| GitHub Actions cannot access Azure | Authentication does not match the repository, branch or environment | Check the authorized OIDC configuration and ask the access owner for help | The workflow authenticates without committed secrets |

---

## When to escalate to the facilitator

- [ ] Build has failed for more than 20 minutes without a solution.
- [ ] Azure subscription appears to be suspended.
- [ ] Any irreversible action was run by mistake, such as `terraform destroy`.

Use the three-line escalation format in [the 20-minute rule](../00-TEAM-FLOW.md#6-the-20-minute-rule).

---

### Continue reading

| Previous | Next |
|---|---|
| [FAQ](FAQ.md)<br/><sub>Frequently asked questions.</sub> | [Troubleshooting](troubleshooting.md)<br/><sub>Common errors and solutions.</sub> |

<sub>[Back to the kit index](README.md)</sub>
