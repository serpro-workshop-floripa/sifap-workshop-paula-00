# Integrações externas

## Seções principais (obrigatórias)

### 1) Inventário de integrações

| Sistema | Tipo (API/DB/fila/etc) | Finalidade | Modelo de autenticação | Criticidade | Evidência |
|---------|------------------------|------------|------------------------|-------------|-----------|
| [nome] | [tipo] | [finalidade] | [autenticação] | [alta/média/baixa] | [arquivo] |

### 2) Armazenamentos de dados

| Armazenamento | Papel | Camada de acesso | Risco principal | Evidência |
|---------------|-------|------------------|-----------------|-----------|
| [db/cache/etc] | [papel] | [módulo] | [risco] | [arquivo] |

### 3) Tratamento de secrets e credenciais

- Fontes de credenciais: [env/gerenciador de secrets/configuração]
- Verificações de valores gravados diretamente: [resultado]
- Observações sobre rotação ou ciclo de vida: [conhecido/desconhecido]

### 4) Confiabilidade e comportamento em falhas

- Comportamento de nova tentativa e espera: [implementado/ausente/parcial]
- Política de timeout: [onde está configurada]
- Comportamento de circuit breaker ou fallback: [se houver]

### 5) Observabilidade das integrações

- Logs de chamadas externas: [sim/não + onde]
- Cobertura de métricas e traces: [sim/não + onde]
- Lacunas de visibilidade: [lista]

### 6) Evidências

- [path/to/integration-wrapper]
- [path/to/config-or-env-template]
- [path/to/monitoring-or-logging-config]

## Seções estendidas (opcionais)

Adicione somente quando necessário:

- Catálogo detalhado por endpoint
- Diagramas de sequência do fluxo de autenticação
- SLA/SLO por integração
- Observações sobre topologia regional e failover
