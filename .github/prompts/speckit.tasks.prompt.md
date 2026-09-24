---
agent: speckit.tasks
---

# Spec-Kit — Gerar tarefas

## Objetivo

Gerar um `tasks.md` executável, organizado por história de usuário.

## Quando invocar

Use este prompt depois que o plano e os artefatos de design estiverem disponíveis.

## Pré-condições

- O repositório e os artefatos exigidos pelo fluxo Spec-Kit devem estar disponíveis.
- Os hooks de extensão aplicáveis devem ser avaliados conforme o corpo do prompt.

## Entradas que a equipe deve fornecer

- A orientação adicional fornecida em `$arguments` e os documentos da funcionalidade.

## O que farei

- Executarei o fluxo Spec-Kit descrito no corpo do prompt.
- Validarei os artefatos e informarei o resultado ao usuário.

## O que NÃO farei

- Não ignorarei gates, dependências, hooks obrigatórios nem validações do fluxo.
- Não alterarei placeholders, comandos, paths, IDs ou estruturas exigidas pelo Spec-Kit.

## Formato de saída

O path de `tasks.md`, contagens, oportunidades de paralelismo, critérios de teste e escopo do mvp.

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

**Verifique hooks de extensão (antes da geração de tarefas)**:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia-o e procure entradas na chave `hooks.before_tasks`
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

1. **Configuração**: Execute `{SCRIPT}` na raiz do repositório e interprete FEATURE_DIR, TASKS_TEMPLATE e a lista AVAILABLE_DOCS. `FEATURE_DIR` e `TASKS_TEMPLATE` devem ser paths absolutos quando fornecidos. `AVAILABLE_DOCS` é uma lista de nomes de documentos ou paths relativos disponíveis em `FEATURE_DIR` (por exemplo, `research.md` ou `contracts/`). Para aspas simples em argumentos como "I'm Groot", use sintaxe de escape, por exemplo: 'I'\''m Groot' (ou aspas duplas, se possível: "I'm Groot").

2. **Carregue os documentos de design**: Leia de FEATURE_DIR:
   - **Obrigatório**: plan.md (stack tecnológica, bibliotecas e estrutura), spec.md (histórias de usuário com prioridades)
   - **Opcional**: data-model.md (entidades), contracts/ (contratos de interface), research.md (decisões), quickstart.md (cenários de teste)
   - **SE EXISTIR**: Carregue `/memory/constitution.md` para obter os princípios do projeto e as restrições de governança
   - Observação: nem todos os projetos têm todos os documentos. Gere tarefas com base no que estiver disponível.

3. **Execute o fluxo de geração de tarefas**:
   - Carregue plan.md e extraia stack tecnológica, bibliotecas e estrutura do projeto
   - Carregue spec.md e extraia as histórias de usuário com suas prioridades (P1, P2, P3, etc.)
   - Se data-model.md existir, extraia as entidades e associe-as às histórias de usuário
   - Se contracts/ existir, associe os contratos de interface às histórias de usuário
   - Se research.md existir, extraia as decisões para as tarefas de configuração
   - Gere tarefas organizadas por história de usuário (consulte Regras para geração de tarefas abaixo)
   - Gere um grafo de dependências que mostre a ordem de conclusão das histórias de usuário
   - Crie exemplos de execução paralela por história de usuário
   - Valide a completude das tarefas (cada história de usuário deve ter todas as tarefas necessárias e ser testável de forma independente)

4. **Gere tasks.md**: Leia o template de tarefas em TASKS_TEMPLATE (da saída JSON acima) e use-o como estrutura. Se TASKS_TEMPLATE estiver vazio, use `.specify/templates/tasks-template.md` como alternativa. Preencha-o com:
   - Nome correto da funcionalidade obtido de plan.md
   - Fase 1: tarefas de configuração (inicialização do projeto)
   - Fase 2: tarefas fundamentais (pré-requisitos bloqueantes para todas as histórias de usuário)
   - Fase 3+: uma fase por história de usuário (na ordem de prioridade de spec.md)
   - Cada fase inclui objetivo da história, critérios de teste independente, testes (se solicitados) e tarefas de implementação
   - Fase final: Acabamento e aspectos transversais
   - Todas as tarefas devem seguir o formato estrito de checklist (consulte Regras para geração de tarefas abaixo)
   - Paths de arquivo claros para cada tarefa
   - Seção de dependências mostrando a ordem de conclusão das histórias
   - Exemplos de execução paralela por história
   - Seção de estratégia de implementação (MVP primeiro e entrega incremental)

### Hooks pós-execução obrigatórios

**Você DEVE concluir esta seção antes de informar a conclusão ao usuário.**

Verifique se `.specify/extensions.yml` existe na raiz do projeto.

- Se não existir ou se nenhum hook estiver registrado em `hooks.after_tasks`, vá para o Relatório de conclusão.
- Se existir, leia-o e procure entradas na chave `hooks.after_tasks`.
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

