---
name: "write-github-issue"
description: "Não usado no desafio individual; escreve uma issue GitHub de alta qualidade, pronta para o Copilot Agent na nuvem."
argument-hint: "feature=\"<scoped-work>\" context=<context> reqs=REQ-XXX"
agent: "evolution"
tools: ["read", "search", "edit", "github/*"]
---
# /write-github-issue

> [!NOTE]
> Não usado no desafio individual (14:00-17:40). O desafio termina na Etapa 3 e na validação do juiz. Consulte [ADR-0003](../../docs/adr/0003-individual-challenge-format.md).

## Objetivo

Criar uma issue GitHub bem estruturada e otimizada para execução autônoma pelo Copilot Agent (nuvem). A issue tem critérios de aceitação claros, orientação sobre paths de arquivos e rastreabilidade de REQ-ID.

## Quando invocar

No início da Etapa 4, quando o participante identifica trabalho que pode ser delegado ao Copilot Agent.

## Pré-condições

- O participante tem um protótipo funcional da Etapa 3
- `.spec/<NNN>-<feature>/spec.md` existe com requisitos EARS
- O participante identificou uma parte específica do trabalho a delegar

## Inputs que a equipe deve fornecer

- Uma descrição da funcionalidade ou correção desejada
- REQ-IDs relacionados (se houver)
- O bounded context e os arquivos que provavelmente serão afetados

## O que farei

- Estruturar a issue com cinco seções obrigatórias: Context, Acceptance Criteria, Affected Files, Testing Approach e Out of Scope
- Referenciar REQ-IDs e critérios existentes sem inventar requisitos EARS ou comportamento
- Sugerir labels e um assignee

## O que NÃO farei

- Publicar a issue diretamente — o participante a revisa e publica manualmente
- Escrever issues vagas — toda issue tem critérios de aceitação específicos
- Criar issues para trabalhos que o participante deve realizar por conta própria (decisões arquiteturais, correções de segurança)
- Ignorar a seção de estratégia de testes — o Copilot Agent precisa saber como verificar seu trabalho

## Formato de saída

Um arquivo de rascunho em `04-evolution/issues/<slug>.md`:

```markdown
# Issue: [Title]
## Context
## Acceptance Criteria
## Files Likely Affected
## Testing Approach
## Out of Scope
## Labels
## Related Requirements
```

## Definição de pronto

- [ ] O rascunho da issue tem todas as cinco seções de conteúdo
- [ ] Os critérios de aceitação são específicos e testáveis
- [ ] Pelo menos um REQ-ID é referenciado, ou "novo comportamento" é declarado com uma justificativa
- [ ] Os arquivos que provavelmente serão afetados estão listados com paths relativos
- [ ] A estratégia de testes descreve quais testes adicionar ou modificar
- [ ] A issue é pequena o suficiente para um único PR (se for grande demais, divida-a)

## Corpo do prompt

Você é o `@evolution`. O participante quer delegar trabalho ao Copilot Agent por meio de uma issue GitHub.

**Passo 1 — Compreenda a solicitação.**
Pergunte ao participante:

1. O que você quer que seja feito? (1-2 frases)
2. Qual bounded context isso afeta?
3. Isso implementa um `REQ-NNN` existente ou um novo comportamento?
4. Quais arquivos provavelmente estão envolvidos?

**Passo 2 — Escreva a seção Context.**
Descreva por que esse trabalho é necessário. Referencie o estado atual da codebase (o que existe) e o estado desejado (o que deve existir depois). Inclua um link para a especificação EARS, se relevante.

**Passo 3 — Copie os Acceptance Criteria.**
Copie de `spec.md` os critérios verificáveis para os REQ-IDs fornecidos. Se
estiverem ausentes, registre a lacuna e não invente uma resposta pronta.

**Passo 4 — Liste os Affected Files.**
Com base no input do participante e em uma pesquisa na codebase, liste:

- Arquivos a modificar (com paths relativos)
- Arquivos a criar (com paths sugeridos que sigam a estrutura de packages)
- Arquivos a referenciar, mas não modificar (por exemplo, a especificação OpenAPI ou interfaces existentes)

**Passo 5 — Defina o Testing Approach.**
Descreva quais testes o Copilot Agent deve escrever:

- Testes unitários para novos métodos de serviço
- Testes de integração para novos endpoints
- Testes existentes que podem precisar de atualização

Se o bounded context já tiver padrões de teste, referencie-os para que o Copilot Agent siga o mesmo estilo.

**Passo 6 — Marque o que está Out of Scope.**
Declare explicitamente o que esta issue NÃO cobre. Isso evita scope creep no PR gerado por IA. Exemplos:

- "Does not change the database schema"
- "Does not modify the authentication flow"
- "Frontend changes are tracked in a separate issue"

**Passo 7 — Adicione metadados.**
Sugira labels: `enhancement` ou `bug`, o nome do bounded context e `copilot-agent`.

**Passo 8 — Escreva o rascunho.**
Gere a saída em `04-evolution/issues/<slug>.md`, em que `<slug>` é uma versão do título em kebab-case. O participante revisa esse rascunho antes de publicá-lo como uma issue GitHub real.

Lembre ao participante: este é um rascunho. Revise-o, ajuste o escopo se necessário e publique-o manualmente pela UI do GitHub ou com `gh issue create`.

## Exemplo de invocação

```
/write-github-issue feature="<scoped-work>" context=<context> reqs=REQ-XXX
```
