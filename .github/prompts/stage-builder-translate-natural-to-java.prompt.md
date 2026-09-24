---
name: "translate-natural-to-java"
description: "Traduz um programa Natural para Java 21 + Spring Boot 3.3 idiomático, preservando a semântica de negócio."
argument-hint: "file=01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSN context=<context> package=<java.package>"
agent: "builder"
tools: ["read", "search", "edit", "execute"]
---
# /translate-natural-to-java

## Objetivo

Traduzir um programa Natural para Java 21 + Spring Boot 3.3 idiomático, preservando a semântica de negócio (não a sintaxe). A saída é Java compilável com Javadoc rastreável até o código-fonte Natural.

## Quando invocar

No início da Etapa 3, quando a equipe começa a implementar bounded contexts com base no design da Etapa 2.

## Pré-condições

- `.spec/<NNN>-<feature>/plan.md` existe com a estrutura de packages exigida
- `.spec/<NNN>-<feature>/spec.md` existe com requisitos EARS
- O bounded context e o package de destino são conhecidos
- O arquivo-fonte Natural está acessível em `01-archaeology/legacy-sifap/`

## Inputs que a equipe deve fornecer

- O path do arquivo do programa Natural (por exemplo, `01-archaeology/legacy-sifap/natural-programs/PGXXXXXX.NSN`)
- O bounded context e o package Java de destino
- Quaisquer requisitos EARS relacionados (REQ-IDs)

## O que farei

- Ler o programa Natural bloco a bloco
- Identificar o propósito de negócio de cada bloco procedural
- Traduzir para Java 21 idiomático (records para DTOs, sealed interfaces, constructor injection)
- Gerar Javadoc vinculado ao arquivo-fonte Natural e ao intervalo de linhas
- Sinalizar lógica órfã (código sem um requisito EARS correspondente) para decisão da equipe
- Escrever e executar testes de comportamento antes de implementar a lógica aprovada correspondente

## O que NÃO farei

- Espelhar a sintaxe Natural linha a linha em Java ("JOBOL" — Java que se parece com Natural)
- Mesclar silenciosamente vários conceitos Natural em uma única classe Java
- Inventar significado de negócio para código pouco claro — a lógica órfã é sinalizada, não interpretada
- Ignorar a leitura prévia dos requisitos EARS — todo bloco traduzido deve ser mapeado para um REQ-ID

## Formato de saída

Arquivos Java no package aprovado em `backend/src/main/java/` e testes
significativos em `backend/src/test/java/`, com rastreabilidade de código-fonte e REQ-ID.

## Definição de pronto

- [ ] Os arquivos Java compilam sem erros
- [ ] Todo método público tem Javadoc que cita o arquivo-fonte Natural e o intervalo de linhas
- [ ] Toda regra de negócio dos requisitos EARS relevantes tem um método correspondente
- [ ] A lógica órfã (código sem um REQ) está documentada com `// ORPHAN: [file:line] - Team decision required`
- [ ] Os testes de comportamento exigidos têm assertions significativas e passam; stubs não implementados ou expectativas não resolvidas não são relatados como concluídos
- [ ] Não há port linha a linha do Natural — a tradução usa recursos idiomáticos do Java 21

## Corpo do prompt

Você é o `@builder`. A equipe selecionou um programa Natural para traduzir para Java.

**Passo 1 — Leia primeiro os requisitos EARS.**
Antes de alterar o arquivo Natural, leia `.spec/<NNN>-<feature>/spec.md` e
identifique todos os requisitos relevantes para esse programa. Liste-os. Esses
requisitos definem o que o código Java *deve* fazer.

**Passo 2 — Leia o programa Natural.**
Abra o arquivo especificado. Leia a seção `DEFINE DATA` para compreender o modelo de dados. Depois, leia a lógica principal bloco a bloco:

- Para cada `IF...THEN...ELSE...END-IF`, identifique a decisão de negócio
- Para cada `READ` ou `FIND`, identifique o padrão de acesso a dados
- Para cada `CALLNAT`, registre a dependência (mas não traduza o destino — essa é uma invocação separada)
- Para cada `PERFORM`, identifique a sub-rotina interna

**Passo 3 — Mapeie os blocos para os requisitos.**
Para cada bloco identificado, encontre o requisito EARS que ele implementa. Se um bloco não tiver requisito correspondente, marque-o como lógica órfã:

```java
// ORPHAN: [natural-file.NSN:L42-58] - No matching REQ. Team decision required: keep, modify, or remove?
```

Pergunte à equipe o que fazer com a lógica órfã antes de prosseguir.

**Passo 4 — Escreva o teste e depois traduza para Java.**
Use `/generate-equivalence-tests` para estabelecer expectativas derivadas do
código-fonte, independentemente da implementação. Escreva primeiro um teste que
falha; a ausência de um oráculo de teste é um bloqueio, não um convite à suposição.

Para cada bloco com requisito correspondente, escreva o equivalente em Java:

- Variáveis de `DEFINE DATA LOCAL` → parâmetros de método ou variáveis locais com tipos apropriados
- `IF...THEN...ELSE` → expressões Java `if/else` ou `switch` (pattern matching do Java 21 quando apropriado)
- `READ LOGICAL BY` → método `findBy*` do Spring Data JPA
- `FIND WITH` → `@Query` JPA com parâmetros nomeados
- `CALLNAT` → chamada de método de serviço (injete a dependência)
- Cálculos de packed decimal → `BigDecimal` com escala e modo de arredondamento explícitos
- Operações com strings → métodos de `String` do Java, observando diferenças de charset

Use recursos idiomáticos do Java 21:

- Records para DTOs e value objects
- Sealed interfaces para discriminated unions quando exigidas pelo domínio
- `Optional` para retornos anuláveis
- Constructor injection (sem `@Autowired` em campos)
- `@Valid` para validação de entrada na camada de controller
- `@Transactional` somente em métodos de serviço, nunca em repositórios

**Passo 5 — Gere Javadoc.**
Todo método público recebe Javadoc que inclui:

```java
/**
 * [Business description].
 *
 * <p>Translated from: {@code [natural-file.NSN#L42-L58]}</p>
 * <p>Implements: REQ-NNN</p>
 */
```

**Passo 6 — Conclua e execute os testes.**
Execute os testes de comportamento e mapeamento escritos para esta alteração.
Verifique resultados de limite, erro e preservação de dados em relação às
expectativas revisadas. Não deixe `TODO`, `fail(...)` ou stubs desabilitados e
declare a tradução como concluída.

**Passo 7 — Verifique o incremento.**
Execute os comandos existentes relevantes de build/teste e registre os resultados
reais. A compilação por si só não comprova equivalência nem uma migração de dados bem-sucedida.

Se uma construção Natural não tiver um recurso idiomático Java claro, apresente duas alternativas à equipe e deixe que ela escolha. Não escolha silenciosamente.

## Exemplo de invocação

```
/translate-natural-to-java file=01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSN context=<context> package=<java.package>
```
