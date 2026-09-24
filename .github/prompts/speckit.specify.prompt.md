---
agent: speckit.specify
---

# Spec-Kit — Especificar

## Objetivo

Transformar a descrição de uma funcionalidade em uma especificação validada.

## Quando invocar

Use este prompt quando houver uma descrição de funcionalidade pronta para especificação.

## Pré-condições

- O repositório e os artefatos exigidos pelo fluxo Spec-Kit devem estar disponíveis.
- Os hooks de extensão aplicáveis devem ser avaliados conforme o corpo do prompt.

## Entradas que a equipe deve fornecer

- A descrição da funcionalidade fornecida em `$arguments`.

## O que farei

- Executarei o fluxo Spec-Kit descrito no corpo do prompt.
- Validarei os artefatos e informarei o resultado ao usuário.

## O que NÃO farei

- Não ignorarei gates, dependências, hooks obrigatórios nem validações do fluxo.
- Não alterarei placeholders, comandos, paths, IDs ou estruturas exigidas pelo Spec-Kit.

## Formato de saída

Os paths de `specify_feature_directory` e `spec_file`, o resultado do checklist e a prontidão para a próxima fase.

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

**Verifique hooks de extensão (antes da especificação)**:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia-o e procure entradas na chave `hooks.before_specify`
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

O texto digitado pelo usuário após `__SPECKIT_COMMAND_SPECIFY__` na mensagem que acionou o comando **é** a descrição da funcionalidade. Pressuponha que ele sempre esteja disponível nesta conversa, mesmo se `{ARGS}` aparecer literalmente abaixo. Não peça que o usuário o repita, a menos que tenha fornecido um comando vazio.

Com base nessa descrição da funcionalidade, faça o seguinte:

1. **Gere um nome curto e conciso** (2 a 4 palavras) para a funcionalidade:
   - Analise a descrição da funcionalidade e extraia as palavras-chave mais significativas
   - Crie um nome curto de 2 a 4 palavras que represente a essência da funcionalidade
   - Use o formato ação-substantivo quando possível (por exemplo, "add-user-auth", "fix-payment-bug")
   - Preserve termos técnicos e siglas (OAuth2, API, JWT, etc.)
   - Mantenha-o conciso, mas descritivo o bastante para compreender a funcionalidade rapidamente
   - Exemplos:
     - "Quero adicionar autenticação de usuário" → "user-auth"
     - "Implementar integração OAuth2 para a API" → "oauth2-api-integration"
     - "Criar um dashboard de analytics" → "analytics-dashboard"
     - "Corrigir o timeout do processamento de pagamentos" → "fix-payment-timeout"

2. **Criação do branch** (opcional, via hook):

   Se um hook `before_specify` tiver sido executado com sucesso nas Verificações pré-execução acima, ele terá criado ou selecionado um branch Git e produzido um JSON com `BRANCH_NAME` e `FEATURE_NUM`. Registre esses valores como referência, mas o nome do branch **não** determina o nome do diretório da especificação.

   Se o usuário fornecer explicitamente `GIT_BRANCH_NAME`, repasse-o ao hook para que o script de branch use o valor exato como nome do branch, sem gerar prefixo ou sufixo.

