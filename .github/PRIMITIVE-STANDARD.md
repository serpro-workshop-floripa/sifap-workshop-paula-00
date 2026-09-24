# Padrão de primitivos do Copilot

`.github/` contém os **primitivos** do Copilot deste kit: agents, prompts, instructions, skills e hooks. Este arquivo define a estrutura obrigatória para que novos primitivos sigam o conjunto existente. A referência principal é [`archaeologist.agent.md`](agents/archaeologist.agent.md).

> [!IMPORTANT]
> O guia [`../docs/DOC-STYLE-GUIDE.md`](../docs/DOC-STYLE-GUIDE.md) governa apenas `docs/` e as pastas numeradas. Os primitivos do Copilot seguem este padrão e não devem ser reestruturados como prosa comum.

## Modelo de harness

```text
Harness = Instructions + Constraints + Feedback + Memory + Evaluation + Governance
```

| Camada | Primitivo responsável |
|---|---|
| Instructions | `copilot-instructions.md`, `instructions/*.instructions.md` |
| Constraints | `hooks/*.json` e escopo `applyTo` |
| Feedback | Prompts e agents que executam checks |
| Memory | ADRs, especificações, testes e histórico Git |
| Evaluation | `workflows/spec-quality.yml` e `scripts/validate-copilot-primitives.py` |
| Governance | Este padrão, aplicado pelo job `copilot-primitives` |

Prefira atualizar um primitivo existente a criar outro quase duplicado.

O [metadado de idioma da branch](language.json) identifica a edição. Nesta cópia, toda a prosa de documentação e dos primitivos usa português brasileiro. Traduções preservam schemas de frontmatter, paths, comandos, branches, identificadores, IDs, fontes legadas e termos técnicos consagrados.

## Regras para todos os primitivos

### Markdown e estilo

- [ ] Use português brasileiro na prosa desta cópia. Preserve elementos técnicos no idioma original.
- [ ] Use exatamente um H1 (`#`) por arquivo, abaixo do frontmatter.
- [ ] Mantenha o padrão de linha em branco dos arquivos vizinhos.
- [ ] Não pule níveis de heading.
- [ ] Declare a linguagem em todo code fence.
- [ ] Use tabelas GFM para duas ou mais dimensões e `- [ ]` para verificações.
- [ ] Termine com exatamente um newline. Não use trailing whitespace, tabs ou blank lines consecutivas.
- [ ] Não use emojis. Use alertas GFM `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]` e `> [!CAUTION]`.
- [ ] Nunca desabilite markdownlint com pragma HTML inline. A configuração única é [`../.markdownlint-cli2.jsonc`](../.markdownlint-cli2.jsonc).

### Conteúdo e precisão

