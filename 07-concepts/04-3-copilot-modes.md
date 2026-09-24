# Os 3 modos do Copilot — Ask, Plan e Agent

> **Trilha:** [Kit do Time](../README.md) › [Conceitos](00-README.md) › **Os 3 modos do Copilot**

**O GitHub Copilot opera em três modos distintos — Ask, Plan e Agent — e escolher o modo errado para uma tarefa desperdiça tempo. Este documento traz critérios objetivos para selecionar o modo certo em cada situação da imersão.**

![Conceito 04](https://img.shields.io/badge/Conceito-04-171717?style=flat-square) ![Usado em todos os estágios](https://img.shields.io/badge/Uso-Todos%20os%20est%C3%A1gios-737373?style=flat-square) ![Duração 15 min](https://img.shields.io/badge/Dura%C3%A7%C3%A3o-15%20min-A3A3A3?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Todos os participantes |
| **Pré-requisitos** | Ler [Agentes e personas](02-agents-and-personas.md) |
| **Tempo estimado** | 15 minutos |
| **Estágio** | Todos os estágios |
| **Resultado esperado** | Saber sem hesitar qual modo usar para cada tarefa |

---

## Conceito

O GitHub Copilot oferece três modos de operação com níveis diferentes de autonomia, custo de tempo e resultado:

- **Ask** — modo conversacional. Você faz perguntas e recebe respostas em texto. Nenhum código é alterado.
- **Plan** — modo de planejamento. Você descreve uma mudança e o Copilot propõe um plano listando os arquivos a tocar e as alterações a fazer — antes da execução.
- **Agent** — modo autônomo. Você fornece uma tarefa bem definida, normalmente como uma Issue, e o Copilot lê o código, implementa a mudança e abre um PR de forma autônoma.

---

## Por que isso importa

Usar o modo errado tem consequências diretas:

- **Ask quando você deveria usar Plan:** você recebe orientação correta, mas precisa executar tudo manualmente, o que torna o trabalho mais lento que o necessário.
- **Agent quando você deveria usar Ask:** o Copilot altera vários arquivos com base em contexto incompleto, gerando um PR defeituoso que leva mais tempo para corrigir do que uma mudança manual.
- **Plan quando você deveria usar Agent:** você revisa um plano passo a passo para uma tarefa grande e bem definida, criando esforço manual desnecessário.

---

## Árvore de decisão

```mermaid
%%{init: {'theme':'neutral','themeVariables':{'fontFamily':'ui-sans-serif, system-ui, sans-serif','primaryColor':'#F5F5F5','primaryTextColor':'#171717','primaryBorderColor':'#171717','lineColor':'#525252','secondaryColor':'#FFFFFF','tertiaryColor':'#FAFAFA','background':'#FFFFFF'}}}%%
flowchart TD
    classDef step fill:#F5F5F5,stroke:#171717,color:#171717
    classDef result fill:#FFFFFF,stroke:#171717,color:#171717,stroke-width:2px
    classDef question fill:#FAFAFA,stroke:#A3A3A3,color:#404040

    Q1{"Você precisa<br/>alterar código?"}:::question
    Q2{"A mudança afeta<br/>mais de um<br/>arquivo?"}:::question
    Q3{"O requisito está<br/>totalmente<br/>especificado?"}:::question

    ASK["Ask<br/><sub>Perguntar, explorar, entender</sub>"]:::result
    PLAN["Plan<br/><sub>Planejar uma mudança com revisão humana</sub>"]:::result
    AGENT["Agent<br/><sub>Delegar uma tarefa completa</sub>"]:::result

    Q1 -- "Não" --> ASK
    Q1 -- "Sim" --> Q2
    Q2 -- "Não (1 arquivo)" --> PLAN
    Q2 -- "Sim" --> Q3
    Q3 -- "Não" --> PLAN
    Q3 -- "Sim, Issue detalhada" --> AGENT
```

---

## Comparação dos três modos

| Critério | Ask | Plan | Agent |
|---|---|---|---|
| **O que faz** | Explica o contexto selecionado | Propõe um plano sem implementar | Executa ações autorizadas no workspace local; não atribui automaticamente uma GitHub Issue |
| **Autonomia** | Nenhuma mudança solicitada no workspace | Somente planejamento | Limitada pela tarefa, pelas permissões e pela revisão humana |
| **Custo de tempo** | Depende do escopo | Inclui a revisão do plano | Inclui implementação, execução de ferramentas e verificação |
| **Quando usar** | Explorar, entender, responder a perguntas | Mudança em vários arquivos com revisão humana | Issue totalmente especificada, com contexto e critérios de aceitação |
| **Pré-requisito** | Nenhum | Contexto do que mudar | Issue com contexto, REQ-IDs, critérios de aceitação e rastreabilidade |
| **Risco de retrabalho** | Nenhum | Baixo | Alto se a Issue estiver incompleta |

---

## Exemplos de prompt por modo — contexto do SIFAP

### Ask — explorar o legado

```text
"Leia comigo o intervalo selecionado da fonte.
Inclua declarações, dependências, E/S e caminhos de erro/transação
que afetem o comportamento observado. Mantenha explícitas as incertezas."
```

```text
"@archaeologist, quais campos do BENEFIC.ddm
são obrigatórios e quais são campos de valores múltiplos (MU)?"
```

### Plan — implementar um requisito com revisão

```text
"Planeje a implementação do REQ-NNN selecionado.
Liste os arquivos a criar ou modificar, a ordem das mudanças
e os testes de integração necessários.
NÃO implemente ainda — estou concluindo o checkpoint de autoavaliação C2."
```

```text
"Planeje a próxima mudança de schema revisada a partir do mapeamento do DBA.
Inspecione as versões Flyway existentes e o contrato real de consulta.
Não invente um campo de destino nem resolva uma ambiguidade dos dados de origem."
```

### Agent local e GitHub coding agent

```text
[Para uma tarefa local revisada:]
- Requisito e tarefa regentes: <referências reais>
- Arquivos e ações permitidos: <escopo revisado>
- Evidência da fonte: <paths e intervalos reais>
- Verificação: <testes de aceitação aprovados>

[Para trabalho de Issue para PR no Estágio 4 posterior ao desafio:]
Verifique a disponibilidade do GitHub coding agent e atribua a Issue revisada
pela ação compatível do repositório. Selecionar o modo Agent local
não atribui uma Issue. Registre a indisponibilidade em vez de inventar uma execução.

O Estágio 4 não é usado no desafio individual; não execute orquestração paralela
de subagentes nem worker harnesses durante o desafio das 14:00 às 17:40.
```

---

## Antipadrões — o que não fazer

| Antipadrão | Consequência | Alternativa correta |
|---|---|---|
| Usar Agent para uma pergunta de dois minutos | Atraso, consumo de contexto e risco de mudanças indesejadas | Use Ask |
| Usar Ask para implementar um service inteiro | Você recebe orientação, mas executa tudo manualmente | Use Plan ou Agent |
| Delegar ao Agent sem uma Issue detalhada | O PR gerado contém código incorreto ou incompleto | Escreva a Issue completa antes de iniciar o Agent |
| Usar Plan durante o Estágio 1 (arqueologia) | O Copilot pode tentar modificar o legado | Use Ask com `@archaeologist` |
| Ignorar a saída do Plan antes da execução | Mudanças inesperadas em arquivos fora do plano | Leia e aprove o plano antes de confirmar |

---

## Custo de tempo estimado

Meça o trabalho real do participante. Raciocínio local, execução de ferramentas, filas de agentes remotos e revisão têm custos diferentes; nenhuma duração fixa decorre do nome do modo. Use os orçamentos dos estágios e a regra de escalonamento de 20 minutos sem enfraquecer os requisitos de evidência.

> [!WARNING]
> O tempo do Agent inclui a revisão do PR gerado. PRs com contexto incompleto podem exigir várias iterações.

---

## Referências

- [Cartão de uma página dos 3 modos](../09-cheat-sheets/copilot-3-modes.md)
- [Agentes e personas](02-agents-and-personas.md)
- [Guia do Estágio 4 — o modo Agent na prática](../04-evolution/GUIDE.md) (posterior ao desafio; não usado no desafio individual)

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Glossário visual](03-visual-glossary.md)<br/><sub>Mais de 30 termos com definição e exemplos do SIFAP.</sub> | [Notação EARS](05-ears-notation.md)<br/><sub>Como escrever requisitos sem ambiguidade.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
