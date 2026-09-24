---
agent: speckit.plan
---

# Spec-Kit — Planejar

## Objetivo

Produzir o plano de implementação e os artefatos de design da funcionalidade.

## Quando invocar

Use este prompt depois que a especificação estiver pronta para planejamento técnico.

## Pré-condições

- O repositório e os artefatos exigidos pelo fluxo Spec-Kit devem estar disponíveis.
- Os hooks de extensão aplicáveis devem ser avaliados conforme o corpo do prompt.

## Entradas que a equipe deve fornecer

- A orientação adicional fornecida em `$arguments` e a especificação ativa.

## O que farei

- Executarei o fluxo Spec-Kit descrito no corpo do prompt.
- Validarei os artefatos e informarei o resultado ao usuário.

## O que NÃO farei

- Não ignorarei gates, dependências, hooks obrigatórios nem validações do fluxo.
- Não alterarei placeholders, comandos, paths, IDs ou estruturas exigidas pelo Spec-Kit.

## Formato de saída

O branch, o path de `impl_plan` e os artefatos gerados.

## Definição de pronto

- [ ] O fluxo descrito no corpo do prompt foi concluído ou um bloqueio foi informado claramente.
- [ ] As validações e os hooks aplicáveis foram processados.
- [ ] O resultado final foi apresentado no formato solicitado.

## Corpo do prompt

### Entrada do usuário

```text
$ARGUMENTS

```

Você **DEVE** considerar a entrada do usuário antes de prosseguir (se não estiver vazia).

### Verificações pré-execução

**Verifique hooks de extensão (antes do planejamento)**:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia-o e procure entradas na chave `hooks.before_plan`
- Se não for possível interpretar o YAML ou se ele for inválido, ignore silenciosamente a verificação de hooks e continue normalmente
- Desconsidere hooks nos quais `enabled` seja explicitamente `false`. Considere habilitados por padrão os hooks sem um campo `enabled`.
- Para cada hook restante, **não** tente interpretar nem avaliar expressões `condition` do hook:
  - Se o hook não tiver o campo `condition` ou se ele for nulo/vazio, considere o hook executável
  - Se o hook definir uma condição não vazia em `condition`, ignore o hook e deixe a avaliação da condição para a implementação de `HookExecutor`

- Para cada hook executável, produza o conteúdo a seguir conforme seu sinalizador `optional` :
  - **Hook opcional** (`optional: true`):

    ```
    ## Extension Hooks

    **Opcional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`

    ```

  - **Hook obrigatório** (`optional: false`):

    ```
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Outline.

    ```

- Se nenhum hook estiver registrado ou `.specify/extensions.yml` não existir, ignore silenciosamente

### Roteiro

1. **Configuração**: Execute `{SCRIPT}` na raiz do repositório e interprete o JSON para FEATURE_SPEC, IMPL_PLAN, SPECS_DIR e BRANCH. Para aspas simples em argumentos como "I'm Groot", use sintaxe de escape, por exemplo: 'I'\''m Groot' (ou aspas duplas, se possível: "I'm Groot").

2. **Carregue o contexto**: Leia FEATURE_SPEC e `/memory/constitution.md`. Carregue o template IMPL_PLAN (já copiado).

3. **Execute o fluxo de planejamento**: Siga a estrutura do template IMPL_PLAN para:
   - Preencha Technical Context (marque incógnitas como "NEEDS CLARIFICATION")
   - Preencha a seção Constitution Check com base na constituição
   - Avalie os gates (ERROR se as violações não forem justificadas)
   - Fase 0: Gere research.md (resolva todos os NEEDS CLARIFICATION)
   - Fase 1: Gere data-model.md, contracts/, quickstart.md
   - Fase 1: Atualize o contexto do agente executando o script do agente
   - Reavalie Constitution Check após o design

### Hooks pós-execução obrigatórios

**Você DEVE concluir esta seção antes de informar a conclusão ao usuário.**

Verifique se `.specify/extensions.yml` existe na raiz do projeto.

- Se não existir ou se nenhum hook estiver registrado em `hooks.after_plan`, vá para o Relatório de conclusão.
- Se existir, leia-o e procure entradas na chave `hooks.after_plan`.
- Se não for possível interpretar o YAML ou se ele for inválido, ignore silenciosamente a verificação de hooks e prossiga para o Relatório de conclusão.
- Desconsidere hooks nos quais `enabled` seja explicitamente `false`. Considere habilitados por padrão os hooks sem um campo `enabled`.
- Para cada hook restante, **não** tente interpretar nem avaliar expressões `condition` do hook:
  - Se o hook não tiver o campo `condition` ou se ele for nulo/vazio, considere o hook executável
  - Se o hook definir uma condição não vazia em `condition`, ignore o hook e deixe a avaliação da condição para a implementação de `HookExecutor`

- Para cada hook executável, produza o conteúdo a seguir conforme seu sinalizador `optional` :
  - **Hook obrigatório** (`optional: false`) — **você DEVE emitir `EXECUTE_COMMAND:` para cada hook obrigatório**:

    ```
    ## Extension Hooks

    **Automatic Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    ```

  - **Hook opcional** (`optional: true`):

    ```
    ## Extension Hooks

    **Opcional Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`

    ```

