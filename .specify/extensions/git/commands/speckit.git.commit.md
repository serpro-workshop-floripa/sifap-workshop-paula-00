---
description: "Faz commit automático das alterações após a conclusão de um comando do Spec Kit"
---

# Fazer commit automático das alterações

Adicione automaticamente todas as alterações à área de preparação e faça commit após a conclusão de um comando do Spec Kit.

## Comportamento

Este comando é invocado como hook após (ou antes de) comandos principais. Ele:

1. Determina o nome do evento a partir do contexto do hook (por exemplo, se invocado como hook `after_specify`, o evento é `after_specify`; se for `before_plan`, o evento é `before_plan`)
2. Verifica a seção `auto_commit` em `.specify/extensions/git/git-config.yml`
3. Consulta a chave específica do evento para saber se o commit automático está ativado
4. Usa `auto_commit.default` como alternativa se não existir uma chave específica para o evento
5. Usa a `message` por comando, se configurada; caso contrário, usa uma mensagem padrão
6. Se estiver ativado e houver alterações sem commit, executa `git add .` + `git commit`

## Execução

Determine o nome do evento a partir do hook que acionou este comando e execute o script:

- **Bash**: `.specify/extensions/git/scripts/bash/auto-commit.sh <event_name>`
- **PowerShell**: `.specify/extensions/git/scripts/powershell/auto-commit.ps1 <event_name>`

Substitua `<event_name>` pelo evento real do hook (por exemplo, `after_specify`, `before_plan`, `after_implement`).

## Configuração

Em `.specify/extensions/git/git-config.yml`:

```yaml
auto_commit:
  default: false          # Chave global — defina true para ativar em todos os comandos
  after_specify:
    enabled: true          # Sobrescrita por comando
    message: "[Spec Kit] Add specification"
  after_plan:
    enabled: false
    message: "[Spec Kit] Add implementation plan"
```

## Degradação controlada

- Se o Git não estiver disponível ou o diretório atual não for um repositório: ignora com um aviso
- Se não existir arquivo de configuração: ignora (desativado por padrão)
- Se não houver alterações para commit: ignora com uma mensagem
