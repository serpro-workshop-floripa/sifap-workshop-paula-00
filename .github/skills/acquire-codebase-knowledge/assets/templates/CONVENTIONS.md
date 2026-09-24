# Convenções de código

## Seções principais (obrigatórias)

### 1) Regras de nomenclatura

| Item | Regra | Exemplo | Evidência |
|------|-------|---------|-----------|
| Arquivos | [REGRA] | [EXEMPLO] | [ARQUIVO] |
| Funções/métodos | [REGRA] | [EXEMPLO] | [ARQUIVO] |
| Tipos/interfaces | [REGRA] | [EXEMPLO] | [ARQUIVO] |
| Constantes/variáveis de ambiente | [REGRA] | [EXEMPLO] | [ARQUIVO] |

### 2) Formatação e lint

- Formatador: [FERRAMENTA + ARQUIVO DE CONFIGURAÇÃO]
- Linter: [FERRAMENTA + ARQUIVO DE CONFIGURAÇÃO]
- Regras aplicadas mais relevantes: [REGRA_1], [REGRA_2], [REGRA_3]
- Comandos de execução: [COMANDOS]

### 3) Convenções de imports e módulos

- Agrupamento e ordem de imports: [REGRA]
- Política de alias em comparação com import relativo: [REGRA]
- Política de exports públicos ou arquivos barrel: [REGRA]

### 4) Convenções de erros e logs

- Estratégia de erros por camada: [RESUMO BREVE]
- Estilo de logs e campos de contexto obrigatórios: [RESUMO]
- Regras de ocultação de dados sensíveis: [RESUMO]

### 5) Convenções de testes

- Regra de nomenclatura e localização dos arquivos de teste: [REGRA]
- Padrão da estratégia de mocks: [REGRA]
- Expectativa de cobertura: [REGRA ou TODO]

### 6) Evidências

- [path/to/lint-config]
- [path/to/format-config]
- [path/to/representative-source-file]

## Seções estendidas (opcionais)

Adicione somente para bases de código grandes ou inconsistentes:

- Matriz de tratamento de erros por camada
- Opções de rigor específicas da linguagem
- Convenções de commits e branches específicas do repositório
- Violações conhecidas de convenções que precisam de correção
