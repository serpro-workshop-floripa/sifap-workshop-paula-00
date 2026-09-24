# Etapa 3 — Implementação

> **Caminho:** [Kit da equipe](../README.md) › **Etapa 3 — Implementação**

**Nesta etapa, o participante constrói do zero o protótipo do SIFAP 2.0: um backend Java 21 + Spring Boot 3.3, um frontend Next.js 15 e PostgreSQL 16, orientado pelos REQ-IDs da Etapa 2.**

![Etapa 3](https://img.shields.io/badge/Etapa-3%20%C2%B7%20Implementa%C3%A7%C3%A3o-171717?style=flat-square) ![Conduzida pelo participante](https://img.shields.io/badge/Lideran%C3%A7a-Participante-404040?style=flat-square) ![Entrega Código e testes](https://img.shields.io/badge/Entrega-C%C3%B3digo%20%2B%20testes-737373?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Responsabilidades de TL + Dev e DBA + QA; o participante prepara a estrutura de CI |
| **Pré-requisitos** | Checkpoint C2 aceito; `spec.md`, `plan.md` e `tasks.md` prontos |
| **Tempo estimado** | 100 min (15:30–17:10) |
| **Etapa** | Etapa 3 — Implementação |
| **Resultado esperado** | Aplicação funcional com PostgreSQL populado a partir do Adabas, dados reconciliados, consultas de beneficiários e testes rastreados até os REQ-IDs |

---

## Onde isto se encaixa no fluxo do dia

![Linha do tempo do dia: pré-evento, 4 etapas e validação integrada, com os três checkpoints C1, C2 e C3](../assets/timeline-stages.svg)

## Quem trabalha aqui

![Distribuição de personas por dupla: visão, arquitetura, implementação, qualidade e operações](../assets/personas-participant.svg)

## Conteúdo desta pasta

O DBA executa a migração aprovada do snapshot para o PostgreSQL; QA a reconcilia
de forma independente, e Desenvolvimento disponibiliza consultas autorizadas de
listagem, pesquisa e detalhes para todos os beneficiários da população acordada.
Somente o histórico de schema do Flyway e seeds de teste não atendem ao C3. Siga o
[guia de migração de dados](../docs/DATA-MIGRATION.md).

| Arquivo | Finalidade |
|---|---|
| [`GUIDE.md`](GUIDE.md) | Guia passo a passo da etapa |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Etapa 2 — Especificação](../02-modern-spec/README.md)<br/><sub>Resumo da especificação moderna e links para modelos de ADR.</sub> | [Etapa 3 — GUIA](GUIDE.md)<br/><sub>15:30–17:10 · Java 21 + Spring Boot + Next.js, com testes.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