Informe o path de tasks.md gerado e um resumo:

- Contagem total de tarefas
- Contagem de tarefas por história de usuário
- Oportunidades de paralelismo identificadas
- Critérios de teste independente para cada história
- Escopo sugerido do MVP (normalmente apenas User Story 1)
- Validação do formato: confirme que TODAS as tarefas seguem o formato de checklist (checkbox, ID, labels e paths de arquivos)

Contexto para geração de tarefas: {ARGS}

O tasks.md deve ser executável imediatamente — cada tarefa deve ser específica o bastante para que um LLM a conclua sem contexto adicional.

### Regras para geração de tarefas

**CRÍTICO**: As tarefas DEVEM ser organizadas por história de usuário para permitir implementação e teste independentes.

**Os testes são OPCIONAIS**: Gere tarefas de teste somente se forem solicitadas explicitamente na especificação da funcionalidade ou se o usuário pedir uma abordagem TDD.

#### Formato do checklist (OBRIGATÓRIO)

Toda tarefa DEVE seguir estritamente este formato:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path

```

**Componentes do formato**:

1. **Checkbox**: SEMPRE comece com `- [ ]` (checkbox Markdown)
2. **ID da tarefa**: número sequencial (T001, T002, T003...) na ordem de execução
3. **Marcador [P]**: inclua SOMENTE se a tarefa puder ser paralelizada (arquivos diferentes e sem dependências de tarefas incompletas)
4. **Label [Story]**: OBRIGATÓRIA somente para tarefas da fase de história de usuário
   - Formato: [US1], [US2], [US3] etc. (corresponde às histórias de usuário de spec.md)
   - Fase de configuração: SEM label de história
   - Fase fundamental: SEM label de história
   - Fases de história de usuário: DEVEM ter label de história
   - Fase de acabamento: SEM label de história

5. **Descrição**: ação clara com o path exato do arquivo

**Exemplos**:

- ✅ CORRETO: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRETO: `- [ ] T005 [P] Implement authentication middleware em src/middleware/auth.py`
- ✅ CORRETO: `- [ ] T012 [P] [US1] Create User model em src/models/user.py`
- ✅ CORRETO: `- [ ] T014 [US1] Implement UserService em src/services/user_service.py`
- ❌ INCORRETO: `- [ ] Create User model` (ID e label de história ausentes)
- ❌ INCORRETO: `T001 [US1] Create model` (checkbox ausente)
- ❌ INCORRETO: `- [ ] [US1] Create User model` (ID da tarefa ausente)
- ❌ INCORRETO: `- [ ] T001 [US1] Create model` (path de arquivo ausente)

#### Organização das tarefas

1. **Das histórias de usuário (spec.md)** - ORGANIZAÇÃO PRINCIPAL:
   - Cada história de usuário (P1, P2, P3...) recebe sua própria fase
   - Associe todos os componentes relacionados à respectiva história:
     - Modelos necessários para essa história
     - Serviços necessários para essa história
     - Interfaces/UI necessárias para essa história
     - Se houver solicitação de testes: testes específicos dessa história
   - Marque as dependências entre histórias (a maioria das histórias deve ser independente)

2. **Dos contratos**:
   - Associe cada contrato de interface → à história de usuário atendida
   - Se houver solicitação de testes: cada contrato de interface → tarefa de teste de contrato [P] antes da implementação na fase dessa história

3. **Do modelo de dados**:
   - Associe cada entidade às histórias de usuário que precisam dela
   - Se a entidade atender várias histórias, coloque-a na história mais antiga ou na fase de configuração
   - Relacionamentos → tarefas da camada de serviço na fase adequada da história

4. **Da configuração/infraestrutura**:
   - Infraestrutura compartilhada → fase de configuração (Fase 1)
   - Tarefas fundamentais/bloqueantes → fase fundamental (Fase 2)
   - Configuração específica da história → na fase dessa história

#### Estrutura das fases

- **Fase 1**: Configuração (inicialização do projeto)
- **Fase 2**: Fundamentos (pré-requisitos bloqueantes — DEVEM ser concluídos antes das histórias de usuário)
- **Fase 3+**: Histórias de usuário em ordem de prioridade (P1, P2, P3...)
  - Em cada história: Testes (se solicitados) → modelos → serviços → endpoints → integração
  - Cada fase deve ser um incremento completo e testável de forma independente

- **Fase final**: Acabamento e aspectos transversais

### Critérios de conclusão do fluxo

- [ ] tasks.md gerado com todas as fases, IDs de tarefa e paths de arquivos
- [ ] Hooks de extensão acionados ou ignorados conforme as regras em Hooks pós-execução obrigatórios acima
- [ ] Conclusão informada ao usuário com contagem de tarefas, detalhamento por história e escopo do MVP

## Exemplo de invocação

```text
`/speckit.tasks`

```
