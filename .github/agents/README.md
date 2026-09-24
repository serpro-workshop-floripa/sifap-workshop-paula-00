# Índice de agents

Este diretório contém os agents personalizados do GitHub Copilot para o workshop — **5** no total, cada um em seu próprio `<name>.agent.md`.

> [!NOTE]
> O Copilot descobre arquivos `*.agent.md` em `.github/agents/`. Invoque um agent pelo `name` com `@<name>` (por exemplo, `@archaeologist`). O `name` também vincula prompts: um arquivo `*.prompt.md` seleciona seu agent pela chave `agent:` do frontmatter; portanto, o ID de um agent é um contrato, não um rótulo.

## O modelo de duas camadas

O kit separa **quando** você está trabalhando de **qual papel** está exercendo.

| Camada | Primitivo | Como é carregado | Por quê |
|---|---|---|---|
| **Etapa** — a fase em que o participante está | Agent, invocado com `@name` | Você o seleciona deliberadamente, uma vez por etapa | Uma etapa tem início, definição de pronto e checkpoint próprio |
| **Papel** — a responsabilidade que você assume pessoalmente | Skill, em [`../skills/`](../skills/) | É carregada automaticamente por sua `description` | Você leva seu papel para todas as etapas; ninguém precisa se lembrar de selecioná-lo novamente |

Uma exceção tem um agent dedicado: **`dba`**. O ciclo de vida dos dados atravessa
as quatro etapas em vez de pertencer a apenas uma; por isso, ele não pode ser um
agent de etapa e é responsável por prompts com escopo de ferramentas que uma
skill não pode vincular. Todos os demais papéis da equipe são skills.

> [!TIP]
> Mantenha o agent de etapa selecionado durante todo o dia e deixe a skill do seu
> papel compor-se com ele. Selecionar `@builder` e pedir lacunas de cobertura
> carrega automaticamente o papel de QA.

## Agents de etapa

Três agents do desafio são executados em sequência pela chave `handoffs:` do frontmatter — `archaeologist -> architect -> builder`. O agent preservado da Etapa 4 (`evolution`) não é usado no desafio individual.

| Etapa | Agent | Invoque | Prompts vinculados | Descrição |
| --- | --- | --- | --- | --- |
| Etapa 1 | [`archaeologist`](archaeologist.agent.md) | `@archaeologist` | 6 | Orienta a leitura real de fontes e dados, registra cobertura, dependências e perguntas sem resposta |
| Etapa 2 | [`architect`](architect.agent.md) | `@architect` | 16 | Define contextos delimitados, escreve especificações EARS, gera ADRs e projeta uma arquitetura de Monólito Modular |
| Etapa 3 | [`builder`](builder.agent.md) | `@builder` | 19 | Traduz Natural para Java, gera JPA a partir de FDTs, escreve testes de equivalência e constrói REST + Next.js |
| Etapa 4 (não usada no desafio) | [`evolution`](evolution.agent.md) | `@evolution` | 16 | Preservado para fluxos posteriores ao desafio; o desafio individual termina na Etapa 3 e na validação do juiz |

## Agent transversal

| Agent | Invoque | Prompts vinculados | Descrição |
| --- | --- | --- | --- |
| [`dba`](dba.agent.md) | `@dba` | 4 | Descoberta de dados Adabas, prontidão da fonte, migração e reconciliação no PostgreSQL, evolução segura do schema e auditoria de queries baseada em evidências |

## Skills de papel que substituíram agents de persona

Nove agents de persona e três agents especialistas foram convertidos em skills.
Os comandos de barra não mudaram; mudou apenas o agent que os hospeda.

| Agent anterior | Skill atual | Prompts movidos para |
| --- | --- | --- |
| `se-ux-ui-designer` | [`ux-research-design`](../skills/ux-research-design/SKILL.md) | não possuía prompts |

A justificativa e os trade-offs estão registrados na [ADR-0002](../../docs/adr/0002-team-roles-as-skills-not-agents.md).

## Responsabilidade pelos prompts

Os 61 prompts em [`../prompts/`](../prompts/) vinculam-se a um agent por sua chave `agent:`:

- Todos os **61** vinculam-se a um dos **5** agents acima — nenhum prompt permanece no `agent: "agent"` genérico integrado. As contagens por agent estão nas colunas **Prompts vinculados** das tabelas.
- Um prompt cujo trabalho pertence a um papel da equipe inicia seu corpo carregando a skill desse papel, de modo que o conhecimento do papel acompanhe a tarefa.

Gere novamente as contagens com `grep -h '^agent:' ../prompts/*.prompt.md | sort | uniq -c`.

## Regra de manutenção

- Renomear um agent interrompe silenciosamente **todos** os prompts vinculados a ele por `agent:`; renomeie juntos o agent e todos os seus vínculos de prompt e execute novamente o validator.
- `description` é a única chave de frontmatter estritamente exigida pelo gate; `handoffs` destina-se apenas aos agents de etapa do desafio e somente quando existe uma próxima etapa.
- Adicionar um novo agent exige uma razão que o modelo de duas camadas ainda não cubra. Um novo **papel** é uma skill; uma nova **fase** é um agent.
- As seções obrigatórias do corpo (`Missão`, `Personas líderes`, `Princípios operacionais`, `O que este agent sabe`, `O que este agent NÃO sabe`, `Prompts disponíveis`, um heading de `Definição de pronto`, `Antipadrões rejeitados por este agent`, `Integração com Spec-Kit`) e o schema completo estão definidos em [`../PRIMITIVE-STANDARD.md`](../PRIMITIVE-STANDARD.md) e são aplicados por [`../scripts/validate-copilot-primitives.py`](../scripts/validate-copilot-primitives.py).
- Ao adicionar um agent, inclua sua linha na camada correta acima e, se um prompt precisar invocá-lo, defina o `agent:` desse prompt com este `name`.
