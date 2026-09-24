# Modelo de NFRD

Use este modelo para restrições de qualidade mensuráveis. As declarações normativas seguem a [notação EARS](./ears-notation.md). Nunca preencha uma meta com um valor padrão que apenas pareça comum no setor quando não houver evidência de carga de trabalho, política ou definição de um responsável.

Use estas seções dentro do `spec.md` da funcionalidade, seguindo o
[vínculo com o kit](../SKILL.md#vínculo-com-este-kit-do-participante). A categoria
não funcional é um metadado; os requisitos continuam usando `REQ-NNN` e `source_legacy:`.

```markdown
---
title: "NFRD: <Project or Feature>"
description: "Restrições de qualidade mensuráveis e envelopes de verificação."
date: "<YYYY-MM-DD>"
version: "0.1.0"
status: "Draft"
companion_frd: "<relative path or not-created>"
---

# NFRD: <Project or Feature>

## 1. Document control

| Campo | Valor |
| --- | --- |
| Responsável | <accountable owner> |
| Revisores | <roles or names> |
| Status | Rascunho |
| Fontes regentes | <SRC-IDs> |
| Última revisão | <YYYY-MM-DD or not-reviewed> |

## 2. Applicability

| Categoria | Aplicável | Justificativa | Responsável |
| --- | --- | --- | --- |
| Desempenho e capacidade | sim/não/desconhecido | <reason> | <owner> |
| Segurança e identidade | sim/não/desconhecido | <reason> | <owner> |
| Confiabilidade e recuperação | sim/não/desconhecido | <reason> | <owner> |
| Privacidade e conformidade | sim/não/desconhecido | <reason> | <owner> |
| Observabilidade e capacidade de suporte | sim/não/desconhecido | <reason> | <owner> |
| Acessibilidade e localização | sim/não/desconhecido | <reason> | <owner> |
| Testabilidade e manutenibilidade | sim/não/desconhecido | <reason> | <owner> |
| Entrega e operabilidade | sim/não/desconhecido | <reason> | <owner> |
| Qualidade, retenção e migração de dados | sim/não/desconhecido | <reason> | <owner> |
| Custo e eficiência de recursos | sim/não/desconhecido | <reason> | <owner> |

## 3. Deployment and measurement contexts

| Contexto | Carga de trabalho e formato dos dados | Região ou topologia | Dependências | Ferramentas de medição | Responsável |
| --- | --- | --- | --- | --- | --- |
| <context> | <users, rate, payload, dataset> | <scope> | <services> | <tool or BLOCKED> | <owner> |

## 4. Quality requirements

### REQ-NNN: <Short title>

- Pattern: <EARS pattern>
- Priority: <P0|P1|P2|P3>
- Status: Proposed
- Source: <SRC-###>
source_legacy: <actual supported source path or justified [GREENFIELD]>
- Justificativa: <why the constraint is needed>
- Aplica-se a: <contexts>
- Responsável: <accountable owner>

> <Canonical EARS statement with an approved measurable constraint, or a statement whose unresolved target is explicitly blocked.>

**Envelope de medição**

| Campo | Valor |
| --- | --- |
| Métrica | <metric> |
| Meta | <approved target or BLOCKED> |
| Agregação | <p95, maximum, rate, count, percentage, or other> |
| Janela de observação | <duration or BLOCKED> |
| Carga de trabalho | <load and data shape or BLOCKED> |
| Ambiente | <context or BLOCKED> |
| Instrumentação | <source of evidence or BLOCKED> |

**Sinais de aceitação**
- AC-REQ-NNN-NN: <observable pass/fail result under the measurement envelope>

**Verificação**
- <test|inspection|analysis|measurement>: <planned evidence>

<Repeat for every applicable quality category.>

## 5. Security and compliance decisions

| Decisão | IDs de requisitos | Fonte ou política | Responsável | Estado |
| --- | --- | --- | --- | --- |
| Método de autenticação | REQ-NNN | <source> | <owner> | <actual status> |
| Modelo de autorização | REQ-NNN | <source> | <owner> | <actual status> |
| Classificação e proteção de dados | REQ-NNN | <source> | <owner> | <actual status> |
| Aplicabilidade de conformidade | REQ-NNN | <source> | <owner> | <actual status> |

## 6. Technology constraints

| Restrição | Justificativa | Fonte | IDs de requisitos | Gatilho de revisão |
| --- | --- | --- | --- | --- |
| <technology or platform constraint> | <why it is mandatory> | <source> | REQ-NNN | <condition> |

<If no technology is mandated, state "No approved technology constraints." Do not promote preferences into requirements.>

## 7. Requirement summary

| ID | Categoria | Prioridade | Contextos | Estado-alvo | Fonte | Status |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-NNN | <category> | <priority> | <contexts> | <target state> | <source> | <actual status> |

## 8. Blockers and open questions

| ID | Fato ou decisão ausente | IDs de requisitos afetados | Responsável | Evidência de resolução |
| --- | --- | --- | --- | --- |
| <blocker ID> | <unknown target or policy> | REQ-NNN | <owner> | <expected evidence> |

## 9. Review record

| Revisor | Decisão | Data | Evidência ou comentários |
| --- | --- | --- | --- |
| <reviewer> | pendente | <date> | <notes> |
```

## Verificações do modelo

- Toda categoria aplicável tem pelo menos um requisito ou uma justificativa explícita para não ter nenhum.
- Toda meta numérica tem fonte, responsável, carga de trabalho, ambiente e método de observação.
- Todo contexto de implantação está coberto por requisitos mensuráveis ou por um bloqueio visível.
- Segurança identifica autenticação, autorização, proteção e comportamento de falha quando aplicável.
- A conformidade é explicitamente aplicável, não aplicável ou bloqueada; nunca é presumida silenciosamente.
- Restrições tecnológicas têm evidências e um gatilho de revisão.
- O status de aprovação não é preenchido previamente.
