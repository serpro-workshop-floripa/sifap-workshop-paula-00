# @builder — Etapa 3: Implementação

> **Caminho:** [Kit da equipe](../../README.md) › [Agentes de etapa](../README.md) › **@builder**

**O agente `@builder` executa a especificação da Etapa 2, transformando requisitos EARS em código Java 21 + Spring Boot + Next.js 15, com testes rastreáveis e migrações Flyway.**

| Campo | Valor |
|---|---|
| **Público-alvo** | Desenvolvedor (líder), Líder Técnico, DBA e Engenheiro de QA durante a Etapa 3 |
| **Pré-requisitos** | Checkpoint da Etapa 2 com `spec.md`, `plan.md`, `tasks.md` e um primeiro incremento priorizado |
| **Tempo estimado** | 15:30–17:10 |
| **Etapa** | Etapa 3 — Implementação |
| **Resultado esperado** | Backend e frontend compilam, os testes passam e os commits incluem `Implements REQ-...` |

![Etapa 3](https://img.shields.io/badge/Stage-3%20%C2%B7%20Implementation-171717?style=flat-square)
![Abordagem construtiva](https://img.shields.io/badge/Approach-Constructive-404040?style=flat-square)

---

## Quando usar

Use este agente quando a especificação existir e o participante precisar construir. O `@builder` não substitui o projeto. Ele executa `spec.md`, `plan.md` e `tasks.md` por meio de código, testes e rastreabilidade.

- **Liderança:** Desenvolvedor
- **Apoio importante:** Líder Técnico, DBA, Engenheiro de QA e Arquiteto de Software
- **Pré-requisito obrigatório:** `spec.md`, `plan.md` e `tasks.md` existem, e o primeiro incremento está priorizado

---

## O que o agente faz

- Traduz regras Natural/Adabas para Java 21 com rastreabilidade de REQ-ID
- Gera entidades JPA a partir dos DDMs do Adabas e explica cada mapeamento
- Cria controllers REST `/api/v1/...` com DTOs, Bean Validation e anotações OpenAPI
- Escreve testes JUnit 5 com Testcontainers para regras de negócio críticas
- Gera alterações de esquema Flyway imutáveis e versionadas e implementa, separadamente e com o DBA, cargas de dados seguras para reexecução
- Cria páginas Next.js 15 App Router que consomem endpoints REST

---

## O que o agente NÃO faz

- Não escreve código sem um REQ-ID referenciado na especificação
- Não cria uma nova arquitetura; segue as ADRs e o plano técnico da Etapa 2
- Não registra CPF, valores de benefícios ou qualquer dado sensível em logs
- Não ignora testes para avançar mais rápido; pelo menos o teste mínimo da regra crítica é obrigatório

---

## Entradas

| Entrada | Local |
|---|---|
| Especificação da funcionalidade | `.spec/<NNN>-<feature>/spec.md` |
| Plano técnico | `.spec/<NNN>-<feature>/plan.md` |
| Lista de tarefas | `.spec/<NNN>-<feature>/tasks.md` |
| ADRs de arquitetura | `02-modern-spec/` ou `docs/adr/` |
| Evidências dos dados de origem e mapeamentos aprovados | `01-archaeology/data-map.md` gerado pelo participante e registro de origem para destino do DBA vinculado em `plan.md` |

---

## Saídas esperadas

| Artefato | Local |
|---|---|
| Código do backend Java 21 | `backend/src/main/java/` |
| Migrações Flyway | `backend/src/main/resources/db/migration/` |
| Preenchimento e reconciliação do PostgreSQL a partir da origem | Pipeline do DBA mais [evidências de dados](../../docs/DATA-MIGRATION.md) independentes da equipe de QA |
| Testes JUnit 5 | `backend/src/test/java/` |
| Código do frontend Next.js | `frontend/` |
| Commits rastreáveis | Mensagem: `Implements REQ-NNN: <short description>` |

---

## Como selecionar o agente no Copilot Chat

- [ ] **Abra o Copilot Chat** no VS Code (`Ctrl+Alt+I` / `Cmd+Alt+I`).
- [ ] **Selecione `@builder`** no seletor de agentes.
- [ ] **Abra `tasks.md`** e identifique a próxima tarefa a implementar.
- [ ] **Cole o prompt inicial** abaixo e pressione Enter.

```text
I am starting Stage 3 — Implementation.
We have spec.md, plan.md, tasks.md, ADRs, and a data model.
Help implement the next traceable task with Java 21 + Spring Boot,
PostgreSQL/JPA, and Next.js, starting with tests for business rules.
```

---

## Exemplos de prompts

| Situação | Prompt útil |
|---|---|
| Entidade JPA | "Gere a entidade a partir deste DDM e explique cada mapeamento." |
| Regra Natural | "Traduza esta regra para Java com nomes claros e um teste de equivalência." |
| Controller REST | "Crie um controller `/api/v1/...` com DTOs, validação e OpenAPI." |
| Frontend | "Crie uma página Next.js App Router que consuma este endpoint sem expor segredos." |
| Testes | "Escreva um teste JUnit para REQ-NNN e adicione o comentário de rastreabilidade." |

---

## Definição de pronto

- [ ] O backend compila, e `mvn test` (ou equivalente) passa.
- [ ] O frontend compila, e `npm test` (ou equivalente) passa quando existir um frontend.
- [ ] O primeiro incremento da funcionalidade opera dentro do escopo selecionado.
- [ ] Uma interface ou um endpoint existe somente quando o escopo exige.
- [ ] As migrações Flyway são aplicadas sem erros a um banco de dados limpo.
- [ ] O PostgreSQL é preenchido a partir do snapshot aprovado do Adabas, sem diferenças de reconciliação não resolvidas.
- [ ] Todos os beneficiários autorizados podem ser consultados por listagem/pesquisa/detalhes reais, com reexecução/retomada e recuperação verificadas.
- [ ] Os testes citam REQ-IDs em comentários inline.
- [ ] Os commits que implementam comportamento mencionam `Implements REQ-...`.

---

## Erros comuns

| Sintoma | Causa | Correção |
|---|---|---|
| Código sem REQ-ID | A tarefa começou sem verificar a especificação | Volte a `tasks.md` e encontre o requisito correspondente |
| Nova decisão de arquitetura na Etapa 3 | Uma especificação incompleta chegou ao builder | Pause, resolva-a na Etapa 2 com `@architect` e depois retome |
| Teste ignorado por pressão de tempo | Pressão de entrega | Escreva pelo menos o teste mínimo da regra crítica antes do commit |
| CPF ou valor aparece nos logs | A política de dados foi ignorada | Mascare os logs; nunca registre `cpf`, `valor` ou `beneficio` diretamente |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [@architect](../02-architect/README.md)<br/><sub>Etapa 2: especificação moderna com Spec-Kit.</sub> | [@evolution](../04-evolution/README.md)<br/><sub>Etapa 4: delegue, revise e registre o resultado.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
