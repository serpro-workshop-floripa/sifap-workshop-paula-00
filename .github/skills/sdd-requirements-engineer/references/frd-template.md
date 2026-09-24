# Modelo de Functional Requirements Document

Use este modelo após a análise de lacunas. As declarações normativas seguem a [notação EARS](./ears-notation.md). Mantenha o documento como `Draft` ou `Ready for review` até que um revisor responsável registre a aprovação.

Neste kit, use estas seções em `.spec/<NNN>-<feature>/spec.md`,
não em um arquivo FRD paralelo. Siga o [vínculo com o repositório](../SKILL.md#vínculo-com-este-kit-do-participante);
o path da fonte e todo o conteúdo dos requisitos são preenchidos pela equipe após a arqueologia.

```markdown
---
title: "<Project or Feature> Functional Requirements Document"
description: "Implementation-neutral functional scope and observable behavior."
date: "<YYYY-MM-DD>"
version: "0.1.0"
status: "Draft"
project_context: "<greenfield|brownfield|modernization|migration|api|mobile|data|saas|internal-tool|cli|infrastructure>"
companion_nfrd: "<relative path or not-created>"
---

# Functional Requirements Document: <Project or Feature>

## 1. Document control

| Field | Value |
| --- | --- |
| Owner | <accountable owner> |
| Reviewers | <roles or names> |
| Status | Draft |
| Governing sources | <SRC-IDs> |
| Last reviewed | <YYYY-MM-DD or not-reviewed> |

## 2. Problem and outcomes

### 2.1 Problem
<Observed problem and affected actors.>

### 2.2 Desired outcomes
| Outcome ID | Observable outcome | Source |
| --- | --- | --- |
| OUT-001 | <business or user outcome> | SRC-001 |

### 2.3 Success signals
| Signal | Measure | Target or blocker | Evidence owner |
| --- | --- | --- | --- |
| <signal> | <how observed> | <approved target or BLOCKED> | <owner> |

## 3. Scope

### 3.1 In scope
- <bounded capability>

### 3.2 Out of scope
- <explicit exclusion and rationale>

### 3.3 Assumptions and blockers
| ID | Type | Statement | Impact if wrong | Owner | State |
| --- | --- | --- | --- | --- | --- |
| ASM-001 | assumption | <statement> | <impact> | <owner> | open |
| BLK-001 | blocker | <missing decision> | <blocked work> | <owner> | open |

## 4. Actors and permissions

| Actor | Goal | Allowed actions | Prohibited actions | Source |
| --- | --- | --- | --- | --- |
| <role> | <goal> | <actions> | <boundaries> | SRC-001 |

## 5. Domain model and lifecycle

| Domain term | Definition | Source |
| --- | --- | --- |
| <term> | <unambiguous definition> | SRC-001 |

<Add a Mermaid state diagram when an entity has a lifecycle. Otherwise state "No lifecycle-dependent entity identified.">

## 6. Functional requirements

### REQ-NNN: <Short title>

- Pattern: <EARS pattern>
- Priority: <P0|P1|P2|P3>
- Status: Proposed
- Source: <SRC-###>
source_legacy: <actual supported source path or justified [GREENFIELD]>
- Rationale: <why the behavior is needed>
- Dependencies: <requirement IDs or none>

> <Canonical EARS statement with one observable response.>

**Acceptance signals**
- AC-REQ-NNN-NN: <observable pass/fail outcome>

**Verification**
- <test|inspection|analysis|measurement>: <planned evidence>

**Failure and recovery**
- <linked unwanted-behavior requirement IDs or not applicable>

<Repeat by domain. Do not organize requirements by UI screen or implementation layer.>

## 7. External interactions

| Interaction | Direction | Contract or event | Failure behavior | Requirement IDs |
| --- | --- | --- | --- | --- |
| <system> | inbound/outbound | <contract> | <observable response> | REQ-NNN |

## 8. Requirement summary

| ID | Domain | Pattern | Priority | Source | Status |
| --- | --- | --- | --- | --- | --- |
| REQ-NNN | <domain> | <pattern> | <priority> | <source> | <actual status> |

## 9. Delivery increments

| Increment | Objective | Requirement IDs | Dependencies | Exit signal |
| --- | --- | --- | --- | --- |
| <increment> | <reviewable outcome> | REQ-NNN | <IDs or none> | <observable signal> |

## 10. Open questions

| ID | Question | Blocks | Owner | Due |
| --- | --- | --- | --- | --- |
| Q-001 | <question> | <requirement or artifact> | <owner> | <date or TBD> |

## 11. Review record

| Reviewer | Decision | Date | Evidence or comments |
| --- | --- | --- | --- |
| <reviewer> | pending | <date> | <notes> |
```

## Verificações do modelo

- Todo ator é referenciado por pelo menos um requisito ou declarado explicitamente como informativo.
- Todo requisito P0 tem uma justificativa de impacto na entrega.
- O comportamento de erro e recuperação está explícito para cada ação principal.
- Os requisitos permanecem neutros quanto à implementação e atômicos.
- As linhas de resumo correspondem exatamente aos registros de requisitos normativos.
- O status de aprovação não é preenchido previamente.
