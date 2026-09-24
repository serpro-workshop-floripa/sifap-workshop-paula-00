---
agent: speckit.checklist
---
# Gerar checklist de qualidade dos requisitos

## Objetivo

Criar testes unitários para a redação dos requisitos, validando qualidade, clareza, consistência,
mensurabilidade e completude, sem testar a implementação.

## Quando invocar

Invoque quando precisar avaliar se os requisitos de uma feature estão claros, completos, consistentes e
prontos para implementação.

## Pré-condições

- A feature ativa deve possuir `spec.md`.
- `plan.md` e `tasks.md` serão usados quando existirem.
- `/memory/constitution.md` será carregado quando existir.

## Inputs que a equipe deve fornecer

```text
$ARGUMENTS
```

Considere o input do usuário antes de prosseguir, quando ele não estiver vazio.

## O que farei

- Esclarecerei o foco, a profundidade, o público e os riscos relevantes.
- Carregarei somente o contexto necessário dos artefatos.
- Criarei ou ampliarei uma checklist em `FEATURE_DIR/checklists/`.
- Avaliarei os requisitos, nunca o comportamento da implementação.
- Manterei rastreabilidade em pelo menos 80% dos itens.

## O que NÃO farei

- Não criarei casos de teste, planos de QA nem procedimentos de execução.
- Não verificarei se código, interfaces ou APIs funcionam.
- Não excluirei nem substituirei conteúdo existente de uma checklist.
- Não inventarei categorias ou requisitos ausentes.

## Formato de saída

Informe o path completo da checklist, a quantidade de itens, se o arquivo foi criado ou ampliado, as áreas
de foco, a profundidade, o ator ou momento de uso e os itens obrigatórios solicitados pelo usuário.

## Definição de pronto

- [ ] A checklist segue `templates/checklist-template.md`, quando disponível.
- [ ] Os IDs CHK### são únicos e globalmente crescentes no arquivo.
- [ ] Todos os itens avaliam a qualidade dos requisitos.
- [ ] Pelo menos 80% dos itens têm referência de rastreabilidade.
- [ ] O conteúdo anterior foi preservado.
- [ ] Os hooks posteriores foram apresentados conforme a configuração.

## Corpo do prompt

### Propósito da checklist: "Unit Tests for English"

**CONCEITO CRÍTICO**: checklists são **UNIT TESTS FOR REQUIREMENTS WRITING**. Elas validam a qualidade, a
clareza e a completude dos requisitos em um domínio.

Não use a checklist para verificação ou teste da implementação:

- Não escreva "Verify the button clicks correctly".
- Não escreva "Test error handling works".
- Não escreva "Confirm the API returns 200".
- Não verifique se o código ou a implementação corresponde à especificação.

Use a checklist para validar a qualidade dos requisitos:

- "Are visual hierarchy requirements defined for all card types?" avalia completude.
- "Is 'prominent display' quantified with specific sizing/positioning?" avalia clareza.
- "Are hover state requirements consistent across all interactive elements?" avalia consistência.
- "Are accessibility requirements defined for keyboard navigation?" avalia cobertura.
- "Does the spec define what happens when logo image fails to load?" avalia casos extremos.

Metáfora: se a especificação fosse código escrito em inglês, a checklist seria sua suíte de testes
unitários. Teste se os requisitos estão bem redigidos, completos, inequívocos e prontos para implementação,
não se a implementação funciona.

### Verificações prévias à execução

Verifique os hooks de extensão antes de gerar a checklist:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia o arquivo e procure entradas na chave `hooks.before_checklist`.
- Se o YAML não puder ser interpretado ou for inválido, ignore silenciosamente a verificação e continue.
- Exclua hooks cujo `enabled` seja explicitamente `false`; considere habilitados por padrão os hooks sem
  esse campo.
- Não interprete expressões `condition`. Considere executável o hook sem `condition`, ou com valor nulo ou
  vazio. Ignore condições não vazias e deixe sua avaliação para HookExecutor.
