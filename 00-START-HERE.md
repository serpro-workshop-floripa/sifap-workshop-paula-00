# Comece aqui: atividades prévias do desafio individual

> **Trilha:** [Kit do desafio individual](README.md) › **Comece aqui**

Use esta página antes do início às 14:00. O desafio começa diretamente em `@archaeologist`; não há um bloco de abertura durante o exercício cronometrado.

![Início](https://img.shields.io/badge/In%C3%ADcio-00-171717?style=flat-square) ![Quando: antes das 14:00](https://img.shields.io/badge/Quando-Antes%20das%2014%3A00-737373?style=flat-square) ![Público: participante individual](https://img.shields.io/badge/P%C3%BAblico-Participante%20individual-A3A3A3?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Um participante trabalhando sozinho |
| **Pré-requisitos** | Git, VS Code, Copilot, Spec-Kit, Java, Node, Docker, clone do repositório e uma origem Adabas autorizada e populada, com rota de extração, prontos antes das 14:00 |
| **Tempo estimado** | 15 minutos de leitura após a configuração |
| **Resultado esperado** | Você sabe o que abrir às 14:00, como realizar as autoverificações C1/C2/C3 e como enviar |

---

## Checklist de atividades prévias (conclua antes das 14:00)

- [ ] Siga [`00-SETUP.md`](00-SETUP.md) e verifique as ferramentas de seu computador.
- [ ] Clone seu próprio repositório privado e crie ou atualize `develop`.
- [ ] Confirme que Copilot Ask, Plan, Agent e os agentes de etapa são carregados no VS Code.
- [ ] Instale e verifique o Spec-Kit oficial (`specify version`).
- [ ] Confirme que os fontes legados locais estão presentes em [`01-archaeology/legacy-sifap/`](01-archaeology/legacy-sifap/).
- [ ] Confirme que a origem Adabas autorizada e populada e a rota de extração suportada estão prontas; mantenha as credenciais fora do Git.
- [ ] Leia o fluxo do desafio em [`00-TEAM-FLOW.md`](00-TEAM-FLOW.md) e as regras do Git em [`00-GIT-WORKFLOW.md`](00-GIT-WORKFLOW.md).
- [ ] Abra o glossário visual: [`07-concepts/03-visual-glossary.md`](07-concepts/03-visual-glossary.md).
- [ ] Leia rapidamente as responsabilidades das 10 funções em [`05-personas/`](05-personas/). Você as cobre sozinho; as funções são skills, não colegas de equipe.

> [!IMPORTANT]
> Não execute orquestração paralela de subagentes, worker harnesses nem fan-out do Copilot CLI durante o desafio. Use os modos Ask, Plan e Agent do Copilot com o agente de etapa ativo.

---

## Às 14:00: abra `@archaeologist`

Às 14:00, abra o Copilot Chat no VS Code e selecione `@archaeologist`.

Use o primeiro prompt para iniciar a Etapa 1:

```text
@archaeologist Start Stage 1 for the individual SIFAP challenge. Help me discover the legacy rules for listing, searching, and viewing all beneficiaries migrated from Adabas to PostgreSQL. Keep every finding tied to legacy files and lines, and prepare me for checkpoint C1.
```

Use `@dba` quando surgirem perguntas sobre descoberta da origem de dados, interpretação de DDM/FDT, extração ou reconciliação.

---

## Cronograma do desafio

Os orçamentos de tempo de referência estão em [`00-TEAM-FLOW.md`](00-TEAM-FLOW.md):

| Horário | Etapa | Agente | Checkpoint |
|---|---|---|---|
| 14:00-14:50 | Etapa 1 — Arqueologia | `@archaeologist` + `@dba` conforme necessário | C1 |
| 14:50-15:30 | Etapa 2 — Especificação | `@architect` + `@dba` conforme necessário | C2 |
| 15:30-17:10 | Etapa 3 — Implementação e migração de dados | `@builder` + `@dba` | Envio C3 |
| 17:10-17:40 | Validação final da banca | Banca | Aceitação ou rejeição |

A capacidade-alvo fixa é consultar — listar, pesquisar e detalhar — **todos** os beneficiários migrados do Adabas para o PostgreSQL, aplicando as regras de validação que você descobrir no sistema legado.

---

## Autoverificações

C1, C2 e C3 substituem os handoffs. Antes de trocar de agente, verifique seus próprios artefatos em relação à mesma definição de pronto.

- **C1 (fim da Etapa 1):** programas/DDMs legados lidos, regras de negócio registradas com evidências, perguntas sobre dados e bloqueios documentados.
- **C2 (fim da Etapa 2):** requisitos EARS, REQ-IDs, `source_legacy:`, plano, tarefas, ADRs e design da migração rastreáveis.
- **C3 (fim da Etapa 3):** implementação, testes, carga de dados, reconciliação, comportamento de reexecução e cobertura da consulta prontos para o PR de envio.

Se estiver travado por 20 minutos, peça ajuda ao suporte do workshop e registre o bloqueio. Reduza a abrangência da capacidade, se necessário, mas nunca a população migrada nem o padrão de verificação.

---

## Linha de chegada

Seu envio será aceito somente se todos estes itens passarem:

1. A CI está verde, incluindo `legacy-traceability` e os jobs de teste.
2. Todo requisito tem um REQ-ID, redação EARS e `source_legacy:`.
3. Os testes passam: `mvn verify` no backend; testes do frontend, caso um frontend tenha sido criado.
4. Os dados estão reconciliados: contagem da origem = carregados + rejeições explicadas; chaves da origem e agregados acordados são reconciliados; nenhuma perda sem explicação; reexecução sem duplicidades.
5. Listagem, pesquisa e detalhes cobrem toda a população migrada de beneficiários, não apenas uma amostra ou a primeira página.

---

## Como enviar

1. Trabalhe em seu próprio repositório.
2. Crie `spec/<NNN>-<feature>` a partir de `develop` durante a Etapa 2.
3. Crie `impl/<NNN>-<feature>` a partir de `develop` durante a Etapa 3.
4. Abra o PR de envio de `impl/<NNN>-<feature>` para `develop`.
5. Preencha o checklist do PR em [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).
6. Notifique a banca.

O horário de criação do PR é o horário do envio. Os dois primeiros participantes cujos envios passarem na validação da banca vencem. O prazo de envio é 17:10; envios rejeitados podem ser corrigidos e reenviados com um novo horário.

---

### Continue a leitura

| Anterior | Próximo |
|---|---|
| [Kit do desafio individual](README.md)<br/><sub>Página principal deste repositório.</sub> | [Fluxo do desafio](00-TEAM-FLOW.md)<br/><sub>Cronograma das 14:00 às 17:40, C1/C2/C3 e linha de chegada.</sub> |

<sub>[Voltar ao índice do kit](README.md)</sub>
