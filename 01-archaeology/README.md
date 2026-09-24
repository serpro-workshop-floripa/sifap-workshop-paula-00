# Etapa 1 — Arqueologia

> **Trilha:** [Kit da Equipe](../README.md) › **Etapa 1 — Arqueologia**

**Visão geral da Etapa 1.** Leia esta página antes de abrir o GUIA; ela apresenta o objetivo, os artefatos esperados e os participantes.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual responsável por todas as atividades da Etapa 1 |
| **Pré-requisitos** | Corpus legado local; trabalho prévio de prontidão dos dados de origem concluído antes das 14:00 |
| **Tempo estimado** | 50 min (14:00–14:50) |
| **Etapa** | Etapa 1 — Arqueologia |
| **Resultado esperado** | Catálogo de regras, mapa de dependências, glossário, relatório de descoberta e evidências da autoavaliação C1 |

![Etapa 1](https://img.shields.io/badge/Etapa-1%20%C2%B7%20Arqueologia-171717?style=flat-square) ![Gate obrigatório](https://img.shields.io/badge/Gate-Gate%20obrigat%C3%B3rio-404040?style=flat-square) ![Desafio individual](https://img.shields.io/badge/Formato-Desafio%20individual-737373?style=flat-square)

> [!IMPORTANT]
> **Leia primeiro:** [`LEGACY-EXPLORATION-CHECKLIST.md`](LEGACY-EXPLORATION-CHECKLIST.md) — gate obrigatório antes de iniciar a Etapa 2. Nenhum requisito EARS é aceito sem rastreabilidade ao código legado.

> [!TIP]
> **Use evidências de código-fonte e de dados.** Fontes Natural, DDMs, o FDT e documentos históricos estão em [`legacy-sifap/`](legacy-sifap/). A leitura do código pode ocorrer offline; o gate de prontidão dos dados também exige uma origem Adabas autorizada e populada e uma rota de extração suportada. Arquivos offline não comprovam as contagens atuais de registros.

---

## O que é a Etapa 1

**Arqueologia de software** é a prática de extrair conhecimento de sistemas legados por meio da leitura sistemática do código-fonte, sem modificá-lo. Neste workshop, a arqueologia tem um objetivo preciso: reunir evidências suficientes para escrever requisitos rastreáveis na Etapa 2.

O cenário SIFAP abrange aproximadamente 30 anos; consulte a
[política de cronologia e evidências do cenário](../README.md#scenario-chronology-and-evidence).
O código e os documentos datados podem divergir. Investigue ambos antes de especificar
o comportamento. As datas e os autores respaldados pelo kit foram transcritos dos
cabeçalhos das fontes em [`legacy-sifap/CHRONOLOGY.md`](legacy-sifap/CHRONOLOGY.md),
e as divergências intencionais presentes nos documentos de época estão listadas no
[registro de divergências](legacy-sifap/DECLARED-DRIFT.md). A CI verifica a estrutura
das referências às fontes e a existência dos arquivos; a revisão humana deve determinar
se as evidências citadas realmente sustentam o requisito.

---

## Onde esta etapa se encaixa no fluxo do workshop

Consulte o [fluxo do desafio](../00-TEAM-FLOW.md) para ver o cronograma das 14:00 às 17:40, os checkpoints de autoavaliação C1/C2/C3 e a validação do juiz.

---

## Quem trabalha nesta etapa

O participante começa diretamente em `@archaeologist` às 14:00 e lê somente os programas Natural e DDMs necessários à capacidade-alvo fixa: consultar, pesquisar e visualizar detalhes de todos os beneficiários migrados com as regras legadas de validação descobertas. Consulte [`GUIDE.md`](GUIDE.md) para ver a sequência da Etapa 1.

O próprio participante assume as responsabilidades de DBA, QA, Visão e Arquitetura. A origem Adabas autorizada e a rota de extração fazem parte do trabalho prévio; a Etapa 1 registra somente as evidências necessárias ao C1 e à posterior verificação do juiz.

---

## Artefatos da Etapa 1

| Arquivo | Finalidade |
|---|---|
| [`LEGACY-EXPLORATION-CHECKLIST.md`](LEGACY-EXPLORATION-CHECKLIST.md) | **Gate obrigatório.** Escopo de leitura da capacidade fixa e critérios de conclusão antes da Etapa 2. |
| [`GUIDE.md`](GUIDE.md) | Guia passo a passo com cronograma. |
| [`glossary.md`](glossary.md) | Glossário de termos e abreviações do domínio SIFAP. |
| [`business-rules-catalog.md`](business-rules-catalog.md) | Catálogo de regras de negócio extraídas com `Programa de origem` obrigatório. |
| [`dependency-map.md`](dependency-map.md) | Mapa de dependências entre programas e DDMs. |
| [`discovery-report.md`](discovery-report.md) | Relatório de descoberta que consolida as evidências da etapa. |
| [`mysteries-checklist.md`](mysteries-checklist.md) | Checklist de rastreabilidade para questões em aberto. |
| [`mysteries-found.md`](mysteries-found.md) | Registro detalhado de questões em aberto, com evidências e responsável. |
| [Template de mapa de dados](templates/data-map.md) | `/map-source-data` gera o `data-map.md` da equipe durante a leitura da origem. |
| [Template de dicionário de declarações](templates/program-data-dictionary.md) | `/map-source-data` gera `program-data-dictionary.md` a partir dos membros examinados. |
| [Template de cobertura de leitura](templates/reading-coverage.md) | O kickoff inicializa o registro; leitores e QA anotam intervalos reais, não uma conclusão copiada. |
| [Template de revisão C1](templates/LEGACY-EXPLORATION-CHECKLIST.md) | Registro não preenchido de evidências e aprovação da autoavaliação; o checklist da etapa continua sendo a referência oficial. |
| [Registros de migração de dados](../docs/data-migration/) | Registros em branco para prontidão da origem, população medida, mapeamento e reconciliação. |

O código legado está em [`legacy-sifap/`](legacy-sifap/) (compartilhado pelo kit).

Esses documentos são gerados **durante a arqueologia** por meio de prompts orientados e
revisão humana. Os templates permanecem sem preenchimento; somente os artefatos gerados
pela equipe recebem achados. O kit não contém mapa de origem preenchido, dicionário de
declarações, registro de leitura concluído nem relatório C1 pré-aprovado.

Os arquivos legados em `legacy-sifap/` são entradas somente leitura do exercício. Não os modifique nem os use para provisionar um laboratório; registre os achados nos artefatos da etapa.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Kit da Equipe](../README.md)<br/><sub>Página principal do repositório.</sub> | [GUIA da Etapa 1](GUIDE.md)<br/><sub>Cronograma de 50 minutos para ler o sistema legado e catalogar regras.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
