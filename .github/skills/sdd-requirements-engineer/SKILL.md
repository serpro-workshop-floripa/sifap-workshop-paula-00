---
name: "sdd-requirements-engineer"
description: "Use ao elicitar, escrever, revisar ou entregar requisitos EARS baseados em evidências legadas descobertas pelo participante, com artefatos Spec-Kit, rastreabilidade e gates SDD."
---

# Engenharia de requisitos SDD com EARS

Transforme intenções incompletas de produto ou evidências de design existentes em requisitos EARS atômicos e em um conjunto coerente de artefatos de desenvolvimento orientado por especificação. Preserve a proveniência desde a fonte inicial até o design, as tarefas, a verificação e a entrega para implementação.

## Quando invocar

- "Transforme estas anotações em um FRD e um NFRD usando EARS."
- "Execute o fluxo SDD completo para esta funcionalidade."
- "Converta este design em requisitos EARS e tarefas rastreáveis."
- "Revise estes requisitos ou artefatos SDD em busca de lacunas e trabalho órfão."
- "Prepare anotações de checkpoint prontas para implementação a partir desta especificação aprovada."

## Modos de operação

### Vínculo com este kit do participante

O [fluxo do kit](../../../09-cheat-sheets/spec-kit-workflow.md) é a autoridade:

- A Etapa 1 gera evidências por leitura guiada; ela não recebe catálogos preenchidos, soluções de mistérios, modelos de destino nem aprovações inventadas.
- Leia as fontes legadas reais antes de escrever EARS. Mantenha mistérios não resolvidos como não confirmados; nenhum requisito deriva de uma pergunta sem resposta.
- Cada funcionalidade fica em `.spec/<NNN>-<feature>/`, fixada em `.specify/feature.json` para que os comandos `/speckit.*` a resolvam. O script upstream `/speckit.specify` grava em uma raiz sem ponto; mova a saída para `.spec/` e nunca mantenha duas árvores. A [instrução de artefatos SDD](../../instructions/sdd-artifacts.instructions.md) rege o layout e os contratos de arquivos.
- Todos os novos requisitos normativos usam `REQ-NNN` e `source_legacy:` com um path de fonte real e compatível ou `[GREENFIELD]` mais a justificativa da equipe. `SRC-###` é proveniência complementar, nunca substituta.
- Emita `source_legacy:` sem marcador de lista nas 20 linhas seguintes à declaração de cada requisito e antes do próximo; o parser atual da CI não aceita um item de lista Markdown. Declare requisitos apenas em `spec.md`; nos demais arquivos, cite REQ-IDs em células de tabela ou no meio da frase, nunca no início de uma linha.
- Preserve IDs existentes de requisitos e de aceitação. Novos IDs de aceitação usam `AC-REQ-NNN-NN`; rótulos FR/NFR descrevem um campo de categoria, não um esquema de identificadores concorrente.
- As dez responsabilidades lógicas das referências incluídas mapeiam para arquivos Spec-Kit em minúsculas, nunca para arquivos em maiúsculas: especificação e rastreabilidade de fontes em `spec.md`; análise e decisões em `research.md`; design em `plan.md`, `data-model.md` e `contracts/`; testes em `quickstart.md` e no mapa de testes de `tasks.md`; tarefas, análise cruzada e verificação em `tasks.md`; checklists em `checklists/`. Vincule ADRs, decisões de escopo e [registros de dados](../../../docs/DATA-MIGRATION.md) em vez de copiá-los.
- Uma funcionalidade só está pronta para C2 quando o conjunto completo de artefatos existe, com arquivos não aplicáveis explicando o motivo. Modos mais restritos atualizam apenas os arquivos que tocam; não há aprovação gerada nem cota obrigatória de diagramas.
- Use somente ferramentas de validação realmente presentes. Este kit tem [spec-quality.yml](../../workflows/spec-quality.yml), `/speckit.analyze`, `/speckit.checklist` e a [validação de primitivos](../../scripts/validate-copilot-primitives.py), não as ferramentas genéricas `scripts/validate-sdd-*`.

### Seleção do modo

| Modo | Ponto de partida | Entrega |
| --- | --- | --- |
| Requisitos | Anotações brutas, PRD, issue, notas de entrevista ou evidência legada | Análise de lacunas, FRD e NFRD |
| SDD completo | Requisitos brutos ou aprovados | Requisitos, especificação, análise, design, tarefas, gates, decisões, verificação e rastreabilidade |
| Design primeiro | Esboço de arquitetura, contrato de API, modelo de dados ou protótipo | Requisitos recuperados, premissas explícitas e, depois, a cadeia SDD completa |
| Validação | FRD, NFRD, especificação, design ou conjunto de tarefas existente | Achados classificados por severidade, declarações EARS corrigidas e decisão de prontidão |
| Entrega | Artefatos SDD revisados | Pacote de implementação delimitado, com gates, dependências e bloqueios não resolvidos |

