---
description: "Use para higiene genérica do Terraform: organização de arquivos, variáveis, outputs, formatação, validação, testes e state. As regras Azure do kit estão em infrastructure.instructions.md."
applyTo: "**/*.tf"
---

# Convenções do Terraform — Higiene geral

Este arquivo complementa as regras oficiais de infraestrutura do kit. **[`infrastructure.instructions.md`](infrastructure.instructions.md) é a fonte autoritativa** para `azurerm ~> 3.x`, `required_version`, tags obrigatórias, secrets, módulos Azure, Managed Identity e gates `terraform fmt` + `terraform validate`. Em caso de diferença, siga o arquivo de infraestrutura. A equipe cria `infra/` nas Etapas 3/4; não existe stack herdada.

## Organização de arquivos

Separe cada módulo por função:

- `main.tf`: resources.
- `variables.tf`: inputs tipados.
- `outputs.tf`: outputs.
- `locals.tf`: valores calculados e expressões repetidas.
- `terraform.tf`: bloco `terraform {}` e requisitos de providers.

Use `snake_case` em variáveis, locals, outputs e nomes de módulos.

## Variáveis e outputs

- Declare `type` e `description` explícitos em cada variável e output.
- Defina defaults apenas para inputs realmente opcionais; nunca defina default para um secret.
- Marque inputs e outputs com secrets como `sensitive = true`. Evite expor secrets em outputs.
- Exponha apenas os valores necessários para outro módulo ou caller.

## Locals e data sources

- Mova expressões repetidas para `locals`, como o mapa `common_tags`.
- Use data sources para ler resources existentes em vez de fixar IDs.
- Referencie diretamente resources criados na mesma configuração.

## Idempotência

Escreva configurações convergentes. Um segundo `terraform apply`, sem mudança de input, deve informar zero alterações. Evite efeitos colaterais de `local-exec` e `null_resource` que se repetem em cada apply.

## Formatação, validação e testes

- Execute `terraform fmt -recursive` e `terraform validate` por módulo antes de cada commit.
- Execute `tflint` para detectar problemas específicos do provider.
- Escreva testes de módulo com `*.tftest.hcl`, cobrindo um caso positivo e um negativo.

## State

Armazene o state em backend remoto no Azure Storage com locking. Nunca versione `*.tfstate`. Trate o state e os módulos obtidos em `.terraform/` como somente leitura; faça alterações por HCL e Terraform CLI.

## Convenções

| Regra | Motivo |
|---|---|
| Uma responsabilidade por arquivo | Mantém os módulos navegáveis |
| Nomes `snake_case`, tipos e descrições explícitos | Produz HCL consistente e autodocumentado |
| `sensitive = true` para secrets | Evita exposição em plans e outputs |
| `fmt`, `validate` por módulo e `tflint` limpos | Corresponde ao gate de infraestrutura |
| State remoto e nunca versionado | Evita conflitos e vazamento de state |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Siga `infrastructure.instructions.md` para Azure | Reinvente as regras Azure do kit |
| Fixe versões, com baseline `azurerm ~> 3.x` | Use providers em `latest` |
| Mantenha o state remoto e somente leitura | Versione ou edite `*.tfstate` manualmente |
| Cubra módulos com testes `*.tftest.hcl` | Entregue módulos sem testes |

## Checklist antes de abrir um PR

- [ ] Os arquivos estão separados por função e os nomes usam `snake_case`.
- [ ] Cada variável e output tem `type` e `description`; secrets usam `sensitive`.
- [ ] `terraform fmt -recursive`, `validate` por módulo e `tflint` passam localmente.
- [ ] As versões dos providers estão fixadas no baseline do kit.
- [ ] O state permanece no backend remoto e nenhum `*.tfstate` está versionado.
