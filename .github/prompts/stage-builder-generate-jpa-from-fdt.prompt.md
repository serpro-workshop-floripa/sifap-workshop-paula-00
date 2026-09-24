---
name: "generate-jpa-from-fdt"
description: "Implementa mapeamentos source-to-target revisados pelo DBA como entities JPA e alterações de schema Flyway, preservando a semântica da fonte e deixando a aceitação da carga de dados para o workflow de migração."
argument-hint: "ddm=01-archaeology/legacy-sifap/adabas-ddms/<DDM>.ddm context=<context> package=<java.package> dateformat=<format>"
agent: "builder"
tools: ["read", "search", "edit", "execute"]
---
# /generate-jpa-from-fdt

## Objetivo

Implementar o mapeamento aprovado da evidência do DDM/FDT de origem e dos
programas em entities JPA e alterações correspondentes de schema Flyway. Não
decida um novo modelo de dados nem use JSONB como padrão para dados MU/PE durante a geração de código.

## Quando invocar

No início da Etapa 3, quando a equipe estiver configurando a camada de dados de um bounded context.

## Pré-condições

- `.spec/<NNN>-<feature>/spec.md`, `plan.md` e `tasks.md` da funcionalidade contêm a propriedade dos dados, os mapeamentos e os requisitos aprovados
- O arquivo DDM está acessível em `01-archaeology/legacy-sifap/adabas-ddms/`
- A equipe selecionou o package de destino com base no design do monólito modular
- O DBA e os arquitetos revisaram a linhagem das chaves de origem, a precisão, a semântica de valores nulos/datas e o tratamento de MU/PE; mapeamentos não resolvidos permanecem como bloqueios

## Inputs que a equipe deve fornecer

- O path do arquivo DDM (por exemplo, `01-archaeology/legacy-sifap/adabas-ddms/DDMXXXXX.ddm`)
- O bounded context e o package Java de destino
- O formato de data usado no sistema legado (por exemplo, packed `YYYYMMDD` ou alpha `YYYY-MM-DD`)
- O mapa de origem real, o dicionário de declarações, o registro source-to-target revisado e os REQ-IDs aplicáveis

## O que farei

- Ler o DDM e o FDT físico disponível como fontes distintas, junto com as declarações dos programas
- Mapear cada campo para o tipo Java/JPA apropriado
- Tratar campos MU usando o mapeamento normalizado revisado; usar JSONB somente com uma exceção aprovada e respaldada por evidências
- Tratar grupos PE como entities `@OneToMany` incorporadas
- Gerar a migration Flyway que cria a tabela PostgreSQL
- Devolver semânticas de campos desconhecidas ao DBA/à Arquitetura, em vez de gerar campos de produção presumidos

## O que NÃO farei

- Inventar significado de negócio para nomes de campos crípticos — semânticas não resolvidas retornam ao DBA/à Arquitetura
- Presumir formatos de data — a equipe deve confirmá-los
- Criar stored procedures — toda a lógica de negócio permanece em Java
- Ignorar campos MU/PE — eles são a parte mais difícil e devem ser tratados explicitamente

## Formato de saída

Dois arquivos:

1. Entity JPA no package de persistência aprovado do módulo backend proprietário.
2. Migration Flyway em `backend/src/main/resources/db/migration/`.

Essas saídas criam o schema, não os registros migrados. Selecione `@dba` e
solicite a execução das tarefas de carga aprovadas e a reconciliação de QA,
conforme o [ciclo de vida dos dados](../../docs/DATA-MIGRATION.md),
para a população source-to-target e a consulta completa de beneficiários.

## Definição de pronto

- [ ] A entity compila sem erros
- [ ] Todo campo de origem mapeado tem seu destino aprovado ou tratamento explícito; não há perda silenciosa
- [ ] Os campos MU seguem o mapeamento normalizado revisado; qualquer exceção JSONB tem evidência e uma ADR
- [ ] Os grupos PE usam `@OneToMany` com uma classe de entity separada
- [ ] A migration Flyway é um DDL PostgreSQL 16 válido
- [ ] Nenhuma semântica não resolvida foi substituída por nomes, tamanhos ou tipos de campo presumidos
- [ ] Campos crípticos são encaminhados para registro humano como questões em aberto quando necessário

## Corpo do prompt

Você é o `@builder`. A equipe precisa criar uma entity JPA a partir de um DDM Adabas.

