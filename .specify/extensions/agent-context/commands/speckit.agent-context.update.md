---
description: "Atualiza a seção gerenciada do Spec Kit no arquivo de contexto do agente de codificação"
---

# Atualizar contexto do agente de codificação

Atualize a seção gerenciada do Spec Kit no arquivo de contexto/instruções do agente de codificação ativo (por exemplo, `CLAUDE.md`, `.github/copilot-instructions.md`, `AGENTS.md`).

## Comportamento

O script lê a configuração da extensão agent-context em
`.specify/extensions/agent-context/agent-context-config.yml` para identificar:

- `context_file` — o caminho do arquivo de contexto do agente de codificação a ser gerenciado.
- `context_markers.start` / `.end` — os delimitadores que envolvem a seção gerenciada. Os padrões são `<!-- SPECKIT START -->` e `<!-- SPECKIT END -->` quando o campo está ausente.

Em seguida, ele cria, substitui ou acrescenta o bloco gerenciado para que a seção aponte para o caminho do plano mais recente quando for possível identificá-lo (`specs/<feature>/plan.md`).

Se `context_file` estiver vazio ou o arquivo não puder ser localizado, o comando informa que não há nada a fazer e termina com sucesso.

## Execução

- **Bash**: `.specify/extensions/agent-context/scripts/bash/update-agent-context.sh [plan_path]`
- **PowerShell**: `.specify/extensions/agent-context/scripts/powershell/update-agent-context.ps1 [plan_path]`

Quando `plan_path` é omitido, o script detecta automaticamente o arquivo `specs/*/plan.md` modificado mais recentemente.
