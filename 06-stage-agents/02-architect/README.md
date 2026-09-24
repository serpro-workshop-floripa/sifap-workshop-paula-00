# @architect — Etapa 2: Especificação

> **Caminho:** [Kit da equipe](../../README.md) › [Agentes de etapa](../README.md) › **@architect**

**O agente `@architect` transforma as evidências coletadas na Etapa 1 em uma especificação moderna e rastreável, usando o GitHub Spec-Kit para produzir `spec.md`, `plan.md` e `tasks.md`.**

| Campo | Valor |
|---|---|
| **Público-alvo** | Dupla de arquitetura (Arquiteto Corporativo + Arquiteto de Software) durante a Etapa 2 |
| **Pré-requisitos** | Checkpoint da Etapa 1 com catálogo de regras e entradas `source_legacy:` disponíveis |
| **Tempo estimado** | 14:50–15:30 |
| **Etapa** | Etapa 2 — Especificação |
| **Resultado esperado** | `spec.md`, `plan.md` e `tasks.md` em `.spec/<NNN>-<feature>/`, aprovados pelo Product Owner |

![Etapa 2](https://img.shields.io/badge/Stage-2%20%C2%B7%20Specification-171717?style=flat-square)
![Abordagem analítica](https://img.shields.io/badge/Approach-Analytical-404040?style=flat-square)

---

## Quando usar

Use este agente depois que o participante tiver descobertas sobre o legado e precisar transformá-las em uma especificação moderna. O `@architect` ajuda a definir contextos delimitados, escrever requisitos EARS, registrar ADRs e preparar a implementação.

- **Liderança:** Arquiteto de Software
- **Apoio importante:** Engenheiro de Requisitos, Arquiteto Corporativo, Product Owner e Líder Técnico
- **Projeto de dados:** o DBA colidera o planejamento da migração; a equipe de QA define verificações independentes de reconciliação e consulta completa de beneficiários
- **Pré-requisito obrigatório:** evidências da Etapa 1 com `source_legacy:` para cada regra

---

## O que o agente faz

- Transforma regras de negócio catalogadas em requisitos EARS com `source_legacy:`
- Compara alternativas de contextos delimitados e identifica prós e contras
- Gera ADRs com contexto, opções, decisão, consequências e riscos
- Executa `/speckit.specify`, `/speckit.clarify` e `/speckit.plan` orientados pela especificação
- Identifica lacunas da especificação antes da implementação

---

## O que o agente NÃO faz

- Não aceita um requisito sem evidência do legado ou uma justificativa `[GREENFIELD]`
- Não escreve código de implementação (essa é a função do `@builder`)
- Não preenche campos ou fluxos ambíguos sem resolução explícita
- Não decide o escopo sem validação do Product Owner

---

## Entradas

| Entrada | Local |
|---|---|
| Catálogo de regras da Etapa 1 | `01-archaeology/business-rules-catalog.md` |
| Mapa de dependências | No catálogo ou em um arquivo Mermaid separado |
| Questões em aberto | Seção do catálogo |
| Mapa da origem, declarações e registro de leitura | Artefatos de dados da Etapa 1 gerados pelo participante |
| Prontidão da origem | Registro de DBA/QA da preparação e da Etapa 1 |
| Checklist de exploração do legado | `01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md` |

---

## Saídas esperadas

| Artefato | Local |
|---|---|
| Especificação da funcionalidade | `.spec/<NNN>-<feature>/spec.md` |
| Plano técnico | `.spec/<NNN>-<feature>/plan.md` |
| Lista de tarefas implementáveis | `.spec/<NNN>-<feature>/tasks.md` |
| Decisões de apoio sobre o escopo | `02-modern-spec/` (somente apoio, não um segundo local de especificação) |

---

## Como selecionar o agente no Copilot Chat

- [ ] **Abra o Copilot Chat** no VS Code (`Ctrl+Alt+I` / `Cmd+Alt+I`).
- [ ] **Selecione `@architect`** no seletor de agentes.
- [ ] **Abra o catálogo de regras da Etapa 1** no editor.
- [ ] **Cole o prompt inicial** abaixo e pressione Enter.

```text
I am starting Stage 2 — Specification.
We have a discovery report, rule catalog, glossary, DDMs, and dependency map.
Help transform confirmed evidence into `spec.md`, `plan.md`, and
`tasks.md` for a thin feature. Do not fill requirements or architecture
without a source, and record open questions separately.
```

---

## Exemplos de prompts

| Situação | Prompt útil |
|---|---|
| Regra de negócio bruta | "Confirme a fonte desta regra antes de propor um requisito EARS com `source_legacy:`." |
| Limite incerto de contexto delimitado | "Compare 2 ou 3 contextos delimitados possíveis e apresente prós e contras." |
| Decisão de arquitetura | "Gere uma ADR com contexto, opções, decisão, consequências e riscos." |
| Plano técnico | "Prepare `/speckit.plan` considerando um Monólito Modular, JPA e PostgreSQL." |
| Migração de dados | Selecione `@dba` e peça: "Revise os mapeamentos entre origem e destino, snapshot, carga, recuperação e testes de consulta usando o [template de migração](../../docs/data-migration/migration-plan.template.md)." |

---

## Definição de pronto

- [ ] O conjunto completo de artefatos (`spec.md`, `research.md`, `plan.md`, `data-model.md`, `contracts/`, `quickstart.md`, `tasks.md`, `checklists/`) existe em `.spec/<NNN>-<feature>/`, e `.specify/feature.json` aponta para ele; um arquivo não aplicável informa o motivo.
- [ ] Todo requisito tem um `source_legacy:` sem marcador, com um caminho real e válido de Natural/JCL/DDM/FDT ou `[GREENFIELD]` justificado, seguindo o [gate de exploração](../../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md).
- [ ] As decisões de apoio sobre o escopo estão em `02-modern-spec/`.
- [ ] O Product Owner revisou e aprovou o escopo durante o checkpoint das 15:00.
- [ ] A [skill de SDD](../../.github/skills/sdd-requirements-engineer/SKILL.md) foi aplicada sem arquivos em maiúsculas, uma segunda árvore de especificação ou alterações em `REQ-NNN`/`source_legacy:`.
- [ ] DBA/QA revisaram a migração e a cobertura completa de beneficiários; decisões de extração ou mapeamento não resolvidas continuam sendo bloqueios de C2.

---

## Erros comuns

| Sintoma | Causa | Correção |
|---|---|---|
| Requisito sem `source_legacy:` | Regra inferida sem evidência do legado | Volte ao catálogo da Etapa 1 e encontre a referência de linha |
| A arquitetura é complexa demais para o tempo disponível | A ambição excede o escopo do workshop | Prefira decisões simples e testáveis que possam ser implementadas em uma hora |
| ADR misturada com opinião não estruturada | O registro não tem estrutura | Use o template: contexto, opções, decisão, consequências |
| A especificação não tem critério de aceitação | O requisito não é testável | Todo requisito precisa de pelo menos um cenário verificável |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [@archaeologist](../01-archaeologist/README.md)<br/><sub>Etapa 1: leia o sistema legado Natural/Adabas.</sub> | [@builder](../03-builder/README.md)<br/><sub>Etapa 3: construa a implementação rastreável.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
