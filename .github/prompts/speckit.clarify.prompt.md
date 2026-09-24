---
agent: speckit.clarify
---
# Esclarecer a especificação da feature

## Objetivo

Detectar e reduzir ambiguidades ou decisões ausentes na especificação ativa e registrar cada esclarecimento
diretamente no arquivo da especificação.

## Quando invocar

Invoque e conclua este fluxo antes de `__SPECKIT_COMMAND_PLAN__`. Se o usuário optar por ignorá-lo, por
exemplo em um spike exploratório, permita a continuidade, mas alerte sobre o aumento do risco de retrabalho.

## Pré-condições

- A feature ativa deve possuir `FEATURE_SPEC`.
- Execute `{SCRIPT}` somente uma vez para descobrir os paths.
- Faça no máximo cinco perguntas durante toda a sessão.

## Inputs que a equipe deve fornecer

```text
$ARGUMENTS
```

Considere o input do usuário antes de prosseguir, quando ele não estiver vazio.

## O que farei

- Mapearei ambiguidades e lacunas de cobertura.
- Farei uma pergunta por vez, priorizada por impacto e incerteza.
- Integrarei cada resposta aceita imediatamente na especificação.
- Revalidarei a checklist de qualidade dos requisitos, quando existir.
- Relatarei cobertura, itens adiados e o próximo comando sugerido.

## O que NÃO farei

- Não farei mais de cinco perguntas.
- Não anteciparei perguntas futuras.
- Não criarei uma especificação quando `FEATURE_SPEC` estiver ausente.
- Não farei perguntas triviais, já respondidas ou puramente estilísticas.
- Não alterarei conteúdo alheio ao esclarecimento aceito.

## Formato de saída

Após o ciclo de perguntas, produza o `## Completion Report` com quantidade de perguntas respondidas, path
atualizado, seções alteradas, estado da checklist, resumo de cobertura e próximo comando.

## Definição de pronto

- [ ] As ambiguidades relevantes foram identificadas e integradas à especificação.
- [ ] A checklist de qualidade foi revalidada, quando existente.
- [ ] Os hooks posteriores foram apresentados ou ignorados conforme as regras.
- [ ] A conclusão contém perguntas respondidas, seções alteradas, checklist e cobertura.

## Corpo do prompt

### Verificações prévias à execução

Verifique os hooks de extensão antes do esclarecimento:

- Verifique se `.specify/extensions.yml` existe na raiz do projeto.
- Se existir, leia o arquivo e procure entradas na chave `hooks.before_clarify`.
- Se o YAML não puder ser interpretado ou for inválido, ignore silenciosamente a verificação e continue.
- Exclua hooks cujo `enabled` seja explicitamente `false`; considere os demais habilitados por padrão.
- Não interprete expressões `condition`. Considere executável o hook sem `condition`, ou com valor nulo ou
  vazio; ignore condições não vazias e deixe sua avaliação para HookExecutor.
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

### Etapas de execução

1. Execute `{SCRIPT}` uma vez na raiz do repositório, no modo combinado `--json --paths-only` ou
   `-Json -PathsOnly`. Interprete somente:
   - `FEATURE_DIR`;
   - `FEATURE_SPEC`;
   - opcionalmente `IMPL_PLAN` e `TASKS` para fluxos encadeados futuros.

   Se o JSON não puder ser interpretado, interrompa e instrua o usuário a executar novamente
   `__SPECKIT_COMMAND_SPECIFY__` ou verificar o ambiente da branch da feature.

   Para aspas simples em argumentos como "I'm Groot", use 'I'\''m Groot' ou, quando possível, aspas duplas:
   "I'm Groot".

2. Se existir, carregue `/memory/constitution.md` para obter princípios e restrições de governança.