3. **Crie o diretório da funcionalidade da especificação**:

   As especificações ficam no diretório padrão `specs/`, a menos que o usuário forneça explicitamente `SPECIFY_FEATURE_DIRECTORY`.

   **Ordem de resolução de `SPECIFY_FEATURE_DIRECTORY`**:
   1. Se o usuário forneceu explicitamente `SPECIFY_FEATURE_DIRECTORY` (por exemplo, por variável de ambiente, argumento ou configuração), use-o sem alterações
   2. Caso contrário, gere-o automaticamente em `specs/`:
      - Verifique `branch_numbering` em `.specify/init-options.json`
      - Se for `"timestamp"`, o prefixo será `YYYYMMDD-HHMMSS` (timestamp atual)
      - Se for `"sequential"` ou estiver ausente, o prefixo será `NNN` (próximo número disponível com três dígitos após examinar os diretórios existentes em `specs/`)
      - Monte o nome do diretório: `<prefix>-<short-name>` (por exemplo, `003-user-auth` ou `20260319-143022-user-auth`)
      - Defina `SPECIFY_FEATURE_DIRECTORY` como `specs/<directory-name>`

   **Crie o diretório e o arquivo de especificação**:
   - `mkdir -p SPECIFY_FEATURE_DIRECTORY`
   - Resolva o `spec-template` ativo pela pilha de resolução de presets/templates do Spec Kit (equivalente a `specify preset resolve spec-template`)
   - Copie o arquivo `spec-template` resolvido para `SPECIFY_FEATURE_DIRECTORY/spec.md` como ponto de partida
   - Defina `SPEC_FILE` como `SPECIFY_FEATURE_DIRECTORY/spec.md`
   - Persista o path resolvido em `.specify/feature.json`:

     ```json
     {
       "feature_directory": "<resolved feature dir>"
     }

     ```

     Grave o valor real do path resolvido (por exemplo, `specs/003-user-auth`), não a string literal `SPECIFY_FEATURE_DIRECTORY`.
     Isso permite que comandos posteriores (`__SPECKIT_COMMAND_PLAN__`, `__SPECKIT_COMMAND_TASKS__` etc.) localizem a funcionalidade sem depender das convenções de nome do branch Git.

   **IMPORTANTE**:
   - Você deve criar somente uma funcionalidade por `__SPECKIT_COMMAND_SPECIFY__` invocação
   - O nome do diretório da especificação e o nome do branch Git são independentes — podem ser iguais, mas essa é uma escolha do usuário
   - O diretório e o arquivo de especificação são sempre criados por este comando, nunca pelo hook

4. Carregue o arquivo `spec-template` ativo resolvido para compreender as seções obrigatórias.

5. **SE EXISTIR**: Carregue `/memory/constitution.md` para obter os princípios do projeto e as restrições de governança.

6. Siga este fluxo de execução:
    1. Interprete a descrição do usuário nos argumentos
       Se estiver vazia: ERRO "Nenhuma descrição de funcionalidade foi fornecida"
    2. Extraia os conceitos principais da descrição
       Identifique atores, ações, dados e restrições
    3. Para aspectos pouco claros:
       - Faça suposições fundamentadas no contexto e nos padrões do setor
       - Marque com [NEEDS CLARIFICATION: pergunta específica] somente se:
         - A escolha afetar significativamente o escopo da funcionalidade ou a experiência do usuário
         - Existirem várias interpretações razoáveis com implicações diferentes
         - Não existir um padrão razoável
       - **LIMITE: no máximo três marcadores [NEEDS CLARIFICATION] ao todo**
       - Priorize esclarecimentos por impacto: escopo > segurança/privacidade > experiência do usuário > detalhes técnicos
    4. Preencha a seção User Scenarios & Testing
       Se não houver um fluxo claro do usuário: ERRO "Não foi possível determinar os cenários do usuário"
    5. Gere Functional Requirements
       Cada requisito deve ser testável
       Use padrões razoáveis para detalhes não especificados (documente as suposições na seção Assumptions)
    6. Defina Success Criteria
       Crie resultados mensuráveis e independentes de tecnologia
       Inclua métricas quantitativas (tempo, desempenho, volume) e medidas qualitativas (satisfação do usuário, conclusão da tarefa)
       Cada critério deve ser verificável sem detalhes de implementação
    7. Identifique Key Entities (se houver dados)
    8. Retorne: SUCCESS (especificação pronta para planejamento)

6. Escreva a especificação em SPEC_FILE usando a estrutura do template, substituindo placeholders por detalhes concretos derivados da descrição da funcionalidade (argumentos) e preservando a ordem das seções e os headings.

