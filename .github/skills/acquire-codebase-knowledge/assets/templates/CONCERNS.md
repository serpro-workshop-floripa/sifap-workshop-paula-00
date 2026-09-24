# Pontos de atenção da base de código

## Seções principais (obrigatórias)

### 1) Principais riscos (priorizados)

| Severidade | Ponto de atenção | Evidência | Impacto | Ação sugerida |
|------------|------------------|-----------|---------|---------------|
| [alta/média/baixa] | [problema] | [arquivo ou saída da varredura] | [impacto] | [próxima ação] |

### 2) Dívida técnica

Liste somente os itens de dívida mais importantes.

| Item de dívida | Por que existe | Onde | Risco se ignorado | Correção sugerida |
|----------------|----------------|------|-------------------|-------------------|
| [item] | [motivo] | [path] | [risco] | [correção] |

### 3) Pontos de atenção de segurança

| Risco | Categoria OWASP (se aplicável) | Evidência | Mitigação atual | Lacuna |
|-------|---------------------------------|-----------|-----------------|--------|
| [risco] | [A01/A03/etc ou N/A] | [path] | [o que existe] | [o que falta] |

### 4) Pontos de atenção de desempenho e escalabilidade

| Ponto de atenção | Evidência | Sintoma atual | Risco de escalabilidade | Melhoria sugerida |
|------------------|-----------|--------------|------------------------|-------------------|
| [problema] | [path/métrica] | [sintoma] | [risco] | [ação] |

### 5) Áreas frágeis ou com muitas alterações

| Área | Por que é frágil | Sinal de alterações frequentes | Estratégia segura de alteração |
|------|------------------|--------------------------------|-------------------------------|
| [path] | [motivo] | [evidência de alterações recentes] | [abordagem] |

### 6) Perguntas `[ASK USER]`

Adicione as perguntas não resolvidas que dependem da intenção da equipe em uma lista numerada.

1. [ASK USER] [pergunta]

### 7) Evidências

- [referência à seção da saída da varredura]
- [path/to/code-file]
- [path/to/config-or-history-evidence]

## Seções estendidas (opcionais)

Adicione somente quando necessário:

- Inventário completo de bugs
- Roteiro de correção por componente
- Estimativas de custo e esforço por ponto de atenção
- Mapeamento de riscos e responsáveis por dependências
