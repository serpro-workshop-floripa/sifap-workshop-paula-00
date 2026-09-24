---
description: "Use ao criar, revisar ou depurar hooks de agentes no GitHub Copilot CLI, cloud agent ou VS Code Local: descriptors, scripts, política, eventos, payloads, decisões e segurança."
applyTo: ".github/hooks/**"
---

# Hooks de agentes — Guia de autoria

Este arquivo define como criar hooks portáveis, seguros e testáveis em `.github/hooks/`. O formato do descriptor e a descoberta de arquivos planos estão no [padrão de primitivos](../PRIMITIVE-STANDARD.md#configuração-de-hooks); não repita essas regras aqui.

## Antes de criar um hook

1. Identifique o harness: Copilot CLI, Agent Host, cloud agent ou VS Code Local. Eventos, payloads e decisões variam.
2. Confirme que o comportamento precisa ser determinístico. Orientações ao modelo pertencem a instructions, skills ou agents.
3. Defina o papel: observar, injetar contexto, modificar ou bloquear. Apenas `preToolUse`, `permissionRequest`, `agentStop` e `subagentStop` tomam decisões.

## Regras de formato

| Regra | Motivo |
|---|---|
| Use `version: 1`, eventos camelCase, `bash`, `powershell`, `cwd: "."` e `timeoutSec` | Formato nativo do Copilot, convertido pelo parser Local |
| Use um script de entrada com um subcomando por evento | Centraliza normalização e política |
| Não deixe outros `*.json` na raiz de `.github/hooks/` | Todo JSON nesse local carrega como hook |
| Use apenas a biblioteca padrão da linguagem escolhida | Evita instalação de dependências |
| Use paths relativos à raiz do repositório | O harness executa com `cwd` na raiz |

## Regras de comportamento

- Normalize payloads Copilot (`toolName`, `toolArgs`, `sessionId`) e Local (`tool_name`, `tool_input`, `session_id`). `toolArgs` pode chegar como string JSON.
- Responda nos dois formatos: campos no nível superior e `hookSpecificOutput` com `hookEventName`.
- Emita exatamente um objeto JSON em stdout.
- Nunca retorne `allow` automático em `preToolUse`; sem finding, não emita decisão.
- Para bloquear, emita JSON `deny`, mensagem em stderr e exit code 2.
- `preToolUse` falha fechado: JSON inválido ou exceção interna resulta em `deny`. Outros eventos falham abertos.
- Termine bem antes de `timeoutSec`; timeout falha aberto no Copilot.
- Limite continuações em `agentStop` e `Stop`.
- Execute comandos como lista argv, sem shell, e valide os inputs.
- Torne mensagens de bloqueio acionáveis: identifique a regra e onde ajustar a política.

## Segurança e privacidade

- Nunca registre prompts, respostas, argumentos brutos, conteúdo de arquivos ou secrets. Audite apenas metadados.
- Nunca coloque credenciais em descriptors, políticas, outputs ou contexto injetado.
- Proteja `.github/hooks/**` contra escrita silenciosa pelo agente.
- Trate regex de comando como alarme, não como fronteira. Combine-a com `tools:` restritos, aprovação no terminal e revisão humana.
- Não leia a transcrição do chat como API estável.

## Testes obrigatórios

Cada mudança em script ou política inclui teste em `.github/hooks/scripts/test_*.py` para passagem sem decisão, `deny`, `ask`, ambos os payloads, JSON inválido e erro.

```bash
python3 -B -m unittest discover -s .github/hooks/scripts -v
```

Valide também em uma sessão real do harness-alvo. `python3 .github/scripts/verify-hooks-loaded.py` verifica as pré-condições estáticas.

## Convenções

| Regra | Motivo |
|---|---|
| Centralize a política em `.github/hooks/config/policy.json` | Mantém um único ponto de revisão |
| Use um script de entrada por família de hooks | Escreve a normalização uma vez |
| Falhe fechado apenas em `preToolUse` | Bloquear outros eventos quebra sessões sem aumentar a segurança |
| Registre apenas metadados | Impede exfiltração de dados pelos hooks |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Centralize regras em `config/policy.json` | Espalhe regras por vários scripts |
| Teste cada regra com um caso que falha sem ela | Confie apenas na leitura do código |
| Documente diferenças entre harnesses | Suponha que um evento exista em todos |
| Use hooks por agente apenas no Local, sabendo que estão em preview | Espere que hooks por agente rodem no Copilot CLI |

## Checklist antes de abrir um PR

- [ ] O evento existe no harness-alvo e o schema foi conferido na referência oficial.
- [ ] O descriptor usa o formato padrão e aponta para um único script de entrada.
- [ ] `preToolUse` ainda falha fechado e nunca retorna `allow` automático.
- [ ] Nenhum dado sensível é registrado ou injetado.
- [ ] O tempo de execução fica bem abaixo de `timeoutSec`.
- [ ] Os testes passam e `policy.json` concorda com os defaults do script.

## Referências

- [Configurar hooks de agentes no VS Code](https://code.visualstudio.com/docs/agent-customization/hooks)
- [Referência de hooks Local no VS Code](https://code.visualstudio.com/docs/agents/reference/hooks-reference)
- [Referência de hooks do GitHub Copilot](https://docs.github.com/en/copilot/reference/hooks-reference)
