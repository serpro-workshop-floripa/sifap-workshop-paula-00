---
name: "doc-style-lint"
description: "Use ao revisar documentação quanto a estilo, clareza, linguagem inclusiva, legibilidade ou conformidade com os guias de estilo da Microsoft ou do Google. Acione para pedidos como \"revise este documento\", \"aplique o guia de estilo\", \"reescreva em linguagem simples\" ou \"verifique linguagem inclusiva\"."
---
# Revisão de estilo da documentação

## Quando invocar

- "Valide este README conforme nosso guia de estilo."
- "Reescreva esta documentação de API em linguagem simples."
- "Procure termos excludentes e jargão."

## Procedimento

### Voz e tom

- Use **voz ativa**: "O sistema armazena o arquivo", não "O arquivo é armazenado pelo sistema".
- Use **presente**: "Retorna uma resposta JSON", não "Retornará uma resposta JSON".
- Use **segunda pessoa** ("você") em guias práticos e **terceira pessoa** em documentação de referência.
- Use headings em **sentence case**, não em Title Case.

### Clareza

- Apresente uma ideia por frase.
- Adote 25 palavras por frase como limite prático.
- Use no máximo cinco frases por parágrafo.
- Evite palavras que minimizam o esforço, como "apenas", "simplesmente" e "facilmente".
- Não use travessão. Prefira vírgulas, parênteses ou dois-pontos.

### Linguagem inclusiva

Substitua:

- "master/slave" por "primary/replica" ou "leader/follower"
- "whitelist/blacklist" por "allowlist/blocklist"
- "guys" por "pessoal", "todas as pessoas" ou "equipe"
- "crazy/insane", como intensificadores, por "significativo" ou "incomum"
- "dummy", em nomes de variáveis, por "example" ou "sample"
- "sanity check" por "quick check" ou "verification"

### Estrutura

- Comece pelo resultado, não pelo contexto.
- Declare no início o que a pessoa aprenderá.
- Resuma documentos longos ao final.
- Use headings descritivos para facilitar a leitura rápida.

### Links

- Escreva textos de links que descrevam o destino. Não use "clique aqui" ou "neste link".
- Use URLs absolutas para fontes externas e relativas para conteúdo interno.
- Verifique links na CI.

### Exemplos de código

- Teste cada trecho executável.
- Use exemplos realistas, não `foo/bar/baz`.
- Identifique placeholders com clareza, por exemplo, `<YOUR-API-KEY>`.

### Números e unidades

- Use algarismos para 10 ou mais e palavras de zero a nove, conforme o estilo Microsoft.
- Use unidades métricas e inclua conversões para públicos diversos.
- Sempre informe a unidade, como "100 MB", não "100".

### Etapas da revisão

1. Leia uma vez como o público pretendido. Avalie a extensão e o nível de detalhe.
2. Execute as verificações automatizadas configuradas no repositório, como Vale, Alex.js ou markdownlint. Informe ferramentas ausentes sem instalá-las.
3. Aplique as regras de estilo seção por seção.
4. Teste cada exemplo de código.
5. Confirme se uma pessoa recém-chegada entenderia o documento no primeiro dia.

### Antipadrões

- Revisar sem executar primeiro os linters automatizados.
- Priorizar estilo em detrimento do conteúdo.
- Substituir a voz da autoria em vez de refiná-la.
- Ignorar acessibilidade, como texto alternativo, níveis de headings e textos de links.

## Modelo de saída

```markdown
## Revisão de estilo: <Documento>

### Resumo
- Legibilidade (nível Flesch-Kincaid): 11 (alvo: <=12)
- Voz passiva: 8% (alvo: <10%)
- Problemas de linguagem inclusiva: 2
- Links quebrados: 0
- Exemplos de código não testados: 3

### Recomendações (10 principais)
| ID | Local | Problema | Correção |
|----|-------|----------|----------|
| 01 | Seção de instalação | Voz passiva | Reescrever em voz ativa |
| 02 | Solução de problemas | "guys" | Substituir por "equipe" |
| 03 | Referência da API | "simply call" | Remover "simply" |
```

## Gate de qualidade

- [ ] O documento passa nos linters configurados no repositório, como Vale, Alex.js ou markdownlint, antes da revisão humana.
- [ ] A voz é ativa e está no presente, com headings em sentence case.
- [ ] Nenhum termo excludente permanece.
- [ ] Cada exemplo de código foi testado e cada link resolve corretamente.
