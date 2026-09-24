---
description: "Use ao criar ou revisar GitHub Actions, workflows de CI/CD, gates YAML, verificações de build e automação de deployment."
applyTo: ".github/workflows/**,.github/actions/**,**/action.yml,**/action.yaml"
---

# Convenções de CI/CD — Gates do GitHub Actions

Este arquivo se aplica a workflows em `.github/workflows/`, actions compostas em `.github/actions/` e arquivos `action.yml` ou `action.yaml`. Ele orienta estrutura, fixação de actions, permissões e honestidade dos gates. Leia [`ci.yml`](../workflows/ci.yml) e [`spec-quality.yml`](../workflows/spec-quality.yml) antes de alterar um gate.

## Gates ativos

| Workflow · Job | O que verifica | Bloqueia? |
|---|---|---|
| `ci.yml` · `detect-changes` | Define outputs `backend`, `frontend` e `infra` para executar apenas jobs relevantes | Não se aplica |
| `ci.yml` · `natural-format` | Rejeita declarações Natural com vírgula decimal em vez de ponto | Sim |
| `ci.yml` · `backend` | JDK 21 + `./mvnw -B verify`; publica Jacoco | Sim |
| `ci.yml` · `frontend` | pnpm 9 + Node 20; lint, typecheck, testes e cobertura | Sim |
| `ci.yml` · `infra` | `terraform fmt`, `init -backend=false` e `validate` por módulo | Sim |
| `spec-quality.yml` · `markdown-lint` | Executa `markdownlint-cli2` em `**/*.md` | Sim |
| `spec-quality.yml` · `spec-traceability` | Avisa sobre REQ-IDs sem referência em testes | Não |
| `spec-quality.yml` · `legacy-traceability` | Exige `source_legacy:` válido para cada REQ-ID | Sim |

> [!IMPORTANT]
> `legacy-traceability` falha o build; `spec-traceability` apenas avisa. Consulte [`spec-quality.yml`](../workflows/spec-quality.yml) para o formato aceito.

## Fixe cada action por SHA

Referencie actions pelo SHA completo de 40 caracteres e mantenha a tag em comentário. Tags são mutáveis.

```yaml
- uses: actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803 # v6
```

## Permissões de privilégio mínimo

Declare `permissions` no início de cada workflow com o menor escopo e amplie por job apenas quando necessário.

```yaml
permissions:
  contents: read

jobs:
  detect-changes:
    permissions:
      contents: read
      pull-requests: read
```

## Jobs condicionais por path

Coloque jobs pesados atrás de `detect-changes` para que PRs apenas de documentação não executem Maven ou Terraform.

```yaml
backend:
  needs: detect-changes
  if: needs.detect-changes.outputs.backend == 'true'
```

## Concorrência e timeouts

Cada workflow cancela runs substituídas e cada job define `timeout-minutes`.

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## Deployment com OIDC

Ainda não existe job de deploy. Quando criar um, autentique no Azure com OIDC, nunca com client secret armazenado, e conceda `id-token: write` apenas ao job.

## Convenções

| Regra | Motivo |
|---|---|
| Fixe actions pelo SHA completo | Evita substituição maliciosa de tags |
| Use `permissions:` com `contents: read` por padrão | Aplica privilégio mínimo |
| Use `concurrency` e `cancel-in-progress` | Evita runs concorrentes e desperdiçadas |
| Defina `timeout-minutes` em cada job | Interrompe steps travados |
| Use OIDC, nunca secret de nuvem armazenado | Evita credenciais de longa duração |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Referencie `@<sha> # vN` | Referencie `@v4`, `@main` ou branch |
| Conceda `id-token: write` por job de deploy | Use `write-all` no workflow |
| Leia o workflow antes de editar um gate | Adivinhe o que o gate verifica |
| Deixe `detect-changes` pular jobs irrelevantes | Execute todos os jobs em todo PR |

## Checklist antes de abrir um PR

- [ ] Cada `uses:` está fixado em SHA completo com comentário de versão.
- [ ] O workflow declara `permissions:` com privilégio mínimo.
- [ ] Cada job define `timeout-minutes` e o workflow define `concurrency`.
- [ ] Novos gates estão descritos com precisão.
- [ ] Steps de nuvem usam OIDC e `id-token: write` restrito.
- [ ] `markdownlint-cli2` e os jobs reproduzíveis passam localmente.
