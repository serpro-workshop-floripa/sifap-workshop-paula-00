---
agent: speckit.constitution
---
# Atualizar a constituição do projeto

## Objetivo

Preencher ou atualizar `.specify/memory/constitution.md`, decidir o incremento semântico de versão e
propagar as mudanças para os artefatos dependentes.

## Quando invocar

Invoque ao criar a constituição do projeto ou alterar princípios, governança, critérios de conformidade ou
regras que afetem templates e orientações de execução.

## Pré-condições

- `.specify/memory/constitution.md` deve existir ou ser inicializado a partir de
  `.specify/templates/constitution-template.md`.
- Os templates e documentos dependentes devem estar disponíveis para validação de consistência.

## Inputs que a equipe deve fornecer

```text
$ARGUMENTS
```

Considere o input do usuário antes de prosseguir, quando ele não estiver vazio.

## O que farei

- Identificarei e preencherei placeholders da constituição.
- Determinarei o incremento MAJOR, MINOR ou PATCH.
- Validarei e atualizarei artefatos dependentes.
- Incluirei um Sync Impact Report no início da constituição.
- Gravarei a constituição completa e apresentarei um resumo final.

## O que NÃO farei

- Não criarei um novo template.
- Não deixarei placeholders sem justificativa explícita.
- Não alterarei a hierarquia de títulos do template.
- Não omitirei a validação dos artefatos dependentes.

## Formato de saída

Apresente a nova versão e a justificativa do incremento, os arquivos que exigem acompanhamento manual e uma
mensagem de commit sugerida.

## Definição de pronto

- [ ] Não restam tokens entre colchetes sem explicação.
- [ ] A versão coincide com o Sync Impact Report.
- [ ] As datas usam o formato ISO YYYY-MM-DD.
- [ ] Os princípios são declarativos, testáveis e inequívocos.
- [ ] Os artefatos dependentes foram atualizados ou marcados como pendentes.
- [ ] Os hooks posteriores foram apresentados conforme a configuração.

## Corpo do prompt

### Verificações prévias à execução

Verifique os hooks de extensão antes de atualizar a constituição:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia o arquivo e procure entradas na chave `hooks.before_constitution`.
- Se o YAML não puder ser interpretado ou for inválido, ignore silenciosamente a verificação e continue.
- Exclua hooks cujo `enabled` seja explicitamente `false`; considere habilitados por padrão os hooks sem
  esse campo.
- Não interprete expressões `condition`. Considere executável o hook sem `condition`, ou com valor nulo ou
  vazio. Ignore condições não vazias e deixe sua avaliação para HookExecutor.
