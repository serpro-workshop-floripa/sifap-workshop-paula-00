# Fluxo do desafio: um participante, três etapas, uma linha de chegada

> **Trilha:** [Kit da equipe](README.md) › **Fluxo do desafio**

**Mantenha este documento fixado na tela durante todo o desafio.** Ele responde a quatro perguntas: o que você faz em cada etapa, quando troca de agente, como verifica seu próprio trabalho e o que constitui a linha de chegada.

![Fluxo](https://img.shields.io/badge/Fluxo-Individual-171717?style=flat-square) ![Duração: 5 min de leitura](https://img.shields.io/badge/Dura%C3%A7%C3%A3o-5%20min%20de%20leitura-737373?style=flat-square) ![Uso: o tempo todo](https://img.shields.io/badge/Uso-O%20tempo%20todo-A3A3A3?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Todos os participantes do desafio |
| **Pré-requisitos** | Atividades prévias concluídas antes das 14:00 (§2) |
| **Tempo estimado** | 5 minutos |
| **Resultado esperado** | Você conhece o cronograma, os checkpoints, a linha de chegada e como enviar |

---

## 1. O formato

- **Individual.** Você trabalha sozinho e cobre todas as 10 funções. As funções são **skills** carregadas automaticamente ([ADR-0002](docs/adr/0002-team-roles-as-skills-not-agents.md)); você troca somente o agente de etapa.
- **Somente as Etapas 1 a 3.** Você avança da arqueologia do legado até uma fatia moderna funcional e validada. A Etapa 4 (evolução) não faz parte do desafio.
- **Mesmo objetivo para todos.** Listar, pesquisar e exibir os detalhes de **todos** os beneficiários migrados do Adabas para o PostgreSQL, aplicando as regras de validação legadas que **você** descobrir.
- **Os dois primeiros participantes cujo envio passar na validação da banca vencem.**
- **Sem orquestrador.** Use os modos Ask, Plan e Agent do Copilot com os agentes de etapa. A orquestração paralela de subagentes não é permitida.

A decisão está registrada na [ADR-0003](docs/adr/0003-individual-challenge-format.md).

---

## 2. Atividades prévias (antes das 14:00)

> [!IMPORTANT]
> Às 14:00, você abre `@archaeologist` e começa. Não há bloco de abertura, portanto tudo abaixo deve estar pronto antes desse horário.

- [ ] Seu próprio repositório (fork ou cópia deste kit), clonado e em `develop`
- [ ] Git, VS Code, Copilot Chat, Spec-Kit (`specify version`), Java 21, Node e Docker funcionando ([Configuração](00-SETUP.md))
- [ ] Acesso à origem Adabas autorizada e populada e a uma rota de extração suportada ([guia de migração de dados](docs/DATA-MIGRATION.md))
- [ ] Este arquivo e a [linha de chegada](#5-linha-de-chegada-e-envio) lidos

---

## 3. Cronograma (14:00-17:40, 220 minutos)

![Linha do tempo do desafio: três etapas e validação da banca](assets/timeline-stages.svg)

| Horário | Etapa | Agente | Checkpoint ao final |
|---|---|---|---|
| **14:00-14:50** | **Etapa 1** — Arqueologia ([guia](01-archaeology/GUIDE.md)) | `@archaeologist` (+ `@dba` para descoberta de dados) | C1 |
| **14:50-15:30** | **Etapa 2** — Especificação ([guia](02-modern-spec/GUIDE.md)) | `@architect` (+ `@dba` para design da migração) | C2 |
| **15:30-17:10** | **Etapa 3** — Implementação e migração de dados ([guia](03-implementation/GUIDE.md)) | `@builder` + `@dba` | C3 = envio |
| **17:10-17:40** | Validação final da banca | Banca | - |

> [!NOTE]
> Os tempos das etapas são orçamentos de referência. Você avança em seu próprio ritmo e pode enviar antes das 17:10. A banca valida os envios à medida que chegam. **17:10 é o prazo de envio.**

---

## 4. Autoverificações (C1, C2, C3)

![Autoverificações C1, C2 e C3 em cada troca de agente](assets/handoffs.svg)

Você não tem outra pessoa para receber um handoff, portanto cada troca de agente é uma **autoverificação**. Antes de avançar, verifique seus próprios artefatos em relação à lista abaixo. Se um item estiver ausente, corrija-o ou registre-o como bloqueio.

### C1: do legado para a especificação (fim da Etapa 1, por volta das 14:50)

| Artefato | Caminho | Critério de conclusão |
|---|---|---|
| Catálogo de regras | `01-archaeology/business-rules-catalog.md` | As regras da capacidade-alvo citam evidências reais de Natural/JCL/DDM/FDT que você leu |
| Relatório de descoberta | `01-archaeology/discovery-report.md` | Fatia fina, evidências e perguntas em aberto |
| Evidências de apoio | `01-archaeology/` | Cobertura de leitura, mapa de dados, dependências e mistérios distinguem itens descobertos, adiados e desconhecidos |
| Descoberta e preparação dos dados | [Registros de migração de dados](docs/data-migration/) | População medida na origem, referências a DDM/FDT, anomalias e rota de extração |

### C2: da especificação para o código (fim da Etapa 2, por volta das 15:30)

| Artefato | Caminho | Critério de conclusão |
|---|---|---|
| Especificação | `.spec/<NNN>-<feature>/spec.md` | REQ-IDs, EARS e `source_legacy:` em todos os requisitos |
| Plano | `.spec/<NNN>-<feature>/plan.md` | Decisões, riscos e abordagem são suficientes para começar |
| Tarefas | `.spec/<NNN>-<feature>/tasks.md` | A ordem de implementação e testes está definida |
| Decisão de escopo | `02-modern-spec/scope-decisions.md` | O que está no escopo e o que foi adiado |
| Design da migração | `plan.md`, `tasks.md` e [registros de migração de dados](docs/data-migration/) | Mapeamentos, snapshot, ordem de carga, rejeições, reexecução/recuperação e reconciliação; as consultas cobrem todos os beneficiários |

### C3: envio (fim da Etapa 3, até 17:10)

| Artefato | Caminho | Critério de conclusão |
|---|---|---|
| Backend | `backend/` | `mvn verify` está verde; a OpenAPI está documentada |
| Frontend (se criado) | `frontend/` | `npm test` está verde; os fluxos principais funcionam |
| Migrações de schema | `backend/src/main/resources/db/migration/` | Scripts Flyway versionados são aplicados uma vez |
| População migrada | PostgreSQL + [registros de migração de dados](docs/data-migration/) | Todos os registros do snapshot foram carregados ou explicitamente rejeitados; chaves e agregados foram reconciliados |
| Consulta de beneficiários | `backend/`, `frontend/` e evidências | Listagem, pesquisa e detalhes cobrem a população completa |
| Reexecução e recuperação | Testes e evidências | Reexecutar o mesmo snapshot não cria duplicidades |

---

## 5. Linha de chegada e envio

Um envio será aceito somente quando **todos** estes itens passarem:

1. A CI está verde, incluindo `legacy-traceability` e os jobs de teste.
2. Todo requisito tem um REQ-ID, EARS e `source_legacy:`.
3. Os testes passam: `mvn verify` no backend e os testes do frontend, caso um frontend tenha sido criado.
4. Os dados estão reconciliados:
   - contagem da origem = carregados + rejeições explicadas;
   - chaves da origem e agregados acordados correspondem;
   - nenhuma perda sem explicação;
   - uma reexecução não cria duplicidades.
5. Listagem, pesquisa e detalhes cobrem a população **completa** de beneficiários migrados, não apenas uma amostra ou a primeira página.

**Como enviar:**

1. Abra o PR `impl/<NNN>-<feature>` -> `develop` em seu repositório.
2. Preencha o checklist de envio no template de PR.
3. Notifique a banca.

O horário de criação do PR é seu timestamp. Se a banca rejeitar o envio, corrija-o e envie novamente; o novo timestamp será considerado.

> [!IMPORTANT]
> Reduza a abrangência da capacidade, nunca a população migrada nem o padrão de verificação. Um resultado incompleto é um incremento verificado acompanhado de bloqueios registrados. Ele não vence, mas é o resultado honesto.

---

## 6. A regra dos 20 minutos

> [!IMPORTANT]
> **Se você permanecer travado no mesmo problema por 20 minutos, pare e peça ajuda ao suporte do workshop.** Registre o bloqueio caso não exista uma solução baseada em evidências.

| Tempo travado | O que fazer |
|---|---|
| 5 min | Reformule a pergunta no Copilot Chat e consulte o guia relevante |
| 10 min | Consulte a [solução de problemas](docs/troubleshooting.md) e o [FAQ](docs/FAQ.md) |
| 20 min | Peça ajuda ao suporte do workshop usando o formato de três linhas abaixo |

```text
1. Goal: What I am trying to achieve
2. Tried: What I already tried (and what happened)
3. Blocker: What is stopping me right now
```

---

## 7. Antipadrões

| Antipadrão | Faça isto em vez disso |
|---|---|
| Ignorar um checkpoint para economizar tempo | Dedique dois minutos a C1, C2 e C3; evidências ausentes custam mais durante a validação |
| Escrever requisitos antes de ler o fonte | Leia primeiro os programas e o DDM da capacidade-alvo (gate obrigatório) |
| Substituir registros de origem por uma seed gerada | Migre a população Adabas autorizada |
| Comprovar as consultas apenas com a primeira página | Comprove listagem, pesquisa e detalhes em toda a população |
| Executar subagentes em paralelo ou um orquestrador | Use os agentes de etapa nos modos Ask, Plan e Agent |
| Editar `01-archaeology/legacy-sifap/` | Trate os fontes legados como somente leitura |

---

## 8. Referência rápida

| Pergunta | Onde encontrar |
|---|---|
| O que faço na etapa N? | §3 e o guia da etapa |
| Estou pronto para trocar de agente? | §4 (C1, C2, C3) |
| O que significa estar concluído? | §5 |
| Está travado? | §6 |
| Qual modo do Copilot? | [`09-cheat-sheets/copilot-3-modes.md`](09-cheat-sheets/copilot-3-modes.md) |
| Qual modelo? | [`09-cheat-sheets/model-routing.md`](09-cheat-sheets/model-routing.md) |
| Qual comando do Spec-Kit? | [`09-cheat-sheets/spec-kit-workflow.md`](09-cheat-sheets/spec-kit-workflow.md) |

---

### Continue a leitura

| Anterior | Próximo |
|---|---|
| [Comece aqui](00-START-HERE.md)<br/><sub>Atividades prévias e primeira ação às 14:00.</sub> | [Configuração](00-SETUP.md)<br/><sub>Configuração do computador: Git, VS Code, Copilot e Spec-Kit.</sub> |

<sub>[Voltar ao índice do kit](README.md)</sub>
