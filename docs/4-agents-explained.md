# The Challenge Stage Agents — Explained

![Concept Type](https://img.shields.io/badge/Type-Concept-171717?style=flat-square)
![Use Understand agent kits](https://img.shields.io/badge/Use-Understand%20agent--kits-737373?style=flat-square)

> **Path:** [Team Kit](../README.md) › [Docs](README.md) › **Challenge Agents Explained**

**Explains why the individual challenge uses stage agents while roles remain auto-loading skills.** Read this when someone asks: "Why do I select a stage agent if I cover every role?"

| Field | Value |
|---|---|
| **Target audience** | Individual workshop participants |
| **Prerequisites** | Skim the persona overview |
| **Expected outcome** | Understand why a phase is an agent and a role is a skill |

---

## Concept

A **role skill** answers: "What responsibility am I applying?" A **stage agent** answers: "How should Copilot behave in this phase?"

Both are necessary and complementary. In the individual challenge, one participant covers all 10 roles, and those role skills load automatically by description. You deliberately select only the current stage agent because each stage has different boundaries, allowed outputs, and definition of done.

> [!NOTE]
> The challenge uses three stage agents — `@archaeologist`, `@architect`, and `@builder` — plus cross-stage `@dba`. `@evolution` remains in the repository for the longer SDLC kit, but it is not used in the individual challenge, which ends at Stage 3 and judge validation. See [ADR-0003](adr/0003-individual-challenge-format.md).

---

## Why there are three challenge stage agents plus `@dba`

| Stage | Working mode | Agent | Primary rule |
|---|---|---|---|
| 1 — Archaeology | Observe and catalog | `@archaeologist` | Do not write code; cite legacy evidence |
| 2 — Specification | Structure and decide | `@architect` | Do not accept a requirement without `source_legacy:` |
| 3 — Implementation and data migration | Build, migrate, and verify | `@builder` | Do not code without a REQ-ID and test path |
| Cross-stage data lifecycle | Discover, map, load, reconcile, recover | `@dba` | Do not replace migrated data with seed data |

Stage 1 is read-only **for legacy inputs** but writes discovery artifacts. Stage 2 writes traceable requirements and design. Stage 3 writes code, migration artifacts, tests, and evidence. Separating these bounds makes the workflow clearer.

---

## Agent anatomy

![Agent anatomy: five layers (Agent + Instructions + Prompts + Skills + MCP)](../assets/agent-anatomy.svg)

| Layer | Purpose | Example |
|---|---|---|
| Agent | Defines mission, tools, and behavior for a phase | `@builder` knows how to implement and test |
| Skill | Carries a role or technique, loaded automatically by description | `persona-qa-engineer`, TDD, ADR, business-rule extraction |
| Instructions | Rules sensitive to file type | Natural/Adabas, Java, frontend |
| Prompts | Reusable actions bound to the agent that owns their moment | `/translate-natural-to-java`, `/write-ears-spec` |
| MCP | Connects the agent to external systems | GitHub, databases, and Azure when configured |

---

## How to use the agents during the challenge

- [ ] **Start with the stage.** Check [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) for the current budget and self-checkpoint.
- [ ] **Select the stage agent in Copilot Chat.** Example: `@architect` in Stage 2.
- [ ] **Use role personas as checklists.** You cover Product Owner through Tech Writer yourself; the role skills compose automatically.
- [ ] **Call on `@dba` for data work.** Use it during discovery, mapping, loading, reconciliation, and rerun/recovery evidence.
- [ ] **Stop at C1, C2, and C3.** Advance only when the self-check definition of done is satisfied.

---

## Interaction flow

During Stage 2, bring a confirmed finding to `@architect` and ask for traceable requirements:

```text
@architect
I confirmed this rule in the legacy sources:
"<confirmed rule>"
Help structure it in EARS with a REQ-ID, acceptance criteria, and source_legacy.
```

The artifact must record only evidence you reviewed:

```yaml
REQ-XXX:
  pattern: <EARS pattern>
  text: "<requirement>"
  source_legacy: <file:lines or [GREENFIELD] + justification>
  acceptance: "<verifiable scenario>"
```

---

## Rule: no supplied exercise answers

Agents guide reading and record participant-reviewed evidence. They do not use a worked solution as a substitute for discovery, and they do not answer or close mysteries without accountable validation. Persona prompts can select the relevant specialist, such as `@dba`, within the current stage's boundaries.

| If you ask... | The agent responds... |
|---|---|
| "Tell me the bounded contexts" | "Show me the program catalog and data map." |
| "Create requirements for everything" | "Let us start with one rule that has a legacy source." |
| "Implement this feature without a specification" | "The REQ-ID, acceptance criterion, and `source_legacy` are missing." |

---

## How to know you understand

You understand the model when you can explain these three statements to someone else:

1. A role skill defines a responsibility and loads itself; a stage agent defines a phase and is selected.
2. The stage agent changes during the challenge; the 10 role responsibilities remain available automatically.
3. Every important artifact must survive outside chat in a version-controlled file.

---

## References

- [Agent kits](../06-stage-agents/README.md)
- [Persona-agent matrix](persona-agent-matrix.md)
- [Challenge flow](../00-TEAM-FLOW.md)
- [Persona kits](../05-personas/README.md)

---

### Continue reading

| Previous | Next |
|---|---|
| [Persona-Agent Matrix](persona-agent-matrix.md)<br/><sub>Role checklist by stage.</sub> | [Challenge Flow](../00-TEAM-FLOW.md)<br/><sub>Schedule and self-checkpoints.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
