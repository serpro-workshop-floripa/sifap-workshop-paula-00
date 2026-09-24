# Arquitetura

## Seções principais (obrigatórias)

### 1) Estilo arquitetural

- Estilo principal: [camadas/funcionalidades/orientado a eventos/outro]
- Motivo desta classificação: [justificativa breve baseada em evidências]
- Restrições principais: [2 a 3 restrições que moldam o design]

### 2) Fluxo do sistema

```text
[entrada] -> [processamento] -> [lógica de domínio] -> [dados/integração] -> [resposta/saída]
```

Descreva o fluxo em 4 a 6 etapas com evidências provenientes de arquivos.

### 3) Responsabilidades das camadas ou dos módulos

| Camada ou módulo | Responsável por | Não deve ser responsável por | Evidência |
|------------------|-----------------|-------------------------------|-----------|
| [nome] | [responsabilidade] | [não responsabilidade] | [arquivo] |

### 4) Padrões reutilizados

| Padrão | Onde foi encontrado | Por que existe |
|--------|----------------------|----------------|
| [singleton/repository/adapter/etc] | [path] | [motivo] |

### 5) Riscos arquiteturais conhecidos

- [Risco 1 + impacto]
- [Risco 2 + impacto]

### 6) Evidências

- [path/to/entrypoint]
- [path/to/main-layer-files]
- [path/to/data-or-integration-layer]

## Seções estendidas (opcionais)

Adicione somente quando necessário:

- Detalhes da ordem de inicialização
- Diagramas da topologia assíncrona ou orientada a eventos
- Catálogo de antipadrões com caminhos de refatoração
- Análise de modos de falha e postura de resiliência