**Passo 1 — Revise as definições de origem e o mapeamento aprovado.**
Abra o DDM especificado, o FDT disponível, as declarações dos programas e o
registro source-to-target revisado. Extraia as definições mapeadas sem confundir seus formatos:

- Número do nível (01 = nível superior, 02+ = filhos)
- Nome curto (nome Adabas de dois caracteres)
- Nome longo (se presente em comentários ou documentação)
- Formato: A (alpha), N (numeric), P (packed), B (binary), D (date), T (time)
- Tamanho
- Tipo de descriptor: DE (pesquisável), MU (multi-value), PE (periodic group), SU (super-descriptor)

Confirme essas definições com o DBA antes de gerar código. Se o mapeamento
planejado ou a semântica da fonte não estiver resolvido, interrompa a implementação
desse campo e registre o bloqueio; não crie uma coluna presumida com um FIXME.

**Passo 2 — Mapeie os tipos.**
Aplique estas regras de mapeamento:

| Adabas | Java | JPA | Observações |
|--------|------|-----|-------|
| A(n) | `String` | `@Column(length = n)` | |
| Quantidade numérica | Tipo inteiro revisado | `@Column` | Identificadores podem exigir strings para preservar zeros à esquerda |
| Decimal numérico | `BigDecimal` | Precisão e escala revisadas | Verifique os dígitos inteiros e fracionários |
| Packed decimal | `BigDecimal` | Precisão e escala revisadas | O tamanho físico em bytes não é a precisão numérica |
| D | `LocalDate` | `@Column` | Pergunte à equipe qual é o formato da fonte |
| T | `LocalDateTime` | `@Column` | |
| B(n) | `byte[]` | `@Lob` | Raro |
| Campo MU | Tipo de coleção revisado | Tabela relacionada por padrão | JSONB somente com uma exceção revisada |
| Grupo PE | `List<EmbeddedEntity>` | `@OneToMany` | Classe de entity separada |

Implemente a escolha da Etapa 2. Se ainda houver alternativas não decididas,
retorne ao planejamento com `@dba` e `@architect`, usando o
[template de migração](../../docs/data-migration/migration-plan.template.md),
em vez de tomar uma decisão de arquitetura implícita.

**Passo 3 — Trate os grupos PE.**
Para cada grupo PE, crie uma classe `@Entity` separada com:

- Sua própria tabela
- Uma back-reference `@ManyToOne` para a entity pai
- Todos os campos do grupo PE mapeados como no Passo 2
- Um campo de índice que rastreia o número da ocorrência

**Passo 4 — Trate os super-descriptors.**
Implemente somente índices justificados pelo padrão de query aprovado. Um
superdescriptor de origem não implica automaticamente um índice PostgreSQL equivalente:

```java
@Table(indexes = @Index(columnList = "field_a, field_b"))
```

**Passo 5 — Preserve as questões não resolvidas.**
Para qualquer campo pouco claro, devolva sua evidência de origem e ambiguidade ao
DBA e aos arquitetos. Não invente seu significado em inglês, tamanho ou tipo.

Se o campo ainda não estiver em `01-archaeology/mysteries-found.md`, informe à
equipe que uma pessoa deve registrá-lo como questão em aberto com evidência
`path:line`. Não descreva uma resposta, confirme uma hipótese nem altere o status do catálogo.

**Passo 6 — Gere a migration Flyway.**
Escreva um script DDL PostgreSQL 16:

- Nome da tabela derivado do nome da entity (snake_case)
- Tipos de coluna correspondentes aos mapeamentos JPA
- Colunas JSONB para campos MU (se JSONB tiver sido selecionado)
- Tabela separada para grupos PE com uma foreign key
- Chaves, relacionamentos e índices respaldados por evidências e revisados
- Constraints aprovadas no plano; a supressão de valores nulos ou apenas um comentário não estabelece `NOT NULL`

Numere a migration: `V[NNN]__create_[table_name].sql`.

**Passo 7 — Verifique a compilação.**
Garanta que a classe da entity compile. Relate quaisquer problemas.

Execute os testes direcionados existentes de mapeamento/repositório no PostgreSQL.
Mantenha a população da origem, a migração de registros, a reconciliação
independente e as queries reais de beneficiários como verificações obrigatórias
separadas no [ciclo de vida dos dados](../../docs/DATA-MIGRATION.md).

## Exemplo de invocação

```
/generate-jpa-from-fdt ddm=01-archaeology/legacy-sifap/adabas-ddms/<DDM>.ddm context=<context> package=<java.package> dateformat=<format>
```
