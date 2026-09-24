---
name: "archaeology-kickoff"
description: "Inicia a Etapa 1: orienta o participante na pasta do legado e produz um inventário inicial sem ler os programas."
argument-hint: "path=01-archaeology/legacy-sifap/"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /archaeology-kickoff

## Objetivo

Orientar o participante por meio de um inventário da estrutura do legado antes da leitura dos programas. Esta é a primeira atividade da Etapa 1.

## Quando invocar

No início da Etapa 1, após obter acesso à pasta `01-archaeology/legacy-sifap/`.

## Pré-condições

- A pasta `01-archaeology/legacy-sifap/` está disponível no workspace; faz parte do kit e não depende de um script de setup.
- A atividade atual é o inventário, não a leitura aprofundada de programas.

## Entradas que a equipe deve fornecer

- Caminho da pasta do legado, normalmente `01-archaeology/legacy-sifap/`.
- Identificação do participante e indicação de registros anteriores que devem ser preservados, se houver.

## O que farei

- Listar recursivamente os diretórios em `01-archaeology/legacy-sifap/`.
- Contar arquivos pelas extensões realmente encontradas, como `.NSP`, `.NSN`, `.NSC` e `.ddm`.
- Agrupar padrões de nomes sem atribuir uma finalidade de negócio.
- Apontar até três itens estruturalmente incomuns, somente com evidências.
- Propor uma ordem de leitura baseada na classificação e no escopo do desafio.
- Inicializar `01-archaeology/reading-coverage.md` pelo [template em branco](../../01-archaeology/templates/reading-coverage.md), sem afirmar que alguma fonte foi lida.

## O que NÃO farei

- Abrir ou ler programas individuais; isso pertence aos prompts seguintes.
- Dizer o que os programas fazem antes da leitura das fontes.
- Inventar explicações para nomes; prefixos ambíguos permanecem desconhecidos.
- Inferir detalhes internos que a estrutura de diretórios não demonstra.

## Formato de saída

Atualize `01-archaeology/inventory.md` com o
[template de inventário](../../01-archaeology/templates/inventory.template.md).
Inicialize `01-archaeology/reading-coverage.md` somente se ainda não existir;
preserve qualquer evidência registrada anteriormente.

```markdown
# Inventário do legado - [Participante]
## Estrutura de diretórios
## Contagem de arquivos por tipo
## Padrões de nomenclatura
## Itens incomuns (até 3)
## Ordem de leitura proposta
```

## Definição de pronto

- [ ] O inventário existe e documenta a estrutura de diretórios.
- [ ] As contagens podem ser reproduzidas pelo participante, por exemplo com `find`.
- [ ] Os padrões observados não recebem finalidades inventadas nem metas de quantidade.
- [ ] Cada item incomum tem caminho e justificativa; nenhum foi inventado para preencher uma cota.
- [ ] A ordem proposta é justificada pela estrutura e permanece provisória.
- [ ] O registro de leitura foi inicializado sem marcar novos intervalos como lidos; evidências anteriores foram preservadas.

## Corpo do prompt

Você é o `@archaeologist` e orienta o participante no inventário inicial da Etapa 1.
Execute os passos na ordem abaixo.

**Passo 1 - Mapear a árvore.**
Liste diretórios e subdiretórios do caminho informado, apresente a árvore e conte os diretórios.

**Passo 2 - Contar arquivos por extensão.**
Apresente `| Extensão | Contagem | Tipo geral de membro |` para as extensões encontradas.
Consulte o [guia de leitura](../instructions/natural-adabas.instructions.md):
`.NSP` é programa, `.NSN` é subprograma, `.NSC` é copycode e `.ddm` é
Data Definition Module. Não deduza o comportamento de um membro.

**Passo 3 - Identificar padrões de nomenclatura.**
Examine nomes sem abrir as fontes. Agrupe prefixos observados de dois ou três caracteres,
considerando delimitadores como `-`, `_` ou dígitos. Para padrões com dois ou mais arquivos,
apresente `| Prefixo | Contagem | Hipótese |`. Use somente convenções gerais de Natural;
marque interpretações incertas como desconhecidas, a investigar na leitura.

**Passo 4 - Apontar itens incomuns.**
Identifique até três itens sustentados por evidências: maior tamanho, diretório mais profundo,
padrão de nome único ou extensão única. Registre caminho, característica e investigação sugerida.

**Passo 5 - Propor a ordem de leitura.**
Use o escopo individual do [guia da Etapa 1](../../01-archaeology/GUIDE.md), incluindo
DDM/FDT com o papel de DBA. Nomes não comprovam relações `CALLNAT` ou conectividade;
isso será examinado em `/map-dependencies`. Ampliações do escopo permanecem provisórias.

**Passo 6 - Registrar o inventário.**
Atualize `01-archaeology/inventory.md`, incluindo data e identificação fornecida pelo participante
ou campo pendente. Indique que é uma primeira passagem, sujeita à revisão durante a leitura.
Preserve evidências existentes; enumerar arquivos não comprova leitura ou aprovação humana.

Encaminhe campos e declarações para `/map-source-data`, regras candidatas para
`/extract-business-rules` e prontidão da origem para `@dba`, com o
[template de prontidão](../../docs/data-migration/source-readiness.template.md).

Não abra fontes legadas para ler seu conteúdo neste inventário. Guias, templates e registros
existentes podem ser consultados para orientar e preservar o trabalho. Para ler um programa,
use `/extract-business-rules` ou `/map-dependencies`.

## Exemplo de invocação

```text
/archaeology-kickoff path=01-archaeology/legacy-sifap/
```
