# Modelo: mapeamento origem-destino

> **Caminho:** [Kit da equipe](../../README.md) > [Migração de dados](../DATA-MIGRATION.md) > **Mapeamento**

**Preencha a partir do mapa de dados e do dicionário de declarações da Etapa 1 da equipe; nenhum modelo de destino do SIFAP é fornecido.**

| Campo | Valor |
|---|---|
| Versão da fonte / referências do mapa de dados e do dicionário | <!-- preencher --> |
| Referência da funcionalidade / dos requisitos / do design | <!-- preencher --> |
| DBA / arquiteto revisor / estado da aprovação | <!-- preencher --> |

## Linhas de mapeamento

| Arquivo / campo / evidência de origem | Formato lógico e representação física | Responsável / campo / tipo no destino | Política de conversão, nulos e precisão | Linhagem de chave de origem / relacionamento / ocorrência | Regra de validação / rejeição |
|---|---|---|---|---|---|
| <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Ambiguidades que exigem revisão

| Questão | Evidências conflitantes | Possível perda de dados ou mudança de comportamento | Responsável / decisão necessária |
|---|---|---|---|
| <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Testes de mapeamento

| Linha de mapeamento / REQ-ID | Cenário | Resultado esperado conforme a evidência | Referência / status do teste |
|---|---|---|---|
| <!-- preencher --> | <!-- preencher: limites, nulos, zeros à esquerda, valores inválidos, ordem MU/PE --> | <!-- preencher --> | <!-- preencher --> |

- [ ] Todo campo de origem pertinente tem um destino ou tratamento explícito aprovado; nenhum descarte silencioso.
- [ ] Identificadores de origem, precisão decimal, semântica de datas/nulos e significado de MU/PE são preservados.
- [ ] Comprimentos físicos em bytes não são confundidos com precisão numérica.
- [ ] Escolhas e exceções de normalização foram revisadas com os arquitetos.
- [ ] Significados desconhecidos permanecem bloqueados até que evidências ou uma decisão registrada os resolvam.
