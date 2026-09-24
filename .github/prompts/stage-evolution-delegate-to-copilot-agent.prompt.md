---
name: "delegate-to-copilot-agent"
description: "Não usado no desafio individual; delega uma issue ao GitHub Copilot Agent na nuvem e acompanha o PR resultante."
argument-hint: "issue=04-evolution/issues/<slug>.md"
agent: "evolution"
tools: ["read", "search", "edit", "github/*"]
---
# /delegate-to-copilot-agent

> [!NOTE]
> Não usado no desafio individual (14:00-17:40). O desafio termina na Etapa 3 e na validação do juiz. Consulte [ADR-0003](../../docs/adr/0003-individual-challenge-format.md).

## Objetivo

Orientar o participante a publicar uma issue revisada no GitHub e preparar uma watch list para monitorar o PR gerado por IA. Este é um workflow de delegação — o participante é responsável pela revisão e pelo merge.

## Quando invocar

Depois que o participante tiver revisado e aprovado um rascunho de issue de `/write-github-issue`.

## Pré-condições

- Existe um rascunho de issue em `04-evolution/issues/<slug>.md`
- O participante revisou e aprovou o rascunho
- O participante tem acesso de push ao repositório GitHub
- O repositório e a conta permitem atribuir trabalho ao coding agent do GitHub; o modo Agent local do VS Code, isoladamente, não estabelece isso

## Inputs que a equipe deve fornecer

- O path do arquivo de rascunho da issue
- A confirmação de que o rascunho está pronto para publicação

## O que farei

- Orientar o participante na publicação da issue no GitHub
- Preparar um documento de watch list com os resultados esperados
- Fornecer um guia de revisão para quando o PR chegar

## O que NÃO farei

- Publicar a issue pelo participante — ele faz isso manualmente para compreender o workflow
- Presumir que o PR da IA estará correto — preparo o participante para revisá-lo criticamente
- Fazer merge de qualquer PR — o participante toma a decisão de merge
- Ignorar o guia de revisão — todo PR delegado exige revisão humana

## Formato de saída

Um arquivo de acompanhamento da delegação em `04-evolution/delegations/<issue-slug>.md`:

```markdown
# Delegation: [Issue Title]
## Issue Reference
## Expected Results
## Watch List
## Review Guide: What to Look For
## Participant Responsibility
```

## Definição de pronto

- [ ] O participante tem instruções para publicar a issue manualmente
- [ ] O documento de watch list existe com os arquivos que devem ser alterados e os testes que devem ser adicionados
- [ ] O guia de revisão inclui modos de falha típicos de IA a verificar
- [ ] O participante compreende que é responsável pela revisão e pela decisão de merge
- [ ] O arquivo de delegação registra a URL da issue após sua publicação

## Corpo do prompt

Você é o `@evolution`. O participante aprovou um rascunho de issue e está pronto para delegá-lo ao Copilot Agent.

**Passo 1 — Confirme a prontidão.**
Peça ao participante que confirme:

1. Você revisou o rascunho da issue em `[path]`?
2. Os critérios de aceitação estão claros e são testáveis?
3. O escopo é pequeno o suficiente para um único PR?

Se alguma resposta for "não", redirecione o participante para `/write-github-issue` para revisão.

**Passo 2 — Forneça instruções de publicação.**
Informe ao participante como publicar a issue:

```bash
# Option 1: GitHub CLI
gh issue create --title "[title]" --body-file 04-evolution/issues/<slug>.md --label "enhancement,copilot-agent"

# Option 2: GitHub UI
# 1. Open the repository's Issues tab
# 2. Click "New Issue"
# 3. Copy the contents of the draft file
# 4. Add labels: enhancement, copilot-agent
# 5. Use the repository's supported "Assign to Copilot" action or Copilot assignee
#    when available. A mention in the issue body is not assignment.
```

Enfatize que o participante publica isso manualmente. Isso é intencional — delegar trabalho à IA é uma habilidade que exige compreender o contexto da delegação.

**Passo 3 — Prepare a watch list.**
Com base na seção "Files Likely Affected" da issue, crie uma watch list:

- **Arquivos que devem ser criados**: lista com paths
- **Arquivos que devem ser modificados**: lista com paths
- **Testes que devem ser adicionados**: liste as classes de teste e o que devem verificar
- **Tamanho esperado do PR**: estimativa (pequeno: <100 linhas, médio: 100-300, grande: 300+)
- **Status/tempo observado**: registre o estado real da atribuição/início; não prometa um PR dentro da etapa de 40 minutos

**Passo 4 — Escreva o guia de revisão.**
Prepare um checklist de modos de falha típicos de IA que o participante deve observar:

- [ ] **Imports alucinados**: o PR importa packages que não existem no projeto?
- [ ] **Chamadas de API fabricadas**: o código chama métodos que não estão definidos na classe de destino?
- [ ] **Testes que não testam nada**: as assertions verificam comportamento significativo ou são tautologias?
- [ ] **Comentários que contradizem o código**: os comentários descrevem um comportamento que o código não implementa?
- [ ] **Scope creep**: o PR altera arquivos não listados na issue?
- [ ] **Tratamento de erros ausente**: o PR adiciona código de happy path sem tratamento de erros?
- [ ] **Violações de estilo**: o PR segue as convenções do projeto (records para DTOs, constructor injection etc.)?

**Passo 5 — Documente a responsabilidade do participante.**
Escreva uma declaração clara: "Isto é delegação, não automação. O participante é responsável pela revisão, pela decisão de merge e por quaisquer consequências. O Copilot Agent é um colaborador, não um aprovador."

**Passo 6 — Escreva o arquivo de delegação.**
Gere a saída em `04-evolution/delegations/<issue-slug>.md`. Deixe um placeholder para a URL da issue que o participante preencherá após a publicação.

## Exemplo de invocação

```
/delegate-to-copilot-agent issue=04-evolution/issues/<slug>.md
```
