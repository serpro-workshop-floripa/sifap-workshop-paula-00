---
agent: speckit.git.initialize
---
# Inicializar repositório Git

Inicializa um repositório Git no diretório atual do projeto quando ainda não existe um.

## Objetivo

Preparar o projeto para controle de versão com uma inicialização segura e um commit inicial.

## Quando invocar

- Ao preparar um projeto que ainda não está dentro de um repositório Git.
- Durante a inicialização do Spec Kit quando o controle de versão estiver disponível.

## Pré-condições

- Execute a partir da raiz do projeto.
- Use o script correspondente à plataforma quando ele estiver disponível.

## Entradas que a equipe deve fornecer

- Nenhuma entrada obrigatória.
- Opcionalmente, um script substituto com etapas de inicialização específicas do projeto.

## O que farei

- Verificarei se o Git está disponível.
- Ignorarei a inicialização se o projeto já estiver dentro de um repositório Git.
- Executarei `git init`, `git add .` e `git commit` com uma mensagem de commit inicial.

## O que NÃO farei

- Não reinicializarei um repositório Git existente.
- Não continuarei após uma falha que deixe o repositório parcialmente inicializado.
- Não impedirei a criação de especificações quando o Git não estiver instalado.

## Formato de saída

Em caso de sucesso:

- `[OK] Git repository initialized`

Em caso de Git indisponível, apresente um aviso e ignore a inicialização. Em caso de falha de um comando Git, apresente o erro e interrompa este comando.

## Definição de pronto

- [ ] A disponibilidade do Git e a existência de um repositório foram verificadas.
- [ ] O script da plataforma ou o fallback foi executado.
- [ ] O repositório foi inicializado integralmente ou a operação foi ignorada de forma controlada.
- [ ] Nenhum estado parcialmente inicializado foi tratado como sucesso.

## Corpo do prompt

Execute o script apropriado a partir da raiz do projeto:

- **Bash**: `.specify/extensions/git/scripts/bash/initialize-repo.sh`
- **PowerShell**: `.specify/extensions/git/scripts/powershell/initialize-repo.ps1`

Se os scripts da extensão não forem encontrados, use o fallback:

- **Bash**: `git init && git add . && git commit -m "Initial commit from Specify template"`
- **PowerShell**: `git init; git add .; git commit -m "Initial commit from Specify template"`

O script trata internamente todas as verificações: ignora a operação se o Git não estiver disponível ou se o diretório já estiver em um repositório Git; caso contrário, executa `git init`, `git add .` e `git commit` com uma mensagem de commit inicial.

O script pode ser substituído para adicionar etapas de inicialização específicas do projeto:

- Modelos personalizados de `.gitignore`.
- Nome padrão da branch com `git config init.defaultBranch`.
- Configuração do Git LFS.
- Instalação de hooks do Git.
- Configuração de assinatura de commits.
- Inicialização do Git Flow.

Se o Git não estiver instalado, avise a pessoa usuária, ignore a inicialização do repositório e permita que o projeto continue funcionando; as especificações ainda podem ser criadas em `specs/`.

Se o Git estiver instalado, mas `git init`, `git add .` ou `git commit` falhar, apresente o erro e interrompa este comando em vez de continuar com um repositório parcialmente inicializado.

## Exemplo de invocação

Inicialize o repositório Git do projeto atual se ele ainda não existir.
