# Modelo: evidências de reconciliação e consulta

> **Caminho:** [Kit da equipe](../../README.md) > [Migração de dados](../DATA-MIGRATION.md) > **Reconciliação**

**O DBA registra a execução real; o QA verifica de forma independente e o PO aceita os resultados observados. Deixe os resultados em branco até a execução.**

| Campo | Evidência da execução |
|---|---|
| Versão da fonte / snapshot / integridade do manifesto | <!-- preencher --> |
| Execução do pipeline / versão do mapeamento / versão do schema de destino | <!-- preencher --> |
| População autorizada | <!-- preencher --> |
| DBA / revisor de QA / data da execução | <!-- preencher --> |
| Referência de evidência restrita | <!-- preencher: sem registros brutos nem credenciais de acesso --> |

## Contabilização dos registros

| Arquivo de origem / unidade da população | Registros de origem | Registros no staging | Registros de origem aceitos | Registros de origem rejeitados | Diferença inexplicada / destinação |
|---|---|---|---|---|---|
| <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

Compare as destinações da origem, não contagens de tabelas de destino sem relação.
Explique qualquer expansão de linhas um-para-muitos por meio do mapeamento aprovado e da linhagem das chaves de origem.

## Reconciliação independente

| Verificação | Expectativa / método da origem | Resultado real no destino | Evidência / revisor | Aprovado, reprovado ou não executado |
|---|---|---|---|---|
| Conjuntos completos de chaves, duplicidades e linhagem da origem | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Campos obrigatórios, tipos, precisão, datas, nulos e zeros à esquerda | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Valores, status e períodos de referência de benefícios e pagamentos, registro a registro | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Relacionamentos e ocorrências/ordem de MU/PE | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Verificações de agregados acordadas, como totais por programa, status e período de referência | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Consulta na aplicação

| Fluxo / REQ-ID | Cenário autorizado | Cobertura da população completa ou das páginas | Resultado observado / evidência | Lacuna / responsável |
|---|---|---|---|---|
| Listagem, incluindo páginas subsequentes | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Pesquisa | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Detalhes e dados relacionados necessários | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Comparação entre legado e moderno para beneficiários comuns e casos extremos | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Acesso não autorizado / tratamento de dados sensíveis | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Nova execução, retomada e recuperação

| Cenário | Contexto de teste isolado | Resultado observado | Evidência / revisor |
|---|---|---|---|
| Nova execução do mesmo snapshot sem duplicidades | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Retomada da carga interrompida ou reinício controlado | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| Recuperação do destino sem alterar a origem nem dados não relacionados | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Aceitação

| Decisão | Resultado / evidência / responsável |
|---|---|
| Rejeições ou diferenças não resolvidas | <!-- preencher --> |
| Beneficiários não consultáveis | <!-- preencher --> |
| Revisão do DBA e do QA independente | <!-- preencher --> |
| Aceitação do PO ou itens bloqueadores | <!-- preencher --> |
| Retenção e limpeza de evidências restritas | <!-- preencher --> |

- [ ] Todo registro de origem está contabilizado e as diferenças inexplicadas são zero.
- [ ] Os valores legados necessários, incluindo valores de benefícios e pagamentos, correspondem à origem registro a registro, não apenas nos totais.
- [ ] Rejeições não resolvidas e lacunas de beneficiários foram solucionadas antes de declarar a migração completa.
- [ ] Todos os beneficiários autorizados podem ser consultados, não apenas amostras.
- [ ] Nova execução/retomada e recuperação do destino foram testadas.
- [ ] Revisão e aceitação refletem evidências reais, não aprovações copiadas.
