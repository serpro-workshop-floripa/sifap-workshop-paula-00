---
agent: speckit.git.feature
---
# Criar branch de feature

Cria e alterna para uma nova branch de feature do Git para a especificação fornecida. Este comando trata **somente da criação da branch** — o diretório e os arquivos da especificação são criados pelo fluxo principal `__SPECKIT_COMMAND_SPECIFY__`.

## Objetivo

Criar uma branch de feature com nome e numeração compatíveis com a configuração do Spec Kit.

## Quando invocar

- Antes de o fluxo `__SPECKIT_COMMAND_SPECIFY__` criar os artefatos de uma nova especificação.
- Quando for necessário criar e acessar a branch correspondente a uma feature.

## Pré-condições

- Verifique se o Git está disponível executando `git rev-parse --is-inside-work-tree 2>/dev/null`.
- Se o Git não estiver disponível, avise a pessoa usuária e ignore a criação da branch.

## Entradas que a equipe deve fornecer

Considere obrigatoriamente a entrada da pessoa usuária antes de prosseguir, quando ela não estiver vazia.

```text
$ARGUMENTS
```

- Descrição da feature em `$ARGUMENTS`.
- Opcionalmente, `GIT_BRANCH_NAME` por variável de ambiente, argumento ou solicitação.

## O que farei

1. Determinarei a estratégia de numeração configurada.
2. Gerarei um nome curto e conciso para a branch.
3. Executarei uma única vez o script apropriado para a plataforma.
4. Interpretarei a saída JSON com `BRANCH_NAME` e `FEATURE_NUM`.

## O que NÃO farei

- Não criarei o diretório nem os arquivos da especificação.
- Não passarei `--number` ao script.
- Não executarei o script mais de uma vez para a mesma feature.
- Não alterarei o valor explícito de `GIT_BRANCH_NAME`.

## Formato de saída

O script produz JSON com:

- `BRANCH_NAME`: nome da branch, como `003-user-auth` ou `20260319-143022-user-auth`.
- `FEATURE_NUM`: prefixo numérico ou de timestamp usado.

## Definição de pronto

- [ ] A entrada da pessoa usuária foi considerada.
- [ ] A precedência de configuração da numeração foi respeitada.
- [ ] `GIT_BRANCH_NAME`, quando fornecido, foi preservado exatamente.
- [ ] O script foi executado no máximo uma vez.
- [ ] A saída contém `BRANCH_NAME` e `FEATURE_NUM`.

## Corpo do prompt

Se a pessoa usuária fornecer explicitamente `GIT_BRANCH_NAME`, repasse-o ao script definindo a variável de ambiente `GIT_BRANCH_NAME` antes da execução. Quando `GIT_BRANCH_NAME` estiver definido:

- O script usa o valor exato como nome da branch e ignora toda geração de prefixo ou sufixo.
- As opções `--short-name`, `--number` e `--timestamp` são ignoradas.
- `FEATURE_NUM` é extraído do nome quando ele começa com um prefixo numérico; caso contrário, recebe o nome completo da branch.

Determine a estratégia de numeração da branch nesta ordem:

1. Consulte o valor `branch_numbering` em `.specify/extensions/git/git-config.yml`.
2. Consulte o valor `branch_numbering` em `.specify/init-options.json` para compatibilidade retroativa.
3. Use `sequential` por padrão se nenhum valor existir.

Gere um nome curto e conciso, com duas a quatro palavras, para a branch:

- Analise a descrição da feature e extraia as palavras-chave mais significativas.
- Use o formato ação-substantivo quando possível, como "add-user-auth" ou "fix-payment-bug".
- Preserve termos técnicos e siglas, como OAuth2, API e JWT.

Execute o script apropriado para a plataforma:

- **Bash**: `.specify/extensions/git/scripts/bash/create-new-feature.sh --json --short-name "<short-name>" "<feature description>"`
- **Bash (timestamp)**: `.specify/extensions/git/scripts/bash/create-new-feature.sh --json --timestamp --short-name "<short-name>" "<feature description>"`
- **PowerShell**: `.specify/extensions/git/scripts/powershell/create-new-feature.ps1 -Json -ShortName "<short-name>" "<feature description>"`
- **PowerShell (timestamp)**: `.specify/extensions/git/scripts/powershell/create-new-feature.ps1 -Json -Timestamp -ShortName "<short-name>" "<feature description>"`

> [!IMPORTANT]
> Não passe `--number`; o script determina automaticamente o próximo número correto. Sempre inclua a opção JSON (`--json` para Bash ou `-Json` para PowerShell) para permitir a interpretação confiável da saída. Execute este script somente uma vez por feature.

Se o Git não estiver instalado ou o diretório atual não for um repositório, ignore a criação da branch com o aviso `[specify] Warning: Git repository not detected; skipped branch creation`. O script ainda deve produzir `BRANCH_NAME` e `FEATURE_NUM` para que o chamador possa referenciá-los.

## Exemplo de invocação

Crie a branch de feature para `$ARGUMENTS`, preservando `GIT_BRANCH_NAME` quando fornecido.
