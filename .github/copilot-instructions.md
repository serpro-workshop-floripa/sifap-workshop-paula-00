# Instruções do GitHub Copilot — Workshop de modernização de legado

Estas instruções definem o que cada participante constrói, a stack adotada e as regras válidas para todo o repositório.

## Ferramentas aprovadas

O workshop usa uma toolchain fixa: VS Code, GitHub Copilot (modos Ask, Plan e Agent), GitHub Spec-Kit, GitHub, Docker/Docker Compose e Terraform. Outros assistentes de IA, IDEs, interfaces de chat web e frameworks de SDD não são permitidos, pois misturar ferramentas rompe a rastreabilidade especificação → código → teste. Consulte a tabela completa em [`README.md`](../README.md).

## Contexto do projeto

O projeto moderniza o sistema Natural/Adabas **SIFAP** (Sistema de Fiscalização e Administração de Pagamentos) para Java 21 + Next.js 15. A [cronologia](../01-archaeology/legacy-sifap/CHRONOLOGY.md) foi transcrita dos cabeçalhos-fonte. Preserve as datas originais e cite esse arquivo em vez de reescrevê-las. [`01-archaeology/legacy-sifap/`](../01-archaeology/legacy-sifap/) contém 24 membros Natural/JCL, 4 DDMs `.ddm` e 1 listagem FDT. As [atribuições](../01-archaeology/legacy-sifap/natural-programs/README.md) abrangem 15 membros atribuídos e 9 de apoio.

O workshop é um **desafio individual** (14:00-17:40). Cada participante executa sozinho as Etapas 1-3, começando em `@archaeologist`. As duas primeiras submissões aprovadas pela validação do juiz vencem. A Etapa 4 e a orquestração paralela de subagentes não fazem parte do desafio. Consulte [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) e [ADR-0003](../docs/adr/0003-individual-challenge-format.md).

O kit tem duas camadas: um agente por etapa (`archaeologist`, `architect`, `builder` e o agente transversal `dba`; `evolution` permanece, mas não é usado) e uma skill para cada um dos 10 papéis cobertos pelo participante. Um novo estágio é um agente; um novo papel é uma skill. Consulte [`06-stage-agents/README.md`](../06-stage-agents/README.md) e [ADR-0002](../docs/adr/0002-team-roles-as-skills-not-agents.md).

Use as skills em [`.github/skills/`](skills/) para fluxos especializados. O Copilot seleciona a skill relevante pela descrição.

## Idioma do repositório