Selecione o menor modo que satisfaça a solicitação. Não gere o conjunto completo de artefatos para revisar um único requisito.

## Política de fontes e evidências

Use esta ordem de precedência:

1. Objetivos, restrições e decisões aprovados pelo usuário.
2. Evidências do repositório, como especificações, código, testes, schemas, ADRs, issues e configuração operacional existentes.
3. Documentação primária datada para comportamentos de plataformas externas que precisem estar atualizados.
4. Premissas explícitas com responsável, impacto e estado de confirmação.

Atribua a cada fonte um identificador estável `SRC-###`. Um artefato derivado não é a fonte primária de um requisito quando o usuário original, o repositório ou uma fonte oficial está disponível. Nunca invente meta, cota, preço, benchmark, obrigação de conformidade ou estado de aprovação.

## Procedimento

1. Estabeleça o escopo e a ação.
   - Inspecione instruções, modelos, especificações e convenções de nomenclatura existentes no repositório antes de criar arquivos.
   - Identifique se a solicitação começa pelos requisitos, pelo design, limita-se à validação ou limita-se ao checkpoint.
   - Registre os paths de saída solicitados e se o usuário já autorizou a criação de arquivos. Se a criação não foi solicitada, devolva rascunhos ou achados de revisão sem gravar arquivos.

2. Classifique o contexto do projeto.

   | Contexto | Ênfase necessária |
   | --- | --- |
   | Greenfield | Resultados, sinais de sucesso, não objetivos e premissas |
   | Brownfield | Comportamento atual, escopo da mudança, compatibilidade e limites de regressão |
   | Modernização ou migração | Paridade com a fonte, correção dos dados, cutover, rollback e desativação |
   | API ou plataforma | Consumidores, contratos, versionamento, limites de taxa e compatibilidade |
   | Dispositivo móvel ou edge | Estados de conectividade, plataformas compatíveis, sincronização e recuperação |
   | Sistema de dados ou IA | Qualidade e linhagem dos dados, evolução de modelo ou schema, avaliação e fallback |
   | SaaS ou multi-tenant | Isolamento, onboarding, direitos de acesso e controles de noisy neighbor |
   | Ferramenta interna ou CLI | Contexto de identidade, distribuição, instalação e suporte |
   | Infraestrutura | Modelo de acesso, ambientes, confiabilidade, observabilidade e rollback |

3. Execute o gate de ambiguidades e lacunas.
   - Classifique cada lacuna como `PRESENT`, `BLOCKER`, `HIGH-RISK ASSUMPTION` ou `NOT APPLICABLE`.
   - Trate atores e permissões, resultado principal, limite do escopo e fonte de autoridade como bloqueios quando ausentes.
   - Faça no máximo três perguntas focadas em bloqueios, uma por vez. Não pergunte sobre fatos respondidos pelas evidências do repositório.
   - Registre itens de alto risco não resolvidos em vez de substituí-los por padrões silenciosos.

4. Escreva ou normalize os requisitos.
   - Leia a [referência de notação EARS](references/ears-notation.md) antes de escrever requisitos normativos.
   - Use o [modelo de FRD](references/frd-template.md) e o [modelo de NFRD](references/nfrd-template.md) quando esses artefatos estiverem no escopo.
   - Atribua IDs estáveis `REQ-NNN` e IDs de aceitação compatíveis com a funcionalidade existente; registre separadamente a categoria funcional ou não funcional.
   - Adicione `source_legacy:` dentro da distância aceita pela CI após cada declaração de requisito; IDs de fonte complementares não o substituem.
   - Escreva uma resposta observável do sistema por declaração EARS. Separe comportamentos compostos.
   - Mantenha os requisitos funcionais neutros quanto à implementação. Coloque restrições tecnológicas reais no NFRD, com justificativa e evidência da fonte.
   - Dê a cada requisito prioridade, fonte, justificativa, sinal de aceitação, método de verificação e estado do ciclo de vida.
   - Expresse NFRs numéricos com contexto de medição: métrica, meta, carga de trabalho, percentil ou agregação, janela de observação, ambiente e responsável pela evidência. Se algum valor necessário for desconhecido, mantenha um bloqueio visível.
   - Adicione um modelo de estados quando o comportamento depender do ciclo de vida de uma entidade.

