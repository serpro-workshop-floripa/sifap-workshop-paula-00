---
agent: speckit.implement
---

# Spec-Kit — Implementar

## Objetivo

Executar a implementação descrita em `tasks.md` e validá-la contra a especificação e o plano.

## Quando invocar

Use este prompt quando a especificação, o plano e `tasks.md` estiverem prontos para execução.

## Pré-condições

- O repositório e os artefatos exigidos pelo fluxo Spec-Kit devem estar disponíveis.
- Os hooks de extensão aplicáveis devem ser avaliados conforme o corpo do prompt.

## Entradas que a equipe deve fornecer

- A descrição ou orientação adicional fornecida em `$arguments`.

## O que farei

- Executarei o fluxo Spec-Kit descrito no corpo do prompt.
- Validarei os artefatos e informarei o resultado ao usuário.

## O que NÃO farei

- Não ignorarei gates, dependências, hooks obrigatórios nem validações do fluxo.
- Não alterarei placeholders, comandos, paths, IDs ou estruturas exigidas pelo Spec-Kit.

## Formato de saída

Um relatório final com o trabalho concluído, validações e eventuais bloqueios.

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

**Verifique hooks de extensão (antes da implementação)**:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia-o e procure entradas na chave `hooks.before_implement`
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

1. Execute `{SCRIPT}` na raiz do repositório e interprete FEATURE_DIR e a lista AVAILABLE_DOCS. Todos os paths devem ser absolutos. Para aspas simples em argumentos como "I'm Groot", use sintaxe de escape, por exemplo: 'I'\''m Groot' (ou aspas duplas, se possível: "I'm Groot").

2. **Verifique o status dos checklists** (se FEATURE_DIR/checklists/ existir):
   - Examine todos os arquivos de checklist no diretório checklists/
   - Para cada checklist, conte:
     - Total de itens: todas as linhas correspondentes a `- [ ]` ou `- [X]` ou `- [x]`
     - Itens concluídos: linhas correspondentes a `- [X]` ou `- [x]`
     - Itens incompletos: linhas correspondentes a `- [ ]`
   - Crie uma tabela de status:

     ```text
     | Checklist | Total | Completed | Inconcluído | Status |
     |-----------|-------|-----------|------------|--------|
     | ux.md     | 12    | 12        | 0          | ✓ PASS |
     | test.md   | 8     | 5         | 3          | ✗ FAIL |
     | security.md | 6   | 6         | 0          | ✓ PASS |

     ```

   - Calcule o status geral:
     - **PASS**: todos os checklists têm zero itens incompletos
     - **FAIL**: um ou mais checklists têm itens incompletos

   - **Se algum checklist estiver incompleto**:
     - Exiba a tabela com as contagens de itens incompletos
     - **STOP** e pergunte: "Alguns checklists estão incompletos. Deseja prosseguir com a implementação mesmo assim? (sim/não)"
     - Aguarde a resposta do usuário antes de continuar
     - Se o usuário disser "no", "wait" ou "stop", interrompa a execução
     - Se o usuário disser "yes", "proceed" ou "continue", prossiga para a etapa 3

   - **Se todos os checklists estiverem completos**:
     - Exiba a tabela mostrando que todos os checklists passaram
     - Prossiga automaticamente para a etapa 3

3. Carregue e analise o contexto da implementação:
   - **OBRIGATÓRIO**: Leia tasks.md para obter a lista completa de tarefas e o plano de execução
   - **OBRIGATÓRIO**: Leia plan.md para obter stack tecnológica, arquitetura e estrutura de arquivos
   - **SE EXISTIR**: Leia data-model.md para obter entidades e relacionamentos
   - **SE EXISTIR**: Leia contracts/ para obter especificações de API e requisitos de teste
   - **SE EXISTIR**: Leia research.md para obter decisões técnicas e restrições
   - **SE EXISTIR**: Leia /memory/constitution.md para obter restrições de governança
   - **SE EXISTIR**: Leia quickstart.md para obter cenários de integração

