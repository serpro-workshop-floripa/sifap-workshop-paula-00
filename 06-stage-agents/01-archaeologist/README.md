# @archaeologist — Etapa 1: Arqueologia

> **Caminho:** [Kit da equipe](../../README.md) › [Agentes de etapa](../README.md) › **@archaeologist**

**O agente `@archaeologist` orienta o participante em uma leitura sistemática do código legado Natural/Adabas, extraindo regras de negócio rastreáveis e mapeando dependências para definir o escopo da Etapa 2.**

| Campo | Valor |
|---|---|
| **Público-alvo** | Todo o participante durante a Etapa 1, com todos os participantes trabalhando em paralelo |
| **Pré-requisitos** | `01-archaeology/legacy-sifap/` disponível no workspace |
| **Tempo estimado** | 11:00–12:00 + 13:30–14:00 |
| **Etapa** | Etapa 1 — Arqueologia |
| **Resultado esperado** | Catálogo de regras com fontes, DDMs mapeados, questões em aberto e escopo da funcionalidade definido |

![Etapa 1](https://img.shields.io/badge/Stage-1%20%C2%B7%20Archaeology-171717?style=flat-square)
![Abordagem investigativa](https://img.shields.io/badge/Approach-Investigative-404040?style=flat-square)

---

## Quando usar

Use este agente enquanto o participante lê o código legado. O `@archaeologist` ajuda o participante a observar, catalogar e formular perguntas. Ele não escreve código moderno nem inventa regras de negócio.

- **Liderança:** Engenheiro de Requisitos
- **Liderança de dados:** DBA, com revisão independente das evidências pela equipe de QA
- **Apoio importante:** Redator Técnico e Arquiteto Corporativo
- **Pré-requisito obrigatório:** ler os programas Natural atribuídos antes de escrever qualquer especificação

---

## O que o agente faz

- Orienta a leitura linha a linha dos programas `.NSN` e das estruturas DDM do Adabas
- Identifica entradas, processamento, saídas e regras de negócio em cada programa
- Mapeia dependências entre programas por meio de `CALLNAT`
- Orienta a leitura de DDM/FDT e declarações com o DBA; o mapeamento da origem pertence a esta etapa, enquanto o projeto PostgreSQL pertence à Etapa 2
- Registra evidências com caminhos de arquivos e referências de linhas
- Identifica questões em aberto sem inventar respostas

---

## O que o agente NÃO faz

- Não lê código legado a menos que o participante abra o arquivo
- Não transforma uma hipótese em requisito confirmado
- Não sugere arquitetura moderna (essa é a função do `@architect` na Etapa 2)
- Não edita arquivos em `01-archaeology/legacy-sifap/` (somente leitura)

---

## Entradas

| Entrada | Local |
|---|---|
| Programas Natural atribuídos | `01-archaeology/legacy-sifap/natural-programs/*.NSN` |
| DDMs do Adabas | `01-archaeology/legacy-sifap/adabas-ddms/*.ddm` |
| Checklist de exploração | `01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md` |

---

## Saídas esperadas

| Artefato | Local |
|---|---|
| Catálogo de regras de negócio | `01-archaeology/business-rules-catalog.md` |
| Mapa de dependências (Mermaid) | `01-archaeology/dependency-map.md` |
| Mapa dos dados de origem e dicionário de declarações | `01-archaeology/data-map.md`, `program-data-dictionary.md` (gerados por meio de `/map-source-data`) |
| Cobertura real da leitura | `01-archaeology/reading-coverage.md` |
| Lista de questões em aberto | `01-archaeology/mysteries-found.md`: quatro espaços de investigação por dupla, 20 por participante, usando o [checklist de dificuldade/evidência](../../01-archaeology/mysteries-checklist.md) |
| Escopo da funcionalidade selecionada | Registrado antes do checkpoint das 14:00 |

Use os [templates em branco](../../01-archaeology/templates/) e o
[ciclo de vida dos dados](../../docs/DATA-MIGRATION.md). O participante gera esses
documentos durante a arqueologia; nenhuma análise completa da origem ou aprovação é fornecida.

---

## Como selecionar o agente no Copilot Chat

- [ ] **Abra o Copilot Chat** no VS Code (`Ctrl+Alt+I` / `Cmd+Alt+I`).
- [ ] **Selecione `@archaeologist`** no seletor de agentes.
- [ ] **Abra o primeiro programa Natural atribuído** no editor antes de enviar o primeiro prompt.
- [ ] **Cole o prompt inicial** abaixo e pressione Enter.

```text
I am starting Stage 1 — Archaeology.
We have Natural/Adabas code in 01-archaeology/legacy-sifap/.
Help the participant examine the assigned programs and record only evidence
and open questions for the scope we will select. Do not infer answers.
```

---

## Exemplos de prompts

| Situação | Prompt útil |
|---|---|
| Programa Natural desconhecido | "Leia este programa comigo e separe entrada, processamento, saída e regras de negócio." |
| DDM do Adabas | "/map-source-data: leia comigo o DDM/FDT selecionado e as declarações; registre evidências e incógnitas, não decisões sobre PostgreSQL." |
| Regra ambígua | "Não invente uma resposta. Registre-a como um mistério com hipótese, evidência e impacto." |
| CALLNAT | "Mapeie quem chama quem e gere um diagrama Mermaid simples." |

---

## Definição de pronto

- [ ] A dupla leu integralmente todos os programas Natural atribuídos.
- [ ] Toda regra considerada para o escopo tem `source_legacy:` com arquivo e linha.
- [ ] O participante consultou DDMs e dependências quando eles afetam a funcionalidade selecionada.
- [ ] As questões em aberto estão registradas sem respostas inventadas.
- [ ] O relatório de descoberta está pronto para o checkpoint das 14:00.
- [ ] O mapa da origem, o dicionário e o registro real de leitura foram gerados a partir das evidências do participante.
- [ ] DBA/QA verificaram a prontidão da origem preenchida e da extração; a ausência de evidências bloqueia a aceitação de dados em C1.

---

## Erros comuns

| Sintoma | Causa | Correção |
|---|---|---|
| O Copilot apresenta generalizações vagas | Nenhum arquivo está aberto no editor | Abra o arquivo `.NSN` e cite a seção específica no prompt |
| A regra de negócio não tem fonte | O participante aceitou uma hipótese como fato | Marque-a como mistério até que exista evidência no código |
| Perde-se tempo detalhando áreas fora do escopo | Nenhuma decisão de escopo foi tomada | Selecione a funcionalidade enxuta antes das 12:00 e limite a leitura a ela |
| Arquivos legados são editados | Confusão sobre a função da etapa | `01-archaeology/legacy-sifap/` é somente leitura |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Agentes de etapa — visão geral](../README.md)<br/><sub>Os 4 agentes, o cronograma e a matriz de responsabilidades.</sub> | [@architect](../02-architect/README.md)<br/><sub>Etapa 2: transforme evidências em uma especificação moderna.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