- Para cada hook executável, produza o bloco correspondente:
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

    Wait for the result of the hook command before proceeding to the Execution Steps.
    ```

- Se não houver hooks registrados ou `.specify/extensions.yml` não existir, prossiga silenciosamente.

### Etapas de execução

1. **Preparação**: execute `{SCRIPT}` na raiz do repositório e interprete o JSON para obter FEATURE_DIR e a
   lista AVAILABLE_DOCS.
   - Todos os paths de arquivo devem ser absolutos.
   - Para aspas simples em argumentos como "I'm Groot", use a sintaxe de escape 'I'\''m Groot' ou, quando
     possível, aspas duplas: "I'm Groot".

2. **Se existir**: carregue `/memory/constitution.md` para obter princípios e restrições de governança.

3. **Esclareça a intenção dinamicamente**: derive até TRÊS perguntas contextuais iniciais, sem catálogo
   predefinido. As perguntas:
   - devem ser geradas a partir da formulação do usuário e dos sinais extraídos de spec/plan/tasks;
   - devem tratar somente de informações que mudem materialmente o conteúdo da checklist;
   - devem ser omitidas individualmente quando `$ARGUMENTS` já for inequívoco;
   - devem privilegiar precisão em vez de amplitude.

   Algoritmo:
   1. Extraia sinais: palavras-chave do domínio, como auth, latency, UX e API; indicadores de risco, como
      "critical", "must" e "compliance"; stakeholders, como "QA", "review" e "security team"; e entregáveis
      explícitos, como "a11y", "rollback" e "contracts".
   2. Agrupe os sinais em até quatro áreas candidatas de foco, ordenadas por relevância.
   3. Identifique público e momento prováveis, como autor, revisor, QA ou release, quando não explícitos.
   4. Detecte dimensões ausentes: amplitude, profundidade, ênfase em riscos, exclusões e critérios de aceite
      mensuráveis.
   5. Formule perguntas usando estes arquétipos:
      - refinamento de escopo;
      - priorização de riscos;
      - calibração de profundidade;
      - definição do público;
      - exclusão de fronteiras;
      - lacuna de classe de cenário.

   Regras de formatação:
   - Ao apresentar opções, gere uma tabela compacta com as colunas `Option | Candidate | Why It Matters`.
   - Limite as opções a A–E; omita a tabela quando uma resposta livre for mais clara.
   - Nunca peça ao usuário para repetir o que já informou.
   - Evite categorias especulativas. Em caso de dúvida, pergunte explicitamente se o item pertence ao escopo.

   Quando a interação não for possível, use:
   - profundidade: Standard;
   - público: Reviewer (PR) para assuntos de código; Author nos demais casos;
   - foco: os dois principais grupos por relevância.

   Apresente as perguntas como Q1/Q2/Q3. Após as respostas, se pelo menos duas classes de cenário
   (Alternate, Exception, Recovery ou domínio Non-Functional) permanecerem incertas, você poderá fazer até
   DUAS perguntas adicionais Q4/Q5, cada uma com justificativa de uma linha. Nunca ultrapasse cinco
   perguntas. Não faça novas perguntas se o usuário recusar.

4. **Entenda a solicitação**: combine `$ARGUMENTS` e as respostas:
   - derive o tema da checklist, como security, review, deploy ou ux;
   - consolide os itens obrigatórios mencionados;
   - mapeie os focos para a estrutura de categorias;
   - infira contexto ausente de spec/plan/tasks sem inventar informações.

5. **Carregue o contexto da feature** em FEATURE_DIR:
   - `spec.md`: requisitos e escopo;
   - `plan.md`, quando existir: detalhes técnicos e dependências;
   - `tasks.md`, quando existir: tarefas de implementação.

   Carregue somente trechos necessários às áreas de foco, resuma seções longas, use divulgação progressiva e
   faça novas leituras apenas quando detectar lacunas.

6. **Gere a checklist**, os "Unit Tests for Requirements":
   - Crie `FEATURE_DIR/checklists/` quando o diretório não existir.
   - Use um nome curto e descritivo do domínio, como `ux.md`, `api.md` ou `security.md`, no formato
     `[domain].md`.
   - Se o arquivo não existir, crie-o e numere os itens a partir de CHK001.
   - Se existir, anexe novos itens e continue após o último CHK ID.
   - Nunca exclua nem substitua conteúdo existente.

   Cada item deve avaliar os próprios requisitos quanto a:
   - **Completude**: todos os requisitos necessários estão presentes?
   - **Clareza**: os requisitos são específicos e inequívocos?
   - **Consistência**: os requisitos estão alinhados entre si?
   - **Mensurabilidade**: os requisitos podem ser verificados objetivamente?
   - **Cobertura**: todos os cenários e casos extremos foram tratados?

   Agrupe por estas categorias:
   - **Requirement Completeness**;
   - **Requirement Clarity**;
   - **Requirement Consistency**;
   - **Acceptance Criteria Quality**;
   - **Scenario Coverage**;
   - **Edge Case Coverage**;
   - **Non-Functional Requirements**;
   - **Dependencies & Assumptions**;
   - **Ambiguities & Conflicts**.

   Estrutura de cada item:
   - use uma pergunta sobre a qualidade do requisito;
   - concentre-se no que está ou não escrito na especificação ou no plano;
   - inclua a dimensão de qualidade entre colchetes;
   - use `[Spec §X.Y]` ao avaliar um requisito existente;
   - use `[Gap]` ao avaliar um requisito ausente.

   Exemplos por dimensão:

   - Completude: "Are error handling requirements defined for all API failure modes? [Gap]"
   - Clareza: "Is 'fast loading' quantified with specific timing thresholds? [Clarity, Spec §NFR-2]"
   - Consistência: "Do navigation requirements align across all pages? [Consistency, Spec §FR-10]"
   - Cobertura: "Are requirements defined for zero-state scenarios? [Coverage, Edge Case]"
   - Mensurabilidade: "Can 'balanced visual weight' be objectively verified? [Measurability, Spec §FR-2]"

   Classifique e cubra cenários Primary, Alternate, Exception/Error, Recovery e Non-Functional. Para cada
   classe, pergunte se os requisitos estão completos, claros e consistentes. Quando uma classe estiver
   ausente, pergunte se foi excluída intencionalmente ou se representa uma lacuna. Inclua resiliência e
   rollback quando houver mutação de estado.

   Requisitos de rastreabilidade:
   - no mínimo 80% dos itens devem incluir uma referência;
   - cada item deve apontar para `[Spec §X.Y]` ou usar `[Gap]`, `[Ambiguity]`, `[Conflict]` ou `[Assumption]`;
   - se não houver sistema de IDs, pergunte se foi estabelecido um esquema de IDs para requisitos e critérios
     de aceite.

   Exponha problemas da qualidade dos requisitos:
   - ambiguidades em termos sem métricas;
   - conflitos entre seções;
   - suposições não validadas;
   - dependências externas não documentadas;
   - definições ausentes.

   Consolide o conteúdo:
   - se houver mais de 40 candidatos, priorize por risco e impacto;
   - combine itens quase duplicados;
   - quando houver mais de cinco casos extremos de baixo impacto, agrupe-os em um único item.

   É absolutamente proibido:
   - iniciar um item com "Verify", "Test", "Confirm" ou "Check" seguido de comportamento da implementação;
   - referenciar execução de código, ações do usuário ou comportamento do sistema;
   - usar "Displays correctly", "works properly" ou "functions as expected";
   - transformar "Click", "navigate", "render", "load" ou "execute" em ações de teste;
   - criar casos de teste, planos de teste ou procedimentos de QA;
   - testar detalhes de implementação, como frameworks, APIs ou algoritmos.

   Padrões obrigatórios:
   - "Are [requirement type] defined/specified/documented for [scenario]?"
   - "Is [vague term] quantified/clarified with specific criteria?"
   - "Are requirements consistent between [section A] and [section B]?"
   - "Can [requirement] be objectively measured/verified?"
   - "Are [edge cases/scenarios] addressed in requirements?"
   - "Does the spec define [missing aspect]?"

7. **Siga a referência estrutural**: use o template canônico `templates/checklist-template.md` para título,
   metadados, categorias e IDs. Se o template não estiver disponível, use um H1, linhas de propósito e data,
   seções `##` por categoria e linhas `- [ ] CHK### <requirement item>`, com IDs globalmente crescentes a
   partir de CHK001.

