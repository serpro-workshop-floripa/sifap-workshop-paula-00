---
agent: speckit.git.validate
---
# Validar branch de feature

Valida se a branch Git atual segue as convenções esperadas de nomenclatura de branches de feature.

## Objetivo

Confirmar que a branch atual e o diretório de especificação correspondente usam um prefixo sequencial ou de timestamp válido.

## Quando invocar

- Antes de executar um fluxo que exija uma branch de feature válida.
- Quando for necessário verificar a associação entre a branch atual e um diretório em `specs/`.

## Pré-condições

- Verifique se o Git está disponível executando `git rev-parse --is-inside-work-tree 2>/dev/null`.
- Se o Git não estiver disponível, produza um aviso e ignore a validação:

  ```
  [specify] Warning: Git repository not detected; skipped branch validation
  ```

## Entradas que a equipe deve fornecer

- Nenhuma entrada obrigatória quando a branch Git atual estiver disponível.
- Como fallback, a variável de ambiente `SPECIFY_FEATURE`.

## O que farei

1. Obterei o nome da branch atual.
2. Validarei o nome com os padrões sequencial e de timestamp.
3. Procurarei o diretório correspondente em `specs/`.
4. Usarei `SPECIFY_FEATURE` como fallback quando não houver um repositório Git.

## O que NÃO farei

- Não alterarei o nome da branch atual.
- Não criarei um diretório de especificação ausente.
- Não falharei quando o Git estiver indisponível e `SPECIFY_FEATURE` não estiver definido.

## Formato de saída

- Branch válida: `✓ On feature branch: <branch-name>`.
- Diretório encontrado: `✓ Spec directory found: <path>`.
- Diretório ausente: `⚠ No spec directory found for prefix <prefix>`.
- Branch inválida: `✗ Not on a feature branch. Current branch: <branch-name>`.
- Orientação de nomenclatura: `Feature branches should be named like: 001-feature-name or 20260319-143022-feature-name`.

## Definição de pronto

- [ ] O nome da branch atual ou `SPECIFY_FEATURE` foi avaliado.
- [ ] Os padrões sequencial e de timestamp foram aplicados sem alteração.
- [ ] O diretório correspondente em `specs/` foi verificado quando aplicável.
- [ ] O resultado apropriado foi apresentado sem alterar o repositório.

## Corpo do prompt

Obtenha o nome da branch atual:

```bash
git rev-parse --abbrev-ref HEAD
```

O nome da branch deve corresponder a um destes padrões:

1. **Sequencial**: `^[0-9]{3,}-`, como `001-feature-name`, `042-fix-bug` ou `1000-big-feature`.
2. **Timestamp**: `^[0-9]{8}-[0-9]{6}-`, como `20260319-143022-feature-name`.

Se estiver em uma branch de feature que corresponda a um dos padrões, produza `✓ On feature branch: <branch-name>` e verifique se o diretório de especificação correspondente existe em `specs/`:

- Para branches sequenciais, procure `specs/<prefix>-*`, em que o prefixo corresponda à parte numérica.
- Para branches de timestamp, procure `specs/<prefix>-*`, em que o prefixo corresponda à parte `YYYYMMDD-HHMMSS`.
- Se o diretório existir, produza `✓ Spec directory found: <path>`.
- Se o diretório não existir, produza `⚠ No spec directory found for prefix <prefix>`.

Se não estiver em uma branch de feature, produza `✗ Not on a feature branch. Current branch: <branch-name>` e `Feature branches should be named like: 001-feature-name or 20260319-143022-feature-name`.

Se o Git não estiver instalado ou o diretório não for um repositório Git, consulte a variável de ambiente `SPECIFY_FEATURE` como fallback. Se ela estiver definida, valide seu valor com os padrões de nomenclatura. Caso contrário, ignore a validação com um aviso.

## Exemplo de invocação

Valide a branch de feature atual e verifique se o diretório correspondente existe em `specs/`.
