---
name: "design-modular-monolith"
description: "Escreve a etapa de projeto de um pacote SDD do architect — ANALYSIS.md, DESIGN.md, DECISIONS.md, contracts/ e o checkpoint de especificação para plano — para um Monólito Modular."
argument-hint: "feature=NNN-feature-name"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /design-modular-monolith

## Objetivo

Conclua a etapa de projeto de `.spec/<NNN>-<feature>/`: `ANALYSIS.md`, `DESIGN.md` com todas as 18 seções do portfólio, `DECISIONS.md`, `contracts/manifest.yaml` com seus contratos e `checkpoints/spec-to-plan.yaml`. O projeto permanece como a menor estrutura de Monólito Modular necessária aos requisitos.

## Quando invocar

Depois que `/write-ears-spec` concluir a etapa de requisitos e a equipe declarar as questões de projeto que bloqueiam a primeira tarefa, na branch `spec/<NNN>-<feature>`. Para um pacote Spec-Kit, use `/speckit.plan`.

> [!NOTE]
> Não o invoque para projetar todo o sistema, adicionar módulos de que nenhum requisito precisa ou antes que `SPECIFICATION.md` exista.

## Pré-condições

- `.spec/<NNN>-<feature>/SPECIFICATION.md` existe e todo requisito tem um `source_legacy:` válido
- O mapa da fonte, o dicionário de dados, a prontidão e as restrições do DBA estão disponíveis ou explicitamente bloqueados
- `02-modern-spec/scope-decisions.md` registra o escopo da funcionalidade

## Inputs que a equipe deve fornecer

- `feature=<NNN>-<feature-name>`
- As questões concretas de projeto que bloqueiam a primeira tarefa (por exemplo, qual módulo é responsável pelos dados de um DDM)
- Restrições que delimitam o projeto (dados sob responsabilidade, ponto de integração, contrato)

## O que farei

- Registrarei evidências, lacunas, opções e riscos em `ANALYSIS.md`
- Preencherei todas as seções de `DESIGN.md`; uma visão que não se aplica declara `NOT APPLICABLE: <reason>`
- Registrarei cada escolha consequente como `DR-NNN` em `DECISIONS.md` e como ADR por `/generate-adr` quando abranger todo o repositório
- Declararei cada contrato de interface em `contracts/manifest.yaml`, fornecido ou não aplicável, com razão, evidência e decisão
- Mapearei cada requisito para componentes de projeto e itens do plano em `checkpoints/spec-to-plan.yaml`
- Projetarei em conjunto a migração de dados com `@dba` a partir do [guia de migração de dados](../../docs/DATA-MIGRATION.md)
- Executarei os gates da etapa de projeto

## O que NÃO farei

- Sugerir microsserviços — o destino é um Monólito Modular
- Escrever código de implementação
- Preencher requisitos, endpoints, schemas ou decisões que a equipe não confirmou
- Iniciar uma linha com um ID de requisito fora de `SPECIFICATION.md`
- Colocar um artefato de funcionalidade em `02-modern-spec/` ou fora de `.spec/`

## Formato de saída

`DESIGN.md` segue o [modelo](../skills/sdd-requirements-engineer/references/spec-templates.md#designmd); sua visão de entrega é o rastro espelhado pelo checkpoint (os valores são ilustrativos):

| Requisitos | Componente | Item do plano | Tarefas | Testes |
|---|---|---|---|---|
| REQ-001 | C-01 `<module>` | P1.1 | — | — |

```yaml
feature: {id: "<NNN>", slug: <feature>}
checkpoint: {generated_on: "<YYYY-MM-DD>", mapping_status: complete}
requirements:
  REQ-001: {design_components: [C-01], plan_items: [P1.1]}
```

## Definição de pronto

- [ ] `ANALYSIS.md`, `DESIGN.md`, `DECISIONS.md`, `contracts/manifest.yaml` e `checkpoints/spec-to-plan.yaml` existem
- [ ] Toda seção de `DESIGN.md` tem conteúdo ou `NOT APPLICABLE: <reason>`, e todo bloco Mermaid usa o tema neutro
- [ ] Todo requisito é mapeado para um componente e um item do plano
- [ ] DBA e QA revisaram a migração de dados, a cobertura completa da população e a recuperação; decisões não resolvidas bloqueiam o C2
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --stage design` passa, ou suas falhas são relatadas

## Corpo do prompt

Você é o `@architect`. A equipe tem um `SPECIFICATION.md` respaldado por evidências; projete a menor estrutura que o atenda.

**Etapa 1 — Leia o estado atual.**

- Abra `SPECIFICATION.md`, `FRD.md`, `NFRD.md`, `.spec/CONSTITUTION.md` e `02-modern-spec/scope-decisions.md`.
- Pare diante de qualquer requisito sem um `source_legacy:` válido.

**Etapa 2 — Analise.**

- Escreva o inventário de evidências, as lacunas, as opções e os riscos em `ANALYSIS.md`. Uma pergunta sem resposta permanece aberta com um responsável.

**Etapa 3 — Projete.**

- Nomeie cada módulo na linguagem de negócio, com os dados de sua responsabilidade exclusiva e a interface em processo usada por outros módulos.
- Preencha todas as 18 seções de `DESIGN.md`; desenhe uma visão Mermaid somente quando ela responder a uma pergunta concreta.

**Etapa 4 — Decida e contrate.**

- Registre cada escolha como `DR-NNN` em `DECISIONS.md`; chame `/generate-adr` para escolhas que abrangem todo o repositório.
- Adicione contratos `/api/v1/{resource}` versionados e declare cada um em `contracts/manifest.yaml`.

**Etapa 5 — Crie o checkpoint e valide.**

- Mapeie todos os requisitos em `checkpoints/spec-to-plan.yaml`.
- Execute `python3 .github/scripts/format-sdd-mermaid.py --package <NNN>` e `python3 .github/scripts/validate-specs.py --package <NNN> --stage design`; relate o resultado literalmente.

## Exemplo de invocação

```text
/design-modular-monolith feature=001-benefit-calculation
```

Espere `.spec/001-benefit-calculation/` com `ANALYSIS.md`, `DESIGN.md`, `DECISIONS.md`, contratos e um checkpoint completo da especificação para o plano.
