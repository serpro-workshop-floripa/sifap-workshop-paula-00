---
agent: speckit.git.commit
---
# Commit automático das alterações

Adiciona e cria automaticamente um commit com todas as alterações após a conclusão de um comando do Spec Kit.

## Objetivo

Executar o commit automático configurável das alterações produzidas por comandos do Spec Kit.

## Quando invocar

- Como hook executado antes ou depois dos comandos principais.
- Quando o evento correspondente puder habilitar um commit em `.specify/extensions/git/git-config.yml`.

## Pré-condições

- O Git deve estar disponível e o diretório atual deve ser um repositório.
- O script da plataforma deve estar disponível.

## Entradas que a equipe deve fornecer

- O nome do evento recebido no contexto do hook, como `after_specify`, `before_plan` ou `after_implement`.
- Opcionalmente, a configuração `auto_commit` em `.specify/extensions/git/git-config.yml`.

## O que farei

1. Determinarei o nome do evento com base no contexto do hook.
2. Consultarei a configuração do evento e o fallback `auto_commit.default`.
3. Usarei a `message` configurada para o comando ou uma mensagem padrão.
4. Quando habilitado e houver alterações, executarei `git add .` e `git commit`.

## O que NÃO farei

- Não criarei um commit quando o recurso estiver desabilitado.
- Não criarei um commit quando não houver alterações.
- Não interromperei o fluxo se o Git, o repositório ou o arquivo de configuração não estiver disponível.

## Formato de saída

- Mensagem de sucesso quando um commit for criado.
- Mensagem informativa quando não houver alterações.
- Aviso quando o Git ou o repositório não estiver disponível.

## Configuração

Em `.specify/extensions/git/git-config.yml`:

```yaml
auto_commit:
  default: false          # Global toggle — set true to enable for all commands
  after_specify:
    enabled: true          # Override per-command
    message: "[Spec Kit] Add specification"
  after_plan:
    enabled: false
    message: "[Spec Kit] Add implementation plan"
```

## Definição de pronto

- [ ] O evento correto foi identificado.
- [ ] A configuração específica do evento ou o fallback foi respeitado.
- [ ] O commit foi criado somente quando habilitado e havia alterações.
- [ ] As condições de degradação controlada foram tratadas sem interromper outros fluxos.

## Corpo do prompt

Este comando é invocado como hook antes ou depois dos comandos principais. Determine o nome do evento a partir do hook que acionou este comando. Por exemplo, para um hook `after_specify`, o evento é `after_specify`; para `before_plan`, o evento é `before_plan`.

Verifique a seção `auto_commit` de `.specify/extensions/git/git-config.yml`, procure a chave específica do evento e use `auto_commit.default` quando ela não existir. Use a `message` específica do comando quando configurada; caso contrário, use uma mensagem padrão.

Execute o script correspondente:

- **Bash**: `.specify/extensions/git/scripts/bash/auto-commit.sh <event_name>`
- **PowerShell**: `.specify/extensions/git/scripts/powershell/auto-commit.ps1 <event_name>`

Substitua `<event_name>` pelo evento real do hook. Se o recurso estiver habilitado e houver alterações sem commit, execute `git add .` e `git commit`.

Use degradação controlada:

- Se o Git não estiver disponível ou o diretório atual não for um repositório, ignore a operação com um aviso.
- Se não houver arquivo de configuração, ignore a operação, pois o recurso é desabilitado por padrão.
- Se não houver alterações para commit, ignore a operação com uma mensagem.

## Exemplo de invocação

Execute o commit automático para o evento `after_specify`.
