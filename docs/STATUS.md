# STATUS do desafio — painel de progresso

> **Caminho:** [Kit do desafio individual](../README.md) › [Documentação](README.md) › **STATUS**

Use este modelo de uma página para acompanhar seu progresso, checkpoints de autoverificação, evidências e bloqueios durante o desafio individual das 14:00 às 17:40.

![Painel](https://img.shields.io/badge/Dashboard-Challenge%20status-171717?style=flat-square) ![Atualização](https://img.shields.io/badge/Update-at%20C1%2FC2%2FC3-737373?style=flat-square) ![Responsável](https://img.shields.io/badge/Owner-Participant-A3A3A3?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual |
| **Frequência de atualização** | Em C1, C2, C3 e sempre que houver bloqueio |
| **Resultado esperado** | Registro claro do que está pronto, em andamento, bloqueado e submetido |

---

## Status geral

| Indicador | Status | Observações |
|---|---|---|
| Ferramentas do laptop validadas | — | Git, gh, VS Code, Copilot, Java, Node, pnpm, Docker, Spec-Kit |
| `develop` pronta | — | A branch existe e pode receber PRs |
| Agentes de etapa disponíveis | — | `@archaeologist`, `@architect`, `@builder`, `@dba` |
| Prontidão da fonte Adabas verificada | — | Fonte populada autorizada e rota de extração |
| CI verde no PR de submissão | — | Incluir `legacy-traceability` e jobs de teste |
| População do PostgreSQL reconciliada | — | Contagem da origem = carregados + rejeições explicadas |
| Consulta completa de beneficiários verificada | — | Listagem, pesquisa e detalhes em toda a população migrada |

---

## Progresso ao longo do desafio

| Etapa | Status | Agente | Orçamento de tempo | Autoverificação concluída? | Observações |
|---|---|---|---|---|---|
| **Etapa 1 — Arqueologia** | Não iniciada | `@archaeologist` + `@dba` | 14:00-14:50 | Não | — |
| **C1 — Autoverificação da descoberta** | Não iniciada | Participante | antes da Etapa 2 | Não | — |
| **Etapa 2 — Especificação** | Não iniciada | `@architect` + `@dba` | 14:50-15:30 | Não | — |
| **C2 — Autoverificação da especificação** | Não iniciada | Participante | antes da Etapa 3 | Não | — |
| **Etapa 3 — Implementação e migração** | Não iniciada | `@builder` + `@dba` | 15:30-17:10 | Não | — |
| **C3 — PR de submissão** | Não iniciada | Participante | até 17:10 | Não | — |
| **Validação do juiz** | Aguardando | Juiz | 17:10-17:40 | Não | — |

**Legenda de status:** Não iniciada · Em andamento · Concluída · Atrasada · Bloqueada · Submetida · Aceita · Rejeitada

---

## Registro dos checkpoints de autoverificação

### C1 — fim da Etapa 1

| Verificação | Status | Evidências / observações |
|---|---|---|
| Programas/DDMs legados da capacidade-alvo lidos | — | — |
| Regras de negócio citadas com evidências de arquivo e linha | — | — |
| Questões de dados, população da fonte e bloqueios de extração registrados | — | — |
| Pronto para escrever requisitos na Etapa 2 | — | — |

### C2 — fim da Etapa 2

| Verificação | Status | Evidências / observações |
|---|---|---|
| `spec/<NNN>-<feature>` criada a partir de `develop` | — | — |
| Todo requisito tem REQ-ID, EARS e `source_legacy:` | — | — |
| Plano, tarefas, ADRs e design de migração são rastreáveis | — | — |
| Testes planejados antes das tarefas de implementação | — | — |
| Pronto para implementar na Etapa 3 | — | — |

### C3 — prontidão para submissão

| Verificação | Status | Evidências / observações |
|---|---|---|
| `impl/<NNN>-<feature>` criada a partir de `develop` | — | — |
| O `mvn verify` do backend passa | — | — |
| Os testes do frontend passam, se um frontend foi construído | — | — |
| Contagem da fonte de dados = carregados + rejeições explicadas | — | — |
| Chaves de origem e agregados acordados reconciliam | — | — |
| A nova execução termina sem duplicidades | — | — |
| A listagem abrange a população completa de beneficiários migrados | — | — |
| A pesquisa abrange a população completa de beneficiários migrados | — | — |
| Os detalhes abrangem beneficiários migrados de toda a população | — | — |
| PR de submissão aberto: `impl/<NNN>-<feature>` -> `develop` | — | — |

---

## Métricas

| Métrica | Meta | Atual |
|---|---|---|
| Requisitos respaldados pelo legado | Todo REQ-ID | — |
| Requisitos `[GREENFIELD]` | Somente com justificativa | — |
| Testes do backend | `mvn verify` passa | — |
| Testes do frontend | Passam se o frontend existir | — |
| Registros de origem contabilizados | Snapshot acordado completo; nenhuma perda inexplicada | — |
| Beneficiários consultáveis pela aplicação moderna | Todos os beneficiários autorizados | — |
| Verificações de nova execução e recuperação dos dados | Aprovadas com evidências registradas | — |
| Timestamp da submissão | Antes ou às 17:10 | — |

---

## Alertas ativos

> [!WARNING]
> Adicione uma entrada abaixo sempre que surgir um bloqueio ou risco. Se estiver bloqueado por 20 minutos, peça apoio do workshop e registre o bloqueio.

- [ ] (nenhum alerta atual)

---

## Resultado da submissão

| Item | Valor |
|---|---|
| PR de submissão | — |
| Submetido em | — |
| Status do juiz | Aguardando / Aceito / Rejeitado |
| Motivo da rejeição, se houver | — |
| Timestamp da nova submissão, se houver | — |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Migração de dados](DATA-MIGRATION.md)<br/><sub>Evidências e aceitação da origem ao destino.</sub> | [Fluxo Git](../00-GIT-WORKFLOW.md)<br/><sub>Regras da branch e do PR de submissão.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
