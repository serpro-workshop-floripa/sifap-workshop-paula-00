# Lessons Learned — Common Challenge Mistakes

![Reference Type](https://img.shields.io/badge/Type-Reference-171717?style=flat-square)
![5 min read](https://img.shields.io/badge/Read-5%20min-737373?style=flat-square)

> **Path:** [Team Kit](../README.md) › [Docs](README.md) › **Lessons Learned**

**Ten failure patterns to watch for**, with plausible consequences and preventive actions. These are learning risks, not measured frequency or timing results.

| Field | Value |
|---|---|
| **Target audience** | Every participant, especially when covering Technical Lead responsibilities |
| **When to read** | Before the workshop starts |
| **Expected outcome** | Recognize failure patterns and know the remedy before it is needed |

---

## The ten most common mistakes

### 1. "We do not need to inspect the legacy system — the briefing is enough"

- **Consequence:** requirements can lack valid evidence; CI rejects missing/invalid citations, and reviewers may find unsupported behavior even when syntax passes.
- **Remedy:** enforce the Stage 1 hard gate — the facilitator validates it at 13:50. See [`01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md`](../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md).

### 2. "I will start coding while someone else writes the specification"

- **Consequence:** the code does not match the EARS requirements. Refactoring happens at the end of the day, and acceptance remains incomplete.
- **Remedy:** Stage 3 starts only after the C2 self-check confirms `spec.md`, `plan.md`, `tasks.md`, and migration design are ready.

### 3. The Product Owner approves everything and nothing becomes out of scope

- **Consequence:** the participant tries to implement 12 features in the timebox and completes none.
- **Remedy:** PO and architects choose a thin, evidence-backed capability with DBA/QA. Defer unrelated work explicitly; do not preselect the payment cycle or invent a rejection quota.

### 4. Everyone uses Copilot differently

- **Consequence:** responses are inconsistent. The participant debates with the assistant instead of producing artifacts.
- **Remedy:** select the stage agent for the current block (`@archaeologist`, `@architect`, `@builder`, plus `@dba` for data work) in Chat.

### 5. Skipping `/speckit.clarify` to save time

- **Consequence:** unresolved ambiguities can become implementation errors; this kit does not assign a measured time saving to clarification.
- **Remedy:** resolve questions that block the selected behavior using evidence. Leave unavailable answers blocked or defer affected scope through review.

### 6. Running `git push --force` on `develop`

- **Consequence:** two people's work is lost without a straightforward recovery path.
- **Remedy:** protect `develop` (Step 4 of `00-SETUP.md`). Never use `--force` on a shared branch.

### 7. Editing an old migration instead of creating a new one

- **Consequence:** Flyway detects a checksum mismatch and the database stops starting.
- **Remedy:** never edit an applied migration file. Always create `V<N+1>__description.sql`. See [`docs/troubleshooting.md`](troubleshooting.md).

### 8. Delegating a vague Issue to Copilot Agent

- **Consequence:** the generated pull request is unusable and the work is discarded.
- **Remedy:** link the Issue to evidence and verifiable acceptance criteria. Clear input improves reviewability but does not guarantee a correct or timely PR.

### 9. Running `terraform apply` instead of `plan`

- **Consequence:** Azure resources are created and billed immediately. The workshop does not authorize `apply`.
- **Remedy:** do not run Stage 4 infrastructure during the individual challenge. Post-challenge infrastructure work may use `terraform plan`; see [`04-evolution/GUIDE.md`](../04-evolution/GUIDE.md).

### 10. Treating schema creation or a test seed as a data migration

- **Consequence:** the application runs but cannot account for or query the original beneficiary population.
- **Remedy:** DBA leads source readiness and migration from the start; QA independently reconciles the snapshot and checks all beneficiary queries. Use [`DATA-MIGRATION.md`](DATA-MIGRATION.md), and retain blockers instead of inventing a successful outcome.

---

## Five habits that distinguish strong submissions

1. **Self-checkpoint at each stage boundary** — C1, C2, and C3 are verified before moving on.
2. **Every pull request has a description** — use the GitHub template and fill in the checklist.
3. **Small commits include a REQ-ID** in the commit message.
4. **The 20-minute rule** — blocked? Ask workshop support and record the blocker.
5. **Trust the process** — do not invent a different workflow halfway through the day.

---

## The fundamental rule

> **Modernization is digital archaeology, not a greenfield project.**
> Treating SIFAP as greenfield risks losing behavior accumulated over approximately 30 years. Preserve the [historical evidence](../README.md#scenario-chronology-and-evidence) before making modern decisions.
> Archaeology supports a defensible increment; production replacement still requires evidence beyond this timeboxed exercise.

---

### Continue reading

| Previous | Next |
|---|---|
| [Leader Checklist](CHECKLIST-LIDER.md)<br/><sub>Hour-by-hour checks for the day.</sub> | [Data Migration](DATA-MIGRATION.md)<br/><sub>DBA-led migration and acceptance.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
