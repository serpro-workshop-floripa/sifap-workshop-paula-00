# Setup guide: individual challenge readiness

> **Track:** [Individual challenge kit](README.md) › **Setup**

Complete these checks before 14:00. The timed challenge starts directly in `@archaeologist`; setup is pre-work.

![Setup](https://img.shields.io/badge/Setup-00-171717?style=flat-square) ![Duration: 45 min](https://img.shields.io/badge/Duration-45%20min-737373?style=flat-square) ![When: before 14:00](https://img.shields.io/badge/When-Before%2014%3A00-A3A3A3?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | One participant on their own laptop |
| **Prerequisites** | GitHub account with Copilot enabled |
| **Estimated time** | 45 minutes after tools and access are available |
| **Expected result** | Verified laptop, repository, Copilot, Spec-Kit, and source-data readiness |

> [!WARNING]
> Windows users: terminal blocks with heredoc or `for` assume Git Bash or WSL. Do not use PowerShell or CMD for those blocks.

---

## 1. Check laptop prerequisites

| Tool | Minimum version | How to check | If missing |
|---|---|---|---|
| Git | 2.40+ | `git --version` | <https://git-scm.com/downloads> |
| GitHub CLI | 2.40+ | `gh --version` | <https://cli.github.com> |
| VS Code | Current supported Stable or Insiders | Help -> About; verify Ask, Plan, Agent, and custom agents | <https://code.visualstudio.com/download> |
| Docker Desktop | 4.30+ | `docker --version` and open the app | <https://www.docker.com/products/docker-desktop> |
| Java 21 JDK | 21 | `java -version` | <https://learn.microsoft.com/java/openjdk/download> |
| Node.js | 20 for the shipped CI pin | `node --version` | <https://nodejs.org/en/download> |
| pnpm | 9 for the shipped frontend CI | `pnpm --version` | <https://pnpm.io/installation> |

These versions are the exercise baseline, not a production support statement. Evaluate runtime support separately before any real deployment.

---

## 2. Create your participant repository

Use the public kit as a template for your own private repository.

1. Open the [public kit](https://github.com/workshop-gbb/datacorp-sifap-modernization-team-kit/tree/main).
2. Click **Use this template** -> **Create a new repository**.
3. Choose the workshop organization provided by facilitators.
4. Use the repository name assigned to you.
5. Set visibility to **Private**.
6. Leave **Include all branches** unchecked unless facilitators say otherwise.

Never push to the public kit. Your work happens only in your private repository.

---

## 3. Clone and create `develop`

```bash
mkdir -p ~/Code && cd ~/Code
git clone --branch main https://github.com/<WORKSHOP_ORG>/<YOUR-REPO>.git
cd <YOUR-REPO>
ls 01-archaeology/legacy-sifap .github/agents .github/prompts .github/instructions .github/skills
git checkout -b develop
git push -u origin develop
```

Protect `main` and `develop` if your repository permissions allow it. Require PRs, conversation resolution, and the real CI checks once they have run.

---

## 4. Turn on GitHub Copilot in VS Code

1. Open the repository root with `code .`.
2. Sign in to GitHub Copilot from VS Code.
3. Open Copilot Chat.
4. Verify Ask, Plan, and Agent modes are available.
5. Ask:

```text
What stack are we using in this project?
```

The answer should include Java 21, Spring Boot 3.3, Next.js 15, PostgreSQL 16, and the SIFAP modernization context. If not, confirm `.github/copilot-instructions.md` is loaded and reload VS Code.

---

## 5. Validate stage agents and role skills

```bash
ls .github/agents .github/prompts .github/instructions .github/skills
```

Open these before 14:00:

- [`06-stage-agents/README.md`](06-stage-agents/README.md)
- [`05-personas/`](05-personas/)
- [`09-cheat-sheets/copilot-3-modes.md`](09-cheat-sheets/copilot-3-modes.md)

You cover all role responsibilities yourself. Do not add a participant roster to globally loaded instructions.

---

## 6. Install official Spec-Kit

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
specify version
```

Replace `vX.Y.Z` with the facilitator-approved release. Confirm command options with `--help`; they can change between releases.

Initialize once at the repository root if `.specify/` is not already present:

```bash
specify init . --integration copilot
```

Do not rerun initialization blindly over existing artifacts.

---

## 7. Understand challenge branch strategy

```text
main                    <- stable, protected
develop                 <- integration branch
spec/NNN-feature        <- Stage 2 specification work
impl/NNN-feature        <- Stage 3 implementation and judged submission
```

Only `spec/` and `impl/` prefixes are used during the timed challenge. The final submission PR is `impl/<NNN>-<feature>` -> `develop`. See [`00-GIT-WORKFLOW.md`](00-GIT-WORKFLOW.md).

---

## 8. Source-data readiness before 14:00

The local Natural sources, DDMs, FDT, and historical documents are read-only evidence. They are not a running Adabas database or a current record export.

- [ ] Confirm the authorized source owner, version, synthetic dataset provenance, and measured population.
- [ ] Confirm participant access permits read-only queries and supported extraction.
- [ ] Establish a supported extraction route and consistent snapshot boundary.
- [ ] Agree the complete authorized beneficiary population and related data required for consultation.
- [ ] Record baseline counts, representative read queries, anomalies, and restricted evidence locations without copying personal data into Git.

If the source is empty, unavailable, or cannot be extracted consistently, record the blocker. Source reading can continue, but migration acceptance remains blocked.

---

## 9. Pre-challenge smoke test

- [ ] Repository opens in VS Code at the root.
- [ ] `git status` works on `develop`.
- [ ] `gh auth status` succeeds.
- [ ] Java, Node, pnpm, Docker, and Specify versions are visible.
- [ ] Copilot answers with the correct stack and project context.
- [ ] `/speckit.*` commands appear in Copilot if Spec-Kit is initialized.
- [ ] Opening **New issue** on GitHub shows the shipped templates.
- [ ] `.github/agents`, `.github/prompts`, `.github/instructions`, and `.github/skills` are present.
- [ ] [`00-TEAM-FLOW.md`](00-TEAM-FLOW.md) and [`00-START-HERE.md`](00-START-HERE.md) have been read.
- [ ] Source-data readiness is verified or explicitly blocked.

When these checks are complete, you are ready to open `@archaeologist` at 14:00.

---

## Troubleshooting

### Copilot does not read project instructions

- Open VS Code at the repository root.
- Restart or reload VS Code.
- Confirm `github.copilot.chat.useProjectInstructions` is enabled.

### `specify init` fails or commands do not appear

- Confirm `uv`, Python 3.11+, and Git are installed.
- Run `specify version`.
- Inspect `.specify/` before rerunning initialization.
- Reload VS Code.

### Docker is unavailable when needed

Check ports and stop only the specific process that conflicts:

```bash
lsof -i :5432 -i :8080 -i :3000
kill <PID>
```

Do not use broad process-kill commands.

### Permission denied when pushing to `main`

Branch protection is working. Push a `spec/` or `impl/` branch and open a PR.

---

### Continue reading

| Previous | Next |
|---|---|
| [Start here](00-START-HERE.md)<br/><sub>Pre-work and 14:00 launch.</sub> | [Git workflow](00-GIT-WORKFLOW.md)<br/><sub>Branch and submission rules.</sub> |

<sub>[Back to the kit index](README.md)</sub>
