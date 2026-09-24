# Extensão de workflow de branches Git

Inicialização de repositório Git, criação de branch de funcionalidade, numeração (sequencial/timestamp), validação, detecção de remoto e commit automático para o Spec Kit.

## Visão geral

Esta extensão fornece operações Git como um módulo opcional e autocontido. Ela gerencia:

- **Inicialização de repositório** com mensagens de commit configuráveis
- **Criação de branch de funcionalidade** com numeração sequencial (`001-feature-name`) ou timestamp (`20260319-143022-feature-name`)
- **Validação de branch** para garantir que as branches sigam as convenções de nomenclatura
- **Detecção de remoto Git** para integração com o GitHub (por exemplo, criação de issue)
- **Commit automático** após comandos principais (configurável por comando com mensagens personalizadas)

## Comandos

| Comando | Descrição |
|---------|-------------|
| `speckit.git.initialize` | Inicializa um repositório Git com uma mensagem de commit configurável |
| `speckit.git.feature` | Cria uma branch de funcionalidade com numeração sequencial ou timestamp |
| `speckit.git.validate` | Valida se a branch atual segue as convenções de nomenclatura de branches de funcionalidade |
| `speckit.git.remote` | Detecta a URL do remoto Git para integração com o GitHub |
| `speckit.git.commit` | Faz commit automático das alterações (ativação/desativação e mensagens configuráveis por comando) |

## Hooks

| Evento | Comando | Opcional | Descrição |
|-------|---------|----------|-------------|
| `before_constitution` | `speckit.git.initialize` | Não | Inicializa o repositório Git antes da constituição |
| `before_specify` | `speckit.git.feature` | Não | Cria a branch de funcionalidade antes da especificação |
| `before_clarify` | `speckit.git.commit` | Sim | Faz commit das alterações pendentes antes do esclarecimento |
| `before_plan` | `speckit.git.commit` | Sim | Faz commit das alterações pendentes antes do planejamento |
| `before_tasks` | `speckit.git.commit` | Sim | Faz commit das alterações pendentes antes da geração de tarefas |
| `before_implement` | `speckit.git.commit` | Sim | Faz commit das alterações pendentes antes da implementação |
| `before_checklist` | `speckit.git.commit` | Sim | Faz commit das alterações pendentes antes do checklist |
| `before_analyze` | `speckit.git.commit` | Sim | Faz commit das alterações pendentes antes da análise |
| `before_taskstoissues` | `speckit.git.commit` | Sim | Faz commit das alterações pendentes antes da sincronização de issues |
| `after_constitution` | `speckit.git.commit` | Sim | Faz commit automático após a atualização da constituição |
| `after_specify` | `speckit.git.commit` | Sim | Faz commit automático após a especificação |
| `after_clarify` | `speckit.git.commit` | Sim | Faz commit automático após o esclarecimento |
| `after_plan` | `speckit.git.commit` | Sim | Faz commit automático após o planejamento |
| `after_tasks` | `speckit.git.commit` | Sim | Faz commit automático após a geração de tarefas |
| `after_implement` | `speckit.git.commit` | Sim | Faz commit automático após a implementação |
| `after_checklist` | `speckit.git.commit` | Sim | Faz commit automático após o checklist |
| `after_analyze` | `speckit.git.commit` | Sim | Faz commit automático após a análise |
| `after_taskstoissues` | `speckit.git.commit` | Sim | Faz commit automático após a sincronização de issues |

## Configuração

A configuração é armazenada em `.specify/extensions/git/git-config.yml`:

```yaml
# Estratégia de numeração de branches: "sequential" ou "timestamp"
branch_numbering: sequential

# Mensagem de commit personalizada para git init
init_commit_message: "[Spec Kit] Initial commit"

# Commit automático por comando (todos desativados por padrão)
# Exemplo: ativar commit automático após specify
auto_commit:
  default: false
  after_specify:
    enabled: true
    message: "[Spec Kit] Add specification"
```

## Instalação

```bash
# Instala a extensão Git incluída (não requer rede)
specify extension add git
```

## Desativação

```bash
# Desativa a extensão Git (a criação de especificações continua sem branches)
specify extension disable git

# Reativa a extensão
specify extension enable git
```

## Degradação controlada

Quando o Git não está instalado ou o diretório não é um repositório Git:
- Os diretórios de especificação ainda são criados em `specs/`
- A criação de branch é ignorada com um aviso
- A validação da branch é ignorada com um aviso
- A detecção do remoto retorna resultados vazios

## Scripts

A extensão inclui scripts multiplataforma:

- `scripts/bash/create-new-feature.sh` — implementação em Bash
- `scripts/bash/git-common.sh` — utilitários Git compartilhados (Bash)
- `scripts/powershell/create-new-feature.ps1` — implementação em PowerShell
- `scripts/powershell/git-common.ps1` — utilitários Git compartilhados (PowerShell)