- Esta cópia publica a documentação e toda a prosa dos primitivos do Copilot em português brasileiro.
- Preserve paths, identificadores, schemas, comandos, branches, IDs, termos técnicos consagrados e fontes legadas no idioma original.
- Mantenha o [seletor de idioma](../README.md#repository-languages) vinculado às branches de idioma existentes e às respectivas instruções.

## Escopo exclusivo do participante

- Mantenha no kit apenas guias de exercícios, modelos, primitivos do Copilot e fontes locais de entrada.
- Site, publicação no Pages, demonstrações do instrutor, gabaritos e soluções de referência pertencem ao repositório privado do instrutor.
- Não publique endereços de acesso, credenciais ou instruções administrativas dos ambientes do instrutor. Cada participante constrói e documenta a própria solução.

## Stack de destino

- **Backend:** Java 21 + Spring Boot 3.3 + JPA/Hibernate + PostgreSQL 16
- **Frontend:** Next.js 15 (App Router) + TypeScript 5 (strict) + Tailwind CSS + shadcn/ui
- **Contêineres:** Docker + Docker Compose, criados pelo participante na Etapa 3 quando necessário
- **IaC:** Terraform (provider Azure `~> 3.x`)
- **CI/CD:** GitHub Actions
- **Testes:** JUnit 5 + Testcontainers no backend; Vitest + Testing Library no frontend

## Regras transversais de implementação

As regras detalhadas de Java, TypeScript, banco de dados, segurança, infraestrutura e testes estão em [`.github/instructions/`](instructions/) e carregam automaticamente para os paths correspondentes.

- Use nomes de classes e comentários em inglês.
- Use `/api/v1/{resource}` nos paths das APIs REST.
- Valide entradas em cada fronteira do sistema.
- Nunca grave secrets, chaves de API ou credenciais no código.
- Nunca exponha dados sensíveis, como CPF e valores de benefícios, em logs. Mascare-os.
- Configure CORS explicitamente. Não use o curinga `*` em produção.
- Use Managed Identity na autenticação entre serviços Azure.
- Escreva testes durante a implementação, não depois.

## Desenvolvimento orientado por especificação (Spec-Kit)

- Cada requisito usa notação **EARS** (Easy Approach to Requirements Syntax).
- Cada requisito tem um **REQ-ID** exclusivo no formato `REQ-NNN`.
- Cada requisito inclui uma linha `source_legacy:` apontando para uma fonte legada ou `[GREENFIELD] + justificativa`.
- Use `01-archaeology/legacy-sifap/natural-programs/*.{NSP,NSN,NSS,NSA,NSL,NSC,NSM,jcl}` ou `01-archaeology/legacy-sifap/adabas-ddms/*.{NSD,ddm,txt}` para requisitos baseados no legado.
- O job `legacy-traceability` rejeita PRs que violem essa regra. Consulte [`01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md`](../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md).
- Testes rastreiam REQ-IDs por comentários inline.
- Cada prefixo de branch nasce de `develop`, nunca de `spec/*`, e retorna por merge em `develop` → `main`. Não existe branch `stage`.
- Use `spec/<NNN>-<feature>` na Etapa 2, `impl/<NNN>-<feature>` na Etapa 3 e `docs/<topic>` para documentação. `infra/<component>` e `agent/<issue-NN>` não são usados no desafio.
- O PR de submissão usa `impl/<NNN>-<feature>` → `develop`. Nunca incorpore `impl/` ou outro prefixo em `spec/`.
- Consulte a tabela completa em [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md).
- Antes de escrever requisitos EARS na Etapa 2, leia os programas Natural e DDMs da capacidade-alvo.

## Regras estritas

- Não suponha a existência de protótipo, conteinerização ou infraestrutura herdada. `backend/`, `frontend/` e `infra/` ainda não existem. Crie apenas o necessário para o recorte na Etapa 3.
- Não escreva requisito EARS sem `source_legacy:`.
- Não adicione dependências sem justificativa em uma ADR.
- Não escreva testes somente depois da implementação.
- Não exponha secrets em commits, logs ou descrições de PR.
- Não faça merge em `main` sem revisão.
- Não pule os checkpoints C1, C2 e C3 de [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md).
- Não execute orquestração paralela de subagentes durante o desafio.
- Não crie `AGENTS.md`, `CLAUDE.md` ou `GEMINI.md` na raiz. Este arquivo é a fonte única de instruções globais. Consulte [ADR-0001](../docs/adr/0001-agent-instructions-single-source-of-truth.md).
- Não adicione nem edite um primitivo do Copilot fora do padrão de [`PRIMITIVE-STANDARD.md`](PRIMITIVE-STANDARD.md).

## Referências

- Fluxo, checkpoints e conclusão: [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md)
- Fluxo Git: [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md)
- Três modos do Copilot: [`09-cheat-sheets/copilot-3-modes.md`](../09-cheat-sheets/copilot-3-modes.md)
- Kits de papéis: [`05-personas/`](../05-personas/)
- Agentes de etapa: [`06-stage-agents/`](../06-stage-agents/)
- Sistema legado SIFAP: [`01-archaeology/legacy-sifap/`](../01-archaeology/legacy-sifap/)
- SDD com Spec-Kit: <https://github.com/github/spec-kit>

<!-- SPECKIT START -->
Para obter contexto adicional sobre tecnologias, estrutura do projeto, comandos shell e outras informações importantes, leia o plano atual.
<!-- SPECKIT END -->
