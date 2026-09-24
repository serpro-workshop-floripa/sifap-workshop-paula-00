# Registros de decisões arquiteturais (ADRs)

> **Caminho:** [Kit do desafio individual](../../README.md) › [Documentação](../README.md) › **ADRs**

Índice dos registros de decisões arquiteturais — uma decisão por arquivo, numerada sequencialmente.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual, especialmente ao atuar como arquiteto ou Technical Lead |
| **Quando criar** | Para toda decisão difícil de revisitar depois (mais de uma hora para reverter) |
| **Resultado esperado** | Histórico auditável das decisões tomadas sob pressão de tempo |

---

## Por que escrever ADRs

Uma ADR preserva o contexto e as compensações de uma decisão para revisão posterior. Seu valor depende de evidências e clareza; este kit não alega uma proporção medida de tempo de escrita ou redução de retrabalho.

## Quando escrever uma ADR

Escreva uma quando:

- Uma decisão for difícil de revisitar depois (mais de uma hora para reverter).
- Mantenedores razoáveis puderem escolher opções diferentes.
- Uma decisão afetar mais de um contexto delimitado, caminho de migração de dados ou questão de implantação.

Não escreva uma ADR para nomes de variáveis, configuração de formatação ou versões menores de bibliotecas.

---

## Índice

| ADR | Título | Status | Data |
|---|---|---|---|
| 0000 | [Modelo](0000-template.md) | template | 2026-04-29 |
| 0001 | [Fonte única de verdade das instruções dos agentes](0001-agent-instructions-single-source-of-truth.md) | accepted | 2026-08-17 |
| 0002 | [Papéis da equipe como skills, não agentes](0002-team-roles-as-skills-not-agents.md) | accepted | 2026-09-15 |
| 0003 | [Formato de desafio individual](0003-individual-challenge-format.md) | accepted | 2026-09-24 |

> [!NOTE]
> Adicione novas ADRs a esta tabela à medida que forem criadas, primeiro com status `proposed` e depois `accepted` após uma revisão responsável.
> As ADRs 0001-0003 regem a manutenção do kit e o formato do desafio. Elas não são decisões preenchidas do exercício SIFAP nem aprovação da arquitetura de um participante.

---

## Como adicionar uma ADR

- [ ] **Abra uma issue** usando o [modelo de issue de ADR](../../.github/ISSUE_TEMPLATE/adr.yml), se houver tempo.
- [ ] **Copie o modelo** — `0000-template.md` → `NNNN-your-title.md` (próximo número sequencial).
- [ ] **Preencha todas as seções** — contexto, decisão, alternativas, consequências e status.
- [ ] **Vincule-a à especificação, ao plano, à tarefa ou ao PR pertinente.**
- [ ] **Registre o estado real da revisão** neste índice. Uma ADR proposta pode permanecer como rascunho; a aceitação exige revisão responsável.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Documentação transversal](../README.md)<br/><sub>Glossário, migração de dados, STATUS e runbook.</sub> | [Etapa 2 — Especificação moderna](../../02-modern-spec/GUIDE.md)<br/><sub>Escreva EARS, ADRs e artefatos de design.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
