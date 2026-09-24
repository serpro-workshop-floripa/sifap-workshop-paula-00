---
agent: speckit.git.remote
---
# Detectar URL remota do Git

Detecta a URL remota do Git para integração com serviços do GitHub, como a criação de issues.

## Objetivo

Identificar com segurança o proprietário, o nome e o provedor do repositório remoto.

## Quando invocar

- Quando um fluxo precisar integrar-se a serviços do GitHub.
- Antes de criar uma issue ou executar outra ação que dependa do repositório remoto.

## Pré-condições

- Verifique se o Git está disponível executando `git rev-parse --is-inside-work-tree 2>/dev/null`.
- Se o Git não estiver disponível, produza um aviso e retorne um resultado vazio:

  ```
  [specify] Warning: Git repository not detected; cannot determine remote URL
  ```

## Entradas que a equipe deve fornecer

- Nenhuma entrada obrigatória.
- O remote `origin` deve estar configurado para que a URL possa ser detectada.

## O que farei

1. Obterei a URL de `remote.origin.url`.
2. Interpretarei os formatos HTTPS e SSH aceitos.
3. Identificarei o proprietário, o nome do repositório e se o remote aponta para o GitHub.

## O que NÃO farei

- Não presumirei que um remote pertence ao GitHub quando a URL não apontar para `github.com`.
- Não produzirei erro quando o Git, o repositório ou o remote não estiver disponível.

## Formato de saída

- **Proprietário do repositório**: extraído da URL, como `github` em `https://github.com/github/spec-kit.git`.
- **Nome do repositório**: extraído da URL, como `spec-kit` em `https://github.com/github/spec-kit.git`.
- **É GitHub**: indica se o remote aponta para um repositório do GitHub.
- Resultado vazio quando as informações remotas não puderem ser determinadas.

## Definição de pronto

- [ ] A URL de `remote.origin.url` foi consultada.
- [ ] Os formatos HTTPS e SSH aceitos foram interpretados corretamente.
- [ ] Um repositório foi identificado como GitHub somente quando a URL aponta para `github.com`.
- [ ] A ausência do remote foi tratada por degradação controlada.

## Corpo do prompt

Execute o comando a seguir para obter a URL remota:

```bash
git config --get remote.origin.url
```

Interprete a URL remota e determine o proprietário do repositório, o nome do repositório e se o remote aponta para um repositório do GitHub.

Formatos de URL aceitos:

- HTTPS: `https://github.com/<owner>/<repo>.git`
- SSH: `git@github.com:<owner>/<repo>.git`

> [!CAUTION]
> Informe um repositório do GitHub SOMENTE se a URL remota realmente apontar para `github.com`. NÃO presuma que o remote é do GitHub se o formato da URL não corresponder.

Se o Git não estiver instalado, o diretório não for um repositório Git ou nenhum remote estiver configurado, retorne um resultado vazio sem produzir erro. Outros fluxos devem continuar sem as informações do remote do Git.

## Exemplo de invocação

Detecte a URL do remote `origin` e informe o proprietário, o repositório e se ele pertence ao GitHub.
