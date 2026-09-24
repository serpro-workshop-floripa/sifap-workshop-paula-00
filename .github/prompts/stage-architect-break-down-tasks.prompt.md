---
name: "break-down-tasks"
description: "Escreve a etapa completa de um pacote SDD do architect — TASKS.md com tarefas RED/GREEN, TESTING.md e os checkpoints de plano para tarefas e cobertura de testes — e então deriva os arquivos gerados."
argument-hint: "feature=NNN-feature-name"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /break-down-tasks

## Objetivo

Transforme o projeto de `.spec/<NNN>-<feature>/` em trabalho test-first ordenado por dependência: `TASKS.md`, `TESTING.md`, `checkpoints/plan-to-tasks.yaml` e `checkpoints/test-coverage.yaml`; depois, gere `TDD.md`, `SOURCE_TRACEABILITY.md`, `CHECKLIST.md`, `CROSS_ANALYSIS.md` e `VERIFICATION.md`.

## Quando invocar

Depois que `/design-modular-monolith` concluir a etapa de projeto, antes do C2. Para um pacote Spec-Kit, use `/speckit.tasks`.

## Pré-condições

- O gate da etapa de projeto passa para o pacote
- A equipe concordou com o primeiro incremento e os níveis de teste necessários
- A [instrução de testes](../instructions/tests.instructions.md) está carregada

## Inputs que a equipe deve fornecer

- `feature=<NNN>-<feature-name>`
- Os comandos de teste usados pelo projeto, ou `PENDING` com um responsável
- Qualquer restrição de ordem (carga de dados antes da consulta, por exemplo)

## O que farei

- Escreverei uma tarefa RED antes de uma tarefa GREEN para cada requisito, com subitens `Files:` e `Acceptance:`
- Adicionarei tarefas de migração de dados, consulta e reconciliação independente de QA quando o projeto exigir
- Desenharei o grafo de dependências com cada tarefa uma única vez e sem ciclos
- Declararei cada teste como `TST-NNN` no catálogo `TESTING.md`, com local, nível, comando e status
- Mapearei itens do plano para tarefas e requisitos para testes nos dois checkpoints
- Gerarei os arquivos derivados e executarei todos os gates

## O que NÃO farei

- Marcar uma tarefa ou afirmar que um teste foi executado sem evidências em `evidence/`
- Escrever código de implementação ou os próprios testes; a Etapa 3 faz isso
- Marcar uma tarefa GREEN antes de sua tarefa RED
- Editar manualmente um arquivo gerado

## Formato de saída

```markdown
- [ ] **T001 [S] [Plan:P1.1] RED** Add a failing test for the rule. Traces REQ-001.
  - Files: `backend/src/test/java/<package>/<Rule>Test.java`.
  - Acceptance: TST-001 fails for the missing behavior.
- [ ] **T002 [S] [Plan:P1.1] GREEN** Implement the minimum behavior. Traces REQ-001.
  - Files: `backend/src/main/java/<package>/<Rule>.java`.
  - Acceptance: TST-001 passes.
```

## Definição de pronto

- [ ] `TASKS.md`, `TESTING.md` e ambos os checkpoints existem com `mapping_status: complete`
- [ ] Todo requisito tem RED antes de GREEN e pelo menos um `TST-NNN`
- [ ] `python3 .github/scripts/generate-sdd-support-artifacts.py --package <NNN> --include-supplements` foi concluído com sucesso
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --strict` passa, ou suas falhas são relatadas

## Corpo do prompt

Você é o `@architect`. Divida o projeto aprovado em tarefas test-first que um builder possa executar sem adivinhar.

**Etapa 1 — Leia o projeto.**

- Abra `DESIGN.md`, `DECISIONS.md`, `checkpoints/spec-to-plan.yaml` e `SPECIFICATION.md`.

**Etapa 2 — Escreva primeiro os testes.**

- Declare linhas `TST-NNN` em `TESTING.md` para cada ID de aceitação e preencha as seções de comandos, falha e medição, contrato de evidências e critérios de saída.

**Etapa 3 — Escreva as tarefas.**

- Para cada item do plano, escreva uma tarefa RED e depois uma tarefa GREEN por requisito; marque `[P]` somente para tarefas independentes.
- Desenhe o grafo de dependências no tema neutro do Mermaid.

**Etapa 4 — Crie o checkpoint.**

- Preencha `plan-to-tasks.yaml` (com um bloco `gate`) e `test-coverage.yaml` (requisitos e testes com comandos).

**Etapa 5 — Gere e valide.**

- Execute o gerador e depois `python3 .github/scripts/validate-specs.py --package <NNN> --strict`; relate o resultado literalmente.

## Exemplo de invocação

```text
/break-down-tasks feature=001-benefit-calculation
```

Espere um pacote `.spec/001-benefit-calculation/` completo, com todos os gates passando e nenhuma tarefa marcada.
