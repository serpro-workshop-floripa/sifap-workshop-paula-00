# ADR-0002: Papéis da equipe são skills; apenas etapas e o ciclo de vida dos dados são agentes

> **Caminho:** [Kit da equipe](../../README.md) › [Documentação](../README.md) › [ADRs](README.md) › **ADR-0002**

| Campo | Valor |
|---|---|
| **Status** | accepted |
| **Data** | 2026-09-15 |
| **Autores** | Mantenedores do kit |
| **Substitui** | N/A |

---

## Contexto

O kit fornecia **17 agentes**: quatro agentes de etapa, 10 agentes de persona e
três especialistas de aprofundamento. Dois desses grupos realizavam trabalhos
diferentes sob o mesmo primitivo.

Uma **etapa** é uma fase na qual toda a equipe entra e da qual sai em conjunto.
Ela tem início, definição de pronto e handoff para a etapa seguinte. A seleção
deliberada é o objetivo: a seleção *é* o ritual.

Um **papel** é uma responsabilidade que uma pessoa mantém em todas as etapas. O
Product Owner não deixa de ser Product Owner quando a Etapa 3 começa. Porém, o
design de agentes de persona exigia selecionar novamente `@product-owner` em
cada conversa e depois selecionar outra vez o agente de etapa para recuperar o
contexto. As duas camadas disputavam um único seletor em vez de se comporem.

Isso gerou três custos concretos:

1. **Carga do seletor.** Dezessete entradas para um workshop de cinco pessoas e
   oito horas.
2. **Carga de ensino.** Três documentos separados explicavam por que duas camadas
   “não eram duplicadas”, um sinal confiável de que a abstração estava errada,
   não a documentação.
3. **Peso morto.** Os três agentes especialistas não tinham **nenhum** prompt.
   Eles já eram conhecimento puro revestido pelo frontmatter de um agente.

As skills resolvem diretamente a parte dos papéis: elas são carregadas a partir
da `description` por correspondência semântica. Assim, o conhecimento chega sem
uma etapa de seleção e se combina com qualquer agente ativo.

Um papel não se enquadra na regra. O **DBA** é responsável pelo ciclo de vida dos
dados, marcado como `Data lead` na matriz de personas em **todas as quatro**
etapas, e possui prompts com escopo de ferramenta (`persona-dba-migration`,
`persona-dba-query-audit`, `postgresql-code-review`,
`postgresql-optimization`). Por definição, ele atua entre etapas, portanto não
pode ser incorporado a um agente de etapa. Seus prompts precisam de um destino
de vinculação que somente um agente fornece.

## Decisão

Manter **cinco agentes**: os quatro agentes de etapa (`archaeologist`,
`architect`, `builder`, `evolution`) e o `dba`.

Converter os nove agentes de persona restantes e os três especialistas em skills
em `.github/skills/`. Vincular cada prompt órfão ao agente de etapa responsável
pelo momento em que o prompt é usado. Iniciar o corpo de cada prompt revinculado
carregando a skill do papel que contém seus limites, procedimento e gate de
qualidade.

A regra para futuros primitivos é: **uma nova fase é um agente; um novo papel é
uma skill.**

## Alternativas consideradas

| Alternativa | Por que foi rejeitada |
|---|---|
| Manter todos os 17 agentes | Preserva todos os custos anteriores e mantém dois primitivos disputando um seletor. |
| Ocultar personas com `user-invocable: false` | É uma opção econômica e reversível que reduz a poluição do seletor. Porém, o conhecimento ainda não se combina com o agente ativo, que é o defeito real. É útil como experimento, não como destino. |
| Converter também o DBA e remover seu agente | O ciclo de vida dos dados abrange todas as quatro etapas e possui quatro prompts com escopo de ferramenta. Incorporá-lo a um agente de etapa representaria incorretamente quando o trabalho acontece. |
| Mesclar os prompts das personas ao corpo dos agentes de etapa | Elimina os comandos slash, que são a parte realmente usada pelas pessoas participantes. |

## Consequências

- **Mais fácil:** há cinco entradas no seletor; o conhecimento do papel chega sem
  solicitação; o modelo de duas camadas precisa de uma tabela em vez de três
  documentos; há 12 primitivos a menos para manter sincronizados.
- **Mais difícil:** uma pessoa participante que queira o contexto completo de um
  papel sob demanda precisa nomeá-lo (`persona-qa-engineer`) em vez de mencioná-lo
  com `@`. A correspondência de skills é semântica, portanto uma `description`
  divergente degrada silenciosamente o carregamento. As descrições passam a ter
  mais peso e são revisadas de acordo.
- **Riscos:** 37 prompts mudaram sua vinculação `agent:` em um único commit. Uma
  aplicação parcial falharia no gate `copilot-primitives`, que é a proteção
  esperada.
- **Mitigações:** o gate valida a integridade de `prompt -> agent` e a igualdade
  entre o `name` da skill e o diretório em cada PR. O arquivo
  [`.github/agents/README.md`](../../.github/agents/README.md) contém o mapeamento
  de agente anterior para skill, permitindo rastrear uma referência desatualizada.

## Observação de 2026-09-24

A [ADR-0003](0003-individual-challenge-format.md) muda o workshop para o formato
de desafio individual. Esta decisão continua válida: uma pessoa participante
alterna os agentes de etapa durante o desafio, enquanto todas as skills de papel
permanecem disponíveis e são carregadas conforme o trabalho exige.

## Relacionados

- REQ-IDs: N/A
- ADRs: [ADR-0001](0001-agent-instructions-single-source-of-truth.md)
- Arquivos relacionados: [`.github/PRIMITIVE-STANDARD.md`](../../.github/PRIMITIVE-STANDARD.md), [`.github/skills/README.md`](../../.github/skills/README.md)

## Referências

- GitHub Docs — Sobre a personalização das respostas do GitHub Copilot: <https://docs.github.com/en/copilot/concepts/response-customization>
- GitHub Docs — Compatibilidade com diferentes tipos de instruções personalizadas: <https://docs.github.com/en/copilot/reference/custom-instructions-support>

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [ADR-0001](0001-agent-instructions-single-source-of-truth.md)<br/><sub>Fonte única de verdade para instruções de agentes.</sub> | [ADRs — Índice](README.md)<br/><sub>Índice das decisões registradas.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
