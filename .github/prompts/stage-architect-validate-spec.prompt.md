---
name: "validate-spec"
description: "Gera novamente arquivos SDD derivados, executa todos os gates de SDD, EARS e TDD em um pacote em .spec/, para o fluxo do architect ou do Spec-Kit, e relata os resultados sem ocultar falhas."
argument-hint: "feature=NNN-feature-name"
agent: "architect"
tools: ["read", "search", "edit", "execute"]
---
# /validate-spec

## Objetivo

Relate se `.spec/<NNN>-<feature>/` está pronto para o C2 executando os gates de SDD do repositório e listando cada falha com seu responsável e correção.

## Quando invocar

Depois de qualquer alteração em um pacote, antes de abrir um PR e no C2, para qualquer um dos fluxos.

## Pré-condições

- O pacote existe em `.spec/`
- Python 3 e PyYAML estão disponíveis (`python3 -m pip install pyyaml`)

## Inputs que a equipe deve fornecer

- `feature=<NNN>-<feature-name>`
- Se warnings contam como falhas (`--strict`) nesta revisão

## O que farei

- Detectarei o fluxo por `SPECIFICATION.md` ou `spec.md`
- Para um pacote do architect, executarei `generate-sdd-support-artifacts.py --package <NNN> --include-supplements` e depois seu `--check`
- Executarei `python3 .github/scripts/validate-specs.py --package <NNN>`, além de `audit-task-evidence.py` e `validate-test-bindings.py --report`
- Agruparei os achados por gate e proporei a menor correção para cada um

## O que NÃO farei

- Enfraquecer um gate, adicionar uma exceção ou editar um arquivo gerado para obter um resultado verde
- Afirmar correção semântica de EARS, aprovação ou comportamento em runtime a partir de um gate textual
- Corrigir um achado inventando evidências

## Formato de saída

```markdown
## Validation — <NNN>-<feature> (<workflow>, <stage>)

| Gate | Result | Findings |
|---|---|---|
| spec-artifacts | pass/fail | <count and first finding> |

Blocking for C2: <list or none>
```

## Definição de pronto

- [ ] Todos os gates foram executados e seus resultados literais foram relatados
- [ ] Cada falha tem um responsável e uma correção proposta
- [ ] Nada foi alterado, exceto arquivos derivados gerados novamente

## Corpo do prompt

Você é o `@architect`. Avalie o pacote em relação aos gates e relate exatamente o que eles dizem.

**Etapa 1 — Identifique o pacote.**

- Resolva `.spec/<NNN>-<feature>/`, seu fluxo e sua etapa.

**Etapa 2 — Gere novamente os arquivos derivados.**

- Somente para pacotes do architect: execute o gerador e depois seu `--check`.

**Etapa 3 — Execute os gates.**

- Execute `validate-specs.py --package <NNN>` e os relatórios de evidências e vínculos.

**Etapa 4 — Relate.**

- Preencha a tabela de saída; marque o C2 como bloqueado enquanto restar qualquer erro.

## Exemplo de invocação

```text
/validate-spec feature=001-benefit-calculation
```

Espere uma tabela de gates para `.spec/001-benefit-calculation/` com cada falha e sua correção.
