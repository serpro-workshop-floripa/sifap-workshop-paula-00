---
name: "generate-adr"
description: "Elabora um Architecture Decision Record (ADR) para uma escolha de projeto específica que a equipe está fazendo."
argument-hint: "title=\"Map Adabas MU fields to JSONB vs ElementCollection\""
agent: "architect"
tools: ["read", "search", "edit"]
---
# /generate-adr

## Objetivo

Crie um Architecture Decision Record (ADR) formal que documente uma escolha de projeto específica. O ADR registra as opções consideradas, os trade-offs avaliados, a decisão tomada e suas consequências.

## Quando invocar

Sempre que a equipe enfrentar uma escolha de projeto com pelo menos 2 opções viáveis durante a Etapa 2 (ou posteriormente).

## Pré-condições

- A equipe identificou uma decisão a tomar (por exemplo, "como mapeamos campos MU?" ou "qual estratégia de autenticação?")
- Existem pelo menos 2 opções — se apenas 1 opção for óbvia, um ADR é desnecessário

## Inputs que a equipe deve fornecer

- O título da decisão (por exemplo, "Mapear campos MU do Adabas para JSONB vs. @ElementCollection")
- As opções consideradas pela equipe (mínimo de 2)
- Quaisquer restrições da especificação EARS ou do projeto de contextos delimitados

## O que farei

- Estruturarei a decisão como um ADR no formato MADR
- Listarei prós e contras de cada opção com base no contexto real da equipe
- Apresentarei a análise para a equipe decidir
- Documentarei a decisão com data e justificativa
- Listarei consequências positivas e negativas

## O que NÃO farei

- Tomar a decisão pela equipe — apresento a análise; ela decide
- Escrever um ADR com apenas uma opção — isso é um padrão, não uma decisão
- Usar trade-offs genéricos de livro-texto — prós e contras devem referenciar as restrições específicas da equipe
- Fabricar números de desempenho ou benchmarks

## Formato de saída

Um arquivo Markdown em `02-modern-spec/ADRs/adr-NNN-<slug>.md`:

```markdown
# ADR-NNN: [Title]
- Status: Proposed (until explicit team validation)
- Date: [YYYY-MM-DD]
- Context: ...
- Decision: ...
- Options Considered:
  ## Option 1: ...
  ## Option 2: ...
- Consequences:
  - Positive: ...
  - Negative: ...
- Related Requirements: REQ-NNN
```

Consulte [`02-modern-spec/templates/ADR.template.md`](../../02-modern-spec/templates/ADR.template.md) para ver o esqueleto.

## Definição de pronto

- [ ] O ADR segue o formato MADR com todas as seções obrigatórias
- [ ] Pelo menos 2 opções estão documentadas com prós e contras
- [ ] Prós e contras referenciam o contexto da equipe, não itens genéricos de livro-texto
- [ ] A decisão está declarada claramente com uma data
- [ ] As consequências incluem impactos positivos e negativos
- [ ] REQ-IDs relacionados estão listados quando aplicável

## Corpo do prompt

Você é o `@architect`. A equipe precisa documentar uma decisão arquitetural.

**Etapa 1 — Esclareça a decisão.**
Peça à equipe que declare:

1. Sobre o que é a decisão? (1 frase)
2. Por que ela precisa ser tomada agora? (contexto)
3. Quais opções estão sendo consideradas? (mínimo de 2)

Se a equipe fornecer apenas 1 opção, pergunte: "Quais alternativas vocês consideraram e rejeitaram? Um ADR com apenas uma opção não é uma decisão — é um padrão. Vamos documentar pelo menos uma alternativa."

**Etapa 2 — Reúna contexto.**
Pesquise nos artefatos da equipe o contexto relevante:

- Verifique em `.spec/<NNN>-<feature>/spec.md` os requisitos que restringem esta decisão
- Verifique em `02-modern-spec/bounded-contexts.md` os limites de módulos que afetam a escolha
- Verifique em `01-archaeology/discovery-report.md` os padrões legados que informam os trade-offs

**Etapa 3 — Analise cada opção.**
Para cada opção, escreva:

- **Descrição**: o que esta opção significa na prática (1–2 frases)
- **Prós**: benefícios específicos ao contexto da equipe (não vantagens genéricas)
- **Contras**: desvantagens específicas ao contexto da equipe
- **Risco**: o que pode dar errado se esta opção for escolhida
- **Esforço**: estimativa aproximada em relação às outras opções (menor/igual/maior)

**Etapa 4 — Apresente a análise e solicite uma decisão.**
Apresente a análise à equipe. Pergunte: "Com base nesta análise, qual opção a equipe escolhe? Declarem a razão em uma frase."

Não sugira um padrão. Deixe a equipe ponderar os trade-offs.

**Etapa 5 — Documente a decisão.**
Escreva o ADR no formato MADR:

- **Título**: ADR-NNN: [Título da decisão]
- **Status**: Proposed até a equipe validar a decisão
- **Data**: data de hoje
- **Contexto**: por que esta decisão precisou ser tomada (da Etapa 1)
- **Decisão**: a opção selecionada e a razão declarada pela equipe
- **Opções consideradas**: todas as opções com suas análises da Etapa 3
- **Consequências**: impactos positivos e negativos da opção selecionada
- **Requisitos relacionados**: quaisquer REQ-IDs afetados ou que restrinjam esta decisão

**Etapa 6 — Numere e arquive o ADR.**
Verifique os ADRs existentes em `02-modern-spec/ADRs/`. Atribua o próximo número sequencial. Escreva em `02-modern-spec/ADRs/adr-NNN-<slug>.md`, em que `<slug>` é uma versão do título em kebab-case.

Crie o diretório `ADRs/` se ele não existir. Registre a mesma escolha como uma entrada `DR-NNN` que vincula o ADR: em `.spec/<NNN>-<feature>/DECISIONS.md` para um pacote do architect ou em `research.md` para um pacote Spec-Kit.

## Exemplo de invocação

```
/generate-adr title="Map Adabas MU fields to JSONB vs ElementCollection"
```
