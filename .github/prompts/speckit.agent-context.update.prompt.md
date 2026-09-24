---
agent: speckit.agent-context.update
---
# Atualizar o contexto do coding agent

## Objetivo

Atualizar a seção gerenciada pelo Spec Kit no arquivo de contexto ou instruções do coding agent ativo.

## Quando invocar

Invoque após criar ou atualizar um plano em `specs/<feature>/plan.md`.

## Pré-condições

- A configuração `.specify/extensions/agent-context/agent-context-config.yml` deve estar disponível.
- O `context_file` configurado deve apontar para o arquivo de contexto que será gerenciado.

## Inputs que a equipe deve fornecer

- Opcionalmente, o argumento `[plan_path]` com o path do plano.
- Sem o argumento, o script detecta o `specs/*/plan.md` modificado mais recentemente.

## O que farei

- Lerei `context_file` e os delimitadores `context_markers.start` / `.end`.
- Criarei, substituirei ou anexarei o bloco gerenciado.
- Apontarei a seção para o plano mais recente que puder ser descoberto.

## O que NÃO farei

- Não falharei quando `context_file` estiver vazio ou o arquivo não puder ser localizado.
- Não alterarei conteúdo fora dos delimitadores gerenciados.

## Formato de saída

O arquivo de contexto configurado será atualizado. Quando não houver trabalho a fazer, o comando encerrará
com sucesso sem produzir alterações.

## Definição de pronto

- [ ] O bloco gerenciado está delimitado por `<!-- SPECKIT START -->` e `<!-- SPECKIT END -->`, ou pelos marcadores configurados.
- [ ] O bloco aponta para o path correto do plano.
- [ ] Nenhum conteúdo fora do bloco gerenciado foi alterado.

## Corpo do prompt

O script lê a configuração da extensão agent-context em
`.specify/extensions/agent-context/agent-context-config.yml` para descobrir:

- `context_file` — o path do arquivo de contexto do coding agent a gerenciar.
- `context_markers.start` / `.end` — os delimitadores ao redor da seção gerenciada. O padrão é
  `<!-- SPECKIT START -->` e `<!-- SPECKIT END -->` quando o campo estiver ausente.

Em seguida, ele cria, substitui ou anexa o bloco gerenciado para que a seção aponte para o path do plano
mais recente quando for possível descobri-lo (`specs/<feature>/plan.md`).

Se `context_file` estiver vazio ou o arquivo não puder ser localizado, o comando informa que não há nada
a fazer e encerra com sucesso.

Execução:

- **Bash**: `.specify/extensions/agent-context/scripts/bash/update-agent-context.sh [plan_path]`
- **PowerShell**: `.specify/extensions/agent-context/scripts/powershell/update-agent-context.ps1 [plan_path]`

Quando `plan_path` for omitido, o script detectará automaticamente o `specs/*/plan.md` modificado mais
recentemente.

## Exemplo de invocação

```shell
.specify/extensions/agent-context/scripts/bash/update-agent-context.sh specs/001-feature/plan.md
```
