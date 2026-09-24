---
description: "Inicializa um repositório Git com um commit inicial"
---

# Inicializar repositório Git

Inicialize um repositório Git no diretório atual do projeto caso ainda não exista.

## Execução

Execute o script apropriado a partir da raiz do projeto:

- **Bash**: `.specify/extensions/git/scripts/bash/initialize-repo.sh`
- **PowerShell**: `.specify/extensions/git/scripts/powershell/initialize-repo.ps1`

Se os scripts da extensão não forem encontrados, use como alternativa:
- **Bash**: `git init && git add . && git commit -m "Initial commit from Specify template"`
- **PowerShell**: `git init; git add .; git commit -m "Initial commit from Specify template"`

O script realiza todas as verificações internamente:
- Ignora se o Git não estiver disponível
- Ignora se já estiver dentro de um repositório Git
- Executa `git init`, `git add .` e `git commit` com uma mensagem de commit inicial

## Personalização

Substitua o script para adicionar etapas de inicialização do Git específicas do projeto:
- Templates `.gitignore` personalizados
- Nomenclatura da branch padrão (`git config init.defaultBranch`)
- Configuração do Git LFS
- Instalação de hooks do Git
- Configuração de assinatura de commits
- Inicialização do Git Flow

## Saída

Em caso de sucesso:
- `[OK] Git repository initialized`

## Degradação controlada

Se o Git não estiver instalado:
- Avise o usuário
- Ignore a inicialização do repositório
- O projeto continua funcionando sem Git (as especificações ainda podem ser criadas em `specs/`)

Se o Git estiver instalado, mas `git init`, `git add .` ou `git commit` falhar:
- Apresente o erro ao usuário
- Interrompa este comando em vez de continuar com um repositório parcialmente inicializado
