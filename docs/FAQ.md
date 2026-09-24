# FAQ — Frequently Asked Questions

> **Path:** [Team Kit](../README.md) › [Docs](README.md) › **FAQ**

**Direct answers to common questions about the SIFAP modernization workshop.**

| Field | Value |
|---|---|
| **Target audience** | Every participant |
| **How to use** | Search the question with `Ctrl+F`. If it is not here, see [troubleshooting.md](troubleshooting.md) |
| **Estimated time** | Selective reading |

---

## About the workshop

<details>
<summary><strong>I do not code. Can I participate?</strong></summary>

Yes. The Product Owner and Tech Writer personas, and part of QA, do not require coding. Read [`07-concepts/`](../07-concepts/) first to become familiar with the concepts. Every `PERSONA.md` includes an "emergency defaults" section.

</details>

<details>
<summary><strong>How long does it last?</strong></summary>

The individual challenge runs 14:00-17:40. The exact schedule is in [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md).

</details>

<details>
<summary><strong>How many people work together?</strong></summary>

One. Each participant works individually and covers all 10 role responsibilities through role skills.

</details>

<details>
<summary><strong>Can I choose only two personas?</strong></summary>

No pair assignment is used in the individual challenge. You cover all 10 role responsibilities yourself; the relevant role skills load as your requests match their descriptions.

</details>

<details>
<summary><strong>What is SIFAP?</strong></summary>

