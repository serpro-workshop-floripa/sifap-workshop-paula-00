# Consolidated Troubleshooting

> **Track:** [Team Kit](../README.md) › [Docs](README.md) › **Troubleshooting**

**A diagnostic and resolution guide for the workshop's most common errors** — use `Ctrl+F` to search for the symptom.

| Field | Value |
|---|---|
| **Audience** | Every participant |
| **How to use** | Use `Ctrl+F` to search for the symptom. If you cannot find it, see [FAQ.md](FAQ.md) |
| **Expected outcome** | The issue is resolved by following the described steps |

---

## Table of contents

- [Setup and environment](#setup-and-environment)
- [Copilot, agents, and personas](#copilot-agents-and-personas)
- [Spec-Kit and EARS](#spec-kit-and-ears)
- [Backend — Java and Spring Boot](#backend--java-and-spring-boot)
- [Frontend — Next.js and Node](#frontend--nextjs-and-node)
- [Docker](#docker)
- [Git and GitHub](#git-and-github)
- [Terraform and Azure](#terraform-and-azure)
- [Plan B — Copilot outage](#plan-b--copilot-outage)

---

## Setup and environment

### Missing local tools (Java, Node, Maven)

| Field | Details |
|---|---|
| **Symptom** | A "command not found" error message for `java`, `node`, or `mvn` |
| **Likely cause** | The local tools have not been installed yet |
| **Fix** | Install the versions specified in [`00-SETUP.md`](../00-SETUP.md), then validate them with `java -version`, `node --version`, and `git --version` |
| **How to confirm** | All three commands return the expected version without errors |

### "git: command not found" in the VS Code terminal (Mac)

| Field | Details |
|---|---|
| **Symptom** | An error occurs when you try to run any `git` command |
| **Likely cause** | The Xcode CLI tools are not installed |
| **Fix** | Run `xcode-select --install` and follow the installer |
| **How to confirm** | `git --version` returns a version without errors |

---

## Copilot, agents, and personas

### Slash command does not appear in Chat

| Field | Details |
|---|---|
| **Symptom** | `/write-ears-spec`, `/map-source-data`, or another shipped prompt does not appear |
| **Likely cause** | VS Code has not reloaded the consolidated `.github/` directory, or the window was opened outside the repository root |
| **Fix** | Confirm that `.github/prompts/` contains files, then reload the window: `Cmd+Shift+P` → _Developer: Reload Window_ |
| **How to confirm** | Commands appear when you type `/` in Chat |

> [!CAUTION]
> Keep one active copy under `.github/`. Intentional primitive maintenance is
> allowed through review and the primitive validator; copying a second tree
> or assuming that guide folders install agents creates drift.

### "I can't select `@archaeologist` in Chat"

| Field | Details |
|---|---|
| **Symptom** | The `@archaeologist` agent does not appear in the Chat selector |
| **Cause 1** | `.github/agents/archaeologist.agent.md` is missing or the workspace root is wrong |
| **Cause 2** | The GitHub Copilot Chat extension is out of date |
| **Fix** | Verify the active agent file under `.github/agents/`, its frontmatter, and the workspace root; then reload or update Copilot |
| **How to confirm** | The agent appears in the Chat dropdown |

### Copilot responds without the relevant context

| Field | Details |
|---|---|
| **Symptom** | Generic responses unrelated to SIFAP (Payment Inspection and Administration System) or the current stage |
| **Likely cause** | No stage agent is selected, or the wrong agent is selected |
| **Fix** | Confirm the current stage and select the corresponding agent from the Chat dropdown |
| **How to confirm** | Responses begin referencing the stage and legacy-system context |

### "I want to use Plan mode, but only Ask is available"

| Field | Details |
|---|---|
| **Symptom** | Plan mode is not available |
| **Likely cause** | The Copilot extension is outdated |
| **Fix** | Update the GitHub Copilot Chat extension in VS Code |
| **How to confirm** | Plan mode appears in the mode selector |

---

## Spec-Kit and EARS

### "`specify version` returns command not found"

| Field | Details |
|---|---|
| **Symptom** | An error occurs when you run any `specify` command |
| **Likely cause** | Spec-Kit is not installed |
| **Fix** | Run the commands below |
| **How to confirm** | `specify version` returns a version number |

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify version
```

### CI rejected the PR: `missing source_legacy`

| Field | Details |
|---|---|
| **Symptom** | CI blocks the pull request with a traceability error |
| **Likely cause** | One or more EARS requirements do not include a `source_legacy:` line |
| **Fix** | Add an unbulleted `source_legacy:` line within 20 lines after the requirement, with an actual supported source path and optional `#L<start>-L<end>`, or `[GREENFIELD] <justification>` |
| **How to confirm** | CI passes on the next run |

See [`07-concepts/05-ears-notation.md`](../07-concepts/05-ears-notation.md) for the correct format.

### `/speckit.clarify` is asking too many questions

| Field | Details |
|---|---|
| **Symptom** | The command asks 10 or more questions |
| **Cause** | The scope or evidence may be too broad or incomplete; command behavior depends on the installed Spec-Kit version |
| **Action** | Resolve scope-blocking questions from evidence. Do not invent answers; narrow capability scope through review or keep affected work blocked |

---

## Backend — Java and Spring Boot

### Backend does not start — Postgres connection error

| Field | Details |
|---|---|
| **Symptom** | A `Connection refused` or similar error occurs when the backend starts |
| **Likely cause** | Postgres is not running, or the URL in `application.yml` is incorrect |
| **Fix** | Check `application.yml` and start Postgres using the method defined for your solution (local, Testcontainers, or Docker Compose) |
| **How to confirm** | The backend starts and responds at `/actuator/health` |

### Flyway: `Migration checksum mismatch`

| Field | Details |
|---|---|
| **Symptom** | A Flyway error occurs when the backend starts |
| **Likely cause** | An existing migration file was edited after it was applied |
| **Fix** | Compare the applied migration with version history, restore only the verified original through review, and add `V<N+1>__description.sql` |
| **How to confirm** | The backend starts without Flyway errors |

> [!CAUTION]
> Never edit migration files that have already been applied (V1, V2, V3...). Always create a new file with the next version number.

### Testcontainers: `Could not find a valid Docker environment`

| Field | Details |
|---|---|
| **Symptom** | Tests that use Testcontainers fail with a Docker environment error |
| **Likely cause** | Docker is not running, or the socket uses a nonstandard path |
| **Fix (macOS)** | Start the configured container runtime and inspect its actual context/socket. Do not force a guessed socket path or replace integration checks with mocks |
| **How to confirm** | The tests pass on the next run |

---

## Frontend — Next.js and Node

### Frontend displays `ECONNREFUSED localhost:8080`

| Field | Details |
|---|---|
| **Symptom** | The frontend page displays a connection refused error |
| **Likely cause** | The backend is not running or is using a different port |
| **Fix** | Confirm that the backend is running and that the frontend URL points to the correct port |
| **How to confirm** | The page loads data normally |

### `Module not found: shadcn/ui`

| Field | Details |
|---|---|
| **Symptom** | A module-not-found error occurs when the frontend starts |
| **Likely cause** | A generated shadcn component or its import alias is missing, or locked dependencies are not installed |
| **Fix** | Inspect the actual component import and alias. Restore the reviewed component or install existing locked dependencies with pnpm; do not assume `shadcn/ui` is a runtime package |
| **How to confirm** | The frontend starts without module errors |

---

## Docker

### `Cannot connect to the Docker daemon`

| Field | Details |
|---|---|
| **Symptom** | Every Docker command fails with a daemon error |
| **Likely cause** | Docker Desktop is stopped |
| **Fix** | Open Docker Desktop and wait for the service to start completely |
| **How to confirm** | `docker ps` returns the container list without errors |

### `port is already allocated`

| Field | Details |
|---|---|
| **Symptom** | The container does not start because of a port conflict |
| **Likely cause** | Port 5432, 8080, or 3000 is already in use by another process |
| **Fix** | Run `lsof -i :8080` to identify and stop the process, or change the port in the local configuration |
| **How to confirm** | The container starts without a port error |

### Docker Desktop reports `Out of memory`

| Field | Details |
|---|---|
| **Symptom** | Containers fail or become slow, and a memory warning appears |
| **Likely cause** | The RAM limit allocated to Docker Desktop is too low |
| **Fix** | Docker Desktop → Settings → Resources → Memory → 8 GB or more |
| **How to confirm** | Containers start and respond normally |

---

## Git and GitHub

### Push rejected: `protected branch`

| Field | Details |
|---|---|
| **Symptom** | `git push` is rejected with a protected-branch message |
| **Likely cause** | A direct push to `main` or `develop` was attempted |
| **Fix** | Create a branch and open a pull request. See [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md) |
| **How to confirm** | The pull request is created successfully |

### Merge conflict

| Field | Details |
|---|---|
| **Symptom** | `<<<<<<<` markers appear in files during a merge or rebase |
| **Likely cause** | Someone changed the same file in `develop` before you |
| **Fix** | Run the block below, resolve the conflicts manually, and complete the rebase |
| **How to confirm** | `git status` no longer shows files with conflicts |

```bash
git fetch origin
git rebase origin/develop
# Resolve conflicts in files containing markers
git add <file>
git rebase --continue
```

### Commit accidentally made directly on `develop`

```bash
git reset --soft HEAD~1
git stash
git checkout -b nova-branch
git stash pop
git commit -m "..."
```

### `gh: command not found`

| Field | Details |
|---|---|
| **Symptom** | An error occurs when you use any `gh` command |
| **Likely cause** | GitHub CLI is not installed |
| **Fix** | `brew install gh && gh auth login` |
| **How to confirm** | `gh --version` returns a version without errors |

---

## Terraform and Azure

### `Error: building AzureRM Client`

| Field | Details |
|---|---|
| **Symptom** | Terraform fails while initializing the Azure provider |
| **Likely cause** | The Azure CLI session has expired or has not been started |
| **Fix** | Run `az login` |
| **How to confirm** | `terraform plan` runs without authentication errors |

### `terraform plan` shows hundreds of new resources

| Field | Details |
|---|---|
| **Symptom** | The `plan` output lists many resources to create |
| **Cause** | The state file is empty — this is the expected behavior on the first run |
| **Action** | Review the plan. Do not run `apply`. |

> [!CAUTION]
> The workshop authorizes only `terraform plan`. Running `terraform apply` creates real Azure resources and immediately incurs costs.

---

## Plan B — Copilot outage

If Copilot Chat stops responding for more than 5 minutes:

> [!WARNING]
> Do not wait passively. The individual challenge lasts 14:00-17:40, and every idle minute has a high cost.

- [ ] **Reload** — try `Cmd+Shift+P` → _Reload Window_. If Copilot returns, continue as usual.
- [ ] **Work manually** — if it remains offline, return to the templates and artifacts you have already produced.
- [ ] **Structure the next artifact** — use the available evidence without inventing data.
- [ ] **Document it in the PR** — write: _"Completed manually in X min (Copilot offline)"_ — this supports judge validation and blocker review.
- [ ] **Record the limitation** — state that the artifact may be less refined than usual because Copilot was offline.

CI continues to validate changes even while Copilot is offline. Work does not stop.

| Artifact without Copilot | Next step |
|---|---|
| EARS in Stage 2 | Use the traceable findings and the [Spec-Kit](../09-cheat-sheets/spec-kit-workflow.md) workflow |
| ADR in Stage 2 | Complete the [ADR template](adr/0000-template.md) |
| Implementation in Stage 3 | Review the prioritized EARS requirements, the DDMs, and your decisions |
| Post-challenge Stage 4 issue | Write the context, acceptance criteria, and change traceability |

---

## When none of the solutions above work

| Time blocked | Action |
|---|---|
| 5 min | Read the error again carefully. Use Copilot Ask: _"What does this error mean: `<paste the error>`"_ |
| 10 min | Re-read the relevant stage guide and evidence |
| 20 min | Raise your hand for the facilitator (TEAM-FLOW §6 rule) |
| 30 min | Pause this task and work on another one while someone helps |

---

### Continue reading

| Previous | Next |
|---|---|
| [PT-BR Kit](../README.md)<br/><sub>Main hub.</sub> | [FAQ](FAQ.md)<br/><sub>Frequently asked questions.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