5. Construa a cadeia de artefatos SDD.
   - Leia os [modelos de artefatos SDD](references/spec-templates.md) e o [padrão de documentos SDD e Mermaid](references/sdd-document-and-mermaid-standard.md).
   - Reutilize `.specify/memory/constitution.md`. Não crie uma constituição local da funcionalidade.
   - Para SDD completo, crie ou atualize o conjunto completo em `.spec/<NNN>-<feature>/`: `spec.md`, `research.md`, `plan.md`, `data-model.md`, `contracts/`, `quickstart.md`, `tasks.md` e `checklists/`, informando o motivo da não aplicabilidade em vez de omitir um arquivo.
   - Use o portfólio completo de design, o tema claro universal do Mermaid, as classes canônicas de grafos e uma visão de entrega que conecte requisitos, componentes, tarefas, dependências, evidências e estado atual versus estado-alvo.
   - Escreva checkboxes de tarefas ordenadas por dependência, com metadados de sequência, plano, requisito, mudança e evidência, além de DAG completo, mapa de testes, gate de conclusão e registro; marque apenas tarefas plenamente evidenciadas e use `[P]` somente quando forem realmente independentes.
   - Use o próximo número livre preenchido com zeros em `.spec/<NNN>-<feature>` e a branch correspondente `spec/<NNN>-<feature>`.

6. Imponha rastreabilidade de ponta a ponta.
   - Dê a cada requisito ativo uma linha explícita de rastreabilidade de fonte em `spec.md`.
   - Mapeie cada requisito ativo aos componentes de design em `plan.md`, às entidades em `data-model.md` quando houver dados envolvidos, às tarefas e aos testes em `tasks.md` e a um cenário de validação em `quickstart.md`.
   - Rejeite requisitos, elementos de design e tarefas órfãos, além de testes sem requisito regente.
   - Registre IDs transferidos, substituídos, divididos, mesclados ou retirados em uma tabela de disposições. Nunca renumere silenciosamente requisitos estáveis.
   - Preserve o mesmo significado normativo entre FRD/NFRD, especificação, design, tarefas e testes. Vincule pelo ID em vez de copiar texto sujeito a divergência.

7. Valide e entregue.
   - Aplique cada verificação pertinente dos [gates de qualidade unificados](references/quality-gates.md).
   - Use o [catálogo de antipadrões](references/anti-patterns.md) para corrigir defeitos antes da entrega.
   - Mantenha os artefatos como `Draft` ou `Ready for review` até que um revisor responsável os aprove.
   - Use `Implemented` ou `Verified` somente quando evidências do repositório ou de execução sustentarem a afirmação.
   - Execute as verificações existentes e aplicáveis de `spec-quality.yml`. Inspecione os comandos nomeados antes de usá-los; ferramentas ausentes são relatadas como indisponíveis, não inventadas ou instaladas apenas para imitar outro framework.
   - Entregue somente o escopo aprovado, os paths dos artefatos, a ordem das dependências, os resultados dos gates e os bloqueios não resolvidos. Não inicie a implementação como parte desta skill.

## Contrato de requisitos EARS

Cada registro de requisito normativo contém:

| Campo | Regra |
| --- | --- |
| ID | `REQ-NNN` estável e exclusivo; categoria e domínio registrados separadamente |
| Padrão | Exatamente um entre ubiquitous, event-driven, state-driven, optional, unwanted ou complex |
| Declaração | Ordem canônica das cláusulas EARS, com `shall` e uma resposta observável |
| Prioridade | P0, P1, P2 ou P3, com justificativa do impacto na entrega |
| Fonte | `source_legacy:` obrigatório, com fonte real ou `[GREENFIELD]` justificado; `SRC-###` complementar opcional |
| Justificativa | Por que o comportamento ou a restrição de qualidade é necessário |
| Aceitação | Pelo menos um sinal de aprovação ou reprovação |
| Verificação | Teste, inspeção, análise ou medição planejada; nenhuma entrega de demonstração do workshop |
| Status | Proposed, ready for review, approved, implemented, verified ou retired |

Priorize pelo impacto evidenciado na entrega: P0 bloqueia o incremento nomeado; P1 perde valor material ou redução de risco, mas tem uma solução alternativa aprovada; P2 pode ser adiado sem violar o objetivo do incremento; P3 não tem impacto material na entrega. Divida um incremento quando seu conjunto P0 não puder ser revisado.

## Limites

- Não implemente código de produto, não altere infraestrutura nem implante recursos.
- Não alegue aprovação de stakeholders, conformidade, desempenho ou verificação sem evidências.
- Não sobrescreva uma constituição, um esquema de IDs de requisitos ou uma convenção de artefatos existente sem uma decisão explícita de compatibilidade.
- Não use uma rota de design primeiro para contornar requisitos, sinais de aceitação ou rastreabilidade de fontes.
- Não force todos os artefatos opcionais em mudanças pequenas quando um conjunto mais leve e rastreável for suficiente.

