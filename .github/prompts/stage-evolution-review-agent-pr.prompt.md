---
name: "review-agent-pr"
description: "Não usado no desafio individual; revisa um PR gerado pelo Copilot Agent na nuvem, com atenção explícita aos modos de falha típicos de IA."
argument-hint: "pr=<number> issue=<slug>"
agent: "evolution"
tools: ["read", "search", "edit", "execute", "github/*"]
---
# /review-agent-pr

> [!NOTE]
> Não usado no desafio individual (14:00-17:40). O desafio termina na Etapa 3 e na validação do juiz. Consulte [ADR-0003](../../docs/adr/0003-individual-challenge-format.md).

## Objetivo

Revisar sistematicamente um pull request gerado pelo Copilot Agent, verificando-o em relação aos critérios de aceitação da issue original e sinalizando modos de falha típicos de IA. Os achados são classificados por severidade.

## Quando invocar

Quando o Copilot Agent cria um PR a partir de uma issue delegada e o participante precisa revisá-lo.

## Pré-condições

- Existe um PR do Copilot Agent (o participante fornece o número do PR ou o nome da branch)
- O rascunho da issue original existe em `04-evolution/issues/<slug>.md`
- A watch list da delegação existe em `04-evolution/delegations/<slug>.md`

## Inputs que a equipe deve fornecer

- O número do PR ou o nome da branch
- O slug da issue original (para referenciar os critérios de aceitação)

## O que farei

- Recuperar o diff do PR e analisar cada arquivo alterado
- Comparar as alterações com os critérios de aceitação da issue
- Verificar modos de falha típicos de IA (APIs alucinadas, testes sem significado, scope creep)
- Classificar os achados por severidade: must-fix, should-fix, can-defer
- Produzir um documento de revisão estruturado

## O que NÃO farei

- Aprovar o PR — o participante decide se fará o merge
- Corrigir problemas automaticamente — eu os relato, e o participante age
- Ignorar PRs não triviais sem sinalizar pelo menos um ponto de revisão
- Aceitar PRs sem testes para novos comportamentos

## Formato de saída

Um documento de revisão em `04-evolution/reviews/<pr-number>.md`:

```markdown
# PR Review: #[number] — [title]
## Acceptance Criteria Verification
| Criterion | Status | Evidence |
## AI Failure Mode Scan
| Check | Result | Details |
## Classified Findings
### Must Fix Before Merge
### Should Fix Before Merge
### Can Fix in Follow-Up
## Recommendation
```

## Definição de pronto

- [ ] Todo critério de aceitação da issue foi verificado (pass/fail/partial)
- [ ] A análise dos modos de falha de IA cobre as sete verificações padrão
- [ ] Todo achado tem um path de arquivo e uma referência de linha
- [ ] Os achados estão classificados como must-fix / should-fix / can-defer
- [ ] Uma recomendação clara é fornecida: merge, merge with fixes ou reject
- [ ] Os testes de novos comportamentos foram verificados (ou sua ausência foi sinalizada como must-fix)

## Corpo do prompt

Você é o `@evolution`. O participante precisa revisar um PR gerado pelo Copilot Agent.

**Passo 1 — Carregue o contexto.**
Leia a issue original em `04-evolution/issues/<slug>.md`. Extraia os critérios de aceitação e a lista de arquivos afetados. Leia a watch list em `04-evolution/delegations/<slug>.md`.

**Passo 2 — Recupere o diff do PR.**
Use somente comandos read-only da GitHub CLI para recuperar dados do PR: `gh pr view <pr-number>` e `gh pr diff <pr-number>`. Não execute comandos de review, merge, comment, write nem qualquer outro comando de mutação no GitHub. Liste cada arquivo alterado, adicionado ou excluído. Compare-os com os arquivos esperados na watch list. Sinalize qualquer alteração inesperada de arquivo como possível scope creep.

**Passo 3 — Verifique os critérios de aceitação.**
Para cada critério de aceitação da issue original:

- **Pass**: o PR implementa claramente esse critério. Cite o código específico.
- **Fail**: o PR não implementa esse critério. Registre o que está faltando.
- **Partial**: alguns aspectos estão implementados, mas não todos. Descreva a lacuna.

**Passo 4 — Analise os modos de falha típicos de IA.**
Verifique cada item abaixo. Para cada verificação, relate Pass ou Fail com referências específicas de arquivo:linha:

1. **Imports alucinados**: todos os imports resolvem para dependências reais do projeto ou classes do JDK?
2. **Chamadas de API fabricadas**: todas as chamadas de método apontam para métodos que realmente existem na classe de destino?
3. **Testes sem significado**: as assertions verificam comportamento real? (Observe `assertTrue(true)`, assertions sobre a entrada em vez da saída ou assertions sobre valores diretamente no código)
4. **Divergência entre comentário e código**: os comentários descrevem corretamente o que o código faz?
5. **Scope creep**: o PR altera arquivos fora do escopo da issue?
6. **Tratamento de erros ausente**: os paths de erro são tratados ou somente o happy path?
7. **Violações de estilo**: o código segue as convenções do projeto (records para DTOs, constructor injection, sem campos `@Autowired`, sem retornos `null`)?

**Passo 5 — Classifique os achados.**
Organize todos os achados em três categorias:

- **Must fix before merge**: bugs, problemas de segurança, testes quebrados, testes ausentes para novos comportamentos e APIs alucinadas. O PR não deve receber merge até que sejam resolvidos.
- **Should fix before merge**: violações de estilo, tratamento de erros incompleto e Javadoc ausente. Devem ser corrigidos, mas não são bloqueios.
- **Can fix in follow-up**: pequenas melhorias, casos de teste adicionais e atualizações de documentação. Registre-os como uma nova issue.

**Passo 6 — Escreva a recomendação.**
Com base nos achados:

- **Merge**: não há itens must-fix. Opcionalmente, registre itens should-fix para o participante tratar.
- **Merge with fixes**: existem itens must-fix, mas são pequenos. Liste as correções específicas exigidas.
- **Reject**: problemas fundamentais (abordagem errada, funcionalidade central ausente, vulnerabilidade de segurança). Explique o motivo e sugira os próximos passos.

**Passo 7 — Escreva o documento de revisão.**
Gere a saída em `04-evolution/reviews/<pr-number>.md`.

Pelo menos um achado deve ser sinalizado em um PR não trivial. Se realmente não houver nada errado, declare: "Nenhum problema must-fix encontrado. O PR atende a todos os critérios de aceitação." — mas isso deve ser raro em código gerado por IA.

## Exemplo de invocação

```
/review-agent-pr pr=<number> issue=<slug>
```
