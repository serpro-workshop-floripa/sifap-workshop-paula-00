# Padrões de testes

## Seções principais (obrigatórias)

### 1) Stack e comandos de testes

- Framework de teste principal: [NOME + VERSÃO]
- Ferramentas de assertions e mocks: [FERRAMENTAS]
- Comandos:

```bash
[executar todos os testes]
[executar testes unitários]
[executar testes de integração/e2e]
[executar cobertura]
```

### 2) Organização dos testes

- Padrão de localização dos arquivos de teste: [junto ao código/pasta tests/etc]
- Convenção de nomenclatura: [padrão]
- Arquivos de setup e onde são executados: [paths]

### 3) Matriz de escopo dos testes

| Escopo | Coberto? | Alvo típico | Observações |
|--------|----------|-------------|-------------|
| Unitário | [sim/não] | [módulos/serviços] | [observações] |
| Integração | [sim/não] | [fronteiras de API/dados] | [observações] |
| E2E | [sim/não] | [fluxos de usuário] | [observações] |

### 4) Estratégia de mocks e isolamento

- Principal abordagem de mocks: [módulo/classe/rede]
- Garantias de isolamento: [o que é redefinido e quando]
- Modo de falha comum nos testes: [observação breve]

### 5) Sinais de cobertura e qualidade

- Ferramenta e limite de cobertura: [valor ou TODO]
- Cobertura atual informada: [valor ou TODO]
- Lacunas conhecidas ou áreas instáveis: [lista]

### 6) Evidências

- [path/to/test-config]
- [path/to/representative-test-file]
- [path/to/ci-or-coverage-config]

## Seções estendidas (opcionais)

Adicione somente quando necessário:

- Padrões de suítes específicos do framework
- Receitas detalhadas de mocks por tipo de dependência
- Catálogo histórico de testes instáveis
- Gargalos de desempenho dos testes e ideias de otimização
