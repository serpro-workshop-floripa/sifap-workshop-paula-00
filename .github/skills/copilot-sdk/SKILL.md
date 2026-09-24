---
name: "copilot-sdk"
description: "Build agentic applications with GitHub Copilot SDK. Use when embedding agents, creating custom tools, streaming responses, managing sessions, connecting MCP servers, or creating custom agents. Verify the installed SDK version, user-controlled model configuration, scoped permissions, and cleanup before generating code."
---
# GitHub Copilot SDK

Use the official SDK to embed Copilot workflows in an explicitly requested
application or tool extension. This is not required to use the workshop's
VS Code stage agents, and does not provide a ready-made SIFAP implementation.

## When to invoke

- "Embed a Copilot agent in our app with the SDK."
- "Add a custom tool with a bounded permission policy."
- "Stream an agent response in the application."
- "Connect an approved MCP server and persist sessions safely."

## Scope and prerequisites

- Inspect the requested application, language, installed SDK/CLI versions and
  existing tests before proposing code. Do not assume an application exists.
- The SDK uses the Copilot CLI. Confirm its availability and authentication;
  never copy credentials into application code, prompts, or logs.
- Check runtime/package compatibility in the selected SDK release. Do not
  treat an old tutorial's runtime minimum as current support evidence.
- Follow the kit's approved stack for SIFAP work. A separate tool extension
  needs its own approved scope and dependency decision.
- Keep `01-archaeology/legacy-sifap/**` read-only. Do not attach raw source data,
  production records, secrets, or unrelated workspace files to a session.

## Version-grounded implementation

Use the installed types and official release documentation as the API contract.
Method signatures, event shapes, transport configuration, permission callbacks,
and session persistence can change. Do not copy snippets from another language
binding or version and claim they compile.

| Area | What to establish before implementation |
|---|---|
| Client | CLI lifecycle, transport, authentication context and ownership |
| Session | User-controlled model ID, system instructions, permitted tools and cancellation |
| Streaming | Actual event names, final/idle/error handling and listener cleanup |
| Custom tools | Typed schema, input validation, authorization and explicit failures |
| MCP | Approved server identity, transport, allowed tools and connectivity |
| Custom agents | Actual configuration schema and inherited permission boundaries |
| Persistence | Authorized session IDs, tenant/user isolation, retention and deletion |
| Shutdown | Cleanup after success, failure, cancellation and session-creation failure |

## Permission and data boundaries

Never use blanket `approveAll` as the application's default policy.
Implement a reviewed permission callback matching the installed SDK:

1. Define the operations and paths the task may access.
2. Validate each request against that boundary and its authenticated owner.
3. Deny requests outside it; require explicit human approval when policy calls
   for it. A model-generated justification is not authorization.
4. Preserve denials, failures and cancellations as distinct outcomes.
5. Record sanitized audit metadata, not secrets or raw request/file contents.

Custom tools also enforce authorization internally. A permission callback is
not a substitute for validating tool arguments, database queries or external
service access.

Attachments require explicit approval and data classification. Use only
authorized synthetic or sanitized material. A generic filename such as a CSV
does not establish permission to read or transmit it.

## Models and configuration

Resolve the model identifier, endpoints, MCP configuration and runtime options
from user-controlled configuration. Verify availability under the actual account
and policy; do not hard-code a provider/model or silently fall back to another.
Missing or invalid configuration is an explicit setup error.

Keep secrets server-side and out of public frontend configuration. Do not log
model requests or responses wholesale when they may contain sensitive data.

## Client and session lifecycle

For the selected SDK binding:

1. Validate configuration before starting a client.
2. Establish cleanup around both client startup and session creation.
3. Create the session with the reviewed permission policy and selected tools.
4. Register only the listeners needed for the requested interaction.
5. Send the request using an explicit timeout/cancellation policy.
6. Handle final response, errors, denials, cancellation and missing response
   distinctly. Do not print an empty value and call it success.
7. Unsubscribe listeners and stop/dispose owned sessions and the client on
   every path, including startup or session-creation failure.

Use `try/finally`, `defer`, or the binding's actual disposal support. Do not
invent an API or assume process shutdown will clean up background work.

## Tools, streaming and multi-turn work

- Build tool schemas from the actual task boundary, not model-invented input
  shapes. Return typed results and explicit failures.
- Keep streaming deltas separate from the final response; an idle signal does
  not prove the requested operation succeeded.
- Reuse sessions only within the authorized user/task boundary. Resuming a
  session must not cross users or tenants.
- Test cancellation, timeouts, rejected permissions and tool failures as well
  as the happy path.
- For MCP connections, test the actual permitted tool subset. Do not expose
  every server tool or assume an integration exists because it is named.

## Output template

Generate the requested implementation and its tests, then report:

```markdown
## Copilot SDK integration - <approved task>
| Concern | Actual configuration or evidence |
|---|---|
| Language / SDK / CLI / runtime | <verified versions> |
| Model configuration | <user-selected identifier and availability> |
| Permission boundary | <approved operations/paths; denial behavior> |
| Tools / MCP | <actual schemas, authorization and configured endpoints, without secrets> |
| Attachments / persistence | <approved data, isolation and retention> |
| Streaming / errors / cancellation | <implemented behavior and tests> |
| Cleanup | <verified success/failure/startup cleanup> |
| Verification | <actual commands and results, or not run> |
```

No model output, successful test, permission grant, or runtime result is
prefilled. A code sketch is not a verified integration.

## Quality gate

- [ ] The selected SDK/CLI/runtime contract was inspected before generating code.
- [ ] Models and endpoints remain user configuration; no blanket permission approval is installed.
- [ ] Tool and attachment access is explicitly authorized, validated and bounded.
- [ ] Errors, missing responses, denials and cancellation are not swallowed.
- [ ] Session isolation, listener cleanup and client disposal work on failure paths.
- [ ] Tests cover the requested behavior and boundaries using the existing toolchain.
- [ ] Actual end-to-end evidence is recorded before declaring the integration complete.

## References

- [Official SDK repository and releases](https://github.com/github/copilot-sdk)
- [First application tutorial](https://github.com/github/copilot-sdk/blob/main/docs/tutorials/first-app.md)
- [Official examples](https://github.com/github/copilot-sdk/tree/main/samples)
- [GitHub MCP server](https://github.com/github/github-mcp-server)
- [Kit primitive standard](../../PRIMITIVE-STANDARD.md)
