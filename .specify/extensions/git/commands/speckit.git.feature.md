---
description: "Cria uma branch de funcionalidade com numeração sequencial ou timestamp"
---

# Criar branch de funcionalidade

Crie e alterne para uma nova branch Git para a especificação informada. No desafio individual, as branches da Etapa 2 usam `spec/<NNN>-<feature>` e as branches de submissão da Etapa 3 usam `impl/<NNN>-<feature>`. Este comando trata **somente da criação da branch** — o diretório e os arquivos da especificação são criados pelo workflow principal `__SPECKIT_COMMAND_SPECIFY__`.

## Entrada do usuário

```text
$ARGUMENTS
```

Você **DEVE** considerar a entrada do usuário antes de prosseguir (se não estiver vazia).

## Sobrescrita por variável de ambiente

Se o usuário fornecer explicitamente `GIT_BRANCH_NAME` (por exemplo, por variável de ambiente, argumento ou solicitação), repasse-a ao script definindo a variável de ambiente `GIT_BRANCH_NAME` antes de invocá-lo. Quando `GIT_BRANCH_NAME` está definida:
- O script usa o valor exato como nome da branch, ignorando toda geração de prefixo/sufixo
- As opções `--short-name`, `--number` e `--timestamp` são ignoradas
- `FEATURE_NUM` é extraído do nome se ele começar com um prefixo numérico; caso contrário, recebe o nome completo da branch

## Pré-requisitos

- Verifique se o Git está disponível executando `git rev-parse --is-inside-work-tree 2>/dev/null`
- Se o Git não estiver disponível, avise o usuário e ignore a criação da branch

## Modo de numeração da branch

Determine a estratégia de numeração da branch verificando a configuração nesta ordem:

1. Verifique o valor de `branch_numbering` em `.specify/extensions/git/git-config.yml`
2. Verifique o valor de `branch_numbering` em `.specify/init-options.json` (compatibilidade retroativa)
3. Use `sequential` como padrão se nenhum deles existir

## Execução

Gere um nome curto e conciso (2 a 4 palavras) para a branch. A menos que `GIT_BRANCH_NAME` seja fornecida explicitamente, crie uma branch de especificação da Etapa 2 usando o prefixo `spec/`:
- Analise a descrição da funcionalidade e extraia as palavras-chave mais significativas
- Use o formato ação-substantivo quando possível (por exemplo, "beneficiary-consultation", "add-user-auth")
- Preserve termos técnicos e acrônimos (OAuth2, API, JWT etc.)
- Prefixe a branch gerada com `spec/` para a Etapa 2. Crie `impl/<NNN>-<feature>` manualmente a partir da `develop` atualizada para a Etapa 3.

Execute o script apropriado para sua plataforma:

- **Bash**: `.specify/extensions/git/scripts/bash/create-new-feature.sh --json --short-name "<short-name>" "<feature description>"`
- **Bash (timestamp)**: `.specify/extensions/git/scripts/bash/create-new-feature.sh --json --timestamp --short-name "<short-name>" "<feature description>"`
- **PowerShell**: `.specify/extensions/git/scripts/powershell/create-new-feature.ps1 -Json -ShortName "<short-name>" "<feature description>"`
- **PowerShell (timestamp)**: `.specify/extensions/git/scripts/powershell/create-new-feature.ps1 -Json -Timestamp -ShortName "<short-name>" "<feature description>"`

**IMPORTANTE**:
- NÃO passe `--number` — o script determina automaticamente o próximo número correto
- Sempre inclua a opção JSON (`--json` para Bash, `-Json` para PowerShell) para que a saída possa ser analisada de forma confiável
- Você deve executar este script apenas uma vez por funcionalidade
- A saída JSON conterá `BRANCH_NAME` e `FEATURE_NUM`

## Degradação controlada

Se o Git não estiver instalado ou o diretório atual não for um repositório Git:
- A criação da branch é ignorada com um aviso: `[specify] Warning: Git repository not detected; skipped branch creation`
- O script ainda produz `BRANCH_NAME` e `FEATURE_NUM` para que o chamador possa referenciá-los

## Saída

O script produz JSON com:
- `BRANCH_NAME`: o nome da branch (por exemplo, `spec/003-user-auth` ou `spec/20260319-143022-user-auth`)
- `FEATURE_NUM`: o prefixo numérico ou timestamp usado
