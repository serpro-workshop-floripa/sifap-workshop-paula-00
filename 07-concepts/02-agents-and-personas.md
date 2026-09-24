# Agentes e personas — as duas camadas de contexto

> **Trilha:** [Kit do Time](../README.md) › [Conceitos](00-README.md) › **Agentes e personas**

**O GitHub Copilot opera com duas camadas de contexto ao mesmo tempo: as skills de papel, que definem as responsabilidades que você cobre sozinho, e o agente de estágio, que define o enquadramento do trabalho atual. Saber combiná-las é essencial para obter respostas relevantes durante a imersão.**

![Conceito 02](https://img.shields.io/badge/Conceito-02-171717?style=flat-square) ![Usado em todos os estágios](https://img.shields.io/badge/Uso-Todos%20os%20est%C3%A1gios-737373?style=flat-square) ![Duração 20 min](https://img.shields.io/badge/Dura%C3%A7%C3%A3o-20%20min-A3A3A3?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Todos os participantes |
| **Pré-requisitos** | Nenhum — leia antes do Estágio 1 |
| **Tempo estimado** | 20 minutos |
| **Estágio** | Todos os estágios |
| **Resultado esperado** | Saber selecionar um agente de estágio e contar com as skills de papel no GitHub Copilot |

---

## Conceito

A imersão usa **duas primitivas que se compõem**, e não dois agentes que competem:

- **Skill de papel** — a responsabilidade que você carrega pessoalmente. Ela vive em `.github/skills/` e carrega **automaticamente** quando o seu pedido casa com a `description` dela. Você nunca a seleciona.
- **Agente de estágio** — a fase em que todo o time está. Você o seleciona com `@nome` uma vez por estágio, e ele permanece selecionado.

As duas camadas coexistem por desenho. Você troca de agente de estágio conforme o desafio avança, e a skill do papel relevante se compõe com o agente ativo sempre que o trabalho exigir aquela responsabilidade.

> [!IMPORTANT]
> São **cinco agentes**, não quinze: os quatro agentes de estágio mais o `@dba`. Todo
> outro papel é uma skill, porque uma responsabilidade atravessa o trabalho,
> enquanto um agente marca uma fase. O ciclo de vida dos dados é a exceção que
> confirma a regra — ele atravessa todos os estágios, então não cabe dentro de um
> só. Consulte o [ADR-0002](../docs/adr/0002-team-roles-as-skills-not-agents.md).

---

## Por que isso importa

Sem um agente de estágio, o Copilot responde com enquadramento genérico e pode sugerir trabalho para o momento errado. Sem o conhecimento do papel, o Copilot responde como um assistente genérico, que não conhece a responsabilidade nem as fronteiras dela.

Com as duas camadas ativas, o Copilot sabe ao mesmo tempo:

- **Quem está perguntando** (fronteira do papel, procedimento e critério de qualidade)
- **Em que contexto o trabalho está** (Estágio 1: arqueologia; Estágio 2: especificação; e assim por diante)

Os papeis são skills porque uma pessoa não troca de papel entre um estágio e outro. Um desenho que obrigava a selecionar o seu papel de novo em cada conversa — e depois selecionar o agente de estágio outra vez para recuperar o contexto do estágio — colocava as duas camadas brigando por um único seletor. As skills eliminam a seleção por completo.

---

## Como elas se combinam

```mermaid
%%{init: {'theme':'neutral','themeVariables':{'fontFamily':'ui-sans-serif, system-ui, sans-serif','primaryColor':'#F5F5F5','primaryTextColor':'#171717','primaryBorderColor':'#171717','lineColor':'#525252','secondaryColor':'#FFFFFF','tertiaryColor':'#FAFAFA','background':'#FFFFFF'}}}%%
flowchart LR
    classDef step fill:#F5F5F5,stroke:#171717,color:#171717
    classDef result fill:#FFFFFF,stroke:#171717,color:#171717,stroke-width:2px
    classDef muted fill:#FAFAFA,stroke:#A3A3A3,color:#404040

    P["Skill de papel<br/><sub>.github/skills/persona-*/<br/>carrega automaticamente pela description</sub>"]:::step
    A["Agente de estágio<br/><sub>@archaeologist | @architect<br/>@builder | @evolution | @dba</sub>"]:::step
    C["GitHub Copilot<br/><sub>Resposta enquadrada pelo papel<br/>E pelo estágio atual</sub>"]:::result

    P --> C
    A --> C
```

---

## Camada 1 — Papéis (carregados automaticamente)

Cada participante cobre **todos os 10 papéis** no desafio individual. O perfil de referência de cada um está em [`05-personas/`](../05-personas/); o conhecimento operacional é a skill correspondente em `.github/skills/`.

| Persona | Papel na imersão | Estágio de maior atuação |
|---|---|---|
| **Product Owner** | Define o escopo e valida requisitos com o negócio | Estágios 1 e 2 |
| **Requirements Engineer** | Lê o legado e converte regras em EARS | Estágios 1 e 2 |
| **Enterprise Architect** | Fornece a visão de sistema (C4 L1 e L2) | Estágio 2 |
| **Software Architect** | Define bounded contexts e contratos de API | Estágio 2 |
| **Technical Lead** | Conduz a preparação de PRs e decisões de implementação | Estágio 3 |
| **Developer** | Implementa código Java e Next.js | Estágio 3 |
| **DBA** | Lidera prontidão da fonte, descoberta, mapeamento, população e recuperação | Preparação e Estágios 1–3 |
| **QA Engineer** | Define verificações independentes de evidências, testes, reconciliação e aceitação da consulta | Estágios 1–3 e validação do juiz |
| **DevOps Engineer** | Configura CI/CD, Terraform e Actions | Somente no Estágio 4 posterior ao desafio |
| **Tech Writer** | Documenta APIs, ADRs e runbooks | Estágios 2 e 3 |

### O que cada papel inclui

| Artefato | Localização | Finalidade |
|---|---|---|
| `PERSONA.md` | `05-personas/0X-name/` | Perfil do papel: responsabilidades, entregáveis e slash commands |
| `SKILL.md` | `.github/skills/persona-*/` | Fronteira, procedimento e critério de qualidade do papel — carregados automaticamente |
| `*.prompt.md` | `.github/prompts/` | Slash commands específicos do papel, vinculados ao agente de estágio dono daquele momento |
| `*.instructions.md` | `.github/instructions/` | Regras aplicadas automaticamente aos caminhos de arquivo correspondentes |

> [!IMPORTANT]
> Revise os arquivos `PERSONA.md` dos papéis antes de começar o desafio. Você
> não seleciona a skill do seu papel: descreva o trabalho e ela carrega. Os slash
> commands só funcionam quando o contexto do repositório está carregado no GitHub
> Copilot.

---

## Camada 2 — Agentes de estágio (kit compartilhado)

No início de cada bloco de trabalho, selecione o agente de estágio correspondente no GitHub Copilot. Isso mantém o Copilot alinhado com a fase atual.

| Estágio | Agente | Enquadramento temático | Papéis que lideram |
|---|---|---|---|
| Estágio 1 — Arqueologia | [`@archaeologist`](../06-stage-agents/01-archaeologist/) | Leitura e interpretação do código legado Natural/Adabas | Requirements Engineer, Tech Writer |
| Estágio 2 — Especificação | [`@architect`](../06-stage-agents/02-architect/) | Especificações EARS, ADRs e o modelo C4 | Enterprise Architect, Software Architect |
| Estágio 3 — Implementação | [`@builder`](../06-stage-agents/03-builder/) | Código Java 21, JPA, Testcontainers e Next.js 15 | Developer, DBA, QA Engineer |
| Estágio 4 — Evolução | [`@evolution`](../06-stage-agents/04-evolution/) | Delegação para o modo Agent, IaC e CI/CD | Mantido para trabalho posterior ao desafio; não é usado no desafio individual |

> [!NOTE]
> O Estágio 4 — Evolução permanece no kit para trabalho posterior ao desafio, mas não é usado no desafio individual. O desafio termina no Estágio 3 e na validação do juiz. Consulte o [ADR-0003](../docs/adr/0003-individual-challenge-format.md).

### Diferença na prática

| Sem agente de estágio selecionado | Com agente de estágio selecionado |
|---|---|
| O Copilot responde no contexto geral do repositório | O Copilot adota o enquadramento do estágio atual |
| As respostas se afastam do bloco de trabalho atual | As respostas permanecem consistentes com o estágio selecionado |
| Pode sugerir ações inadequadas ao momento (por exemplo, código no Estágio 1) | Ele se mantém dentro do escopo do estágio atual |

---

## Como selecioná-los

### Skill de papel

Você não a seleciona. Descreva o trabalho com as suas palavras e a skill correspondente carrega a partir da `description` dela. Perguntar ao `@builder` "onde estão as nossas lacunas de cobertura?" carrega o papel de QA sem seleção nenhuma.

Para forçar um papel específico, nomeie-o: "use a skill `persona-qa-engineer`".

### Agente de estágio

1. No início de cada estágio, selecione o agente indicado no fluxo do desafio.
2. Mantenha esse agente selecionado até chegar ao próximo checkpoint de autoavaliação.
3. Selecionar outro agente **substitui** o ativo; agentes não se empilham. As skills de papel continuam carregando dentro do agente que estiver ativo.
4. Um prompt pode selecionar o próprio agente por meio de `agent:`; preserve as fronteiras de leitura e escrita do estágio atual.

### A exceção transversal

O `@dba` é um agente, e não uma skill, porque o ciclo de vida dos dados percorre o desafio e possui prompts com escopo de ferramentas. Selecione-o quando o trabalho for migração de dados, reconciliação ou auditoria de consultas, e depois volte ao agente de estágio.

---

## Exemplo no SIFAP

**Cenário:** você está cobrindo Requirements Engineering no Estágio 2. Você acabou de concluir o C1 no fim do Estágio 1.

```
1. O fluxo do desafio orienta: "Selecione @architect no chat."

2. Você seleciona @architect.
   Resultado: o GitHub Copilot passa a enquadrar as respostas
   no contexto de especificação e arquitetura.

3. Você usa o modo Ask para se orientar:
   "@architect, qual é a ordem recomendada para especificar
   as regras de business-rules-catalog.md?"

4. Use o prompt de estágio ou persona apropriado com uma regra revisada:
   /write-ears-spec feature=<NNN>-<feature>
   Cite o intervalo real da fonte que você leu.
   Não forneça uma regra pronta nem um nome de programa presumido.

5. O requisito EARS inclui um REQ-ID e source_legacy.
   O CI valida a rastreabilidade no PR.
```

---

## Erros comuns e como evitá-los

| Sintoma | Causa | Correção |
|---|---|---|
| O Copilot sugere código durante o Estágio 1 | Agente de estágio errado ou ausente | Selecione `@archaeologist` e confirme o estágio atual |
| O slash command não é reconhecido | Janela do Copilot aberta fora da raiz do repositório | Reabra o VS Code na raiz do repositório |
| As respostas não correspondem ao estágio atual | O agente errado está selecionado | Confirme o agente ativo no início de cada estágio |
| O conhecimento do papel nunca aparece | O pedido foi vago demais para casar com a `description` de uma skill | Nomeie o trabalho, ou nomeie a skill: "use a skill `persona-qa-engineer`" |
| Procurar `@product-owner` no seletor | Os papeis viraram skills; somente os estágios e o `@dba` são agentes | Mantenha o agente de estágio e descreva o trabalho do papel |

---

## Checklist de ativação

- [ ] **Revise os arquivos `PERSONA.md` dos papéis.** Eles estão em `05-personas/`.
- [ ] **Teste um slash command de papel** no GitHub Copilot para confirmar que o contexto do repositório está carregado.
- [ ] **No início de cada estágio, selecione o agente correto.**
- [ ] **Confirme o agente ativo antes de fazer perguntas técnicas críticas.**

---

## Referências

- [Lista completa de personas](../05-personas/OVERVIEW.md)
- [Agentes de estágio](../06-stage-agents/)
- [Cartão dos 3 modos do Copilot](../09-cheat-sheets/copilot-3-modes.md)

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Spec-Driven Development](01-spec-driven-development.md)<br/><sub>Por que especificar antes de codificar e o ciclo do Spec-Kit.</sub> | [Glossário visual](03-visual-glossary.md)<br/><sub>Mais de 30 termos com definição, exemplo do SIFAP e referência.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