SIFAP (Payment Inspection and Administration System) models a government payment
system with approximately 30 years of history in Natural/Adabas. The supplied
history begins in 1997; 2026 is the workshop reference year. See the
[chronology](../README.md#scenario-chronology-and-evidence). You modernize a
bounded increment, not the entire system in one day.

</details>

---

## About Copilot

<details>
<summary><strong>Which Copilot model should I use?</strong></summary>

Sonnet 4.6 for most tasks. Haiku for mechanical, repetitive tasks. Opus for complex architectural decisions. See [`09-cheat-sheets/model-routing.md`](../09-cheat-sheets/model-routing.md).

</details>

<details>
<summary><strong>When should I use Ask, Plan, or Agent?</strong></summary>

- **Ask** — discuss and understand.
- **Plan** — plan a change across multiple files.
- **Agent** — delegate a complete Issue.

Reference: [`07-concepts/04-3-copilot-modes.md`](../07-concepts/04-3-copilot-modes.md).

</details>

<details>
<summary><strong>Can Agent merge by itself?</strong></summary>

No. Agent opens a pull request. Review it with the same care you would apply to a human contribution.

</details>

<details>
<summary><strong>Can I use Cursor, Codeium, or another assistant?</strong></summary>

No. The toolchain is fixed: use only GitHub Copilot. See [`.github/copilot-instructions.md`](../.github/copilot-instructions.md).

</details>

---

## About Spec-Kit and EARS

<details>
<summary><strong>Why does every EARS requirement need `source_legacy:`?</strong></summary>

To ensure you modernized the real system, not only the briefing. CI rejects pull requests without this field. See [`01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md`](../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md).

</details>

<details>
<summary><strong>What if the feature is new and has no legacy equivalent?</strong></summary>

Use `source_legacy: "[GREENFIELD] <justification>"`. Confirm that
the selected capability has no supplied legacy equivalent; a terminal type
alone does not establish which authentication the system used.

</details>

<details>
<summary><strong>Can I skip `/speckit.clarify`?</strong></summary>

No. Skipping it means ambiguities become Stage 3 bugs, when they cost much more to fix.

</details>

<details>
<summary><strong>`/speckit.analyze` reports problems. What should I do?</strong></summary>

Resolve them before implementation. Each finding prevents later rework.

</details>

---

## About Git and branches

<details>
<summary><strong>Can I commit directly to `main`?</strong></summary>

No. Always use a pull request. See rule 1 in [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md).

</details>

<details>
<summary><strong>Which branch prefix should I use?</strong></summary>

- `spec/<NNN>-<feature>` in Stage 2
- `impl/<NNN>-<feature>` in Stage 3

Both feature branches start from `develop`. `infra/` branch prefixes are not used in the individual challenge. See the complete table in [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md).

</details>

<details>
<summary><strong>How is my PR approved?</strong></summary>

Green CI plus judge validation. The submission PR is `impl/<NNN>-<feature>` → `develop` in your repository, with the checklist filled in.

</details>

<details>
<summary><strong>Can I run `git push --force`?</strong></summary>

Only on your own branch, and only with `--force-with-lease`. Never on `develop` or `main`.

</details>

---

## About Terraform and Azure

<details>
<summary><strong>Can I run `terraform apply`?</strong></summary>

> [!CAUTION]
> No. Only `terraform plan` is authorized during the workshop. Running `apply` creates real Azure resources and incurs costs.

</details>

<details>
<summary><strong>Where should I store secrets?</strong></summary>

In Azure Key Vault. Never in `variables.tf` or committed `.env` files. When creating `infra/`, model secrets through Key Vault and Managed Identity.

</details>

---

## About stages and self-checkpoints

<details>
<summary><strong>What are "self-checkpoints C1, C2, and C3"?</strong></summary>

They are self-verification points at each agent switch. You check the same artifacts formerly reviewed at stage boundaries before moving on. Details are in [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md).

</details>

<details>
<summary><strong>Can I start Stage 2 while Stage 1 is still in progress?</strong></summary>

No. Without completed Stage 1 archaeology, EARS requirements will lack `source_legacy:` and CI will reject the pull request.

</details>

<details>
<summary><strong>Who leads each stage?</strong></summary>

See [`05-personas/OVERVIEW.md`](../05-personas/OVERVIEW.md). Summary:

- Stage 1 — you work in `@archaeologist`, with `@dba` for data discovery
- Stage 2 — you work in `@architect`, with `@dba` for migration design
- Stage 3 — you work in `@builder` and `@dba`
- Final validation — the judge validates the submission

Stage 4 is not part of the individual challenge.

</details>


<details>
<summary><strong>Who wins the individual challenge?</strong></summary>

The first two participants whose submissions pass judge validation win. A submission is the PR `impl/<NNN>-<feature>` → `develop` in the participant repository, with the checklist filled in and the judge notified. The PR creation time is the timestamp; rejected submissions may be fixed and resubmitted with a new timestamp.

</details>

<details>
<summary><strong>What counts as finishing?</strong></summary>

CI must be green, every requirement must have REQ-ID, EARS and `source_legacy:`, tests must pass, source data must reconcile, reruns must avoid duplicates, and list/search/detail must cover the complete migrated beneficiary population.

</details>

<details>
<summary><strong>Can I use parallel subagents or an orchestrator?</strong></summary>

No. Use Copilot Ask, Plan and Agent modes with the stage agents. Copilot CLI fan-out, worker harnesses and parallel subagent orchestration are not allowed in the individual challenge.

</details>

<details>
<summary><strong>Is Stage 4 included?</strong></summary>

No. The individual challenge ends at Stage 3 and judge validation. Stage 4 files remain in the kit for post-challenge work only.

</details>

---

## About blockers

<details>
<summary><strong>I am blocked. What should I do?</strong></summary>

Use the 20-minute rule ([`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) §6):

| Time blocked | Action |
|---|---|
| 5 min | Try to resolve it yourself |
| 10 min | Re-read the relevant guide and evidence |
| 20 min | Ask workshop support and record the blocker |
| 30 min | Reduce capability breadth, never the migrated population or verification standard |

</details>

<details>
<summary><strong>How do I ask for help efficiently?</strong></summary>

Use three lines: (1) Objective, (2) What I tried, (3) The blocker. See the example in [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) §6.

</details>

---

### Continue reading

| Previous | Next |
|---|---|
| [Troubleshooting](troubleshooting.md)<br/><sub>Common errors and solutions.</sub> | [PT-BR Kit](../README.md)<br/><sub>Main hub.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
