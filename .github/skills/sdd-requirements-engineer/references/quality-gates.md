# Gates de qualidade unificados para SDD e EARS

Aplique toda verificação pertinente. Marque cada uma como `PASS`, `FAIL`, `BLOCKED` ou `NOT APPLICABLE` e cite o artefato, o ID do requisito, o ID da fonte ou a evidência usada. Um pacote só passa quando nenhuma verificação aplicável falha ou permanece bloqueada.

Aplique o [vínculo com o kit](../SKILL.md#vínculo-com-este-kit-do-participante).
FRD/NFRD e os nomes de artefatos em maiúsculas abaixo são seções lógicas em `spec.md`,
`plan.md` e `tasks.md`, não um pacote paralelo obrigatório. Use somente os
diagramas e verificações pertinentes ao escopo selecionado.

## G1. Escopo e evidências

- [ ] G1.01 O modo de operação e as entregas solicitadas estão explícitos.
- [ ] G1.02 O contexto do projeto e o limite do sistema estão identificados.
- [ ] G1.03 Os atores principais, as permissões e as ações proibidas são conhecidos.
- [ ] G1.04 O resultado principal e o limite do escopo são conhecidos.
- [ ] G1.05 Os artefatos e as convenções existentes no repositório foram inspecionados.
- [ ] G1.06 Toda fonte tem um ID `SRC-###` estável e uma classe de fonte.
- [ ] G1.07 As premissas têm impacto, responsável e estado de confirmação.
- [ ] G1.08 Metas, políticas ou aprovações sem sustentação permanecem bloqueios visíveis.
- [ ] G1.09 A criação de arquivos ocorreu somente quando solicitada ou explicitamente autorizada.

## G2. Requisitos EARS

- [ ] G2.01 Todo requisito normativo tem um ID estável e exclusivo.
- [ ] G2.02 Todo requisito normativo registra exatamente uma classificação EARS.
- [ ] G2.03 A ordem das cláusulas corresponde ao padrão EARS selecionado.
- [ ] G2.04 A declaração usa `shall` e nomeia o sistema ou componente responsável.
- [ ] G2.05 A declaração tem uma resposta observável e nenhum comportamento composto oculto.
- [ ] G2.06 Pré-condições, gatilhos, opcionalidade e condições indesejadas estão explícitos quando aplicáveis.
- [ ] G2.07 Requisitos funcionais declaram comportamento, não implementação.
- [ ] G2.08 Todo requisito tem fonte, justificativa, prioridade, sinal de aceitação, método de verificação e status.
- [ ] G2.09 Toda prioridade tem uma justificativa baseada em impacto.
- [ ] G2.10 Caminhos de erro, entrada inválida, timeout, falha de dependência e recuperação estão cobertos quando aplicáveis.
- [ ] G2.11 Comportamentos dependentes do ciclo de vida têm um modelo de estados e requisitos state-driven.
- [ ] G2.12 Termos e unidades são definidos de forma consistente.
- [ ] G2.13 Todo `REQ-NNN` declarado tem um `source_legacy:` válido para a CI; IDs de fonte complementares não o substituem.
- [ ] G2.14 Mistérios sem resposta e hipóteses não validadas não foram promovidos a requisitos.

## G3. Prontidão do FRD

- [ ] G3.01 Problema, resultados desejados, sinais de sucesso, itens no escopo e não objetivos estão explícitos.
- [ ] G3.02 Todo ator participa de um requisito ou é explicitamente informativo.
- [ ] G3.03 Os requisitos estão agrupados por domínio e preservam IDs estáveis.
- [ ] G3.04 As interações externas incluem contratos e comportamento de falha.
- [ ] G3.05 As linhas de resumo correspondem exatamente aos registros normativos.
- [ ] G3.06 Os incrementos de entrega estão ordenados por dependência e podem ser revisados.
- [ ] G3.07 Todo requisito P0 é justificado como essencial ao incremento nomeado.
- [ ] G3.08 Perguntas em aberto identificam o responsável e o escopo afetado.

## G4. Prontidão do NFRD

- [ ] G4.01 Toda categoria de qualidade tem uma decisão de aplicabilidade.
- [ ] G4.02 Toda categoria aplicável tem requisitos ou um bloqueio explícito.
- [ ] G4.03 Toda métrica define meta, agregação, janela, carga de trabalho, ambiente, instrumentação e responsável.
- [ ] G4.04 Toda meta numérica cita evidências ou aprovação do responsável.
- [ ] G4.05 Todo contexto de implantação tem cobertura ou um bloqueio visível.
- [ ] G4.06 Autenticação, autorização, proteção de dados e comportamento diante de abuso ou falha estão cobertos quando aplicáveis.
- [ ] G4.07 Requisitos de confiabilidade definem detecção, degradação, recuperação, RTO ou RPO somente quando aplicáveis e com fonte.
- [ ] G4.08 A conformidade é aplicável, não aplicável ou está bloqueada com um responsável.
- [ ] G4.09 O escopo de acessibilidade e localização está explícito para superfícies voltadas ao usuário.
- [ ] G4.10 Qualidade, linhagem, migração, retenção e exclusão de dados estão cobertas quando aplicáveis.
- [ ] G4.11 Restrições tecnológicas têm fonte, justificativa e gatilhos de revisão.
- [ ] G4.12 Para migração de dados, são tratadas a prontidão da fonte por DBA/QA, a cobertura completa de beneficiários, a reconciliação e a recuperação; evidências apenas de seed ou schema não são aceitas.
- [ ] G4.13 A verificação independente é atribuída a outro participante nomeado, não ao DBA mudando para sua persona de QA; execução e aprovação permanecem planejadas ou bloqueadas até haver evidências reais.

## G5. Integridade dos artefatos SDD

- [ ] G5.01 A constituição existente do repositório é reutilizada ou existe um artefato de governança justificado.
- [ ] G5.02 `SPECIFICATION.md` contém os requisitos ativos canônicos.
- [ ] G5.03 `ANALYSIS.md` registra evidências, lacunas, riscos e alternativas.
- [ ] G5.04 `DESIGN.md` cobre arquitetura, dados, interfaces, segurança, falhas e trade-offs exigidos pelo escopo.
- [ ] G5.05 Diagramas Mermaid estão presentes e válidos quando arquitetura, contexto, implantação, estado, sequência, fluxo de dados ou ciclo de vida forem relevantes.
- [ ] G5.06 `TASKS.md` está ordenado por dependência, e toda tarefa tem um resultado de evidência esperado.
- [ ] G5.07 Toda tarefa `[P]` é independente tanto nas dependências quanto na superfície de mudança.
- [ ] G5.08 `CHECKLIST.md` contém gates de revisão, implementação, verificação e entrega aplicáveis ao escopo.
- [ ] G5.09 `DECISIONS.md` registra escolhas relevantes, alternativas, consequências, evidências e gatilhos de revisão.
- [ ] G5.10 Artefatos opcionais só existem quando as convenções do repositório ou o risco os justificam.
- [ ] G5.11 Todo tipo Mermaid usa o tema claro universal; diagramas semelhantes a grafos contêm as classes canônicas default/zone/external, e tipos não estilizados não contêm `classDef`.
- [ ] G5.12 `DESIGN.md` inclui uma visão de entrega que mapeia requisitos por componentes, tarefas ou plano, dependências, testes ou evidências e estado atual versus estado-alvo.
- [ ] G5.13 Toda tarefa tem checkbox, marcador de sequência, mapeamento de plano, rastreio de requisito e superfície de mudança; o DAG de tarefas cobre todas elas, e tarefas marcadas correspondem ao registro da varredura de verificação.

## G6. Rastreabilidade e ciclo de vida

- [ ] G6.01 Todo requisito ativo tem uma linha explícita de fonte primária.
- [ ] G6.02 Todo requisito ativo é mapeado para design, tarefas, aceitação e verificação.
- [ ] G6.03 Todo elemento de design é mapeado para um ou mais requisitos regentes.
- [ ] G6.04 Toda tarefa de implementação é mapeada para um ou mais requisitos ou para uma obrigação de governança com fonte.
- [ ] G6.05 Todo item de verificação é mapeado para um requisito e um sinal de aceitação.
- [ ] G6.06 Nenhum requisito ativo, elemento de design, tarefa ou item de verificação está órfão.
- [ ] G6.07 Resumos copiados não redefinem nem contradizem declarações normativas canônicas.
- [ ] G6.08 IDs divididos, mesclados, transferidos, substituídos e retirados têm disposições explícitas.
- [ ] G6.09 IDs históricos estáveis não são renomeados em massa silenciosamente.
- [ ] G6.10 Contagens e valores de status entre artefatos concordam.

## G7. Prontidão e checkpoint

- [ ] G7.01 Os status dos artefatos não excedem as evidências disponíveis de aprovação ou execução.
- [ ] G7.02 Verificações com falha ou bloqueadas incluem responsável e ação corretiva.
- [ ] G7.03 O escopo de implementação aprovado é um conjunto explícito de IDs de requisitos.
- [ ] G7.04 As dependências e a ordem estão claras para um agente de implementação.
- [ ] G7.05 As evidências de validação necessárias e as condições de parada estão explícitas.
- [ ] G7.06 O comportamento externo atual cita evidências primárias datadas.
- [ ] G7.07 O checkpoint exclui bloqueios não resolvidos.
- [ ] G7.08 O relatório de entrega segue o modelo de saída da skill.

## Regra de decisão

- `PASS`: todas as verificações aplicáveis passam.
- `READY FOR REVIEW`: não restam bloqueios, mas a aprovação responsável está pendente.
- `BLOCKED`: pelo menos um fato, decisão, fonte ou mapeamento necessário está ausente.
- `FAIL`: um artefato ou requisito aplicável viola uma verificação que pode ser corrigida com as evidências disponíveis.

Não converta `BLOCKED` ou `FAIL` em uma formulação com aparência de sucesso.