3. Carregue a especificação atual e faça uma varredura estruturada de ambiguidade e cobertura. Para cada
   categoria, registre internamente Clear, Partial ou Missing. Não apresente o mapa bruto, exceto quando
   nenhuma pergunta for necessária.

   **Functional Scope & Behavior**:
   - objetivos principais do usuário e critérios de sucesso;
   - declarações explícitas de fora de escopo;
   - diferenciação de papéis e personas.

   **Domain & Data Model**:
   - entidades, atributos e relacionamentos;
   - identidade e unicidade;
   - ciclo de vida e transições de estado;
   - premissas de volume e escala.

   **Interaction & UX Flow**:
   - jornadas e sequências críticas;
   - estados de erro, vazio e carregamento;
   - acessibilidade e localização.

   **Non-Functional Quality Attributes**:
   - desempenho, com metas de latência e throughput;
   - escalabilidade e limites;
   - confiabilidade, disponibilidade e recuperação;
   - observabilidade, incluindo logs, métricas e traces;
   - segurança, privacidade, authN/Z e proteção de dados;
   - conformidade e restrições regulatórias.

   **Integration & External Dependencies**:
   - serviços ou APIs externos e modos de falha;
   - formatos de importação e exportação;
   - protocolos e versionamento.

   **Edge Cases & Failure Handling**:
   - cenários negativos;
   - rate limiting e throttling;
   - resolução de conflitos, como edições concorrentes.

   **Constraints & Tradeoffs**:
   - restrições de linguagem, armazenamento e hospedagem;
   - tradeoffs e alternativas rejeitadas.

   **Terminology & Consistency**:
   - termos canônicos do glossário;
   - sinônimos evitados ou termos descontinuados.

   **Completion Signals**:
   - testabilidade dos critérios de aceite;
   - indicadores mensuráveis de Definition of Done.

   **Misc / Placeholders**:
   - TODOs e decisões não resolvidas;
   - adjetivos ambíguos, como "robust" e "intuitive", sem quantificação.

   Para cada categoria Partial ou Missing, crie uma oportunidade de pergunta, exceto quando a resposta não
   mudar materialmente a implementação ou validação, ou quando a informação for mais adequada à fase de
   planejamento.

4. Gere internamente uma fila priorizada de no máximo cinco perguntas. Não apresente todas de uma vez.
   - Cada pergunta deve aceitar uma seleção curta de duas a cinco opções mutuamente exclusivas ou uma
     resposta de até cinco palavras.
   - Pergunte somente sobre decisões que afetem arquitetura, modelo de dados, decomposição de tarefas,
     testes, UX, operação ou conformidade.
   - Equilibre categorias e priorize áreas de alto impacto.
   - Exclua respostas já presentes, preferências estilísticas e detalhes de execução do plano que não
     bloqueiem a correção.
   - Se houver mais de cinco categorias, escolha as cinco maiores por Impact * Uncertainty.

5. Conduza o ciclo sequencial:
   - Apresente EXATAMENTE UMA pergunta por vez.
   - Para múltipla escolha, analise todas as opções e recomende a mais adequada segundo boas práticas,
     padrões comuns, redução de riscos e alinhamento ao projeto.
   - Formate a recomendação como:

     ```text
     **Recommended:** Option [X] - <reasoning>
     ```

   - Apresente todas as opções nesta tabela:

     ```markdown
     | Option | Description |
     |--------|-------------|
     | A | <Option A description> |
     | B | <Option B description> |
     | C | <Option C description> |
     | Short | Provide a different short answer (<=5 words) |
     ```

   - Depois da tabela, informe:

     ```text
     You can reply with the option letter (e.g., "A"), accept the recommendation by saying "yes" or "recommended", or provide your own short answer.
     ```

   - Para resposta curta sem opções significativas, use:

     ```text
     **Suggested:** <your proposed answer> - <brief reasoning>
     Format: Short answer (<=5 words). You can accept the suggestion by saying "yes" or "suggested", or provide your own answer.
     ```

   - Se o usuário responder "yes", "recommended" ou "suggested", aceite a recomendação anterior.
   - Caso contrário, valide se a resposta corresponde a uma opção ou respeita o limite de cinco palavras.
   - Se houver ambiguidade, peça desambiguação sem consumir uma nova pergunta.
   - Registre a resposta na memória de trabalho e avance.
   - Encerre quando todas as ambiguidades críticas forem resolvidas, o usuário disser "done", "good" ou
     "no more", ou cinco perguntas tiverem sido feitas.

6. Após CADA resposta aceita, faça a integração incremental:
   - Mantenha em memória a especificação e seu conteúdo bruto.
   - Na primeira integração, garanta a existência de `## Clarifications`, logo após a seção contextual de
     nível mais alto, e de `### Session YYYY-MM-DD` para a data atual.
   - Anexe uma linha `- Q: <question> → A: <final answer>`.
   - Aplique o esclarecimento à seção adequada:
     - ambiguidade funcional → Functional Requirements;
     - interação ou atores → User Stories ou Actors;
     - entidades → Data Model;
     - requisito não funcional → Success Criteria > Measurable Outcomes;
     - fluxo negativo → Edge Cases / Error Handling;
     - conflito terminológico → normalize o termo e use `(formerly referred to as "X")` uma única vez,
       quando necessário.
   - Substitua declarações invalidadas em vez de duplicá-las.
   - Salve `FEATURE_SPEC` após cada integração, com sobrescrita atômica.
   - Preserve a ordem das seções e mantenha o texto inserido mínimo e testável.

