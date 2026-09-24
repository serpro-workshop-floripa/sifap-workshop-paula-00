# Registros de migração de dados

> **Caminho:** [Kit da equipe](../../README.md) > [Documentação](../README.md) > **Registros de migração de dados**

**Registros de apoio em branco para o [ciclo de vida dos dados](../DATA-MIGRATION.md) liderado pelo DBA.**

| Modelo | Quando a equipe o preenche | Arquivo gerado pela equipe | Responsável / revisor |
|---|---|---|---|
| [Prontidão da fonte](source-readiness.template.md) | Preparação e Etapa 1 | [planejado] `docs/data-migration/source-readiness.md` | DBA / QA e responsável pela fonte |
| [Plano de migração](migration-plan.template.md) | Etapa 2, vinculado ao `plan.md` da funcionalidade | [planejado] `docs/data-migration/migration-plan.md` | DBA + arquitetos / QA |
| [Mapeamento origem-destino](source-to-target.template.md) | Etapa 2, a partir da leitura real da fonte | [planejado] `docs/data-migration/source-to-target.md` | DBA / arquitetos + Desenvolvedor |
| [Reconciliação e consulta](reconciliation.template.md) | Etapa 3, após a execução | [planejado] `docs/data-migration/reconciliation.md` | Participante nos papéis DBA / QA / PO; validação independente pela banca |

Selecione `@dba` e solicite, em texto livre, a fase necessária: prontidão,
planejamento, execução autorizada ou validação. Informe os templates e as
evidências disponíveis; para auditar consultas, indique os arquivos reais.
Não sobrescreva evidências existentes nem marque um modelo como concluído apenas porque ele existe.

Mapas de origem, dicionários de declarações, cobertura de leitura e questões em
aberto da Etapa 1 usam os [modelos de arqueologia](../../01-archaeology/templates/).
Requisitos formais, planos de arquitetura e tarefas permanecem na árvore
`.spec/<NNN>-<feature>/` existente; estes registros não substituem artefatos do Spec-Kit.

Todos os resultados de execução e aprovações estão em branco. Mantenha extratos
sensíveis e evidências no nível de registro fora do repositório.
