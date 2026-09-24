---
description: "Use when creating, reviewing, or debugging agent hooks (GitHub Copilot CLI, cloud agent, VS Code Local): descriptors in .github/hooks/*.json, hook scripts, policy, events, payloads, decisions, and security."
applyTo: ".github/hooks/**"
---

# Agent Hooks — Authoring Guide

This file opens when you edit anything under `.github/hooks/`. It defines how to build portable, safe, and testable hooks. The descriptor shape and the flat-file discovery rule are in the [primitive standard](../PRIMITIVE-STANDARD.md#hook-configuration); do not repeat them here.

## Before Creating a Hook

1. Identify the target harness: Copilot (CLI, Agent Host, cloud agent) or VS Code Local. Events, payloads, and decisions differ.
2. Confirm the behavior must be **deterministic**. Guidance for the model belongs in instructions, skills, or agents, not in a hook.
3. Decide the role: observe, inject context, modify, or block. Only `preToolUse`, `permissionRequest`, `agentStop`, and `subagentStop` make decisions.

## Format Rules

| Rule | Rationale |
|---|---|
| Descriptors use `version: 1`, camelCase events, `bash` and `powershell`, `cwd: "."`, and `timeoutSec` | Native Copilot format, converted by the Local parser |
| One entry script with one subcommand per event | Shared normalization and policy, no diverging scripts |
| No `*.json` other than descriptors at the root of `.github/hooks/` | Every JSON file there loads as a hook; configuration goes in `config/` |
| Scripts use only the chosen language's standard library | Works in any project without installing dependencies |
| Paths are relative to the repository root | The harness runs with `cwd` at the root |

## Behavior Rules

- **Normalize both payloads:** `toolName`/`toolArgs`/`sessionId` (Copilot) and `tool_name`/`tool_input`/`session_id` (Local). `toolArgs` may arrive as a JSON string.
- **Answer in both formats:** top-level fields (`permissionDecision`, `additionalContext`, `decision`) and `hookSpecificOutput` with `hookEventName`.
- **Emit exactly one JSON object** on stdout. Two concatenated objects are invalid JSON and are ignored.
- **Never return an automatic `allow`** from `preToolUse`; with no finding, emit no decision so normal confirmations remain.
- **Block with a `deny` JSON, a stderr message, and exit code 2.** That blocks in both Copilot and Local.
- **`preToolUse` fails closed:** invalid JSON or an internal exception results in `deny`. Other events fail open with a stderr message.
- **Finish well before `timeoutSec`.** A timeout fails open in Copilot; a slow hook protects nothing.
- **Bound continuations** in `agentStop`/`Stop`: count blocks and release after a maximum; every continuation costs credits.
- **Run commands as an argv list**, without a shell, and validate inputs before using them.
- **Make block messages actionable:** name the rule that fired and where to adjust the policy.

## Security and Privacy

- Never log prompts, responses, raw arguments, file contents, or secrets. Audit metadata only (event, tool, result, rule).
- Never place credentials in descriptors, policy, output, or injected context.
- Protect `.github/hooks/**` against silent writes by the agent.
- A command regex is an alarm, not a boundary: combine it with restricted `tools:`, terminal approval, and human review.
- Do not read the chat transcript as a stable API; its format changes across versions and harnesses.

## Required Tests

Every script or policy change ships with a test in `.github/hooks/scripts/test_*.py` covering at least: pass-through without a decision, `deny`, `ask`, both payload formats, invalid JSON, and the error path. Run:

```bash
python3 -B -m unittest discover -s .github/hooks/scripts -v
```

Then validate in a real session of the target harness (Chat: Configure Hooks and the hooks output channel in VS Code; a CLI restart in Copilot CLI). `python3 .github/scripts/verify-hooks-loaded.py` checks the static preconditions.

## Conventions

| Rule | Rationale |
|---|---|
| Centralize policy in `.github/hooks/config/policy.json` | One place to review and change a rule |
| One entry script per harness-neutral hook family | Normalization is written once |
| Fail closed only in `preToolUse` | Blocking elsewhere breaks sessions without adding safety |
| Metadata-only audit logs | Hooks never become a data-exfiltration path |

## Do / Do Not

| Do | Do not |
|---|---|
| Centralize the policy in `config/policy.json` | Spread rules across several scripts |
| Test each new rule with a case that fails without it | Rely on reading the code |
| Document harness differences next to the hook | Assume an event exists in every harness |
| Use per-agent hooks (`hooks:` in `.agent.md`) only in Local, knowing they are in preview | Expect per-agent hooks to run in Copilot CLI |

## Checklist Before Opening a PR

- [ ] The event exists in the target harness and its input/output schema was checked against the official reference.
- [ ] The descriptor uses the standard format and points to the single entry script.
- [ ] `preToolUse` still fails closed and never returns an automatic `allow`.
- [ ] No sensitive data is logged or injected.
- [ ] Execution time stays well below `timeoutSec`.
- [ ] Tests cover the change and pass; `policy.json` and the script defaults agree.

## References

- [Configure agent hooks in VS Code](https://code.visualstudio.com/docs/agent-customization/hooks)
- [Local hooks reference (VS Code)](https://code.visualstudio.com/docs/agents/reference/hooks-reference)
- [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference)
