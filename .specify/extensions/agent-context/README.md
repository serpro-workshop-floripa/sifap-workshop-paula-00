# Extensão de contexto do agente de codificação

Esta extensão incluída gerencia o **arquivo de contexto/instruções do agente de codificação** (por exemplo, `CLAUDE.md`, `.github/copilot-instructions.md`, `AGENTS.md`, `GEMINI.md`, …) para a integração ativa.

Ela controla o ciclo de vida da seção gerenciada delimitada pelos marcadores configuráveis de início/fim (padrões: `<!-- SPECKIT START -->` / `<!-- SPECKIT END -->`).

## Por que uma extensão?

Nem todo usuário do Spec Kit deseja que o Spec Kit escreva no arquivo de contexto do agente de codificação. Extrair esse comportamento para uma extensão dedicada permite:

- **Desativar** completamente com `specify extension disable agent-context` — assim, o Spec Kit nunca criará nem modificará o arquivo de contexto do agente.
- **Personalizar os marcadores** editando `.specify/extensions/agent-context/agent-context-config.yml` — tanto a camada Python quanto os scripts incluídos respeitam o mesmo valor de `context_markers`.
- **Atualizar sob demanda** com `/speckit.agent-context.update` ou automaticamente por meio dos hooks declarados em `extension.yml` (`after_specify`, `after_plan`).

## Comandos

| Comando | Descrição |
|---------|-------------|
| `speckit.agent-context.update` | Atualiza a seção gerenciada no arquivo de contexto do agente com o caminho do plano atual. |

## Configuração

Toda a configuração passa pelo arquivo de configuração da própria extensão em
`.specify/extensions/agent-context/agent-context-config.yml`:

```yaml
# Caminho do arquivo de contexto do agente de codificação gerenciado por esta extensão
context_file: CLAUDE.md

# Delimitadores da seção gerenciada do Spec Kit
context_markers:
  start: "<!-- SPECKIT START -->"
  end: "<!-- SPECKIT END -->"
```

- `context_file` — o caminho relativo ao projeto do arquivo de contexto do agente de codificação, gravado por `specify init` e `specify integration install`.
- `context_markers.start` / `.end` — os delimitadores ao redor da seção gerenciada. Edite-os para usar marcadores personalizados.

## Requisitos

Os scripts de atualização incluídos exigem **Python 3** com **PyYAML** para o processamento de YAML/upsert (o PowerShell também pode usar `ConvertFrom-Yaml` quando disponível).

O PyYAML acompanha a CLI `specify` e normalmente está disponível pelo mesmo interpretador `python3`. Se um hook informar *"PyYAML is required … not available in the current Python environment"*, isso significa que o `python3` do sistema é diferente daquele usado para instalar o Spec Kit. Para resolver, execute:

```bash
pip install pyyaml
# ou use o interpretador específico utilizado pelo Spec Kit:
/path/to/speckit-python -m pip install pyyaml
```

## Desativação

```bash
specify extension disable agent-context
```

Quando desativado, o Spec Kit ignora a criação, atualização e remoção do arquivo de contexto (os gates ficam em `upsert_context_section()` e `remove_context_section()`).