8. **Relate o resultado**: informe o path completo, a quantidade de itens e se criou um arquivo ou anexou
   conteúdo. Resuma as áreas de foco, a profundidade, o ator ou momento de uso e os itens obrigatórios
   solicitados.

Cada invocação de `__SPECKIT_COMMAND_CHECKLIST__` usa um nome curto e descritivo e cria ou amplia o arquivo.
Isso permite várias checklists, como `ux.md`, `test.md` e `security.md`, com nomes fáceis de reconhecer.

### Tipos de checklist e exemplos

**UX Requirements Quality:** `ux.md`

- "Are visual hierarchy requirements defined with measurable criteria? [Clarity, Spec §FR-1]"
- "Are accessibility requirements specified for all interactive elements? [Coverage, Gap]"
- "Is fallback behavior defined when images fail to load? [Edge Case, Gap]"

**API Requirements Quality:** `api.md`

- "Are error response formats specified for all failure scenarios? [Completeness]"
- "Are rate limiting requirements quantified with specific thresholds? [Clarity]"
- "Are retry/timeout requirements defined for external dependencies? [Coverage, Gap]"

**Performance Requirements Quality:** `performance.md`

- "Are performance requirements quantified with specific metrics? [Clarity]"
- "Are performance targets defined for all critical user journeys? [Coverage]"
- "Are degradation requirements defined for high-load scenarios? [Edge Case, Gap]"

