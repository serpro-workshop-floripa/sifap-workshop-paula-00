---
description: "Valida se a branch atual segue as convenções de nomenclatura de branches de funcionalidade"
---

# Validar branch de funcionalidade

Valide se a branch Git atual segue as convenções esperadas de nomenclatura de branches de funcionalidade.

## Pré-requisitos

- Verifique se o Git está disponível executando `git rev-parse --is-inside-work-tree 2>/dev/null`
- Se o Git não estiver disponível, exiba um aviso e ignore a validação:
  ```
  [specify] Warning: Git repository not detected; skipped branch validation
  ```

## Regras de validação

Obtenha o nome da branch atual:

```bash
git rev-parse --abbrev-ref HEAD
```

O nome da branch deve corresponder a um destes padrões:

1. **Sequencial**: `^[0-9]{3,}-` (por exemplo, `001-feature-name`, `042-fix-bug`, `1000-big-feature`)
2. **Timestamp**: `^[0-9]{8}-[0-9]{6}-` (por exemplo, `20260319-143022-feature-name`)

## Execução

Se estiver em uma branch de funcionalidade (corresponder a qualquer um dos padrões):
- Saída: `✓ On feature branch: <branch-name>`
- Verifique se o diretório de especificação correspondente existe em `specs/`:
  - Para branches sequenciais, procure `specs/<prefix>-*`, em que o prefixo corresponde à parte numérica
  - Para branches com timestamp, procure `specs/<prefix>-*`, em que o prefixo corresponde à parte `YYYYMMDD-HHMMSS`
- Se o diretório de especificação existir: `✓ Spec directory found: <path>`
- Se o diretório de especificação estiver ausente: `⚠ No spec directory found for prefix <prefix>`

Se NÃO estiver em uma branch de funcionalidade:
- Saída: `✗ Not on a feature branch. Current branch: <branch-name>`
- Saída: `Feature branches should be named like: 001-feature-name or 20260319-143022-feature-name`

## Degradação controlada

Se o Git não estiver instalado ou o diretório não for um repositório Git:
- Verifique a variável de ambiente `SPECIFY_FEATURE` como alternativa
- Se estiver definida, valide o valor em relação aos padrões de nomenclatura
- Se não estiver definida, ignore a validação com um aviso
