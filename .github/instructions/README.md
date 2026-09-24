# Índice de instruções

Este diretório contém as instruções específicas por arquivo do GitHub Copilot para o workshop.

> [!IMPORTANT]
> O Copilot descobre arquivos `*.instructions.md` em `.github/instructions/` e seus subdiretórios. Este workshop os mantém diretamente neste diretório para facilitar a revisão do índice e dos escopos.

## Arquivos de instrução

| Arquivo | Descrição | Escopo `applyTo` |
| --- | --- | --- |
| `agent-skills.instructions.md` | Use ao criar, revisar ou depurar GitHub Copilot Agent Skills. | `.github/skills/**/SKILL.md` |
| `backend.instructions.md` | Use ao implementar APIs, serviços, controllers, validação e tratamento de erros no backend. | `backend/src/main/java/**,backend/src/test/java/**` |
| `cicd.instructions.md` | Use ao criar ou revisar GitHub Actions, workflows de CI/CD e gates YAML. | `.github/workflows/**,.github/actions/**,**/action.yml,**/action.yaml` |
| `database.instructions.md` | Use ao escrever repositórios, migrações, alterações de schema, SQL e índices. | `backend/src/main/java/**/infrastructure/**,backend/src/main/resources/db/migration/**` |
| `draw-io.instructions.md` | Use ao criar, editar ou revisar diagramas draw.io e XML mxGraph. | `**/*.drawio,**/*.drawio.svg,**/*.drawio.png` |
| `frontend-spec.instructions.md` | Use com Next.js 15 App Router, TypeScript, Tailwind CSS, shadcn/ui e Server Components. | `frontend/app/**,frontend/components/**,frontend/src/app/**,frontend/src/components/**,frontend/**/*.ts,frontend/**/*.tsx` |
| `frontend.instructions.md` | Use ao construir componentes, páginas, interações, estado e fluxos acessíveis. | `frontend/app/**,frontend/components/**,frontend/src/app/**,frontend/src/components/**` |
| `infrastructure.instructions.md` | Use com IaC, Terraform, Bicep, Azure e configuração de ambientes. | `infra/**,**/*.tf,**/*.bicep,compose*.yml,compose*.yaml,docker-compose*.yml,docker-compose*.yaml` |
| `java-junit5-assertions.instructions.md` | Use com assertions JUnit 5 em testes Java do backend. | `**/*Test.java,**/*IT.java,**/*Steps.java,**/*StepDefs.java` |
| `modular-monolith.instructions.md` | Use ao projetar ou revisar o Monólito Modular, limites por funcionalidade, JPA e Strangler Fig. | `backend/src/main/java/**,backend/pom.xml,backend/build.gradle*` |
| `natural-adabas.instructions.md` | Use ao ler Natural/Adabas, FDTs, convenções legadas e fluxos batch. | `01-archaeology/legacy-sifap/**,**/*.NSP,**/*.nsp,**/*.NSN,**/*.nsn,**/*.NSS,**/*.nss,**/*.NSA,**/*.nsa,**/*.NSL,**/*.nsl,**/*.NSC,**/*.nsc,**/*.NSM,**/*.nsm,**/*.NSD,**/*.nsd,**/*.NAT,**/*.nat,**/*.CPY,**/*.cpy,**/*.DDM,**/*.ddm,**/*.jcl,**/*.JCL` |
| `security.instructions.md` | Use com autenticação, autorização, criptografia, secrets e código sensível. | `backend/src/main/java/**/auth/**,backend/src/main/java/**/security/**,backend/src/main/java/**/config/**,backend/src/main/resources/**,frontend/**/auth/**,frontend/**/middleware.ts` |
| `terraform.instructions.md` | Use para higiene genérica do Terraform; as regras Azure ficam em `infrastructure.instructions.md`. | `**/*.tf` |
| `tests.instructions.md` | Use ao criar ou revisar testes, estratégia, cobertura, regressão e gates de qualidade. | `backend/src/test/**,**/*.test.*,**/*.spec.*,**/tests/**` |

## Regra de manutenção

Os requisitos usam a skill de validação EARS. As regras executáveis de rastreabilidade permanecem em [spec-quality.yml](../workflows/spec-quality.yml).

- Cada arquivo deve manter frontmatter YAML válido apenas com os campos necessários `description` e `applyTo`.
- `applyTo` é uma única string entre aspas; separe vários globs por vírgula, sem espaços.
- Evite `applyTo: "**"`; prefira globs específicos.
- Mantenha o padrão: introdução → seções temáticas → `## Convenções` → `## Faça / Não faça` → `## Checklist antes de abrir um PR`.
- Ao criar uma área, adicione um arquivo `*.instructions.md` plano neste diretório e atualize este índice.
