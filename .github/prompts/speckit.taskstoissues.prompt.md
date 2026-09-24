---
agent: speckit.taskstoissues
---

# Spec-Kit — Converter tarefas em issues

## Objetivo

Converter as tarefas da funcionalidade em issues no repositório github correto.

## Quando invocar

Use este prompt quando `tasks.md` estiver pronto e o remote Git apontar para GitHub.

## Pré-condições

- O repositório e os artefatos exigidos pelo fluxo Spec-Kit devem estar disponíveis.
- Os hooks de extensão aplicáveis devem ser avaliados conforme o corpo do prompt.

## Entradas que a equipe deve fornecer

- A orientação adicional fornecida em `$arguments` e a lista de tarefas ativa.

## O que farei

- Executarei o fluxo Spec-Kit descrito no corpo do prompt.
- Validarei os artefatos e informarei o resultado ao usuário.

## O que NÃO farei

- Não ignorarei gates, dependências, hooks obrigatórios nem validações do fluxo.
- Não alterarei placeholders, comandos, paths, IDs ou estruturas exigidas pelo Spec-Kit.

## Formato de saída

As issues criadas no repositório correspondente ao remote git.

## Definição de pronto

- [ ] O fluxo descrito no corpo do prompt foi concluído ou um bloqueio foi informado claramente.
- [ ] As validações e os hooks aplicáveis foram processados.
- [ ] O resultado final foi apresentado no formato solicitado.

## Corpo do prompt

### Entrada do usuário

```text
$ARGUMENTS

```

Você **DEVE** considerar a entrada do usuário antes de prosseguir (se não estiver vazia).

### Verificações pré-execução

**Verifique hooks de extensão (antes da conversão de tarefas em issues)**:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia-o e procure entradas na chave `hooks.before_taskstoissues`
- Se não for possível interpretar o YAML ou se ele for inválido, ignore silenciosamente a verificação de hooks e continue normalmente
- Desconsidere hooks nos quais `enabled` seja explicitamente `false`. Considere habilitados por padrão os hooks sem um campo `enabled`.
- Para cada hook restante, **não** tente interpretar nem avaliar expressões `condition` do hook:
  - Se o hook não tiver o campo `condition` ou se ele for nulo/vazio, considere o hook executável
  - Se o hook definir uma condição não vazia em `condition`, ignore o hook e deixe a avaliação da condição para a implementação de `HookExecutor`

- Para cada hook executável, produza o conteúdo a seguir conforme seu sinalizador `optional` :
  - **Hook opcional** (`optional: true`):

    ```
    ## Extension Hooks

    **Opcional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`

    ```

  - **Hook obrigatório** (`optional: false`):

    ```
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Outline.

    ```

- Se nenhum hook estiver registrado ou `.specify/extensions.yml` não existir, ignore silenciosamente

### Roteiro

1. Execute `{SCRIPT}` na raiz do repositório e interprete FEATURE_DIR e a lista AVAILABLE_DOCS. Todos os paths devem ser absolutos. Para aspas simples em argumentos como "I'm Groot", use sintaxe de escape, por exemplo: 'I'\''m Groot' (ou aspas duplas, se possível: "I'm Groot").
1. **SE EXISTIR**: Carregue `/memory/constitution.md` para obter os princípios do projeto e as restrições de governança.
1. Do script executado, extraia o path de **tasks**.
1. Obtenha o remote Git executando:

```bash
git config --get remote.origin.url

```

> [!CAUTION]
> PROSSIGA PARA AS PRÓXIMAS ETAPAS SOMENTE SE O REMOTE FOR UMA URL DO GITHUB

1. Para cada tarefa da lista, use o servidor MCP do GitHub para criar uma nova issue no repositório correspondente ao remote Git.

> [!CAUTION]
> NUNCA, EM NENHUMA CIRCUNSTÂNCIA, CRIE ISSUES EM REPOSITÓRIOS QUE NÃO CORRESPONDAM À URL DO REMOTE

### Verificações pós-execução

**Verifique hooks de extensão (depois da conversão de tarefas em issues)**:
Verifique se `.specify/extensions.yml` existe na raiz do projeto.

- Se existir, leia-o e procure entradas na chave `hooks.after_taskstoissues`
- Se não for possível interpretar o YAML ou se ele for inválido, ignore silenciosamente a verificação de hooks e continue normalmente
- Desconsidere hooks nos quais `enabled` seja explicitamente `false`. Considere habilitados por padrão os hooks sem um campo `enabled`.
- Para cada hook restante, **não** tente interpretar nem avaliar expressões `condition` do hook:
  - Se o hook não tiver o campo `condition` ou se ele for nulo/vazio, considere o hook executável
  - Se o hook definir uma condição não vazia em `condition`, ignore o hook e deixe a avaliação da condição para a implementação de `HookExecutor`

- Para cada hook executável, produza o conteúdo a seguir conforme seu sinalizador `optional` :
  - **Hook opcional** (`optional: true`):

    ```
    ## Extension Hooks

    **Opcional Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`

    ```

  - **Hook obrigatório** (`optional: false`):

    ```
    ## Extension Hooks

    **Automatic Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    ```

- Se nenhum hook estiver registrado ou `.specify/extensions.yml` não existir, ignore silenciosamente

## Exemplo de invocação

```text
`/speckit.taskstoissues`

```
