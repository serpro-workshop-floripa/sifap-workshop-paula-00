# Modelo de FRD

Use este modelo após a análise de lacunas. As declarações normativas seguem a [notação EARS](./ears-notation.md). Mantenha o documento como `Draft` ou `Ready for review` até que um revisor responsável registre a aprovação.

Neste kit, use estas seções em `.spec/<NNN>-<feature>/spec.md`,
não em um arquivo FRD paralelo. Siga o [vínculo com o repositório](../SKILL.md#vínculo-com-este-kit-do-participante);
o path da fonte e todo o conteúdo dos requisitos são preenchidos pela equipe após a arqueologia.

```markdown
---
title: "FRD: <Project or Feature>"
description: "Escopo funcional neutro quanto à implementação e comportamento observável."
date: "<YYYY-MM-DD>"
version: "0.1.0"
status: "Draft"
project_context: "<greenfield|brownfield|modernization|migration|api|mobile|data|saas|internal-tool|cli|infrastructure>"
companion_nfrd: "<relative path or not-created>"
---

# FRD: <Project or Feature>

## 1. Document control

| Campo | Valor |
| --- | --- |
| Responsável | <accountable owner> |
| Revisores | <roles or names> |
| Status | Rascunho |
| Fontes regentes | <SRC-IDs> |
| Última revisão | <YYYY-MM-DD or not-reviewed> |

## 2. Problem and outcomes

### 2.1 Problema
<Observed problem and affected actors.>

### 2.2 Resultados desejados
| ID do resultado | Resultado observável | Fonte |
| --- | --- | --- |
| OUT-001 | <business or user outcome> | SRC-001 |

### 2.3 Sinais de sucesso
| Sinal | Medida | Meta ou bloqueio | Responsável pela evidência |
| --- | --- | --- | --- |
| <signal> | <how observed> | <approved target or BLOCKED> | <owner> |

## 3. Scope

### 3.1 Incluído no escopo
- <bounded capability>

### 3.2 Fora do escopo
- <explicit exclusion and rationale>

### 3.3 Premissas e bloqueios
| ID | Tipo | Declaração | Impacto se incorreta | Responsável | Estado |
| --- | --- | --- | --- | --- | --- |
| ASM-001 | premissa | <statement> | <impact> | <owner> | aberto |
| BLK-001 | bloqueio | <missing decision> | <blocked work> | <owner> | aberto |

## 4. Actors and permissions

| Ator | Objetivo | Ações permitidas | Ações proibidas | Fonte |
| --- | --- | --- | --- | --- |
| <role> | <goal> | <actions> | <boundaries> | SRC-001 |

## 5. Domain model and lifecycle

| Termo de domínio | Definição | Fonte |
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
- Justificativa: <why the behavior is needed>
- Dependências: <requirement IDs or none>

> <Canonical EARS statement with one observable response.>

**Sinais de aceitação**
- AC-REQ-NNN-NN: <observable pass/fail outcome>

**Verificação**
- <test|inspection|analysis|measurement>: <planned evidence>

**Falha e recuperação**
- <linked unwanted-behavior requirement IDs or not applicable>

<Repeat by domain. Do not organize requirements by UI screen or implementation layer.>

## 7. External interactions

| Interação | Direção | Contrato ou evento | Comportamento em caso de falha | IDs de requisitos |
| --- | --- | --- | --- | --- |
| <system> | entrada/saída | <contract> | <observable response> | REQ-NNN |

## 8. Requirement summary

| ID | Domínio | Padrão | Prioridade | Fonte | Status |
| --- | --- | --- | --- | --- | --- |
| REQ-NNN | <domain> | <pattern> | <priority> | <source> | <actual status> |

## 9. Delivery increments

| Incremento | Objetivo | IDs de requisitos | Dependências | Sinal de saída |
| --- | --- | --- | --- | --- |
| <increment> | <reviewable outcome> | REQ-NNN | <IDs or none> | <observable signal> |

## 10. Open questions

| ID | Pergunta | Bloqueia | Responsável | Prazo |
| --- | --- | --- | --- | --- |
| Q-001 | <question> | <requirement or artifact> | <owner> | <date or TBD> |

## 11. Review record

| Revisor | Decisão | Data | Evidência ou comentários |
| --- | --- | --- | --- |
| <reviewer> | pendente | <date> | <notes> |
```

## Verificações do modelo

- Todo ator é referenciado por pelo menos um requisito ou declarado explicitamente como informativo.
- Todo requisito P0 tem uma justificativa de impacto na entrega.
- O comportamento de erro e recuperação está explícito para cada ação principal.
- Os requisitos permanecem neutros quanto à implementação e atômicos.
- As linhas de resumo correspondem exatamente aos registros de requisitos normativos.
- O status de aprovação não é preenchido previamente.