7. Após CADA gravação e ao final, valide:
   - exatamente um item por resposta aceita na sessão de esclarecimentos;
   - no máximo cinco perguntas aceitas;
   - nenhum placeholder vago que a resposta deveria resolver;
   - nenhuma alternativa anterior contraditória;
   - Markdown válido, com apenas `## Clarifications` e `### Session YYYY-MM-DD` como novos títulos;
   - uso consistente do termo canônico.

8. Grave a especificação atualizada em `FEATURE_SPEC`.

9. Revalide a Spec Quality Checklist, quando `FEATURE_DIR/checklists/requirements.md` existir:
   - Se não existir, ignore silenciosamente esta etapa.
   - Leia somente linhas de checkbox GitHub que correspondam a `- [ ]`, `- [x]` ou `- [X]`, inclusive com
     indentação, fora de code fences.
   - Registre o estado e o texto de cada item antes da avaliação.
   - Reavalie cada item contra a especificação atualizada.
   - Altere somente o marcador quando o estado realmente mudar:
     - aprovado e desmarcado: `[ ]` → `[x]`;
     - reprovado e marcado: `[x]`/`[X]` → `[ ]`;
     - sem mudança: preserve o marcador, inclusive a caixa usada.
   - Preserve todo o restante do conteúdo, a ordem e os espaços.
   - Calcule as listas Newly passing, Regressions e Still unchecked.
   - Registre a contagem antes/depois, por exemplo, `12/16 → 15/16 items passing`.

### Regras de comportamento

- Se não houver ambiguidades relevantes, responda exatamente:
  "No critical ambiguities detected worth formal clarification." e sugira prosseguir.
- Se `FEATURE_SPEC` estiver ausente, instrua o usuário a executar `__SPECKIT_COMMAND_SPECIFY__`; não crie
  uma especificação.
- Nunca ultrapasse cinco perguntas; tentativas de esclarecer a mesma pergunta não contam como novas.
- Evite perguntas especulativas de stack, salvo quando sua ausência bloquear a clareza funcional.
- Respeite pedidos de encerramento como "stop", "done" e "proceed".
- Se nenhuma pergunta for necessária, apresente um resumo compacto com todas as categorias Clear.
- Ao atingir a cota com categorias relevantes pendentes, liste-as em Deferred com justificativa.

Contexto para priorização:

```text
{ARGS}
```

### Mandatory Post-Execution Hooks

Conclua esta seção antes de informar o término ao usuário.

Verifique `.specify/extensions.yml`:

- Se não existir ou não houver hooks em `hooks.after_clarify`, avance para `## Completion Report`.
- Se o YAML for inválido, ignore silenciosamente a verificação.
- Exclua hooks cujo `enabled` seja `false` e considere os demais habilitados por padrão.
- Não interprete `condition`; execute somente hooks sem condição ou com condição nula ou vazia.
- Para cada hook obrigatório (`optional: false`), emita `EXECUTE_COMMAND:`:

  ```text
  ## Extension Hooks

  **Automatic Hook**: {extension}
  Executing: `/{command}`
  EXECUTE_COMMAND: {command}
  ```

- Para cada hook opcional (`optional: true`), emita:

  ```text
  ## Extension Hooks

  **Optional Hook**: {extension}
  Command: `/{command}`
  Description: {description}

  Prompt: {prompt}
  To execute: `/{command}`
  ```

### Completion Report

Depois do ciclo ou do encerramento antecipado, informe:

- quantidade de perguntas feitas e respondidas;
- path da especificação atualizada;
- nomes das seções alteradas;
- estado da Spec Quality Checklist, com contagem antes/depois, itens recém-aprovados, regressões e itens
  ainda desmarcados;
- tabela de cobertura de cada categoria com Status Resolved, Deferred, Clear ou Outstanding;
- recomendação para prosseguir a `__SPECKIT_COMMAND_PLAN__` ou executar
  `__SPECKIT_COMMAND_CLARIFY__` novamente;
- próximo comando sugerido.

### Done When

- [ ] Spec ambiguities identified and clarifications integrated into spec file
- [ ] Spec quality checklist re-validated against updated spec (if `FEATURE_DIR/checklists/requirements.md` exists)
- [ ] Extension hooks dispatched or skipped according to the rules in Mandatory Post-Execution Hooks above
- [ ] Completion reported to user with questions answered, sections touched, checklist status, and coverage summary

## Exemplo de invocação

```text
__SPECKIT_COMMAND_CLARIFY__ esclarecer retenção de dados e recuperação de falhas
```
