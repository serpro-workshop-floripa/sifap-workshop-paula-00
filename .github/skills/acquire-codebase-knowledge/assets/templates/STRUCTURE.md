# Estrutura da base de código

## Seções principais (obrigatórias)

### 1) Mapa de alto nível

Liste somente arquivos e diretórios relevantes do nível superior.

| Path | Finalidade | Evidência |
|------|------------|-----------|
| [path/] | [finalidade] | [fonte] |

### 2) Pontos de entrada

- Ponto de entrada principal do runtime: [ARQUIVO]
- Pontos de entrada secundários (worker/cli/jobs): [ARQUIVOS ou NENHUM]
- Como o ponto de entrada é selecionado (script/configuração): [OBSERVAÇÃO]

### 3) Limites dos módulos

| Limite | O que pertence aqui | O que não deve estar aqui |
|--------|----------------------|---------------------------|
| [módulo/camada] | [responsabilidade] | [lógica proibida] |

### 4) Regras de nomenclatura e organização

- Padrão de nomes de arquivos: [kebab/camel/Pascal + exemplos]
- Padrão de organização de diretórios: [funcionalidade/camada/domínio]
- Convenções de aliases de import ou paths: [REGRA]

### 5) Evidências

- [path/to/root-tree-source]
- [path/to/entry-config]
- [path/to/key-module]

## Seções estendidas (opcionais)

Adicione somente quando a complexidade do repositório exigir:

- Mapas detalhados de subdiretórios por funcionalidade ou camada
- Detalhes da ordem de middleware e inicialização
- Limites entre layouts gerados e código-fonte
- Mapas de estrutura por workspace do monorepo
