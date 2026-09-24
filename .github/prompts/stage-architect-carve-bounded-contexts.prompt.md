---
name: "carve-bounded-contexts"
description: "Avalia as hipóteses de limites da Etapa 1 e decide os contextos delimitados do Monólito Modular."
argument-hint: "report=01-archaeology/discovery-report.md"
agent: "architect"
tools: ["read", "search", "edit"]
---
# /carve-bounded-contexts

## Objetivo

Transforme as hipóteses de limites do relatório de descoberta da Etapa 1 em contextos delimitados avaliados e decididos. Cada contexto recebe nome, responsabilidades, dados sob sua responsabilidade e regras de comunicação entre contextos.

## Quando invocar

No início da Etapa 2, imediatamente após revisar o relatório de descoberta da Etapa 1.

## Pré-condições

- `01-archaeology/discovery-report.md` contém as evidências reais de limites da equipe ou uma questão de projeto delimitada, sem contagem obrigatória de hipóteses
- A equipe revisou o relatório de descoberta e está pronta para tomar decisões arquiteturais

## Inputs que a equipe deve fornecer

- Path do relatório de descoberta
- Quaisquer restrições ou preferências adicionais da equipe

## O que farei

- Lerei as hipóteses de limites no relatório de descoberta
- Avaliarei cada hipótese segundo três critérios: coesão, acoplamento e frequência de mudança
- Apresentarei à equipe a análise de cada hipótese
- Documentarei rejeições com justificativa
- Formalizarei os contextos aceitos com nomes, responsabilidades e propriedade dos dados

## O que NÃO farei

- Decidir automaticamente quais hipóteses aceitar — a equipe toma a decisão final
- Propor microsserviços — este é um Monólito Modular
- Fabricar contexto de negócio para as hipóteses — trabalho somente com o que a Etapa 1 descobriu
- Pular os critérios de avaliação — toda hipótese recebe a análise completa

## Formato de saída

Um arquivo Markdown em `02-modern-spec/bounded-contexts.md`:

```markdown
# Bounded Context Map
## Evaluation Criteria
## Hypothesis Evaluation
### [Hypothesis Name] — ACCEPTED / REJECTED
## Final Bounded Contexts
### [Context Name]
- Responsibility:
- Owned data (DDMs/tables):
- Public interface:
- Why it is a separate context:
## Inter-Context Communication
## Context Map Mermaid Diagram
```

## Definição de pronto

- [ ] Toda hipótese do relatório de descoberta foi avaliada segundo os três critérios
- [ ] Hipóteses rejeitadas têm justificativa documentada
- [ ] Somente os contextos delimitados necessários ao recorte selecionado estão definidos e revisados
- [ ] Cada contexto tem um parágrafo de responsabilidade, lista de dados sob sua responsabilidade e esboço da interface pública
- [ ] Um diagrama Mermaid do mapa de contextos mostra as relações entre contextos
- [ ] Caminhos de comunicação são definidos somente onde evidências e requisitos os exigem; nenhum acoplamento artificial é adicionado

## Corpo do prompt

Você é o `@architect`. A equipe está iniciando a Etapa 2 e precisa decidir os contextos delimitados do Monólito Modular.

**Etapa 1 — Leia o relatório de descoberta.**
Abra `01-archaeology/discovery-report.md`. Extraia a seção de hipóteses de limites. Liste cada hipótese com nome, programas incluídos, DDMs sob sua responsabilidade e justificativa.

**Etapa 2 — Avalie segundo três critérios.**
Para cada hipótese, analise:

**Coesão** — As regras de negócio deste grupo estão relacionadas à mesma capacidade de negócio? Verifique revisando as regras confirmadas em `01-archaeology/business-rules-catalog.md` que pertencem a este grupo. Alta coesão = candidato forte.

**Acoplamento** — Quantas dependências atravessam este limite? Verifique o mapa de dependências em `01-archaeology/dependency-map.md`. Conte as arestas que cruzariam este contexto e outros. Baixo acoplamento = candidato forte. Alto acoplamento sugere que o limite pode estar mal posicionado.

**Frequência de mudança** — Use registros datados de alterações ou o histórico
real de versões quando disponíveis. Um nome de arquivo ou aresta de chamada não
comprova frequência de mudança conjunta; marque este critério como desconhecido
quando as evidências históricas forem insuficientes.

Apresente cada avaliação como um scorecard: Alto/Médio/Baixo para cada critério.

**Etapa 3 — Apresente à equipe para decisão.**
Para cada hipótese, apresente:

- O scorecard
- Uma recomendação (aceitar, rejeitar ou mesclar com outra hipótese)
- A justificativa

Então pergunte à equipe: "Vocês aceitam esta recomendação? Caso contrário, o que mudariam?"

A equipe toma a decisão final. Se ela substituir sua recomendação, documente a justificativa.

**Etapa 4 — Formalize os contextos aceitos.**
Para cada contexto delimitado aceito, escreva:

- **Nome**: um nome na linguagem de negócio confirmado pela equipe, não um nome técnico de serviço
- **Responsabilidade**: um parágrafo descrevendo pelo que este contexto responde
- **Dados sob responsabilidade**: quais DDMs/tabelas pertencem exclusivamente a este contexto
- **Interface pública**: quais operações este contexto expõe a outros contextos (assinaturas de métodos ou nomes de eventos — não implementação)
- **Por que é um contexto próprio**: uma frase conectando-o aos critérios de avaliação

**Etapa 5 — Defina a comunicação entre contextos.**
Para cada par de contextos que precisa se comunicar, especifique:

- A direção (A chama B ou bidirecional)
- O mecanismo: chamada de método em processo por uma interface, evento de domínio ou tipo do kernel compartilhado
- Os dados trocados (somente IDs? DTOs completos? Eventos?)

Reforce que este é um Monólito Modular. A comunicação é em processo, não HTTP entre serviços.

**Etapa 6 — Desenhe o mapa de contextos.**
Crie um diagrama somente quando ele esclarecer a questão de projeto. Use o
[tema neutro do kit](../../docs/DOC-STYLE-GUIDE.md), com responsabilidades e
relações de comunicação respaldadas pela fonte, nunca uma arquitetura SIFAP
preenchida previamente.

**Etapa 7 — Escreva a saída.**
Escreva em `02-modern-spec/bounded-contexts.md`.

## Exemplo de invocação

```
/carve-bounded-contexts report=01-archaeology/discovery-report.md
```
