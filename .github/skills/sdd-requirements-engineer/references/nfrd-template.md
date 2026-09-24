# Modelo de Non-Functional Requirements Document

Use este modelo para restrições de qualidade mensuráveis. As declarações normativas seguem a [notação EARS](./ears-notation.md). Nunca preencha uma meta com um valor padrão que apenas pareça comum no setor quando não houver evidência de carga de trabalho, política ou definição de um responsável.

Use estas seções dentro do `spec.md` da funcionalidade, seguindo o
[vínculo com o kit](../SKILL.md#vínculo-com-este-kit-do-participante). A categoria
não funcional é um metadado; os requisitos continuam usando `REQ-NNN` e `source_legacy:`.

```markdown
---
title: "<Project or Feature> Non-Functional Requirements Document"
description: "Measurable quality constraints and verification envelopes."
date: "<YYYY-MM-DD>"
version: "0.1.0"
status: "Draft"
companion_frd: "<relative path or not-created>"
---

# Non-Functional Requirements Document: <Project or Feature>

## 1. Document control

| Field | Value |
| --- | --- |
| Owner | <accountable owner> |
| Reviewers | <roles or names> |
| Status | Draft |
| Governing sources | <SRC-IDs> |
| Last reviewed | <YYYY-MM-DD or not-reviewed> |

## 2. Applicability

| Category | Applies | Rationale | Owner |
| --- | --- | --- | --- |
| Performance and capacity | yes/no/unknown | <reason> | <owner> |
| Security and identity | yes/no/unknown | <reason> | <owner> |
| Reliability and recovery | yes/no/unknown | <reason> | <owner> |
| Privacy and compliance | yes/no/unknown | <reason> | <owner> |
| Observability and supportability | yes/no/unknown | <reason> | <owner> |
| Accessibility and localization | yes/no/unknown | <reason> | <owner> |
| Testability and maintainability | yes/no/unknown | <reason> | <owner> |
| Delivery and operability | yes/no/unknown | <reason> | <owner> |
| Data quality, retention, and migration | yes/no/unknown | <reason> | <owner> |
| Cost and resource efficiency | yes/no/unknown | <reason> | <owner> |

## 3. Deployment and measurement contexts

| Context | Workload and data shape | Region or topology | Dependencies | Measurement tooling | Owner |
| --- | --- | --- | --- | --- | --- |
| <context> | <users, rate, payload, dataset> | <scope> | <services> | <tool or BLOCKED> | <owner> |

## 4. Quality requirements

### REQ-NNN: <Short title>

- Pattern: <EARS pattern>
- Priority: <P0|P1|P2|P3>
- Status: Proposed
- Source: <SRC-###>
source_legacy: <actual supported source path or justified [GREENFIELD]>
- Rationale: <why the constraint is needed>
- Applies to: <contexts>
- Owner: <accountable owner>

> <Canonical EARS statement with an approved measurable constraint, or a statement whose unresolved target is explicitly blocked.>

**Measurement envelope**

| Field | Value |
| --- | --- |
| Metric | <metric> |
| Target | <approved target or BLOCKED> |
| Aggregation | <p95, maximum, rate, count, percentage, or other> |
| Observation window | <duration or BLOCKED> |
| Workload | <load and data shape or BLOCKED> |
| Environment | <context or BLOCKED> |
| Instrumentation | <source of evidence or BLOCKED> |

**Acceptance signals**
- AC-REQ-NNN-NN: <observable pass/fail result under the measurement envelope>

**Verification**
- <test|inspection|analysis|measurement>: <planned evidence>

<Repeat for every applicable quality category.>

## 5. Security and compliance decisions

| Decision | Requirement IDs | Source or policy | Owner | State |
| --- | --- | --- | --- | --- |
| Authentication method | REQ-NNN | <source> | <owner> | <actual status> |
| Authorization model | REQ-NNN | <source> | <owner> | <actual status> |
| Data classification and protection | REQ-NNN | <source> | <owner> | <actual status> |
| Compliance applicability | REQ-NNN | <source> | <owner> | <actual status> |

## 6. Technology constraints

| Constraint | Rationale | Source | Requirement IDs | Revisit trigger |
| --- | --- | --- | --- | --- |
| <technology or platform constraint> | <why it is mandatory> | <source> | REQ-NNN | <condition> |

<If no technology is mandated, state "No approved technology constraints." Do not promote preferences into requirements.>

## 7. Requirement summary

| ID | Category | Priority | Contexts | Target state | Source | Status |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-NNN | <category> | <priority> | <contexts> | <target state> | <source> | <actual status> |

## 8. Blockers and open questions

| ID | Missing fact or decision | Affected requirement IDs | Owner | Resolution evidence |
| --- | --- | --- | --- | --- |
| <blocker ID> | <unknown target or policy> | REQ-NNN | <owner> | <expected evidence> |

## 9. Review record

| Reviewer | Decision | Date | Evidence or comments |
| --- | --- | --- | --- |
| <reviewer> | pending | <date> | <notes> |
```

## Verificações do modelo

- Toda categoria aplicável tem pelo menos um requisito ou uma justificativa explícita para não ter nenhum.
- Toda meta numérica tem fonte, responsável, carga de trabalho, ambiente e método de observação.
- Todo contexto de implantação está coberto por requisitos mensuráveis ou por um bloqueio visível.
- Segurança identifica autenticação, autorização, proteção e comportamento de falha quando aplicável.
- A conformidade é explicitamente aplicável, não aplicável ou bloqueada; nunca é presumida silenciosamente.
- Restrições tecnológicas têm evidências e um gatilho de revisão.
- O status de aprovação não é preenchido previamente.
