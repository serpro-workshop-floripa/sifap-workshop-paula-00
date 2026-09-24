---
name: "write-ears-spec"
description: "Escreve a etapa de requisitos de um pacote SDD do architect — FRD.md, NFRD.md e SPECIFICATION.md — a partir de regras confirmadas da Etapa 1, com declarações EARS e rastreabilidade source_legacy."
argument-hint: "feature=NNN-feature-name rules=01-archaeology/business-rules-catalog.md"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /write-ears-spec

## Objetivo

Crie ou atualize a etapa de requisitos do pacote do architect em `.spec/<NNN>-<feature>/`: `FRD.md`, `NFRD.md` e `SPECIFICATION.md`, completos conforme seus modelos e contendo somente regras confirmadas da Etapa 1 como requisitos EARS. Perguntas em aberto permanecem perguntas.

## Quando invocar

No início da Etapa 2, após o C1, na branch `spec/<NNN>-<feature>`, quando o participante escolher a Opção A (fluxo do architect). Para a Opção B, use `/speckit.specify`.

> [!NOTE]
> Este prompt não explora o sistema legado (use `/catalog-mysteries`) nem projeta módulos (use `/design-modular-monolith`).

## Pré-condições

- `01-archaeology/business-rules-catalog.md` contém as regras confirmadas da funcionalidade
- A equipe leu cada fonte legada antes de elaborar o rascunho
- A [skill de SDD](../skills/sdd-requirements-engineer/SKILL.md), sua [referência EARS](../skills/sdd-requirements-engineer/references/ears-notation.md) e a [instrução de artefatos SDD](../instructions/sdd-artifacts.instructions.md) estão carregadas

## Inputs que a equipe deve fornecer

- `feature=<NNN>-<feature-name>` — o próximo número livre preenchido com zeros em `.spec/`
- `rules=01-archaeology/business-rules-catalog.md` — somente suas linhas **Confirmed** podem ser promovidas
- O subconjunto de regras confirmadas no escopo e qualquer justificativa `[GREENFIELD]` assumida pela equipe
- Prontidão dos dados revisada pelo DBA e escopo de consulta de beneficiários aprovado pelo PO

## O que farei

- Criarei o scaffold do pacote com `python3 .github/scripts/export-spec-library.py --new-package <NNN>-<feature>` quando ele não existir
- Registrarei a escolha do fluxo e os adiamentos em `02-modern-spec/scope-decisions.md`
- Verificarei cada intervalo de linhas legado citado antes de escrever um requisito
- Escreverei cada requisito uma vez em `SPECIFICATION.md`, no formato de registro do modelo, com o próximo `REQ-NNN` ou `NFR-NNN`
- Preencherei todas as seções de `FRD.md` e `NFRD.md`, citando IDs de requisitos sem repeti-los
- Copiarei sem alterações cada item não validado de `01-archaeology/mysteries-found.md` para a tabela de perguntas em aberto
- Executarei os gates da etapa de requisitos; os arquivos derivados virão quando os checkpoints existirem

## O que NÃO farei

- Criar um requisito sem `source_legacy:` válido ou `[GREENFIELD]` justificado
- Promover uma hipótese ou pergunta em aberto, respondê-la ou alterar seu status
- Escrever `spec.md`, `plan.md` ou `tasks.md` em um pacote do architect, ou qualquer arquivo fora de `.spec/`
- Deixar uma seção do modelo vazia ou um placeholder sem preencher; escreverei `NOT APPLICABLE: <reason>`
- Inventar fatos de negócio, metas ou aprovações do SIFAP

## Formato de saída

Cada registro em `.spec/<NNN>-<feature>/SPECIFICATION.md` (os valores são ilustrativos):

```markdown
- **REQ-001:** If <unwanted condition from the confirmed rule>, then the <system> shall <one observable response>.
  source_legacy: 01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSN#L<start>-L<end>
  - Priority: P0. Source: SRC-001. Status: Draft.
  - Pattern: Unwanted behavior
  - Rationale: <why the rule exists, from the evidence>
  - Acceptance: AC-REQ-001-01 Given <state>, When <trigger>, Then <observable outcome>.
  - Verification: TST-001
```

`FRD.md` e `NFRD.md` seguem os modelos [FRD](../skills/sdd-requirements-engineer/references/frd-template.md) e [NFRD](../skills/sdd-requirements-engineer/references/nfrd-template.md).

## Definição de pronto

- [ ] `FRD.md`, `NFRD.md` e `SPECIFICATION.md` existem em `.spec/<NNN>-<feature>/`
- [ ] Todo requisito tem uma declaração EARS com `shall`, um `source_legacy:` válido na CI e um `AC-<ID>-NN`
- [ ] Toda seção tem conteúdo ou `NOT APPLICABLE: <reason>`; perguntas em aberto permanecem com o status inalterado
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --only validate-sdd-documents --only validate-spec-artifacts` passa, ou suas falhas são relatadas
- [ ] DBA/QA e PO revisaram os critérios de migração e consulta

## Corpo do prompt

Você é o `@architect`. Promova regras confirmadas da Etapa 1 para a etapa de requisitos de um pacote do architect. Você transcreve evidências em requisitos; nunca as inventa. Primeiro, carregue [sdd-requirements-engineer](../skills/sdd-requirements-engineer/SKILL.md) no modo `Requirements`.

**Etapa 1 — Confirme o fluxo e o escopo.**

- Confirme que a equipe escolheu a Opção A; caso contrário, pare e indique `/speckit.specify`.
- Liste somente linhas **Confirmed** do catálogo atribuídas à funcionalidade; registre adiamentos em `02-modern-spec/scope-decisions.md`.

**Etapa 2 — Crie o scaffold do pacote.**

- Execute `python3 .github/scripts/export-spec-library.py --new-package <NNN>-<feature>` se `.spec/<NNN>-<feature>/` não existir. Ele nunca sobrescreve um arquivo.

**Etapa 3 — Valide cada fonte.**

- Abra o membro citado (`.NSP`, `.NSN`, `.NSC`, `.NSA`, `.NSL`, `.jcl` ou `.ddm`) e confirme que o intervalo de linhas contém a lógica. Uma citação não resolvida retorna à equipe como pergunta em aberto.

**Etapa 4 — Escreva os registros EARS.**

- Um registro por comportamento com o padrão EARS correspondente e exatamente um `shall`.
- Coloque `source_legacy:` na linha após a declaração, indentado e sem marcador; registre a fonte como `SRC-NNN` no registro de fontes.
- Dê a cada critério de aceitação um ID `AC-<ID>-NN` no formato Dado/Quando/Então.

**Etapa 5 — Conclua FRD.md e NFRD.md.**

- Preencha todas as seções; cite IDs de requisitos em tabelas ou no meio de frases; declare `NOT APPLICABLE: <reason>` quando uma seção não se aplicar.

**Etapa 6 — Leve adiante as perguntas em aberto.**

- Copie cada item não validado de `01-archaeology/mysteries-found.md` para a tabela de perguntas em aberto, mantendo evidência, responsável e status inalterados.

**Etapa 7 — Valide.**

- Execute `python3 .github/scripts/validate-specs.py --package <NNN> --stage requirements` e relate o resultado literalmente.

## Exemplo de invocação

```text
/write-ears-spec feature=001-benefit-calculation rules=01-archaeology/business-rules-catalog.md
```

Espere `.spec/001-benefit-calculation/` com `FRD.md`, `NFRD.md` e `SPECIFICATION.md` completos, cada requisito com fonte e aceitação, e perguntas em aberto levadas adiante sem alterações.
