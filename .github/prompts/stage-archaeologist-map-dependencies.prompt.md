---
name: "map-dependencies"
description: "Mapeia dependências programa a programa (CALLNAT, INCLUDE) e programa a dados (acesso a DDM) para um escopo selecionado."
argument-hint: "scope=01-archaeology/legacy-sifap/natural-programs/ recursive=true"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /map-dependencies

## Objetivo

Construa um grafo de dependências para um escopo selecionado da base de código legado, rastreando chamadas CALLNAT, diretivas INCLUDE e padrões de acesso a dados DDM. Gere um diagrama Mermaid em que cada aresta cite sua fonte.

## Quando invocar

Depois que a equipe concluir o inventário inicial e quiser entender como os programas se relacionam entre si e com os dados.

## Pré-condições

- `01-archaeology/inventory.md` existe
- A pasta `01-archaeology/legacy-sifap/` está acessível
- A equipe selecionou um escopo: um único programa, um fluxo batch ou uma família de transações

## Inputs que a equipe deve fornecer

- O escopo a analisar: path de um arquivo específico, um diretório ou um conjunto de arquivos
- Se o rastreamento deve ser recursivo (seguir os alvos de CALLNAT até suas próprias chamadas CALLNAT) ou de apenas um nível

## O que farei

- Pesquisarei todas as declarações `CALLNAT`, `PERFORM` e `INCLUDE` no escopo
- Para cada CALLNAT, identificarei o nome do subprograma de destino e verificarei se ele existe na base de código
- Pesquisarei declarações de acesso a dados: `READ`, `FIND`, `GET`, `STORE`, `UPDATE`, `DELETE` e `HISTOGRAM`, incluindo suas referências a DDM/arquivo de destino
- Construirei um grafo Mermaid com dois tipos de aresta: programa a programa e programa a dados
- Listarei referências quebradas (CALLNATs para programas que não existem na pasta)
- Registrarei no registro de leitura somente intervalos da fonte realmente revisados com a equipe; encaminharei a semântica dos campos para `/map-source-data`

## O que NÃO farei

- Inventar conexões ausentes no código-fonte — toda aresta deve ter arquivo e número de linha
- Adivinhar o que um alvo de CALLNAT faz com base no nome — mapeio apenas a aresta, não o comportamento do alvo
- Presumir qualquer estrutura de programa — leio o que realmente existe
- Seguir referências fora da pasta `01-archaeology/legacy-sifap/`

## Formato de saída

Um arquivo Mermaid em `01-archaeology/dependency-map.mmd` e um arquivo Markdown de apoio em `01-archaeology/dependency-map.md`:

```markdown
# Dependency Map — [Scope Description]
## Mermaid Diagram
## Program-to-Program Edges
| Source | Target | Type | File | Line |
## Program-to-Data Edges
| Program | DDM/File | Operation | File | Line |
## Broken References
## Observations
```

## Definição de pronto

- [ ] O arquivo Mermaid existe e renderiza um grafo válido
- [ ] Cada nó do grafo corresponde a um arquivo real na base de código
- [ ] Cada aresta cita um arquivo-fonte e um número de linha
- [ ] Referências quebradas (alvos não encontrados) estão listadas explicitamente
- [ ] Arestas de acesso a dados distinguem as operações READ, FIND, STORE, UPDATE e DELETE

## Corpo do prompt

Você é o `@archaeologist`. A equipe quer mapear dependências em parte da base de código legado. Você rastreará todas as relações entre programas e entre programas e dados.

**Etapa 1 — Identifique o escopo.**
Confirme o escopo com a equipe. É um único programa (rastrear sua árvore de chamadas), um diretório (todos os programas nele) ou um conjunto nomeado de arquivos? Registre o limite do escopo — não pesquise fora dele, a menos que a equipe solicite explicitamente rastreamento recursivo.

**Etapa 2 — Pesquise declarações CALLNAT.**
No escopo, pesquise todas as ocorrências de `CALLNAT`. Para cada uma, extraia:

- O programa chamador (path do arquivo)
- O nome do subprograma de destino (o argumento string de CALLNAT)
- O número da linha
- Os parâmetros passados (liste-os; não os interprete)

Verifique se cada subprograma de destino existe como arquivo na pasta `01-archaeology/legacy-sifap/`. Se não existir, adicione-o à lista de referências quebradas.

**Etapa 3 — Pesquise diretivas INCLUDE.**
No escopo, pesquise todas as declarações `INCLUDE`. Para cada uma, extraia:

- O programa que faz a inclusão (path do arquivo)
- O nome do copycode
- O número da linha

Verifique se o copycode existe na base de código.

**Etapa 4 — Pesquise chamadas PERFORM.**
No escopo, localize cada `PERFORM` e sua definição real. Uma sub-rotina interna
resolvida é uma dependência intraprograma. Um alvo externo ou não resolvido
precisa de sua própria entrada de evidência/referência; não presuma que todo
`PERFORM` é interno nem fabrique uma sub-rotina ausente.

**Etapa 5 — Pesquise declarações de acesso a dados.**
No escopo, pesquise `READ`, `FIND`, `GET`, `STORE`, `UPDATE`, `DELETE` e `HISTOGRAM`. Para cada uma, extraia:

- O programa que realiza o acesso
- O DDM ou número de arquivo referenciado
- O tipo de operação
- O número da linha
- Qualquer descritor usado em FIND ou READ LOGICAL (a chave de pesquisa)

**Etapa 6 — Construa o grafo Mermaid.**
Crie um fluxograma Mermaid com:

- Nós de programa (retângulos)
- Nós de DDM/dados (cilindros com a sintaxe `[(name)]`)
- Arestas CALLNAT (setas contínuas rotuladas como "CALLNAT")
- Arestas INCLUDE (setas tracejadas rotuladas como "INCLUDE")
- Arestas de acesso a dados (setas para nós de dados rotuladas com a operação)

Use o tema neutro do Mermaid do [guia de estilo da documentação](../../docs/DOC-STYLE-GUIDE.md):
preenchimento dos nós `#F5F5F5`, contorno/texto `#171717` e cor das linhas `#525252`.

**Etapa 7 — Documente referências quebradas e observações.**
Liste todos os alvos de CALLNAT ou INCLUDEs que referenciem arquivos não encontrados na base de código. Esses são sinais importantes — podem indicar arquivos ausentes, programas renomeados ou chamadas a sistemas externos.

Adicione uma seção de observações registrando o total de programas no escopo, o total de arestas encontradas, o programa mais conectado (maior grau), o DDM mais acessado e qualquer programa isolado (sem arestas de entrada ou saída).

**Etapa 8 — Escreva os arquivos de saída.**
Escreva o diagrama Mermaid em `01-archaeology/dependency-map.mmd` e a documentação de apoio em `01-archaeology/dependency-map.md`.

Preserve o registro existente da equipe e atualize o registro de leitura somente
para intervalos realmente examinados. Use `/map-source-data` para evidências de
DDM/FDT e declarações; não infira um modelo PostgreSQL a partir das arestas de
dependência nem revele respostas de mistérios.

Toda aresta deve citar um arquivo-fonte e um número de linha. Se não encontrar uma fonte para uma aresta, não a inclua. Não fabrique conexões.

## Exemplo de invocação

```
/map-dependencies scope=01-archaeology/legacy-sifap/natural-programs/ recursive=true
```
