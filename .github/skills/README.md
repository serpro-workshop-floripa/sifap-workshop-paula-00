# Índice de skills

Este diretório contém as skills de agent do GitHub Copilot para o workshop: **54** no total, cada uma em seu próprio arquivo `<name>/SKILL.md`.

> [!NOTE]
> O Copilot descobre arquivos `SKILL.md` em `.github/skills/<name>/` e carrega automaticamente uma skill ao comparar semanticamente a solicitação com sua `description`. Essa comparação não é visível para as pessoas, por isso este índice existe. As descrições abaixo são essenciais: cada uma informa quando usar a skill e deve permanecer precisa.

## Skills por área

As 54 skills estão agrupadas pela finalidade. Cada skill aparece em exatamente um grupo.

### Papéis de equipe (11 skills)

Estas skills contêm as responsabilidades que antes pertenciam a agents de personas. Elas carregam automaticamente no agent de etapa ativo, sem exigir uma nova seleção de papel. A justificativa está em [ADR-0002](../../docs/adr/0002-team-roles-as-skills-not-agents.md).

| Skill | Descrição |
|-------|-----------|
| [`ux-research-design`](ux-research-design/) | Jobs-to-be-Done, jornadas de usuário, arquitetura da informação e critérios de aceitação de acessibilidade. Produz pesquisa, nunca código de componentes. |

> [!NOTE]
> O papel de DBA não está nesta lista. Ele permanece como agent (`@dba`) porque o ciclo de vida dos dados atravessa as quatro etapas e possui prompts com ferramentas específicas.

### Workshop, SDD e requisitos (7 skills)

| Skill | Descrição |
|-------|-----------|
| [`sdd-requirements-engineer`](sdd-requirements-engineer/) | Use para autoria e validação de EARS baseada em evidências e preparação de checkpoints com Spec-Kit oficial, `REQ-NNN`, `source_legacy:` e critérios de aceitação da migração de dados. Não cria uma árvore SDD paralela nem soluções preenchidas dos exercícios. |
| [`user-story-refine`](user-story-refine/) | Use ao refinar itens do backlog, dividir épicos ou validar critérios INVEST. Acione para "refinar história", "dividir épico", "critérios de aceitação", "história de usuário" e "INVEST". |
| [`code-modernization`](code-modernization/) | Use ao modernizar um sistema legado com um fluxo disciplinado que preserve o comportamento. Acione para modernização, código legado, COBOL, extração de regras de negócio e reescrita com preservação de comportamento. |

### Backend Java e Spring Boot (6 skills)

| Skill | Descrição |
|-------|-----------|
| [`create-spring-boot-java-project`](create-spring-boot-java-project/) | Use para iniciar um backend Spring Boot ou gerar um projeto-base. Cria um esqueleto Java 21 por start.spring.io com Maven, springdoc-openapi, ArchUnit e Docker Compose, alinhado à stack Spring Boot 3.3 do kit. |
| [`java-springboot`](java-springboot/) | Use ao criar ou revisar backend Spring Boot com estrutura idiomática: organização por funcionalidade, injeção por construtor, DTOs e validação, transações em serviços, Spring Data JPA e configuração segura. |
| [`java-docs`](java-docs/) | Use ao escrever, revisar ou melhorar Javadoc e documentação de API Java, com sentenças de resumo, `@param`, `@return`, `@throws`, `{@code}`, `@since` e documentação herdada. |
| [`java-junit`](java-junit/) | Use ao escrever ou revisar testes unitários JUnit 5 de lógica de negócio Java, com Arrange-Act-Assert, ciclo de vida, testes parametrizados, assertions e Mockito. Para testes slice ou de integração do Spring Boot, use `spring-boot-testing`. |
| [`spring-boot-testing`](spring-boot-testing/) | Use ao escolher ou implementar testes slice e de integração do Spring Boot, como `@WebMvcTest`, `@DataJpaTest`, `@RestClientTest`, `@JsonTest`, `@SpringBootTest`, Testcontainers, Mockito e AssertJ. Destina-se a Spring Boot 3.3 + JUnit 5. |

### Dados e banco de dados (4 skills)

| Skill | Descrição |
|-------|-----------|

### Frontend e testes (4 skills)

| Skill | Descrição |
|-------|-----------|
| [`playwright-generate-test`](playwright-generate-test/) | Use para gerar um teste end-to-end Playwright em TypeScript a partir de um cenário. Controle o Playwright MCP etapa por etapa e execute o teste até que passe. |
| [`tdd-workflow`](tdd-workflow/) | Use ao praticar desenvolvimento orientado a testes, escrever primeiro um teste que falha ou seguir red-green-refactor. Acione para "TDD", "red-green-refactor", "test first", "failing test" e "write a test". |
| [`test-strategy`](test-strategy/) | Use ao definir estratégia de testes, formato da pirâmide, metas de cobertura ou investimentos entre testes unitários, de integração e E2E. |

### Azure, IaC e CI/CD (14 skills)

| Skill | Descrição |
|-------|-----------|

### Documentação e diagramas (4 skills)

| Skill | Descrição |
|-------|-----------|
| [`doc-style-lint`](doc-style-lint/) | Use ao revisar documentação quanto a estilo, clareza, linguagem inclusiva, legibilidade ou conformidade com guias de estilo da Microsoft ou do Google. |

### Contexto da base de código e ferramentas do Copilot (4 skills)

| Skill | Descrição |
|-------|-----------|
| [`acquire-codebase-knowledge`](acquire-codebase-knowledge/) | Use quando a pessoa pedir explicitamente para mapear, documentar ou facilitar a integração em uma base de código existente. Não use em implementações rotineiras, correções de bugs ou alterações restritas sem descoberta em todo o repositório. |
| [`copilot-sdk`](copilot-sdk/) | Use ao criar aplicações agênticas com GitHub Copilot SDK, incorporar agents, criar ferramentas personalizadas, transmitir respostas, gerenciar sessões, conectar servidores MCP ou criar agents personalizados. |

## Regra de manutenção

- O valor de `name:` em `SKILL.md` deve corresponder exatamente ao nome do diretório pai, com letras minúsculas, números e hífens e no máximo 64 caracteres. Caso contrário, o Copilot não carrega a skill.
- Somente `name` e `description` são chaves válidas no frontmatter. Outras chaves, como `license`, `allowed-tools`, `compatibility` ou `metadata`, falham no gate `copilot-primitives`.
- `description` aceita no máximo **1024 caracteres** e deve informar quando usar a skill, pois é o único sinal usado pelo Copilot para carregamento automático.
- O corpo de cada skill precisa conter, nesta ordem: `## Quando invocar`, uma seção substantiva de procedimento, `## Modelo de saída` e `## Gate de qualidade`.
- O schema completo e o contrato das seções estão em [`../PRIMITIVE-STANDARD.md`](../PRIMITIVE-STANDARD.md) e são aplicados por [`../scripts/validate-copilot-primitives.py`](../scripts/validate-copilot-primitives.py). Ao adicionar uma skill, inclua sua linha no grupo correspondente e atualize a contagem total.
