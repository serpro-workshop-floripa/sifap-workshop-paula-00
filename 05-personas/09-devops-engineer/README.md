# DevOps Engineer — Copilot Kit

> **Track:** [Team Kit](../../README.md) › [Personas](../OVERVIEW.md) › **DevOps Engineer**

**Reference kit for the DevOps Engineer persona in the SIFAP modernization workshop.**

![Persona](https://img.shields.io/badge/Persona-DevOps%20Engineer-171717?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Person taking the DevOps Engineer persona in the workshop |
| **Focus** | GitHub Actions CI/CD, Terraform infrastructure as code for Azure, observability, and incident response |
| **SDLC phase** | Stages 1-3: local readiness, required CI checks, and submission evidence |
| **Expected outcome** | Green pipeline, reproducible build, valid `terraform plan`, and documented local execution |

Read first: [PERSONA.md](PERSONA.md).

---

## Concept

The DevOps Engineer owns the path from a code commit to something that runs reliably. In the SIFAP (Payment Inspection and Administration System) modernization workshop, this persona ensures that any team machine can start the local environment, GitHub Actions validates every PR, and Terraform describes the target Azure topology even when it is not applied during the workshop.

Why it matters: without a reliable pipeline, the Developer lacks fast feedback, the QA Engineer lacks a stable test environment, and integrated acceptance risks failing because of the environment rather than the code.

## Persona kit

All active artifacts live in the repository root `.github/` directory. This folder is a reference; edit the files under `.github/` when maintenance is needed.

| File | Type | Purpose |
|---|---|---|
| `PERSONA.md` | Profile | DevOps Engineer responsibilities, stages, prompts, and rubrics |
| `.github/skills/persona-devops-engineer/SKILL.md` | Skill | CI/CD, infrastructure as code, monitoring, and incidents |
| `.github/prompts/persona-devops-engineer-pipeline.prompt.md` | Prompt | `/pipeline` |
| `.github/prompts/persona-devops-engineer-iac-module.prompt.md` | Prompt | `/iac-module` |
| `.github/prompts/persona-devops-engineer-incident-rca.prompt.md` | Prompt | `/incident-rca` |
| `.github/instructions/cicd.instructions.md` | Instructions | CI/CD conventions |
| `.github/instructions/infrastructure.instructions.md` | Instructions | Infrastructure conventions |

> [!TIP]
> Verify optional integrations through the [persona setup guidance](../README.md#how-to-activate-your-persona); do not overwrite existing configuration or assume a server is available.

## Where active artifacts live

- Agents: `.github/agents/`
- Prompts: `.github/prompts/persona-*.prompt.md`
- Skills: `.github/skills/`
- Instructions: `.github/instructions/`

## Best practices

- [ ] **Treat everything as code.** Infrastructure, configuration, policies, and runbooks must be versioned.
- [ ] **Keep pipelines under 10 minutes.** Longer pipelines become bottlenecks; parallelize or remove redundant steps.
- [ ] **Store secrets exclusively in a vault.** Never use a versioned `.env`, loose CI variables, or source code.
- [ ] **Choose a deployment strategy based on rollback cost.** Blue/green and canary solve different problems.

## Apply the workflow to SIFAP

Support DBA source readiness before Stage 1, then inspect the participant's actual
pipeline and environment needs. Extend only the CI/IaC required by the approved
slice. Record the commands and results that really occurred; do not assume a
registry, deployed infrastructure, or a successful plan. Use the
[data lifecycle](../../docs/DATA-MIGRATION.md) for migration readiness and recovery,
and keep source administration details outside this kit.

## References

- [Terraform Best Practices](https://developer.hashicorp.com/terraform/language/style)
- [GitHub Actions Hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
- [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/)
- [The DevOps Handbook — Gene Kim et al.](https://itrevolution.com/product/the-devops-handbook-second-edition/)

---

### Continue reading

| Previous | Next |
|---|---|
| [Persona overview](../OVERVIEW.md)<br/><sub>Role-by-stage checklist for the 10 personas.</sub> | [PERSONA.md](PERSONA.md)<br/><sub>Complete DevOps Engineer persona profile.</sub> |

<sub>[Back to the kit index](../../README.md)</sub>
