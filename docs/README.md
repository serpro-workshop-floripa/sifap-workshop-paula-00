# Documentação

> **Caminho:** [Kit do desafio individual](../README.md) › **Documentação**

**Idioma:** português brasileiro (`develop`). Use o [seletor de idioma](../README.md#idiomas-do-repositório) para acessar a documentação traduzida e as instruções do Copilot específicas de cada branch.

Documentação transversal usada durante o desafio individual.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual |
| **Pré-requisitos** | Ler [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) |
| **Tempo estimado** | 5 min |
| **Resultado esperado** | Saber onde encontrar decisões, orientações de migração de dados, acompanhamento de status e solução de problemas |

---

## Como usar esta pasta

- [ ] **Antes das 14:00** — leia [STATUS.md](STATUS.md) e [DATA-MIGRATION.md](DATA-MIGRATION.md).
- [ ] **Durante a Etapa 1** — atualize o [glossário da Etapa 1](../01-archaeology/glossary.md) e registre as fontes legadas.
- [ ] **Durante a Etapa 2** — crie ADRs em [adr/](adr/) para decisões de design não triviais.
- [ ] **Durante a Etapa 3** — registre evidências de migração, reconciliação e validação sem dados sensíveis.
- [ ] **Antes da submissão** — preencha o checklist do PR e a seção C3 de STATUS.

## Estrutura

| Caminho | Finalidade |
|---|---|
| [`adr/`](adr/) | Registros de decisões arquiteturais, incluindo a ADR-0003 sobre o formato do desafio |
| [`../01-archaeology/glossary.md`](../01-archaeology/glossary.md) | Glossário do domínio preenchido durante a Etapa 1 |
| [`DATA-MIGRATION.md`](DATA-MIGRATION.md) | Prontidão da fonte, descoberta, migração, reconciliação e consulta de beneficiários |
| [Cronologia do cenário](../README.md#cenário-cronologia-e-evidências) | Aproximadamente 30 anos de história, datas originais das fontes e o ano de referência 2026 do workshop |
| [Cronologia canônica](../01-archaeology/legacy-sifap/CHRONOLOGY.md) | Datas, autores e índice de nomes transcritos dos cabeçalhos-fonte |
| [Divergências declaradas](../01-archaeology/legacy-sifap/DECLARED-DRIFT.md) | Contradições deliberadas entre documentos de época e código |
| [Evidências e dificuldade dos mistérios](../01-archaeology/mysteries-checklist.md) | Níveis de investigação, comparação de fontes, escalonamento e resultados honestos não resolvidos |
| [`data-migration/`](data-migration/) | Registros em branco para suas próprias evidências e decisões sobre dados |
| [`4-agents-explained.md`](4-agents-explained.md) | Explicação dos agentes de etapa e das skills de papel |
| [`persona-agent-matrix.md`](persona-agent-matrix.md) | Responsabilidades dos papéis entre as etapas |
| [`sdlc-flow-guide.md`](sdlc-flow-guide.md) | Referência ampliada do processo; [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) continua sendo a fonte de verdade do cronograma do desafio |
| [`STATUS.md`](STATUS.md) | Acompanhamento do progresso individual, C1/C2/C3 e submissão ao juiz |
| [`runbook.md`](runbook.md) | Como executar o sistema localmente, na CI e no Azure, caso seja construído |

## Convenções

- Use uma ADR por decisão duradoura. Numere-as sequencialmente: `0001-title.md`, `0002-title.md`.
- Mantenha os termos do glossário em ordem alfabética, com citações da fonte legada em que cada termo se originou.
- Toda decisão importante se torna uma ADR. Uma conversa no chat não é um registro suficiente.
- Todo termo do glossário originado no sistema legado precisa de uma fonte (`.NSN`, `.ddm` ou documento histórico).
- Nunca registre credenciais, CPF, NIS, valores de benefícios nem detalhes de administração da fonte no Git.

## Definição de pronto da documentação

- [ ] O glossário inclui fontes legadas.
- [ ] As ADRs incluem contexto, opções, decisão e consequências.
- [ ] Os registros de migração apontam para evidências sanitizadas de prontidão, carga, reconciliação e consulta.
- [ ] Os links internos apontam para os arquivos corretos.
- [ ] Os documentos explicam o motivo antes do procedimento.

## Links rápidos

- [Fluxo do desafio](../00-TEAM-FLOW.md)
- [Responsabilidades dos papéis](../05-personas/)
- [Guia da Etapa 1](../01-archaeology/GUIDE.md)
- [Fluxo Git](../00-GIT-WORKFLOW.md)

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Cartões de referência](../09-cheat-sheets/README.md)<br/><sub>Referências rápidas de Copilot, Spec-Kit e modelos.</sub> | [Glossário visual](../07-concepts/03-visual-glossary.md)<br/><sub>Termos técnicos e de domínio do SIFAP.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
