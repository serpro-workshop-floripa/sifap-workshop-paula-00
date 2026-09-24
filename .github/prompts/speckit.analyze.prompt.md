---
agent: speckit.analyze
---
# Analisar consistência da especificação

## Objetivo

Identificar inconsistências, duplicações, ambiguidades e itens subespecificados entre `spec.md`, `plan.md`
e `tasks.md` antes da implementação.

## Quando invocar

Invoque somente depois que `__SPECKIT_COMMAND_TASKS__` produzir um `tasks.md` completo.

## Pré-condições

- `spec.md`, `plan.md` e `tasks.md` devem existir no diretório da feature.
- `/memory/constitution.md` deve estar disponível para validar os princípios do projeto.
- A análise é estritamente somente leitura.

## Inputs que a equipe deve fornecer

```text
$ARGUMENTS
```

Considere o input do usuário antes de prosseguir, quando ele não estiver vazio.

## O que farei

- Carregarei apenas o contexto necessário dos artefatos.
- Construirei modelos semânticos de requisitos, histórias, tarefas e princípios.
- Detectarei duplicações, ambiguidades, subespecificação, conflitos constitucionais e lacunas de cobertura.
- Produzirei um relatório compacto, métricas e próximos passos.

## O que NÃO farei

- Não modificarei arquivos.
- Não inventarei seções ausentes.
- Não enfraquecerei, reinterpretarei nem ignorarei princípios da constituição.
- Não aplicarei correções sem aprovação explícita do usuário.

## Formato de saída

Produza um relatório Markdown com achados priorizados, resumo de cobertura, problemas de alinhamento com a
constituição, tarefas não mapeadas, métricas e próximos passos.

## Definição de pronto

- [ ] Todos os três artefatos principais foram analisados.
- [ ] Os princípios da constituição foram validados.
- [ ] Os achados têm IDs estáveis, severidade, localização e recomendação.
- [ ] Nenhum arquivo foi modificado.
- [ ] Os hooks posteriores foram apresentados conforme a configuração.

## Corpo do prompt

### Verificações prévias à execução

Verifique os hooks de extensão antes da análise:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia o arquivo e procure entradas na chave `hooks.before_analyze`.
- Se o YAML não puder ser interpretado ou for inválido, ignore silenciosamente a verificação dos hooks e
  continue normalmente.
- Exclua hooks cujo campo `enabled` seja explicitamente `false`. Considere habilitados por padrão os hooks
  sem o campo `enabled`.
- Para cada hook restante, não tente interpretar nem avaliar expressões do campo `condition`:
  - Se o hook não tiver o campo `condition`, ou se ele for nulo ou vazio, considere o hook executável.
  - Se o hook definir uma `condition` não vazia, ignore-o e deixe a avaliação para a implementação de
    HookExecutor.
- Para cada hook executável, produza o bloco correspondente ao valor de `optional`:
  - Hook opcional (`optional: true`):

    ```text
    ## Extension Hooks

    **Optional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```

  - Hook obrigatório (`optional: false`):

    ```text
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Goal.
    ```

- Se não houver hooks registrados ou `.specify/extensions.yml` não existir, prossiga silenciosamente.

### Restrições operacionais

**ESTRITAMENTE SOMENTE LEITURA**: não modifique nenhum arquivo. Produza um relatório de análise
estruturado. Ofereça um plano de correção opcional; o usuário deve aprová-lo explicitamente antes de
qualquer comando posterior de edição manual.

**Autoridade da constituição**: a constituição do projeto (`/memory/constitution.md`) é inegociável no
escopo desta análise. Conflitos com a constituição são automaticamente CRITICAL e exigem ajuste da
especificação, do plano ou das tarefas, nunca diluição, reinterpretação ou omissão silenciosa do princípio.
Se um princípio precisar mudar, isso deve ocorrer em uma atualização separada e explícita da constituição,
fora de `__SPECKIT_COMMAND_ANALYZE__`.

### Etapas de execução

#### 1. Inicializar o contexto da análise

Execute `{SCRIPT}` uma vez na raiz do repositório e interprete o JSON para obter FEATURE_DIR e
AVAILABLE_DOCS. Derive os paths absolutos:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md

