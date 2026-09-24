# Stack de tecnologia

## Seções principais (obrigatórias)

### 1) Resumo do ambiente de execução

| Área | Valor | Evidência |
|------|-------|-----------|
| Linguagem principal | [VALOR] | [FILE_PATH] |
| Runtime + versão | [VALOR] | [FILE_PATH] |
| Gerenciador de pacotes | [VALOR] | [FILE_PATH] |
| Sistema de módulos/build | [VALOR] | [FILE_PATH] |

### 2) Frameworks e dependências de produção

Liste somente dependências de produção de alto impacto, como frameworks, dados, transporte e autenticação.

| Dependência | Versão | Papel no sistema | Evidência |
|-------------|--------|------------------|-----------|
| [NOME] | [VERSÃO] | [PAPEL] | [FILE_PATH] |

### 3) Toolchain de desenvolvimento

| Ferramenta | Finalidade | Evidência |
|------------|------------|-----------|
| [FERRAMENTA] | [LINT/FORMAT/TEST/BUILD] | [FILE_PATH] |

### 4) Comandos principais

```bash
[comando de instalação]
[comando de build]
[comando de teste]
[comando de lint]
```

### 5) Ambiente e configuração

- Fontes de configuração: [LISTE OS ARQUIVOS]
- Variáveis de ambiente obrigatórias: [VAR_1], [VAR_2], [TODO]
- Restrições de implantação e runtime: [OBSERVAÇÃO BREVE]

### 6) Evidências

- [path/to/manifest]
- [path/to/runtime-config]
- [path/to/build-or-ci-config]

## Seções estendidas (opcionais)

Adicione somente quando necessário para repositórios complexos:

- Taxonomia completa de dependências por categoria
- Flags detalhadas do compilador e do runtime
- Matriz de ambientes (dev/stage/prod)
- Detalhes do gerenciador de processos e do runtime de contêineres