4. **Verificação da configuração do projeto**:
   - **REQUIRED**: Crie/verifique arquivos de ignore com base na configuração real do projeto:

   **Lógica de detecção e criação**:
   - Verifique se o comando a seguir é bem-sucedido para determinar se o repositório é um repositório Git (crie/verifique .gitignore nesse caso):

     ```sh
     git rev-parse --git-dir 2>/dev/null

     ```

   - Verifique se Dockerfile* existe ou se Docker aparece em plan.md → crie/verifique .dockerignore
   - Verifique se .eslintrc* existe → crie/verifique .eslintignore
   - Verifique se eslint.config.* existe → garanta que as entradas `ignores` da configuração cubram os padrões obrigatórios
   - Verifique se .prettierrc* existe → crie/verifique .prettierignore
   - Verifique se .npmrc ou package.json existe → crie/verifique .npmignore (se houver publicação)
   - Verifique se existem arquivos Terraform (*.tf) → crie/verifique .terraformignore
   - Verifique se .helmignore é necessário (charts Helm presentes) → crie/verifique .helmignore

   **Se o arquivo de ignore já existir**: Verifique se ele contém os padrões essenciais e acrescente apenas os padrões críticos ausentes
   **Se o arquivo de ignore estiver ausente**: Crie-o com o conjunto completo de padrões da tecnologia detectada

   **Padrões comuns por tecnologia** (da stack tecnológica de plan.md):
   - **Node.js/JavaScript/TypeScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
   - **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
   - **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
   - **C#/.NET**: `bin/`, `obj/`, `*.user`, `*.suo`, `packages/`
   - **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
   - **Ruby**: `.bundle/`, `log/`, `tmp/`, `*.gem`, `vendor/bundle/`
   - **PHP**: `vendor/`, `*.log`, `*.cache`, `*.env`
   - **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`, `*.rlib`, `*.prof*`, `.idea/`, `*.log`, `.env*`
   - **Kotlin**: `build/`, `out/`, `.gradle/`, `.idea/`, `*.class`, `*.jar`, `*.iml`, `*.log`, `.env*`
   - **C++**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.so`, `*.a`, `*.exe`, `*.dll`, `.idea/`, `*.log`, `.env*`
   - **C**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.a`, `*.so`, `*.exe`, `*.dll`, `autom4te.cache/`, `config.status`, `config.log`, `.idea/`, `*.log`, `.env*`
   - **Swift**: `.build/`, `DerivedData/`, `*.swiftpm/`, `Packages/`
   - **R**: `.Rproj.user/`, `.Rhistory`, `.RData`, `.Ruserdata`, `*.Rproj`, `packrat/`, `renv/`
   - **Universal**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `.vscode/`, `.idea/`

   **Padrões específicos de ferramentas**:
   - **Docker**: `node_modules/`, `.git/`, `Dockerfile*`, `.dockerignore`, `*.log*`, `.env*`, `coverage/`
   - **ESLint**: `node_modules/`, `dist/`, `build/`, `coverage/`, `*.min.js`
   - **Prettier**: `node_modules/`, `dist/`, `build/`, `coverage/`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - **Terraform**: `.terraform/`, `*.tfstate*`, `*.tfvars`, `.terraform.lock.hcl`
   - **Kubernetes/k8s**: `*.secret.yaml`, `secrets/`, `.kube/`, `kubeconfig*`, `*.key`, `*.crt`

5. Interprete tasks.md e extraia sua estrutura:
   - **Fases das tarefas**: configuração, testes, núcleo, integração e acabamento
   - **Dependências das tarefas**: regras de execução sequencial versus paralela
   - **Detalhes das tarefas**: ID, descrição, paths de arquivos e marcadores de paralelismo [P]
   - **Fluxo de execução**: ordem e requisitos de dependência

6. Execute a implementação seguindo o plano de tarefas:
   - **Execução fase a fase**: conclua cada fase antes de passar à seguinte
   - **Respeite as dependências**: execute as tarefas sequenciais em ordem; tarefas paralelas [P] podem ser executadas em conjunto
   - **Siga a abordagem TDD**: execute tarefas de teste antes das tarefas de implementação correspondentes
   - **Coordenação por arquivo**: tarefas que afetam os mesmos arquivos devem ser executadas sequencialmente
   - **Checkpoints de validação**: verifique a conclusão de cada fase antes de prosseguir

7. Regras de execução da implementação:
   - **Configuração primeiro**: inicialize estrutura, dependências e configuração do projeto
   - **Testes antes do código**: se precisar escrever testes para contratos, entidades e cenários de integração
   - **Desenvolvimento principal**: implemente modelos, serviços, comandos CLI e endpoints
   - **Trabalho de integração**: conexões de banco de dados, middleware, logging e serviços externos
   - **Acabamento e validação**: testes unitários, otimização de desempenho e documentação

8. Acompanhamento do progresso e tratamento de erros:
   - Informe o progresso após cada tarefa concluída
   - Interrompa a execução se qualquer tarefa não paralela falhar
   - Para tarefas paralelas [P], continue com as tarefas bem-sucedidas e informe as que falharam
   - Forneça mensagens de erro claras com contexto para depuração
   - Sugira próximos passos se a implementação não puder prosseguir
   - **IMPORTANTE** Nas tarefas concluídas, marque a tarefa como [X] no arquivo de tarefas.

9. Validação da conclusão:
   - Verifique se todas as tarefas obrigatórias foram concluídas
   - Verifique se as funcionalidades implementadas correspondem à especificação original
   - Valide se os testes passam e se a cobertura atende aos requisitos
   - Confirme que a implementação segue o plano técnico

Observação: Este comando pressupõe que exista um detalhamento completo das tarefas em tasks.md. Se as tarefas estiverem incompletas ou ausentes, sugira executar `__SPECKIT_COMMAND_TASKS__` primeiro para gerar novamente a lista de tarefas.

### Hooks pós-execução obrigatórios

**Você DEVE concluir esta seção antes de informar a conclusão ao usuário.**

Verifique se `.specify/extensions.yml` existe na raiz do projeto.

- Se não existir ou se nenhum hook estiver registrado em `hooks.after_implement`, vá para o Relatório de conclusão.
- Se existir, leia-o e procure entradas na chave `hooks.after_implement`.
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

Informe o status final com um resumo do trabalho concluído.

### Critérios de conclusão do fluxo

- [ ] Todas as tarefas em tasks.md concluídas e marcadas como `[X]`
- [ ] Implementação validada em relação à especificação, ao plano e à cobertura de testes
- [ ] Hooks de extensão acionados ou ignorados conforme as regras em Hooks pós-execução obrigatórios acima
- [ ] Conclusão informada ao usuário com um resumo do trabalho concluído

## Exemplo de invocação

```text
`/speckit.implement`

```