### Relatório de conclusão

O comando termina após o planejamento da Fase 2. Informe o branch, o path de IMPL_PLAN e os artefatos gerados.

### Fases

#### Fase 0: roteiro e pesquisa

1. **Extraia as incógnitas de Technical Context** acima:
   - Para cada NEEDS CLARIFICATION → uma tarefa de pesquisa
   - Para cada dependência → tarefa de boas práticas
   - Para cada integração → tarefa de padrões

2. **Gere e acione agentes de pesquisa**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"

   ```

3. **Consolide as descobertas** em `research.md` usando o formato:
   - Decisão: [o que foi escolhido]
   - Justificativa: [por que foi escolhido]
   - Alternativas consideradas: [o que mais foi avaliado]

**Saída**: research.md com todos os NEEDS CLARIFICATION resolvidos

#### Fase 1: design e contratos

**Pré-requisitos:** `research.md` concluído

1. **Extraia entidades da especificação da funcionalidade** → `data-model.md`:
   - nome da entidade, campos e relacionamentos
   - regras de validação dos requisitos
   - transições de estado, quando aplicável

2. **Defina contratos de interface** (se o projeto tiver interfaces externas) → `/contracts/`:
   - Identifique quais interfaces o projeto expõe a usuários ou outros sistemas
   - Documente o formato de contrato adequado ao tipo de projeto
   - Exemplos: APIs públicas de bibliotecas, schemas de comandos para ferramentas CLI, endpoints de serviços web, gramáticas de parsers e contratos de UI para aplicações
   - Ignore se o projeto for totalmente interno (scripts de build, ferramentas de uso único etc.)

3. **Crie um guia de validação quickstart** → `quickstart.md`:
   - Documente cenários de validação executáveis que comprovem o funcionamento da funcionalidade de ponta a ponta
   - Inclua pré-requisitos, comandos de configuração, comandos de teste/execução e resultados esperados
   - Use links ou referências aos contratos e aos detalhes do modelo de dados em vez de duplicá-los
   - Não inclua código completo de implementação, corpos de modelos/serviços/controllers, migrações nem suítes completas de teste
   - Mantenha este artefato como guia de validação/execução; os detalhes de implementação pertencem a `tasks.md` e à fase de implementação

4. **Atualização do contexto do agente**:
   - Atualize a referência ao plano entre os marcadores `<!-- SPECKIT START -->` e `<!-- SPECKIT END -->` em `__CONTEXT_FILE__` para apontar para o arquivo de plano criado na etapa 1 (o path de IMPL_PLAN)

**Saída**: data-model.md, /contracts/*, quickstart.md, arquivo de contexto do agente atualizado

### Regras principais

- Use paths absolutos em operações do sistema de arquivos e paths relativos ao projeto em referências na documentação e nos arquivos de contexto do agente
- ERRO em falhas de gate ou esclarecimentos não resolvidos

### Critérios de conclusão do fluxo

- [ ] Fluxo de planejamento executado e artefatos de design gerados
- [ ] Hooks de extensão acionados ou ignorados conforme as regras em Hooks pós-execução obrigatórios acima
- [ ] Conclusão informada ao usuário com branch, path do plano e artefatos gerados

## Exemplo de invocação

```text
`/speckit.plan`

```