**Security Requirements Quality:** `security.md`

- "Are authentication requirements specified for all protected resources? [Coverage]"
- "Are data protection requirements defined for sensitive information? [Completeness]"
- "Are security failure/breach response requirements defined? [Gap, Exception Flow]"

### Anti-exemplos

Errado: os itens abaixo testam a implementação, não os requisitos.

```markdown
- [ ] CHK001 - Verify landing page displays 3 episode cards [Spec §FR-001]
- [ ] CHK002 - Test hover states work correctly on desktop [Spec §FR-003]
- [ ] CHK003 - Confirm logo click navigates to home page [Spec §FR-010]
- [ ] CHK004 - Check that related episodes section shows 3-5 items [Spec §FR-005]
```

Correto: os itens abaixo testam a qualidade dos requisitos.

```markdown
- [ ] CHK001 - Are the number and layout of featured episodes explicitly specified? [Completeness, Spec §FR-001]
- [ ] CHK002 - Are hover state requirements consistently defined for all interactive elements? [Consistency, Spec §FR-003]
- [ ] CHK003 - Are navigation requirements clear for all clickable brand elements? [Clarity, Spec §FR-010]
- [ ] CHK004 - Is the selection criteria for related episodes documented? [Gap, Spec §FR-005]
- [ ] CHK005 - Are loading state requirements defined for asynchronous episode data? [Gap]
- [ ] CHK006 - Can "visual hierarchy" requirements be objectively measured? [Measurability, Spec §FR-001]
```

Diferenças principais:

- Errado: testa se o sistema funciona. Correto: testa se os requisitos estão bem escritos.
- Errado: verifica comportamento. Correto: valida a qualidade do requisito.
- Errado: pergunta "Does it do X?". Correto: pergunta "Is X clearly specified?".

### Verificações posteriores à execução

Após gerar a checklist, verifique `.specify/extensions.yml` e procure entradas em
`hooks.after_checklist`. Aplique as mesmas regras de parsing, `enabled` e `condition` usadas nos hooks
prévios. Para cada hook executável, produza:

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

Se não houver hooks registrados ou `.specify/extensions.yml` não existir, prossiga silenciosamente.

## Exemplo de invocação

```text
__SPECKIT_COMMAND_CHECKLIST__ criar checklist de segurança para revisão do PR
```
