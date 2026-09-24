---
description: "Use ao escrever repositórios, mudanças de schema Flyway, migração Adabas para PostgreSQL, reconciliação, SQL, índices e alterações seguras para recuperação."
applyTo: "backend/src/main/java/**/infrastructure/**,backend/src/main/resources/db/migration/**"
---

# Convenções de banco de dados — Schema, migração e repositórios

Este arquivo orienta persistência e migrações no PostgreSQL 16. Limites de entidades estão em [modular-monolith.instructions.md](modular-monolith.instructions.md), leitura legada em [natural-adabas.instructions.md](natural-adabas.instructions.md) e ownership das etapas em [DATA-MIGRATION.md](../../docs/DATA-MIGRATION.md).

## Evolução de schema e migração de registros

Migrações Flyway são versionadas, progressivas e imutáveis depois de aplicadas em banco compartilhado. Nomeie-as `V<n>__<snake_case_description>.sql`. Use uma alteração lógica por arquivo. Nunca edite checksum aplicado nem esconda drift com `IF NOT EXISTS` indiscriminado.

O histórico de schema não é log de migração de registros. A carga Adabas exige snapshot aprovado, mapeamentos, linhagem de chaves, manifesto de execução, checkpoint/resume, prevenção de duplicidade, contabilização e recuperação. Separe transferências grandes das migrações de schema.

- Comece de uma origem populada, autorizada e verificada; não substitua por seeds PostgreSQL.
- Preserve o input restrito e imutável.
- Valide fronteiras e reporte rejeições explicitamente.
- Defina replay/resume para o mesmo snapshot e proteja dados de destino não relacionados.
- QA verifica chaves, campos, relações, ocorrências MU/PE e agregados antes de C3.

## Valores monetários e fidelidade à origem

Mapeie valores monetários e packed decimals para PostgreSQL `NUMERIC(precision, scale)` e Java `BigDecimal`, nunca `float`, `double`, `real` ou `money`. Determine dígitos, sinal e encoding por DDM/FDT, programas e runtime. Preserve zeros à esquerda, datas, fuso, null/suppression e valores vazios.

Normalize MU/PE em tabelas relacionadas, salvo decisão revisada baseada em evidências. Preserve identidade e ordem das ocorrências quando exigido.

## Repositórios e consultas

Use queries derivadas do Spring Data ou JPQL `@Query` com parâmetros nomeados. Queries nativas também vinculam valores. Identificadores e ordenação exigem allowlists.

- Mantenha transações da aplicação nos serviços.
- Retorne `Optional<T>` para registros possivelmente ausentes.
- Use projections e evite campos sensíveis desnecessários.
- Forneça paginação estável, limitada e autorizada.
- Teste toda a população aprovada, não só uma amostra.
- Preserve auditoria append-only.

## Índices e constraints

Declare constraints e índices revisados em migrações versionadas. Uniqueness, foreign keys e `CHECK` exigem evidência. Escolha índices pela query real, seletividade, plan e custo de escrita. Para tabelas grandes, avalie locks e `CREATE INDEX CONCURRENTLY`, documentando configuração Flyway e recuperação.

## Alterações seguras para recuperação

Use expand/backfill/contract quando a compatibilidade exigir:

| Fase | Trabalho | Condição de segurança |
|---|---|---|
| Expand | Adicionar estruturas compatíveis | A aplicação existente continua operando |
| Backfill/migrate | Transferir em lotes retomáveis | Validação, contabilização e checkpoints explícitos |
| Contract | Remover estruturas antigas após verificação | Readers migrados e janela de recuperação revisada |

Registre estratégia testada de recuperação ou correção progressiva. Não suponha `flyway undo`. Teste recuperação de dados separadamente e nunca altere a origem para fazer a reconciliação passar.

## Segurança de execução e performance

Analise plans com dados representativos. `EXPLAIN ANALYZE` executa a instrução; use apenas queries autorizadas e somente leitura em ambiente isolado. Higienize plans e logs.

## Convenções

| Regra | Motivo |
|---|---|
| `V<n>__snake_case.sql` imutável | Mantém histórico auditável |
| Evidências separadas para schema e carga | Flyway não comprova sucesso da migração de registros |
| `NUMERIC` e `BigDecimal` | Preserva valores financeiros |
| Parameter binding e transações em serviços | Protege queries e fronteiras |
| Índices medidos e constraints revisadas | Evita mudanças especulativas |
| Replay/resume e recuperação isolada | Garante movimento confiável |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Crie nova migração progressiva | Edite migração aplicada |
| Carregue o snapshot aprovado | Chame seed de teste de migração |
| Contabilize cada registro da origem | Descarte rejeições silenciosamente |
| Verifique cobertura e autorização | Aceite tela baseada apenas em amostra |
| Teste recuperação com ferramentas reais | Suponha que rollback de schema restaure dados |

## Checklist antes de abrir um PR

- [ ] Definições e mapeamentos rastreiam evidências reais.
- [ ] Migrações aplicadas permanecem imutáveis e pipelines de schema e dados são distintos.
- [ ] Identificadores, decimais, datas, null e MU/PE são preservados.
- [ ] Queries vinculam parâmetros e respeitam autorização.
- [ ] A reconciliação independente não tem diferenças não resolvidas.
- [ ] Replay/resume e recuperação foram testados sem alterar a origem.
- [ ] Registros sensíveis, extracts e credenciais permanecem fora do Git.