## Cuidados

- Histórias de usuário expressam intenção, mas não são requisitos normativos; sinais de aceitação concordam com os requisitos sem redefini-los.
- `shall` pertence às declarações EARS; tecnologias nomeadas são restrições com fonte ou preferências de design não resolvidas, não requisitos funcionais automáticos.
- Uma formulação de desempenho não é mensurável sem a definição da carga de trabalho e do método de observação.

## Divulgação progressiva e recursos incluídos

Carregue somente os recursos exigidos pelo modo selecionado:

- [Notação EARS](references/ears-notation.md): sintaxe, classificação, exemplos, defeitos e referências acadêmicas.
- [Modelo de FRD](references/frd-template.md): escopo funcional, atores, requisitos de domínio, aceitação e entrega em fases.
- [Modelo de NFRD](references/nfrd-template.md): restrições de qualidade mensuráveis e envelopes de medição.
- [Modelos de artefatos SDD](references/spec-templates.md): responsabilidades completas dos artefatos e modelos concisos.
- [Padrão de documentos SDD e Mermaid](references/sdd-document-and-mermaid-standard.md): contratos canônicos de artefatos, tema claro universal para diagramas, contrato de checklist e registro de tarefas e gates executáveis.
- [Gates de qualidade unificados](references/quality-gates.md): verificações detalhadas de prontidão, EARS, rastreabilidade e checkpoints.
- [Catálogo de antipadrões](references/anti-patterns.md): defeitos de requisitos e SDD, com ações corretivas.

## Modelo de saída

Retorne exatamente esta estrutura:

```markdown
## SDD EARS result

**Status:** completed | ready-for-review | blocked
**Mode:** requirements | full-sdd | design-first | validation | checkpoint
**Project context:** <classification>
**Summary:** <one-sentence outcome>

### Artifacts
| Artifact | Path or result | Status |
| --- | --- | --- |
| <name> | <path, draft, or not requested> | <draft|ready-for-review|blocked> |

### Requirements and gaps
- Functional requirements: <count>
- Non-functional requirements: <count>
- Blockers: <IDs and reason, or none>
- High-risk assumptions: <IDs and owner, or none>

### EARS and traceability evidence
- EARS validation: <passed count>/<applicable count>
- Source coverage: <covered requirements>/<active requirements>
- Cross-artifact coverage: <covered requirements>/<active requirements>
- Orphans or lifecycle dispositions: <none or summary>

### Quality gates
- Result: <pass|fail>
- Failed checks: <gate IDs and fixes, or none>
- Approval state: <draft|ready-for-review|approved with evidence>

### Handoff
- Ready for implementation: <yes|no>
- Approved scope: <requirement IDs or none>
- Dependencies: <ordered summary>
- Open questions: <questions or none>
```

## Gate de qualidade

- [ ] O modo de operação selecionado é o menor que satisfaz a solicitação.
- [ ] A precedência das fontes, as premissas, os bloqueios e a autorização de gravação de arquivos estão explícitos.
- [ ] Todo requisito normativo atende ao contrato de requisitos EARS.
- [ ] O conteúdo de FRD e NFRD está completo para cada categoria aplicável.
- [ ] Os artefatos SDD são internamente consistentes e proporcionais ao escopo.
- [ ] Todo diagrama Mermaid usa o tema claro universal e todo diagrama semelhante a grafo contém as classes neutras canônicas.
- [ ] O design em `plan.md` mapeia requisitos por componentes, tarefas, dependências, testes ou evidências e estado atual versus estado-alvo.
- [ ] Checkboxes, dependências, mapa de testes e registro de verificação de `tasks.md` concordam; implementação parcial não é marcada como concluída.
- [ ] Todo requisito ativo é rastreável desde a fonte até o design, as tarefas, a aceitação e a verificação.
- [ ] Mudanças no ciclo de vida dos requisitos preservam IDs ou incluem disposições explícitas.
- [ ] Nenhuma métrica, aprovação, alegação de compatibilidade ou fato atual sobre plataforma é fabricado.
- [ ] Toda verificação detalhada aplicável dos [gates de qualidade unificados](references/quality-gates.md) passa ou é relatada como bloqueio.
- [ ] A resposta segue exatamente `## Modelo de saída`.
- [ ] Todo recurso incluído e referenciado por esta skill existe.
- [ ] As verificações existentes e aplicáveis do kit foram executadas, ou as indisponíveis foram relatadas explicitamente sem alegação de sucesso.
- [ ] `.spec/`, o conjunto completo de artefatos em minúsculas, `REQ-NNN`, `source_legacy:` e o escopo exclusivo do participante são preservados; nenhum pacote em maiúsculas, segunda árvore ou solução pronta é gerado.