7. **Validação da qualidade da especificação**: após escrever a especificação inicial, valide-a conforme os critérios de qualidade:

   a. **Crie o checklist de qualidade da especificação**: Gere um arquivo de checklist em `SPECIFY_FEATURE_DIRECTORY/checklists/requirements.md` usando a estrutura do template de checklist com estes itens de validação:

      ```markdown
      # Specification Quality Checklist: [FEATURE NAME]

      **Purpose**: Validate specification concluídoness and quality before proceeding to planning
      **Created**: [DATE]
      **Feature**: [Link to spec.md]

      ## Content Quality

      - [ ] No implementation details (languages, frameworks, APIs)
      - [ ] Focused on user value and business needs
      - [ ] Written for non-technical stakeholders
      - [ ] All mandatory sections concluídod

      ## Requirement Completeness

      - [ ] No [NEEDS CLARIFICATION] markers remain
      - [ ] Requirements are testable and unambiguous
      - [ ] Success criteria are measurable
      - [ ] Success criteria are technology-agnostic (no implementation details)
      - [ ] All acceptance scenarios are defined
      - [ ] Edge cases are identified
      - [ ] Scope is clearly bounded
      - [ ] Dependencies and assumptions identified

      ## Feature Readiness

      - [ ] All functional requirements have clear acceptance criteria
      - [ ] User scenarios cover primary flows
      - [ ] Feature meets measurable outcomes defined in Success Criteria
      - [ ] No implementation details leak into specification

      ## Notes

      - Items marked incomplete require spec updates before `__SPECKIT_COMMAND_CLARIFY__` or `__SPECKIT_COMMAND_PLAN__`

      ```

   b. **Execute a verificação de validação**: Revise a especificação conforme cada item do checklist:
      - Para cada item, determine se passa ou falha
      - Documente os problemas específicos encontrados (cite as seções relevantes da especificação)

   c. **Trate os resultados da validação**:

      - **Se todos os itens passarem**: Marque o checklist como concluído e prossiga para a seção Hooks pós-execução obrigatórios

      - **Se houver itens com falha (exceto [NEEDS CLARIFICATION])**:
        1. Liste os itens com falha e os problemas específicos
        2. Atualize a especificação para corrigir cada problema
        3. Execute a validação novamente até que todos os itens passem (no máximo três iterações)
        4. Se ainda houver falhas após três iterações, documente os problemas restantes nas observações do checklist e avise o usuário

      - **Se permanecerem marcadores [NEEDS CLARIFICATION]**:
        1. Extraia todos os [NEEDS CLARIFICATION: ...] marcadores da especificação
        2. **VERIFICAÇÃO DO LIMITE**: Se houver mais de três marcadores, mantenha somente os três mais críticos (por impacto em escopo/segurança/UX) e faça suposições fundamentadas para os demais
        3. Para cada esclarecimento necessário (no máximo três), apresente opções ao usuário neste formato:

           ```markdown
           ## Question [N]: [Topic]

           **Context**: [Quote relevant spec section]

           **What we need to know**: [Specific question from NEEDS CLARIFICATION marker]

           **Suggested Answers**:

           | Option | Answer | Implications |
           |--------|--------|--------------|
           | A      | [First suggested answer] | [What this means for the feature] |
           | B      | [Second suggested answer] | [What this means for the feature] |
           | C      | [Third suggested answer] | [What this means for the feature] |
           | Custom | Provide your own answer | [Explain how to provide custom input] |

           **Your choice**: _[Wait for user response]_

           ```

        4. **CRÍTICO - Table Formatting**: Garanta que as tabelas Markdown estejam formatadas corretamente:
           - Use espaçamento consistente e pipes alinhados
           - Cada célula deve ter espaços ao redor do conteúdo: `| Content |` não `|Content|`
           - O separador do cabeçalho deve ter pelo menos três hifens: `|--------|`
           - Teste se a tabela é renderizada corretamente na visualização Markdown
        5. Numere as perguntas sequencialmente (Q1, Q2, Q3 - no máximo três ao todo)
        6. Apresente todas as perguntas juntas antes de aguardar as respostas
        7. Aguarde o usuário responder com suas escolhas para todas as perguntas (por exemplo, "Q1: A, Q2: Custom - [detalhes], Q3: B")
        8. Atualize a especificação substituindo cada marcador [NEEDS CLARIFICATION] pela resposta selecionada ou fornecida pelo usuário
        9. Execute a validação novamente depois que todos os esclarecimentos forem resolvidos

   d. **Atualize o checklist**: Após cada iteração de validação, atualize o arquivo de checklist com o status atual de aprovação/reprovação

### Hooks pós-execução obrigatórios

**Você DEVE concluir esta seção antes de informar a conclusão ao usuário.**

Verifique se `.specify/extensions.yml` existe na raiz do projeto.

- Se não existir ou se nenhum hook estiver registrado em `hooks.after_specify`, vá para o Relatório de conclusão.
- Se existir, leia-o e procure entradas na chave `hooks.after_specify`.
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

Informe a conclusão ao usuário com:

- `SPECIFY_FEATURE_DIRECTORY` — o path do diretório da funcionalidade
- `SPEC_FILE` — o path do arquivo da especificação
- Resumo dos resultados do checklist
- Prontidão para a próxima fase (`__SPECKIT_COMMAND_CLARIFY__` ou `__SPECKIT_COMMAND_PLAN__`)

