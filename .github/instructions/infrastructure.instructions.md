---
description: "Use ao criar ou revisar infraestrutura como código, Terraform, Bicep, resources Azure e configuração de ambientes."
applyTo: "infra/**,**/*.tf,**/*.bicep,compose*.yml,compose*.yaml,docker-compose*.yml,docker-compose*.yaml"
---

# Convenções de infraestrutura — Terraform e Compose

Este arquivo se aplica a `infra/`, `*.tf`, `*.bicep` e YAML de Compose. Use Terraform com `azurerm ~> 3.x` como ferramenta principal. Use Bicep apenas quando um módulo realmente exigir. A equipe cria `infra/` nas Etapas 3/4; não existe stack herdada.

## Provider e versões

Fixe o provider e a versão mínima do Terraform. Mantenha um bloco `provider "azurerm"` por configuração.

```hcl
terraform {
  required_version = ">= 1.9.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}
```

## Organização de módulos

Use um módulo por área de serviço Azure para limitar blast radius e esclarecer ownership.

```text
infra/
├── networking/
├── compute/
├── database/
└── monitoring/
```

## Tags obrigatórias

Cada resource inclui `project`, `environment` e `owner`. Adicione `cost-center` quando a equipe o controlar. Defina as tags uma vez em `locals`.

```hcl
locals {
  common_tags = {
    project     = var.project
    environment = var.environment
    owner       = var.owner
  }
}
```

## Secrets

> [!WARNING]
> Secrets ficam apenas em `azurerm_key_vault_secret`, nunca em defaults de variables, `locals`, `.tfvars` ou state versionado. Marque inputs secretos com `sensitive = true` e injete-os pela sessão OIDC do pipeline.

## Managed Identity

Use Managed Identity na autenticação entre serviços, não connection strings com senhas. Atribua a identidade e conceda acesso ao Key Vault por role assignment.

## Nomenclatura

Resources usam `{project}-{env}-{resource}-{region}`.

| Resource | Exemplo |
|---|---|
| Resource group | `sifap-prod-rg-brs` |
| PostgreSQL server | `sifap-prod-psql-brs` |

## Formatação e validação

A CI executa `terraform fmt -check -recursive`, `terraform init -backend=false` e `terraform validate` por módulo. Antes do push, execute `terraform fmt -recursive` e `terraform -chdir=<module> validate`.

## Paridade com Docker Compose

Use Compose apenas no desenvolvimento local. Fixe imagens por digest, mantenha secrets em `.env` ignorado pelo Git e nunca versione credenciais.

```yaml
services:
  db:
    image: postgres:16@sha256:<digest>
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```

## Convenções

| Regra | Motivo |
|---|---|
| `azurerm ~> 3.x` e `required_version` fixados | Produz plans reproduzíveis |
| Um módulo por área de serviço | Reduz blast radius |
| Tags obrigatórias em todos os resources | Permite rastrear custo, auditoria e limpeza |
| Secrets apenas no Key Vault | Evita credenciais no código |
| Managed Identity | Evita senhas entre serviços |
| `fmt` e `validate` limpos | Corresponde ao gate da CI |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Aplique `local.common_tags` em todo resource | Entregue resource sem tags |
| Marque secret como `sensitive = true` | Coloque secret em default ou `.tfvars` |
| Fixe imagens Compose por digest | Use `postgres:latest` |
| Autentique por Managed Identity | Incorpore senha em connection string |

## Checklist antes de abrir um PR

- [ ] O provider é `azurerm ~> 3.x` e `required_version` está fixado.
- [ ] Cada resource tem tags `project`, `environment` e `owner`.
- [ ] Secrets aparecem apenas no Key Vault e inputs secretos usam `sensitive`.
- [ ] A autenticação entre serviços usa Managed Identity.
- [ ] `terraform fmt` e `validate` por módulo passam.
- [ ] Compose fixa digests e lê secrets de `.env` ignorado.
