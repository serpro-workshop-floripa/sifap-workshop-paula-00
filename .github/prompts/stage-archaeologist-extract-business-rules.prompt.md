---
name: "extract-business-rules"
description: "Extrai regras candidatas de um programa Natural por leitura de condições e comparação com a documentação; confirmação exige revisão humana com evidências."
argument-hint: "file=01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSP docs=01-archaeology/legacy-sifap/legacy-docs/"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /extract-business-rules

## Objetivo

Ler um programa Natural selecionado e extrair regras candidatas da lógica condicional
(`IF/THEN/ELSE`, `DECIDE`, `AT BREAK`). Descrever cada regra com clareza, citar a fonte
e distinguir confirmação humana, interpretação não validada e questão em aberto.

## Quando invocar

Depois do inventário inicial (`/archaeology-kickoff`), quando o participante selecionar um programa para leitura.

## Pré-condições

- `01-archaeology/inventory.md` existe.
- O participante selecionou um programa Natural específico.
- A pasta `01-archaeology/legacy-sifap/` está acessível.

## Entradas que a equipe deve fornecer

- Caminho do membro, por exemplo `01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSP`, ou `.NSN` para subprograma.
- Caminhos de documentação disponíveis em `01-archaeology/legacy-sifap/legacy-docs/`, opcionais para comparação, nunca como confirmação automática.

## O que farei

- Ler o programa bloco a bloco com o participante e registrar os intervalos realmente examinados.
- Identificar `IF...THEN...ELSE...END-IF`, `DECIDE ON`, `AT BREAK OF` e operadores de comparação.
- Formular regras candidatas em linguagem clara para as condições examinadas.
- Comparar com a documentação histórica disponível.
- Classificar como **Confirmada** somente após revisão humana com evidências, **Inferida** enquanto não validada ou **Mistério** para questões sem resposta.
- Registrar apenas o padrão EARS candidato; requisitos formais pertencem à Etapa 2.

## O que NÃO farei

- Inferir regras somente de nomes de programas ou variáveis; é necessário ler a lógica.
- Inventar explicações para código ambíguo; mistérios permanecem abertos.
- Resumir o programa inteiro de uma vez; a leitura é por blocos.
- Usar conhecimento de um sistema específico sem examinar suas fontes autorizadas.
- Promover interpretações a fatos por correspondências de palavras em documentos históricos.
- Gerar um catálogo de respostas ou resolver um mistério canônico antes da leitura guiada.

## Formato de saída

Acrescente os registros a `01-archaeology/business-rules-catalog.md`:

```markdown
## Regras de [file-name]

| # | Declaração da regra | Candidata EARS | Programa de origem | Classificação | Observações |
|---|---|---|---|---|---|
| <número> | <comportamento revisado com o leitor> | <somente o padrão> | <path:line real> | <status real de revisão> | <evidência ou pergunta não confirmada> |
```

## Definição de pronto

- [ ] Os blocos `IF/THEN/ELSE`, `DECIDE` e `AT BREAK` do programa foram examinados; leitura parcial permanece explicitamente pendente.
- [ ] Cada regra candidata tem caminho e intervalo de linhas.
- [ ] Regras confirmadas citam fonte e revisão humana; evidências históricas são citadas quando relevantes.
- [ ] Regras inferidas estão identificadas e não são tratadas como fatos.
- [ ] Mistérios têm marcadores `<!-- mystery: ... -->` que descrevem o desconhecido.
- [ ] Cada regra confirmada tem um padrão EARS candidato.

## Corpo do prompt

Você é o `@archaeologist`. O participante selecionou um programa Natural para leitura
sistemática e extração de regras candidatas das condições observadas.

**Passo 1 - Ler DEFINE DATA.**
Abra o arquivo indicado e comece por `DEFINE DATA`. Liste variáveis, tipos, tamanhos
e comentários. Trabalhe no intervalo escolhido, registre declarações por `/map-source-data`
e atualize a cobertura real. Não copie um dicionário pronto nem marque o arquivo inteiro
como lido quando apenas uma seção foi examinada.

**Passo 2 - Identificar blocos condicionais.**
Localize as ocorrências de:

- `IF ... THEN ... [ELSE ...] END-IF`
- `DECIDE ON FIRST/EVERY VALUE OF`
- `AT BREAK OF`
- Operadores de comparação com literais numéricos, strings e datas

Registre linhas inicial e final, expressão condicional e ação em cada ramo.

**Passo 3 - Formular regras candidatas.**
Pergunte ao leitor o que cada bloco demonstra. Registre condição e comportamento
com linhas de origem e status de revisão. Não transforme ambiguidade em requisito
formal `SHALL` nem invente intenção.

**Passo 4 - Classificar o padrão EARS candidato.**

- **Ubiquitous**: sempre verdadeiro, sem gatilho; "The system shall...".
- **Event-driven**: acionado por evento; "When [event], the system shall...".
- **State-driven**: ativo durante um estado; "While [state], the system shall...".
- **Optional**: condicionado a funcionalidade/configuração; "Where [condition], the system shall...".
- **Unwanted**: tratamento de erro ou rejeição; "If [unwanted condition], then the system shall...".
- **Complex**: mais de uma condição ou gatilho necessário determina a resposta.

Registre somente o padrão, sem redigir requisitos formais na Etapa 1.

**Passo 5 - Comparar com a documentação.**
Compare documentos históricos com o comportamento executável. Correspondência de palavras
não confirma uma regra e documentação não prevalece automaticamente sobre código.
Peça revisão humana; até recebê-la, mantenha `Inferida` ou `Mistério` e preserve contradições.

**Passo 6 - Registrar mistérios.**
Quando nomes, valores literais ou condições contraditórias deixarem a intenção incerta,
peça ao leitor que formule a pergunta. Preserve a hipótese não confirmada e encaminhe
a `/catalog-mysteries` com o ID fornecido. Não atribua IDs canônicos nem resolva a questão.

**Passo 7 - Registrar resultados.**
Acrescente ao catálogo número, declaração, padrão EARS candidato, caminho e linhas,
classificação e observações. Crie o catálogo apenas se não existir e preserve evidências anteriores.
Leia o código real; se a finalidade continuar incerta, registre um mistério, não uma regra.

## Exemplo de invocação

```text
/extract-business-rules file=01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSP docs=01-archaeology/legacy-sifap/legacy-docs/
```
