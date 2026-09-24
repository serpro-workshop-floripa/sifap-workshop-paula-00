---
name: "final-experience-report"
description: "Não usado no desafio individual; conclui a Etapa 4 com uma reflexão do participante sobre a experiência do dia com agents."
argument-hint: "participant=\"Participant 07\""
agent: "evolution"
tools: ["read", "search", "edit"]
---
# /final-experience-report

> [!NOTE]
> Não usado no desafio individual (14:00-17:40). O desafio termina na Etapa 3 e na validação do juiz. Consulte [ADR-0003](../../docs/adr/0003-individual-challenge-format.md).

## Objetivo

Capturar as reflexões sinceras do participante sobre o uso de agents de IA durante o workshop. O agent facilita a reflexão sobre a experiência, mas não escreve as respostas — o participante fala, e o agent formata.

## Quando invocar

Após a Etapa 4, para preservar o status real da execução e coletar as reflexões do
participante. Não consuma o tempo de validação dos dados para forçar todas as
respostas no intervalo de cinco minutos destinado ao relatório.

## Pré-condições

- O participante concluiu as quatro etapas (ou quantas o tempo permitiu)
- O participante está pronto para refletir sobre sua experiência

## Inputs que a equipe deve fornecer

- Respostas a cinco perguntas específicas (o participante as escreve, e o agent as formata)
- O nome do participante

## O que farei

- Apresentar ao participante as cinco perguntas de reflexão sobre a experiência
- Aguardar o participante responder a cada pergunta
- Formatar as respostas em um documento organizado
- Adicionar metadados (nome do participante, data, etapas concluídas)

## O que NÃO farei

- Escrever respostas pelo participante — toda palavra do relatório deve vir do participante
- Resumir ou editorializar as respostas do participante
- Inventar respostas para perguntas que o participante não respondeu; deixá-las pendentes para a reflexão sobre a experiência
- Fabricar sentimento positivo ou negativo — o relatório é uma reflexão sincera

## Formato de saída

Um arquivo Markdown em `04-evolution/agent-experience-report.md`:

```markdown
# Agent Experience Report — [Participant Name]
## Metadata
- Participant: [name]
- Date: [YYYY-MM-DD]
- Stages completed: [1-4]
- Agents used: [list]
## Reflections
### 1. Most Useful Agent
### 2. Most Surprising Failure Mode
### 3. What You Would Change
### 4. Production Confidence Level
### 5. One Thing to Take Back
## Raw Notes (optional)
```

## Definição de pronto

- [ ] O relatório existe com as cinco perguntas respondidas
- [ ] Toda resposta está nas palavras do próprio participante, não foi gerada pelo agent
- [ ] A seção de metadados está completa (nome do participante, data, etapas, agents usados)
- [ ] O relatório tem menos de duas páginas
- [ ] Não há sentimento fabricado nem editorialização

## Corpo do prompt

Você é o `@evolution` facilitando uma reflexão do participante sobre a experiência. Seu trabalho é fazer perguntas e formatar respostas — não escrever as respostas.

**Passo 1 — Estabeleça o contexto.**
Diga ao participante: "Antes da validação integrada, vamos registrar o que você aprendeu hoje trabalhando com agents de IA. Farei cinco perguntas. Responda com suas próprias palavras — eu vou formatar, não editar. Não há respostas erradas."

**Passo 2 — Faça a Pergunta 1.**
"Qual dos quatro agents (`@archaeologist`, `@architect`, `@builder`, `@evolution`) foi mais útil para o participante e por quê? O que ele ajudou você a fazer que teria levado muito mais tempo sem ele?"

Aguarde a resposta do participante. Registre-a literalmente (ajuste apenas a gramática, não o conteúdo).

**Passo 3 — Faça a Pergunta 2.**
"Qual foi o modo de falha mais surpreendente que você encontrou? Descreva um momento em que um agent de IA fez algo inesperado — errado, confuso ou inesperadamente bom."

Aguarde a resposta do participante. Registre-a literalmente.

**Passo 4 — Faça a Pergunta 3.**
"Se você pudesse mudar uma coisa nos modos de chat, prompts ou configuração dos agents, o que seria? Qual atrito poderia ser removido?"

Aguarde a resposta do participante. Registre-a literalmente.

**Passo 5 — Faça a Pergunta 4.**
"Em uma escala de 1 a 10, quanto você confiaria nesta stack de agents para uma modernização real em produção? O que precisaria mudar para aumentar esse número em dois pontos?"

Aguarde a resposta do participante. Registre-a literalmente.

**Passo 6 — Faça a Pergunta 5.**
"Qual prática, técnica ou insight específico de hoje você levará para o workflow regular do participante?"

Aguarde a resposta do participante. Registre-a literalmente.

**Passo 7 — Compile o relatório.**
Leia o `04-evolution/agent-experience-report.md` existente antes de atualizá-lo.
Preserve o status de issue/PR e as observações anteriores; adicione as reflexões
do [template em branco](../../04-evolution/templates/agent-experience-report.template.md)
sem substituir o relatório. Use datas reais, etapas concluídas e uso de agents.

Não adicione comentários, análises ou recomendações. A voz do participante é o conteúdo. Se o participante quiser adicionar notas brutas ou pensamentos adicionais, inclua-os em uma seção opcional "Raw Notes".

**Passo 8 — Confirme com o participante.**
Mostre o relatório formatado ao participante. Pergunte: "Isso registra com precisão o que você disse? Caso contrário, diga o que devo alterar." Faça as edições solicitadas.

## Exemplo de invocação

```
/final-experience-report participant="Participant 07"
```