**OBSERVAÇÃO:** a criação do branch é tratada pelo hook `before_specify` (extensão Git). A criação do diretório e do arquivo da especificação é sempre tratada por este comando principal.

### Diretrizes rápidas

- Concentre-se em **O QUE** os usuários precisam e **POR QUÊ**.
- Evite COMO implementar (sem stack tecnológica, APIs ou estrutura de código).
- Escreva para stakeholders de negócio, não para desenvolvedores.
- NÃO crie checklists incorporados à especificação. Isso será feito por um comando separado.

#### Requisitos das seções

- **Seções obrigatórias**: devem ser preenchidas para toda funcionalidade
- **Seções opcionais**: inclua somente quando forem relevantes para a funcionalidade
- Quando uma seção não se aplicar, remova-a por completo (não a deixe como "N/A")

#### Para geração por IA

Ao criar esta especificação a partir de um prompt do usuário:

1. **Faça suposições fundamentadas**: Use contexto, padrões do setor e padrões comuns para preencher lacunas
2. **Documente as suposições**: Registre padrões razoáveis na seção Assumptions
3. **Limite os esclarecimentos**: No máximo três [NEEDS CLARIFICATION] marcadores — use-os somente para decisões críticas que:
   - Afetem significativamente o escopo da funcionalidade ou a experiência do usuário
   - Tenham várias interpretações razoáveis com implicações diferentes
   - Não tenham um padrão razoável

4. **Priorize os esclarecimentos**: escopo > segurança/privacidade > experiência do usuário > detalhes técnicos
5. **Pense como uma pessoa de testes**: Todo requisito vago deve falhar no item "testável e inequívoco" do checklist
6. **Áreas comuns que exigem esclarecimento** (somente se não houver um padrão razoável):
   - Escopo e limites da funcionalidade (incluir/excluir casos de uso específicos)
   - Tipos de usuário e permissões (se houver várias interpretações conflitantes possíveis)
   - Requisitos de segurança/conformidade (quando forem juridicamente/financeiramente significativos)

**Exemplos de padrões razoáveis** (não pergunte sobre eles):

- Retenção de dados: Práticas padrão do setor para o domínio
- Metas de desempenho: Expectativas padrão de aplicações web/móveis, salvo especificação em contrário
- Tratamento de erros: Mensagens amigáveis com fallbacks adequados
- Método de autenticação: Sessão padrão ou OAuth2 para aplicações web
- Padrões de integração: Use padrões adequados ao projeto (REST/GraphQL para web services, chamadas de função para bibliotecas, argumentos CLI para ferramentas etc.)

#### Diretrizes para critérios de sucesso

Os critérios de sucesso devem ser:

1. **Mensuráveis**: Inclua métricas específicas (tempo, porcentagem, contagem, taxa)
2. **Independentes de tecnologia**: Sem menção a frameworks, linguagens, bancos de dados ou ferramentas
3. **Focados no usuário**: Descreva resultados da perspectiva do usuário/negócio, não detalhes internos do sistema
4. **Verificáveis**: Podem ser testados/validados sem conhecer detalhes de implementação

**Bons exemplos**:

- "Os usuários concluem o checkout em menos de três minutos"
- "O sistema comporta 10.000 usuários simultâneos"
- "95% das pesquisas retornam resultados em menos de um segundo"
- "A taxa de conclusão da tarefa melhora em 40%"

**Exemplos inadequados** (focados na implementação):

- "O tempo de resposta da API é inferior a 200 ms" (técnico demais; use "Os usuários veem os resultados instantaneamente")
- "O banco de dados processa 1.000 TPS" (detalhe de implementação; use uma métrica voltada ao usuário)
- "Os componentes React renderizam com eficiência" (específico de framework)
- "A taxa de acerto do cache Redis é superior a 80%" (específico de tecnologia)

### Critérios de conclusão do fluxo

- [ ] Especificação escrita em `SPEC_FILE` e validada conforme o checklist de qualidade
- [ ] Hooks de extensão acionados ou ignorados conforme as regras em Hooks pós-execução obrigatórios acima
- [ ] Conclusão informada ao usuário com o diretório da funcionalidade, o path do arquivo de especificação e os resultados do checklist

## Exemplo de invocação

```text
`/speckit.specify <descrição da funcionalidade>`

```