- [ ] Cite a fonte autoritativa de cada convenção. Branches vêm de [`../00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md), leitura legada de [`instructions/natural-adabas.instructions.md`](instructions/natural-adabas.instructions.md) e EARS da skill correspondente.
- [ ] Preserve os prefixos `spec/<NNN>-<feature>`, `impl/<NNN>-<feature>`, `infra/<component>`, `docs/<topic>` e `agent/<issue-NN>`, todos criados de `develop`. Nunca incorpore `impl/` em `spec/`.
- [ ] Nunca invente fatos do SIFAP. Um primitivo ensina a descobrir comportamento, não declara regras de negócio.
- [ ] Use apenas a toolchain aprovada. VS Code com GitHub Copilot é o único editor e assistente aprovado.
- [ ] Chame o evento de workshop, nunca de `hackathon`.
- [ ] Preserve os paths atuais. `backend/`, `frontend/` e `infra/` ainda não existem; a equipe cria apenas o necessário.

## Frontmatter por tipo de primitivo

O schema de frontmatter é fechado. Uma chave desconhecida, removida ou inválida falha o gate. Coloque strings `name` e `description` entre aspas.

### Frontmatter de agent

Arquivo: `agents/<id>.agent.md`.

| Chave | Observações |
|---|---|
| `name` | ID do agent; renomear quebra referências `agent:` |
| `description` | Única chave obrigatória pelo gate |
| `tools` | Adicione apenas ferramentas necessárias |
| `model` | Opcional |
| `handoffs` | Apenas agents sequenciais de etapa |
| `target`, `user-invocable`, `disable-model-invocation`, `metadata`, `agents` | Opcionais |
| `mcp-servers` | Apenas GitHub.com e CLI |
| `argument-hint` | Apenas VS Code |

Remova a chave aposentada `infer:`.

> [!NOTE]
> Apenas agents de **etapa** usam `handoffs`: `archaeologist -> architect -> builder`. O agent terminal `evolution` e o agent transversal `dba` não usam. Papéis de equipe são skills, não agents. Consulte [ADR-0002](../docs/adr/0002-team-roles-as-skills-not-agents.md).

### Frontmatter de prompt

Arquivo: `prompts/<name>.prompt.md`. Chaves válidas: `name`, `description`, `agent`, `model`, `tools`, `argument-hint`.

- `agent:` aponta para `ask`, `agent`, `plan` ou arquivo em `agents/`.
- Remova `mode:` e `tested_with:`.

### Frontmatter de instruction

Arquivo: `instructions/<name>.instructions.md`. Chaves válidas: `applyTo`, `name`, `description`, `excludeAgent`.

- Use globs concretos em `applyTo`.
- `applyTo: "**"` falha o gate.

### Instruções globais do repositório

`copilot-instructions.md` não usa frontmatter e carrega em todas as requests. Mantenha-o com no máximo 100 linhas.

- Inclua apenas contexto global, stack, regras transversais e proibições.
- Não repita regras específicas de linguagem ou path.
- Mantenha a stack mesmo antes de `backend/` e `frontend/` existirem.
- Evite instruções para ler outro documento, roteamento de ferramentas, regras de tom e limites de resposta.
- Nesta cópia, a prosa global e dos primitivos usa português brasileiro. Preserve paths, IDs, schemas, fontes legadas, branches e código.

### Frontmatter de skill

Arquivo: `skills/<dir>/SKILL.md`. Apenas `name` e `description` são válidos.

- `name` corresponde exatamente ao diretório.
- `description` informa quando usar a skill e tem até 1024 caracteres.
- Remova `license`, `allowed-tools`, `compatibility` e `metadata`.

### Configuração de hooks

Um hook é um JSON plano em `hooks/<name>.json`. O script fica em `hooks/<name>/` e deve ser executável.

- `version` é `1`.
- Eventos incluem `sessionStart`, `sessionEnd`, `userPromptSubmitted`, `preToolUse` e `postToolUse`.
- O `type` do handler é `command`, `http` ou `prompt`.

Um hook `preToolUse` bloqueia com:

```json
{"permissionDecision":"deny","permissionDecisionReason":"..."}
```

## Seções obrigatórias do corpo

O script `scripts/validate-copilot-primitives.py` verifica a estrutura.

| Primitivo | Seções `##` obrigatórias, na ordem |
|---|---|
| Agent | `Missão`, `Personas líderes`, `Princípios operacionais`, `O que este agente sabe`, `O que este agente NÃO sabe`, `Prompts disponíveis`, heading iniciado por `Definição de pronto`, `Antipadrões que este agente rejeita`, `Integração com Spec-Kit` |
| Prompt | `Objetivo`, `Quando invocar`, `Pré-condições`, `Entradas que a equipe deve fornecer`, `O que farei`, `O que NÃO farei`, `Formato de saída`, opcional `Regras de <arquivo>`, `Definição de pronto`, `Corpo do prompt`, `Exemplo de invocação` |
| Instruction | Seções temáticas, depois `Convenções`, `Faça / Não faça`, `Checklist antes de abrir um PR` |
| Skill | `Quando invocar`, uma seção de procedimento, `Modelo de saída`, `Gate de qualidade` |

## Esqueletos

Copie um esqueleto, preserve frontmatter e ordem, e substitua placeholders.

### Esqueleto de instruction

````markdown
---
description: "Use quando <situação>."
applyTo: "<glob>,<glob>"
---

# <Tópico> — Guia

<Introdução breve.>

## <Tópico concreto>

<Orientação e exemplos.>

## Convenções

| Regra | Motivo |
|---|---|
| <regra> | <motivo> |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| <faça> | <não faça> |

## Checklist antes de abrir um PR

- [ ] <item verificável>
````

### Esqueleto de skill

`name` deve ser igual ao diretório `skills/<dir>/`.

````markdown
---
name: "<dir>"
description: "Use quando <gatilho>."
---
# <Título da skill>

## Quando invocar

- "<pedido que deve carregar a skill>"

## <Procedimento>

<Checklist, tabela ou passos.>

## Modelo de saída

```markdown
<formato produzido>
```

## Gate de qualidade

- [ ] <verificação objetiva>
````

### Esqueleto de hook

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "bash": ".github/hooks/<name>/<script>.sh",
        "cwd": ".",
        "timeoutSec": 10
      }
    ]
  }
}
```

## Aplicação do padrão

- O job `copilot-primitives` executa [`scripts/validate-copilot-primitives.py`](scripts/validate-copilot-primitives.py).
- O job `markdown-lint` executa a configuração raiz.
- `spec-traceability` e `legacy-traceability` verificam REQ-ID e `source_legacy`.
- `MD025` e `MD040` estão desabilitados no markdownlint, mas o validator ainda exige um H1 e a revisão exige linguagem nos fences.
- Transforme erros recorrentes em guardrails de código ou CI e ADR quando mudarem uma decisão durável.

Implementações de referência: [`agents/archaeologist.agent.md`](agents/archaeologist.agent.md), [`prompts/stage-archaeologist-extract-business-rules.prompt.md`](prompts/stage-archaeologist-extract-business-rules.prompt.md), `skills/ears-validate/SKILL.md` e [`instructions/modular-monolith.instructions.md`](instructions/modular-monolith.instructions.md).

## Checklist de autoria

- [ ] O primitivo está na pasta correta e usa o suffix correto.
- [ ] O frontmatter usa apenas chaves válidas.
- [ ] Todas as seções obrigatórias aparecem na ordem.
- [ ] Há um H1, hierarquia válida, linguagem nos fences e um newline final.
- [ ] Convenções citam fontes autoritativas, sem fatos inventados nem ferramentas proibidas.
- [ ] A prosa está em português brasileiro e elementos técnicos permanecem intactos.
- [ ] Links relativos resolvem.
- [ ] `python3 .github/scripts/validate-copilot-primitives.py` e `npx markdownlint-cli2 "<file>"` passam.
