---
name: "greenfield-feature"
description: "Não usado no desafio individual; delimita e entrega uma pequena capacidade que o sistema legado não podia oferecer, concluindo o arco de modernização com evidência [GREENFIELD] rastreável."
argument-hint: "capability=\"<one sentence>\" context=<bounded-context>"
agent: "evolution"
tools: ["read", "search", "edit", "github/*"]
---
# /greenfield-feature

> [!NOTE]
> Não usado no desafio individual (14:00-17:40). O desafio termina na Etapa 3 e na validação do juiz. Consulte [ADR-0003](../../docs/adr/0003-individual-challenge-format.md).

## Objetivo

Entregar uma capacidade deliberadamente pequena que o sistema Natural/Adabas não podia oferecer e registrar por que a stack moderna a torna possível. Este é o passo que responde à pergunta que orienta todo o dia: o que agora é possível e não era antes.

## Quando invocar

Na Etapa 4, depois que o incremento da Etapa 3 for executado com dados migrados e o participante tiver revisado pelo menos uma delegação. Invoque por último, nunca como substituto do trabalho de equivalência.

## Pré-condições

- O incremento da Etapa 3 passa no build e em seus testes
- Os dados migrados estão carregados e reconciliados, ou seus bloqueios estão registrados
- `.spec/<NNN>-<feature>/spec.md` existe e seus requisitos respaldados pelo legado já estão rastreados
- Restam pelo menos 15 minutos no timebox da etapa

## Inputs que a equipe deve fornecer

- Uma frase que descreva a capacidade
- O bounded context ao qual ela pertence
- A constraint legada que ela remove, com evidência dessa constraint
- Quem a aceita: o Product Owner, durante o bloco de validação final

## O que farei

- Testar a candidata em relação a uma constraint que o participante possa indicar no corpus, não a uma afirmação genérica de que mainframes são antigos
- Reduzir a candidata até que caiba no tempo restante e dizer claramente quando ela não couber
- Escrever um requisito com `source_legacy: [GREENFIELD]` e uma justificativa por escrito, no formato aceito pelo gate de rastreabilidade
- Encaminhar o trabalho por Ask, depois Plan e, em seguida, por uma delegação, para que o participante exercite toda a sequência de modos em um único entregável
- Registrar o resultado com honestidade, incluindo uma capacidade delimitada, mas não entregue

## O que NÃO farei

- Permitir que um requisito greenfield omita sua justificativa, o que o gate `legacy-traceability` rejeita
- Apresentar uma capacidade como nova quando o sistema legado já a tinha de outra forma
- Permitir que este passo consuma o tempo reservado para aceitação dos dados
- Enfraquecer um requisito existente respaldado pelo legado para fazer o novo caber
- Alegar valor de negócio que o Product Owner não confirmou

## Formato de saída

Um requisito adicionado a `.spec/<NNN>-<feature>/spec.md`:

```markdown
### REQ-NNN — <capability name>

**EARS:** When <trigger>, the system shall <observable behavior>.

source_legacy: [GREENFIELD] <why no legacy equivalent exists, and which
constraint in the corpus prevented it — cite path#Lstart-Lend for the
constraint, not for the behavior>

**Acceptance**

- Given <precondition>, when <action>, then <observable result>.

**Why the legacy system could not do this**

| Legacy constraint | Evidence | What the modern stack changes |
|---|---|---|
| <constraint> | `<path>#L<start>-L<end>` | <capability that removes it> |
```

E uma entrada de encerramento em [`04-evolution/agent-experience-report.md`](../../04-evolution/agent-experience-report.md).

## Regras de ears-validate

- Todo requisito contém um `REQ-NNN` exclusivo e um padrão EARS.
- `source_legacy:` é obrigatório em todo requisito, incluindo este.
- `[GREENFIELD]` é válido somente com uma justificativa escrita na mesma entrada.
- Os critérios de aceitação usam Given/When/Then e são verificáveis de forma independente.
- Um requisito que o participante não consegue verificar hoje é registrado como deferred, não como done.

## Definição de pronto

- [ ] A capacidade está declarada em uma frase compreensível para um leitor não técnico
- [ ] A constraint legada que ela remove cita uma localização real do corpus
- [ ] Existe um `REQ-NNN` com `source_legacy: [GREENFIELD]` e uma justificativa
- [ ] O participante usou Ask, depois Plan e, em seguida, uma delegação nesse único item
- [ ] Um teste cobre o novo comportamento, ou sua ausência está registrada como bloqueio
- [ ] O Product Owner a aceitou ou registrou por que a aceitação está pendente
- [ ] Nenhum requisito respaldado pelo legado perdeu cobertura para abrir espaço para ela

## Corpo do prompt

Você é o `@evolution`. O participante tem um incremento funcional e agora conclui o arco adicionando uma capacidade que o sistema legado não podia oferecer.

**Passo 1 — Teste a premissa.**

- Pergunte qual constraint legada a capacidade remove e solicite sua localização no corpus.
- Rejeite respostas genéricas como "o mainframe era limitado". Procure uma constraint específica que o participante realmente leu: geometria fixa de tela, path exclusivamente batch, padrão de acesso por uma única chave, largura de campo, saída somente em relatório.
- Se nenhuma constraint puder ser citada, informe isso e peça ao participante que escolha outra candidata. Uma alegação greenfield sem fundamento é pior do que nenhuma.

**Passo 2 — Reduza-a até que caiba.**

- Informe o tempo restante na etapa.
- Ofereça a menor versão que ainda demonstre o ponto e nomeie o que foi removido.
- Se nem mesmo a menor versão couber, escreva o requisito, marque-o como deferred e pare. Uma intenção registrada é um resultado honesto.

**Passo 3 — Escreva o requisito.**

- Produza um `REQ-NNN` no Formato de saída acima.
- Coloque a citação do corpus na *constraint*, nunca no novo comportamento, pois, por definição, o novo comportamento não tem fonte legada.
- Confirme que a justificativa é específica o suficiente para que um revisor que nunca viu a discussão compreenda por que ela é greenfield.

**Passo 4 — Percorra a sequência de modos neste único item.**

- Ask: peça ao participante que pergunte como a capacidade deve se comportar e qual boundary é responsável por ela.
- Plan: produza o plano de alterações no nível de arquivos e a lista de testes antes de qualquer edição.
- Delegate: entregue a implementação a uma execução autorizada e depois revise o diff e os testes como pessoa.
- Registre qual modo fez o quê. Este item é a evidência mais clara do participante sobre quando valeu a pena usar cada modo.

**Passo 5 — Conclua o arco.**

- Adicione o resultado ao relatório de experiência: o que foi entregue, o que foi removido, quanto tempo levou e qual modo conduziu o trabalho.
- Peça ao Product Owner que o aceite durante o bloco de validação final ou que declare o bloqueio.
- Declare claramente se a capacidade teria sido viável no sistema legado e com base em qual evidência.

## Exemplo de invocação

```text
/greenfield-feature capability="<one sentence>" context=<bounded-context>
```
