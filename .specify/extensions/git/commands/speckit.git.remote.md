---
description: "Detecta a URL do remoto Git para integração com o GitHub"
---

# Detectar URL do remoto Git

Detecte a URL do remoto Git para integração com serviços do GitHub (por exemplo, criação de issue).

## Pré-requisitos

- Verifique se o Git está disponível executando `git rev-parse --is-inside-work-tree 2>/dev/null`
- Se o Git não estiver disponível, exiba um aviso e retorne vazio:
  ```
  [specify] Warning: Git repository not detected; cannot determine remote URL
  ```

## Execução

Execute o comando a seguir para obter a URL do remoto:

```bash
git config --get remote.origin.url
```

## Saída

Analise a URL do remoto e determine:

1. **Proprietário do repositório**: extraia da URL (por exemplo, `github` de `https://github.com/github/spec-kit.git`)
2. **Nome do repositório**: extraia da URL (por exemplo, `spec-kit` de `https://github.com/github/spec-kit.git`)
3. **É GitHub**: indica se o remoto aponta para um repositório do GitHub

Formatos de URL compatíveis:
- HTTPS: `https://github.com/<owner>/<repo>.git`
- SSH: `git@github.com:<owner>/<repo>.git`

> [!CAUTION]
> Informe um repositório do GitHub SOMENTE se a URL do remoto realmente apontar para github.com.
> NÃO presuma que o remoto seja do GitHub se o formato da URL não corresponder.

## Degradação controlada

Se o Git não estiver instalado, o diretório não for um repositório Git ou nenhum remoto estiver configurado:
- Retorne um resultado vazio
- NÃO gere erro — outros workflows devem continuar sem informações do remoto Git
