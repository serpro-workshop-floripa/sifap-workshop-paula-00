# Padrão de documentos SDD e Mermaid

Use este documento como referência de conteúdo para artefatos oficiais do Spec-Kit em `specs/`.
O [vínculo com o kit](../SKILL.md#vínculo-com-este-kit-do-participante) é a autoridade:
os nomes em maiúsculas abaixo descrevem responsabilidades em `spec.md`, `plan.md`
e `tasks.md`, não arquivos adicionais obrigatórios nem uma árvore `.specs/` paralela.

## Responsabilidades dos artefatos

| Artefato | Responsabilidade obrigatória |
| --- | --- |
| `SPECIFICATION.md` | Declarações canônicas REQ/NFR, aceitação, premissas, dependências, decisões em aberto e status de implementação baseado em evidências |
| `ANALYSIS.md` | Resumo dos gates, rastreabilidade bidirecional, evidências datadas, achados, condições de aprovação e aprovação formal |
| `DESIGN.md` | Arquitetura, contexto, componentes, implantação, estado, sequências, dados, interfaces, falhas, segurança, observabilidade, superfície de implementação, rastreabilidade da entrega e estado por fases |
| `TASKS.md` | Gate prévio, regras de execução, DAG de dependências, mapeamento de testes, checkboxes por fase, gate de conclusão e registro de execução |
| `TESTING.md` | Testes nomeados, comandos determinísticos, injeção de falhas, contrato de evidências, critérios de saída e estado de verificação datado |
| `DECISIONS.md` | Decisões estáveis, status, contexto, alternativas, consequências, rastros, evidências e gatilhos de revisão |
| `checkpoints/` | Fechamento legível por máquina de requisito para plano, tarefa e teste |
| `contracts/` | Contratos versionados de API ou estado, ou manifesto revisado de não aplicabilidade |

## Tema Mermaid universal

Siga o [guia de estilo da documentação do kit](../../../../docs/DOC-STYLE-GUIDE.md).
Inicie blocos Mermaid com a diretiva neutra do kit:

```text
%%{init: {'theme':'neutral','themeVariables':{'fontFamily':'ui-sans-serif, system-ui, sans-serif','primaryColor':'#F5F5F5','primaryTextColor':'#171717','primaryBorderColor':'#171717','lineColor':'#525252','secondaryColor':'#FFFFFF','tertiaryColor':'#FAFAFA','background':'#FFFFFF'}}}%%
```

Para `flowchart`, `graph` e `classDiagram`, inclua estas
definições exatamente uma vez:

```text
classDef default fill:#F5F5F5,stroke:#171717,color:#171717
classDef zone fill:#FFFFFF,stroke:#525252,color:#171717
classDef external fill:#FAFAFA,stroke:#A3A3A3,color:#404040
```

Use `zone` para limites sob responsabilidade da funcionalidade e agrupamentos lógicos, e `external` para
atores, sistemas externos, especificações vizinhas ou fontes de evidência
fora do limite da funcionalidade. `stateDiagram`, `sequenceDiagram`, `erDiagram`
e `gantt` herdam o tema universal e não devem conter `classDef`.
Renderizadores atuais de `stateDiagram-v2` tratam `default` como token reservado.

Mantenha os diagramas revisáveis:

- menos de 40 nós por bloco;
- rótulos curtos, com detalhes em tabelas adjacentes;
- rótulos de aresta entre aspas;
- IDs explícitos de subgrafos;
- nenhuma cor cromática;
- estados atual, parcial, planejado, bloqueado e alvo separados.

## Portfólio de design obrigatório

Quando forem relevantes para a funcionalidade, `DESIGN.md` inclui:

1. Architecture Overview
2. System Context
3. Component or Service Map
4. Deployment View
5. State Model
6. Critical Sequences
7. Data Flow or Data Lifecycle
8. Data Model
9. Interfaces and Contracts
10. Error, Security, Threat, and Observability design
11. Implementation Surface
12. Delivery and Traceability View
13. Risks and Trade-Offs
14. Phased Development

A visão de entrega mapeia IDs REQ/NFR reais para componentes de design, itens de plano e
tarefas, IDs de dependências ou especificações vizinhas, testes ou evidências e
estado atual versus estado-alvo. Não invente implementação ou aprovação para
completar um diagrama.

## Contrato de tarefas

Use uma entrada com checkbox por tarefa:

```text
- [ ] **T001 [S] [Plan:P1.1] RED** Adicione um teste de contrato que falhe. Rastreia REQ-001.
  - Arquivos: `<actual test path for the selected Java or TypeScript feature>`.
  - Aceitação: TST-C001 falha antes da implementação e passa depois dela.
```

- `[S]` significa sequencial; `[P]` significa independente nas dependências e na superfície de mudança.
- O DAG de dependências contém cada tarefa exatamente uma vez.
- O mapa de testes nomeia os requisitos regentes e os testes planejados ou executados.
- `[x]` é permitido somente quando a tarefa aparece no registro datado
  `Marked complete by verification sweep:` e sua evidência de aceitação
  existe.
- Código parcial existente permanece desmarcado até que o sinal completo de aceitação seja
  demonstrado.

## Validação obrigatória

Use as verificações reais definidas em
[spec-quality.yml](../../../workflows/spec-quality.yml) e o validador de
primitivos existente quando os primitivos mudarem. Inspecione os scripts disponíveis antes
de executá-los. Geradores e validadores SDD genéricos não acompanham este kit;
não alegue que existem nem fabrique sua saída. Use evidências revisadas dos artefatos
para verificações sem gate executável.

Relate uma verificação com falha ou bloqueada como tal. Nunca enfraqueça um gate, adicione uma baseline
nem crie evidência vazia apenas para obter um resultado verde.
