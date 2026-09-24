# Data Migration Records

> **Path:** [Team Kit](../../README.md) > [Documentation](../README.md) > **Data migration records**

**Blank supporting records for the DBA-led [data lifecycle](../DATA-MIGRATION.md).**

| Template | When the team fills it | Generated team file | Owner / reviewer |
|---|---|---|---|
| [Source readiness](source-readiness.template.md) | Preparation and Stage 1 | `docs/data-migration/source-readiness.md` | DBA / QA and source owner |
| [Migration plan](migration-plan.template.md) | Stage 2, linked from feature `plan.md` | `docs/data-migration/migration-plan.md` | DBA + architects / QA |
| [Source-to-target mapping](source-to-target.template.md) | Stage 2, from actual source reading | `docs/data-migration/source-to-target.md` | DBA / architects + Developer |
| [Reconciliation and consultation](reconciliation.template.md) | Stages 3-4, after execution | `docs/data-migration/reconciliation.md` | DBA / independent QA + PO |

Use `/migration phase=readiness`, `phase=plan`, or `phase=implement` for the
appropriate step, and `/query-audit` for actual query paths. Do not overwrite
existing team evidence or mark a template complete merely because it exists.

Stage 1 source maps, declaration dictionaries, reading coverage, and open
questions use the [archaeology templates](../../01-archaeology/templates/).
Formal requirements, architecture plans, and tasks remain in the existing
`.spec/<NNN>-<feature>/` tree; these records do not replace Spec-Kit artifacts.

All execution results and approvals are unfilled. Keep sensitive extracts and
record-level evidence outside the repository.
