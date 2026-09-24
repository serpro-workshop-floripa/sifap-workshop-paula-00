# Modelo: apoio ao plano de migração

> **Caminho:** [Kit da equipe](../../README.md) > [Migração de dados](../DATA-MIGRATION.md) > **Plano de migração**

**O participante preenche este documento na Etapa 2 com `@dba` e `@architect`, solicitando a revisão do plano em texto livre; vincule-o no `plan.md` formal da funcionalidade.**

| Campo | Decisão do participante |
|---|---|
| Funcionalidade / REQ-IDs / especificação e plano formais | <!-- preencher --> |
| Papéis abrangidos (DBA / Arquitetura / QA / Desenvolvedor / PO) | <!-- preencher --> |
| Prontidão da fonte e evidências de arqueologia | <!-- preencher --> |
| População autorizada e escopo da consulta | <!-- preencher --> |
| Status da aprovação e bloqueios | <!-- preencher: não aprovar previamente --> |

## Contrato de extração

| Propriedade | Decisão / evidência / informação ausente |
|---|---|
| Versão da fonte, limite do snapshot, arquivos relacionados e escritas concorrentes | <!-- preencher --> |
| Interface, formato e versão de extração compatíveis | <!-- preencher --> |
| Layout, codificação, chaves de origem, manifesto e verificações de integridade | <!-- preencher --> |
| Validação de completude e armazenamento restrito autorizado | <!-- preencher --> |

## Design de migração e recuperação

| Questão | Abordagem planejada | Requisito / evidência aplicável | Responsável |
|---|---|---|---|
| Mapeamento origem-destino e linhagem | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Versão do schema e responsabilidade pelo módulo | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Staging, validação e ordem de carga ciente das dependências | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Rejeições e correção aprovada | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Limites de lote/transação e prevenção de duplicidades | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Checkpoints, interrupção, replay e retomada | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Recuperação do destino e proteção de dados não relacionados | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Compatibilidade da aplicação e limite de cutover | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Verificação planejada antes da implementação

| Verificação | Método de teste / inspeção | Regra de aceitação esperada | Tarefa / autoverificação |
|---|---|---|---|
| Cobertura completa das chaves de origem e contabilização dos registros | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Preservação de campos/relacionamentos/ocorrências | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Agregados financeiros acordados | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Listagem/pesquisa/detalhe autorizados para todos os beneficiários | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Nova execução/retomada e recuperação do destino | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

- [ ] Os requisitos formais mantêm `REQ-NNN`, critérios de aceitação e `source_legacy:`.
- [ ] As responsabilidades de DBA, Arquitetura, QA e PO foram revisadas durante a autoverificação de dados C2.
- [ ] Decisões ausentes de extração, mapeamento ou aceitação permanecem como bloqueios.