Interrompa com uma mensagem de erro se algum arquivo obrigatório estiver ausente e instrua o usuário a
executar o comando de pré-requisito correspondente.

Para aspas simples em argumentos como "I'm Groot", use a sintaxe de escape: por exemplo,
'I'\''m Groot' ou, quando possível, aspas duplas: "I'm Groot".

#### 2. Carregar artefatos com divulgação progressiva

Carregue somente o contexto mínimo necessário de cada artefato.

Em `spec.md`:

- visão geral e contexto;
- requisitos funcionais;
- critérios de sucesso com resultados mensuráveis, como desempenho, segurança, disponibilidade, sucesso
  do usuário e impacto de negócio;
- histórias de usuário;
- casos extremos, quando existirem.

Em `plan.md`:

- escolhas de arquitetura e stack;
- referências ao modelo de dados;
- fases;
- restrições técnicas.

Em `tasks.md`:

- IDs das tarefas;
- descrições;
- agrupamento por fase;
- marcadores de paralelismo [P];
- paths de arquivos referenciados.

Na constituição:

- carregue `/memory/constitution.md` para validar os princípios.

#### 3. Construir modelos semânticos

Crie representações internas sem incluir os artefatos brutos na saída:

- **Inventário de requisitos**: para cada Functional Requirement (FR-###) e Success Criterion (SC-###),
  registre uma chave estável. Use o identificador FR-/SC- explícito como chave principal quando existir e,
  opcionalmente, derive também um slug de frase imperativa para facilitar a leitura, por exemplo,
  "User can upload file" → `user-can-upload-file`. Inclua somente Success Criteria que exijam trabalho
  implementável, como infraestrutura de testes de carga ou ferramentas de auditoria de segurança. Exclua
  métricas de resultado pós-lançamento e KPIs de negócio, como "Reduce support tickets by 50%".
- **Inventário de histórias e ações do usuário**: ações distintas com critérios de aceite.
- **Mapeamento de cobertura de tarefas**: associe cada tarefa a um ou mais requisitos ou histórias por
  inferência de palavras-chave, IDs explícitos ou frases-chave.
- **Conjunto de regras da constituição**: extraia nomes de princípios e declarações normativas MUST/SHOULD.

#### 4. Executar passagens de detecção eficientes em tokens

Concentre-se em achados de alto sinal. Limite a 50 achados no total e agregue o restante em um resumo de
excedentes.

##### A. Detecção de duplicações

- Identifique requisitos quase duplicados.
- Marque a formulação de menor qualidade para consolidação.

##### B. Detecção de ambiguidades

- Sinalize adjetivos vagos, como fast, scalable, secure, intuitive e robust, sem critérios mensuráveis.
- Sinalize placeholders não resolvidos, como TODO, TKTK, ??? e `<placeholder>`.

##### C. Subespecificação

- Identifique requisitos com verbos, mas sem objeto ou resultado mensurável.
- Identifique histórias de usuário sem alinhamento com critérios de aceite.
- Identifique tarefas que referenciem arquivos ou componentes não definidos na especificação ou no plano.

##### D. Alinhamento com a constituição

- Identifique requisitos ou elementos do plano que conflitem com um princípio MUST.
- Identifique seções ou gates de qualidade obrigatórios ausentes.

##### E. Lacunas de cobertura

- Identifique requisitos sem tarefas associadas.
- Identifique tarefas sem requisito ou história mapeados.
- Identifique Success Criteria que exijam trabalho implementável, como desempenho, segurança ou
  disponibilidade, mas não estejam refletidos nas tarefas.

##### F. Inconsistências

- Identifique desvio terminológico, quando o mesmo conceito recebe nomes diferentes entre arquivos.
- Identifique entidades de dados presentes no plano, mas ausentes na especificação, ou vice-versa.
- Identifique contradições na ordem das tarefas, como integração anterior à preparação da base sem nota de
  dependência.
- Identifique requisitos conflitantes, como exigir Next.js em um ponto e Vue em outro.

#### 5. Atribuir severidade

Use esta heurística:

- **CRITICAL**: viola um MUST da constituição, indica ausência de artefato principal ou mostra requisito sem
  cobertura que bloqueia a funcionalidade básica.
- **HIGH**: requisito duplicado ou conflitante, atributo ambíguo de segurança ou desempenho, ou critério de
  aceite não testável.
- **MEDIUM**: desvio terminológico, ausência de cobertura de tarefa não funcional ou caso extremo
  subespecificado.
- **LOW**: melhoria de estilo ou redação e redundância pequena que não afeta a ordem de execução.

#### 6. Produzir relatório compacto

Produza um relatório Markdown sem gravar arquivos, com esta estrutura:

```markdown
## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Duplication | HIGH | spec.md:L120-134 | Two similar requirements ... | Merge phrasing; keep clearer version |
```

Adicione uma linha por achado e gere IDs estáveis prefixados pela inicial da categoria.

Inclua a tabela de resumo de cobertura:

```markdown
| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|
```

Inclua também, preservando estes títulos que o Spec-Kit procura:

- `**Constitution Alignment Issues:**`, quando houver;
- `**Unmapped Tasks:**`, quando houver;
- `**Metrics:**`, com Total Requirements, Total Tasks, Coverage %, Ambiguity Count, Duplication Count e
  Critical Issues Count.

#### 7. Fornecer próximos passos

Ao final do relatório, produza um bloco conciso de Next Actions:

- Se houver problemas CRITICAL, recomende resolvê-los antes de `__SPECKIT_COMMAND_IMPLEMENT__`.
- Se houver somente problemas LOW/MEDIUM, informe que o usuário pode prosseguir e apresente sugestões.
- Sugira comandos explícitos, como executar `__SPECKIT_COMMAND_SPECIFY__` para refinamento,
  `__SPECKIT_COMMAND_PLAN__` para ajustar a arquitetura ou editar manualmente `tasks.md` para cobrir
  'performance-metrics'.

#### 8. Oferecer correções

Pergunte ao usuário: "Deseja que eu sugira edições concretas para corrigir os N principais problemas?"
Não aplique as correções automaticamente.

#### 9. Verificar hooks de extensão posteriores

Após apresentar o relatório, verifique se `.specify/extensions.yml` existe na raiz do projeto:

- Se existir, leia o arquivo e procure entradas na chave `hooks.after_analyze`.
- Se o YAML não puder ser interpretado ou for inválido, ignore silenciosamente a verificação e continue.
- Exclua hooks cujo `enabled` seja explicitamente `false`; considere os demais habilitados por padrão.
- Não interprete expressões `condition`. Considere executável o hook sem `condition`, ou com valor nulo ou
  vazio; ignore condições não vazias e deixe a avaliação para HookExecutor.
- Para cada hook executável, produza o bloco correspondente:
  - Hook opcional (`optional: true`):

    ```text
    ## Extension Hooks

    **Optional Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```

  - Hook obrigatório (`optional: false`):

    ```text
    ## Extension Hooks

    **Automatic Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}
    ```

- Se não houver hooks registrados ou `.specify/extensions.yml` não existir, prossiga silenciosamente.

### Princípios operacionais

#### Eficiência de contexto

- **Mínimo de tokens de alto sinal**: concentre-se em achados acionáveis, não em documentação exaustiva.
- **Divulgação progressiva**: carregue os artefatos aos poucos; não despeje todo o conteúdo na análise.
- **Saída eficiente em tokens**: limite a tabela de achados a 50 linhas e resuma o excedente.
- **Resultados determinísticos**: novas execuções sem alterações devem produzir IDs e contagens consistentes.

#### Diretrizes da análise

- Nunca modifique arquivos, pois esta análise é somente leitura.
- Nunca invente seções ausentes; relate a ausência com precisão.
- Priorize violações da constituição, que são sempre CRITICAL.
- Prefira exemplos a regras exaustivas e cite ocorrências específicas.
- Quando não houver problemas, produza corretamente um relatório de sucesso com estatísticas de cobertura.

Contexto:

```text
{ARGS}
```

## Exemplo de invocação

```text
__SPECKIT_COMMAND_ANALYZE__ revisar cobertura de segurança e desempenho
```
