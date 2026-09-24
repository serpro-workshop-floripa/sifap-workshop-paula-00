---
description: "Use ao criar, editar ou revisar pacotes de Spec-Driven Development em .spec/ ou a constituição do Spec-Kit, incluindo EARS, rastreabilidade e status."
applyTo: ".spec/**,.specify/memory/**"
---

# Artefatos de Spec-Driven Development — Guia

Este arquivo define layouts e contratos em `.spec/`. A skill [sdd-requirements-engineer](../skills/sdd-requirements-engineer/SKILL.md) define o procedimento e os templates. O agente `@architect`, scripts em `.github/scripts/` e [spec-quality.yml](../workflows/spec-quality.yml) produzem e validam os arquivos.

## Escolha um workflow por pacote

| | Workflow architect | Workflow Spec-Kit |
|---|---|---|
| Conduzido por | Prompts `@architect` e skill SDD | Comandos `/speckit.*` |
| Pasta | `.spec/<NNN>-<feature>/` | `.spec/<NNN>-<feature>/` |
| Arquivos | Pacote uppercase | `spec.md`, `plan.md`, `tasks.md` e derivados |
| Detectado por | `SPECIFICATION.md` | `spec.md` |

Registre a escolha em `02-modern-spec/scope-decisions.md`. Um pacote com os dois arquivos falha.

## Layout do pacote architect

```text
.spec/
├── CONSTITUTION.md
└── <NNN>-<feature>/
    ├── checkpoints/
    ├── contracts/
    ├── evidence/
    ├── ANALYSIS.md
    ├── DECISIONS.md
    ├── DESIGN.md
    ├── FRD.md
    ├── NFRD.md
    ├── SPECIFICATION.md
    ├── TASKS.md
    ├── TDD.md
    └── TESTING.md
```

Crie o pacote com `python3 .github/scripts/export-spec-library.py --new-package <NNN>-<feature>`. Gere derivados com `python3 .github/scripts/generate-sdd-support-artifacts.py --package <NNN> --include-supplements`; não os edite manualmente.

## Completude

- Cada arquivo autoral contém todas as seções H2 do template, na ordem.
- Use `NOT APPLICABLE: <reason>` quando não se aplicar.
- Use `PENDING` ou `BLOCKED` com owner para desconhecidos.
- Nunca invente atores, regras, diagramas, decisões ou aprovações para preencher seções.

## Registros de requisitos

`SPECIFICATION.md` é o único local de declarações normativas.

```markdown
- **REQ-001:** When <trigger>, the <system> shall <one observable response>.
  source_legacy: 01-archaeology/legacy-sifap/natural-programs/<MEMBER>.NSN#L<start>-L<end>
  - Acceptance: AC-REQ-001-01 Given <state>, When <trigger>, Then <outcome>.
  - Verification: TST-001
```

- `REQ-NNN` é funcional e `NFR-NNN` não funcional; ambos são exclusivos.
- Use um padrão EARS e exatamente um `shall` por registro.
- `source_legacy:` fica próximo da declaração, sem backticks, e cita path real com linhas válidas ou `[GREENFIELD] <justification>`.
- Fora de `SPECIFICATION.md`, cite IDs no meio de frases ou células.
- Cada ID ativo aparece em requisitos, design, tasks, testes e checkpoints; testes o citam em comentário.

## Tasks, testes e evidências

- Use uma checkbox por task com ID, fase RED/GREEN, plan e rastreabilidade.
- RED precede GREEN.
- Uma task só é concluída com `Evidence:` e entrada no ledger.
- `TESTING.md` declara cada `TST-NNN`; `test-coverage.yaml` mapeia requisitos.
- Status nunca excede evidência. `Implemented` exige tasks concluídas; `Verified` também exige testes.

## Pacotes Spec-Kit

Os templates em `.specify/templates/` controlam arquivos lowercase. Mova a saída `specs/` para `.spec/` com `git mv` e atualize `.specify/feature.json`. As regras compartilhadas de requisitos, fontes, TDD, status e Mermaid continuam válidas.

## Gates executáveis

| Comando | O que comprova |
|---|---|
| `python3 .github/scripts/validate-specs.py [--package NNN] [--strict]` | Executa todos os gates |
| `validate-spec-artifacts.py` | Layout, seções e placeholders |
| `validate-sdd-documents.py` | EARS, fontes e cobertura entre arquivos |
| `validate-task-graph.py` | Tasks, dependências, ciclos e RED/GREEN |
| `validate-spec-status.py` | Status coerente com evidências |
| `validate-test-bindings.py` | Testes citam requisitos |
| `generate-sdd-support-artifacts.py --include-supplements --check` | Derivados atualizados |

Gates textuais não comprovam significado EARS, aprovação humana, renderização ou equivalência comportamental.

## Convenções

| Regra | Motivo |
|---|---|
| Pacotes em `.spec/<NNN>-<kebab-slug>/` | Mantém referências estáveis |
| Um workflow por pacote | Gates dependem de um layout |
| Arquivos derivados são regenerados | Evita drift |
| IDs estáveis | Preserva referências entre arquivos |
| Evidências datadas e sem dados sensíveis | Protege informações reguladas |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Crie o pacote pelo script e preencha seções | Deixe placeholders |
| Mantenha EARS apenas em `SPECIFICATION.md` | Duplique declarações normativas |
| Regenere derivados após mudanças | Edite arquivos gerados |
| Use `NOT APPLICABLE: <reason>` | Exclua seção inaplicável |
| Relate gates falhando | Simule aprovação ou conclusão |

## Checklist antes de abrir um PR

- [ ] O pacote usa um workflow e contém os arquivos exigidos.
- [ ] Cada seção tem conteúdo ou `NOT APPLICABLE`.
- [ ] Cada requisito tem EARS, `source_legacy:` e acceptance ID.
- [ ] RED precede GREEN e tasks concluídas têm evidências.
- [ ] Arquivos gerados estão atualizados.
- [ ] `python3 .github/scripts/validate-specs.py --package <NNN> --strict` passa ou as falhas estão no PR.
