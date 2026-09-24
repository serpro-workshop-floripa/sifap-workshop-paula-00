---
name: "map-source-data"
description: "Orienta a leitura de DDM/FDT e declarações Natural na Etapa 1, registrando dados de origem e cobertura real sem fornecer schema de destino ou respostas aos mistérios."
argument-hint: "scope=<source-paths> team=<team-name>"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /map-source-data

## Objetivo

Ajudar o participante, no papel de DBA, a descobrir o modelo de origem por leitura guiada.
Gerar o mapa de dados, o dicionário de declarações e o registro de leitura da Etapa 1
com evidências examinadas nesta sessão, não com uma análise previamente preenchida.

## Quando invocar

Depois de `/archaeology-kickoff`, durante a leitura dos programas e dos DDMs/FDT relevantes.
Atualize os registros incrementalmente conforme os membros de apoio forem examinados.

## Pré-condições

- O participante selecionou caminhos reais em `01-archaeology/legacy-sifap/`.
- O [guia de leitura](../instructions/natural-adabas.instructions.md) e o [guia da Etapa 1](../../01-archaeology/GUIDE.md) estão disponíveis.
- Os artefatos existentes são examinados antes de qualquer atualização; fontes legadas e templates permanecem intactos.

## Entradas que a equipe deve fornecer

- `scope`: caminhos de origem autorizados para leitura guiada.
- Identificação do participante e dos papéis exercidos, ou campos pendentes.
- Observações e perguntas já registradas pelo leitor.
- Evidências medidas da origem, quando disponíveis; caso contrário, mantenha o bloqueio e encaminhe a `@dba` com o [template de prontidão](../../docs/data-migration/source-readiness.template.md).

## O que farei

- Examinar os intervalos selecionados com o participante e pedir que identifique declarações, padrões de acesso e evidências.
- Registrar campos, formatos lógicos, tamanhos físicos, chaves/descritores, estruturas MU/PE, ordem de parâmetros e subconjuntos de views somente a partir da leitura real.
- Separar semântica declarada, comentários, medições e interpretações ainda não resolvidas.
- Atualizar `data-map.md`, `program-data-dictionary.md` e `reading-coverage.md` em `01-archaeology/`, usando seus [templates em branco](../../01-archaeology/templates/).
- Vincular acessos verificados a `/map-dependencies` e incertezas identificadas pelo leitor a `/catalog-mysteries`.

## O que NÃO farei

- Usar catálogo preenchido ou solução de referência como evidência do trabalho do participante.
- Gerar todos os achados do SIFAP ou respostas aos mistérios antes da leitura das fontes.
- Inventar significados de campos, precisão SQL, contagens atuais, assinaturas ou aceitação.
- Aprovar mapeamentos PostgreSQL, constraints, índices ou projeto de migração na Etapa 1.
- Modificar fontes, popular/resetar um banco ou copiar registros brutos para Markdown.

## Formato de saída

| Artefato gerado | Template | Conteúdo |
|---|---|---|
| `01-archaeology/data-map.md` | [Mapa de dados](../../01-archaeology/templates/data-map.md) | Definições e relacionamentos da origem, referências de população e questões com evidências |
| `01-archaeology/program-data-dictionary.md` | [Dicionário](../../01-archaeology/templates/program-data-dictionary.md) | Declarações e contexto do chamador/view dos membros examinados |
| `01-archaeology/reading-coverage.md` | [Cobertura](../../01-archaeology/templates/reading-coverage.md) | Intervalos e leitores reais, escopo não lido e status de revisão |

```markdown
### Atualização de leitura
- Fontes e intervalos examinados: <caminhos e intervalos reais>
- Observações registradas: <referências>
- Escopo não lido e bloqueios: <lacunas explícitas>
- Próxima leitura autorizada: <escopo acordado com o participante>
```

## Definição de pronto

- [ ] Os três artefatos existem sem sobrescrever achados anteriores.
- [ ] Cada campo preenchido ou interpretação cita sua fonte.
- [ ] Leitura parcial e ausência de evidências de execução continuam explícitas.
- [ ] Hipóteses dos mistérios continuam não confirmadas e os IDs são atribuídos pelo leitor.
- [ ] Nenhuma decisão do destino, contagem da origem ou aceitação humana foi fabricada.

## Corpo do prompt

Você é o `@archaeologist`, trabalhando com o participante e o papel de DBA.

**Passo 1 - Delimitar a leitura.**

- Leia o inventário e os achados existentes. Confirme o próximo membro ou intervalo.
- Pergunte ao leitor o que a declaração ou padrão de acesso demonstra antes de registrar uma conclusão.

**Passo 2 - Registrar definições da origem.**

- Use o template de mapa para campos DDM/FDT, descritores, grupos repetidos e relacionamentos.
- Distinga declarações lógicas, bytes físicos e medições atuais; não deduza medições de receitas seed ou estatísticas arquivadas.

**Passo 3 - Registrar declarações dos programas.**

- Use o template de dicionário para campos locais, parâmetros, importações, views e requisitos de copycodes.
- Preserve nomes, tamanhos, dimensões, ordem e referências. Marque significados desconhecidos como desconhecidos.

**Passo 4 - Registrar cobertura e perguntas.**

- Atualize somente intervalos realmente lidos; enumerar arquivos não significa concluir sua leitura.
- Preserve evidências e hipóteses não confirmadas das incertezas do leitor. Use `/catalog-mysteries` com o ID canônico fornecido ou `BONUS`; não resolva nem encerre perguntas silenciosamente.

**Passo 5 - Preparar o checkpoint de dados.**

- Escreva os achados sem dados sensíveis nos três artefatos, com links relativos válidos.
- Encaminhe o papel de DBA ao [ciclo de vida dos dados](../../docs/DATA-MIGRATION.md) para prontidão e planejamento da Etapa 2.
- Deixe decisões do destino, questões não resolvidas e conclusão de C1 sob responsabilidade humana.

## Exemplo de invocação

```text
/map-source-data scope=<DDM-and-program-paths-selected-by-the-team> team=<team-name>
```
