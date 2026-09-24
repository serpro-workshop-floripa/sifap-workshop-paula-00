# Etapa 2 — Especificação

> **Caminho:** [Kit da equipe](../README.md) › **Etapa 2 — Especificação**

**Nesta etapa, o participante usa `@architect` para transformar descobertas do legado em requisitos rastreáveis, um plano técnico e tarefas implementáveis usando o GitHub Spec-Kit.**

![Etapa 2](https://img.shields.io/badge/Etapa-2%20%C2%B7%20Especifica%C3%A7%C3%A3o-171717?style=flat-square) ![Conduzida por architect](https://img.shields.io/badge/Lideran%C3%A7a-%40architect-404040?style=flat-square) ![Entrega Spec-Kit](https://img.shields.io/badge/Entrega-Spec--Kit-737373?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante usando `@architect`, com `@dba` para o projeto de migração |
| **Pré-requisitos** | Etapa 1 concluída; checkpoint C1 aceito pelo PO |
| **Tempo estimado** | 40 min (14:50–15:30) |
| **Etapa** | Etapa 2 — Especificação |
| **Resultado esperado** | `spec.md`, `plan.md` e `tasks.md` rastreáveis, incluindo migração de dados sob responsabilidade do DBA e aceitação da consulta |

> [!IMPORTANT]
> Requisitos, planos e tarefas formais ficam em `.spec/<NNN>-<feature>/spec.md`, `plan.md` e `tasks.md`.
> Esta pasta contém apenas material de apoio, modelos e decisões de escopo da Etapa 2 e não substitui os artefatos do Spec-Kit.

---

## Onde isto se encaixa no fluxo do dia

Consulte o cronograma do desafio em [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md). A Etapa 2 ocorre das 14:50 às 15:30 e termina no checkpoint C2.

## Responsabilidades abrangidas aqui

O participante assume pessoalmente as responsabilidades de arquitetura, requisitos, produto, QA e documentação; `@dba` apoia o projeto de migração.

## Conteúdo desta pasta

O DBA projeta em conjunto com Arquitetura os mapeamentos da origem para o destino,
o snapshot e o plano de carga e recuperação. Visão aprova a cobertura de beneficiários,
e QA define as verificações de reconciliação e consulta antes da implementação. Use o
[guia de migração de dados](../docs/DATA-MIGRATION.md) como checklist do C2.

| Arquivo | Finalidade |
|---|---|
| [`GUIDE.md`](GUIDE.md) | Guia cronometrado e regra de localização dos artefatos |
| [`scope-decisions.md`](scope-decisions.md) | Registro da seleção de escopo, adiamentos e perguntas em aberto |
| [`ADR-TEMPLATE.md`](ADR-TEMPLATE.md) | Apoio para uma decisão arquitetural que bloqueia o plano |
| [`templates/ADR.template.md`](templates/ADR.template.md) | Modelo de ADR para uso por meio de `/generate-adr` |
| [`templates/bounded-contexts.template.md`](templates/bounded-contexts.template.md) | Modelo de mapa de bounded contexts |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Etapa 1 — Arqueologia](../01-archaeology/README.md)<br/><sub>Resumo da arqueologia e links para o GUIA detalhado.</sub> | [Etapa 2 — GUIA](GUIDE.md)<br/><sub>14:50–15:30 · Crie spec.md, plan.md e tasks.md para o recorte de consulta de beneficiários.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