- Para cada hook executável, produza:
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

    Wait for the result of the hook command before proceeding to the Outline.
    ```

- Se não houver hooks registrados ou `.specify/extensions.yml` não existir, prossiga silenciosamente.

### Fluxo de execução

Você está atualizando a constituição em `.specify/memory/constitution.md`. Esse arquivo é um TEMPLATE com
placeholders entre colchetes, como `[PROJECT_NAME]` e `[PRINCIPLE_1_NAME]`. Sua tarefa é obter ou derivar
valores concretos, preencher o template com precisão e propagar as alterações aos artefatos dependentes.

Se `.specify/memory/constitution.md` ainda não existir, ele deveria ter sido inicializado a partir de
`.specify/templates/constitution-template.md` durante a preparação do projeto. Se estiver ausente, copie o
template primeiro.

1. Carregue a constituição existente em `.specify/memory/constitution.md`.
   - Identifique cada placeholder no formato `[ALL_CAPS_IDENTIFIER]`.
   - O usuário pode exigir menos ou mais princípios do que o template. Quando ele informar uma quantidade,
     respeite-a e siga a estrutura geral.

2. Obtenha ou derive os valores:
   - Se o input do usuário fornecer um valor, use-o.
   - Caso contrário, infira-o do contexto do repositório, como README, docs e versões anteriores da
     constituição incorporadas ao histórico disponível.
   - Para datas de governança, `RATIFICATION_DATE` é a data original de adoção. Se for desconhecida, pergunte
     ou marque TODO. `LAST_AMENDED_DATE` é a data atual quando houver mudanças; caso contrário, preserve a
     anterior.
   - Incremente `CONSTITUTION_VERSION` conforme o versionamento semântico:
     - MAJOR: remoção ou redefinição incompatível de princípios ou governança;
     - MINOR: novo princípio ou seção, ou ampliação material da orientação;
     - PATCH: esclarecimentos, redação, correções tipográficas ou refinamentos sem mudança semântica.
   - Se o tipo de incremento for ambíguo, apresente a justificativa proposta antes de concluir.

3. Redija a constituição atualizada:
   - Substitua todos os placeholders por texto concreto. Somente preserve slots do template que o projeto
     tenha escolhido intencionalmente não definir e justifique cada um.
   - Preserve a hierarquia de títulos. Remova comentários quando substituídos, salvo quando ainda oferecerem
     orientação útil.
   - Garanta que cada seção Principle tenha um nome sucinto, um parágrafo ou lista de regras inegociáveis e
     uma justificativa explícita quando ela não for óbvia.
   - Garanta que Governance descreva o procedimento de alteração, a política de versionamento e as
     expectativas de revisão de conformidade.

4. Execute a checklist de propagação de consistência:
   - Leia `.specify/templates/plan-template.md` e alinhe qualquer `Constitution Check` ou regra aos princípios.
   - Leia `.specify/templates/spec-template.md` e atualize o alinhamento de escopo e requisitos quando a
     constituição adicionar ou remover seções e restrições obrigatórias.
   - Leia `.specify/templates/tasks-template.md` e garanta que a categorização das tarefas reflita tipos
     exigidos pelos princípios, como observabilidade, versionamento e disciplina de testes.
   - Leia cada arquivo em `.specify/templates/commands/*.md`, inclusive este, e remova referências
     desatualizadas ou específicas de um agent, como CLAUDE, quando a orientação precisar ser genérica.
   - Leia documentos de orientação de runtime, como `README.md`, `docs/quickstart.md` ou instruções de agent,
     quando existirem, e atualize referências aos princípios alterados.

5. Produza um Sync Impact Report como comentário HTML no início da constituição atualizada:
   - mudança de versão: anterior → nova;
   - princípios modificados, incluindo título anterior → novo quando renomeados;
   - seções adicionadas;
   - seções removidas;
   - templates que exigem atualização, com ✅ updated ou ⚠ pending e seus paths;
   - TODOs de acompanhamento para placeholders adiados intencionalmente.

6. Valide antes da saída final:
   - não há tokens entre colchetes sem explicação;
   - a linha de versão coincide com o relatório;
   - as datas usam ISO YYYY-MM-DD;
   - os princípios são declarativos, testáveis e não usam linguagem vaga. Substitua "should" por MUST/SHOULD
     acompanhado da justificativa adequada.

7. Grave o conteúdo completo em `.specify/memory/constitution.md`, substituindo o arquivo.

8. Apresente ao usuário:
   - a nova versão e a justificativa do incremento;
   - arquivos marcados para acompanhamento manual;
   - uma mensagem de commit sugerida, por exemplo:
     `docs: amend constitution to vX.Y.Z (principle additions + governance update)`.

### Requisitos de formatação e estilo

- Use os títulos Markdown exatamente como aparecem no template; não promova nem rebaixe níveis.
- Quebre linhas longas de justificativa para facilitar a leitura, idealmente abaixo de 100 caracteres, sem
  impor quebras artificiais.
- Mantenha uma única linha em branco entre as seções.
- Não use espaços ao final das linhas.

Se o usuário fornecer atualizações parciais, como a revisão de um único princípio, ainda assim execute as
etapas de validação e decisão de versão.

Se faltar informação crítica, como uma data de ratificação realmente desconhecida, insira
`TODO(<FIELD_NAME>): explanation` e inclua o item no Sync Impact Report.

Não crie um novo template. Sempre opere sobre `.specify/memory/constitution.md`.

### Verificações posteriores à execução

Após atualizar a constituição, verifique `.specify/extensions.yml` e procure entradas em
`hooks.after_constitution`:

- Se o YAML for inválido, ignore silenciosamente a verificação.
- Exclua hooks cujo `enabled` seja explicitamente `false` e considere os demais habilitados por padrão.
- Não interprete `condition`; execute somente hooks sem condição ou com condição nula ou vazia.
- Para cada hook opcional (`optional: true`), produza:

  ```text
  ## Extension Hooks

  **Optional Hook**: {extension}
  Command: `/{command}`
  Description: {description}

  Prompt: {prompt}
  To execute: `/{command}`
  ```

- Para cada hook obrigatório (`optional: false`), produza:

  ```text
  ## Extension Hooks

  **Automatic Hook**: {extension}
  Executing: `/{command}`
  EXECUTE_COMMAND: {command}
  ```

Se não houver hooks registrados ou `.specify/extensions.yml` não existir, prossiga silenciosamente.

## Exemplo de invocação

```text
__SPECKIT_COMMAND_CONSTITUTION__ adicionar princípio obrigatório de rastreabilidade e testes
```
