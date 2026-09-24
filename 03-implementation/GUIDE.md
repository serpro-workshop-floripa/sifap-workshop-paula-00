# Etapa 3 — Implementação (100 min)

> **Caminho:** [Kit da equipe](../README.md) › [Etapa 3](README.md) › **GUIA**

**Este guia conduz o participante pela construção do protótipo funcional do SIFAP 2.0, desde a estrutura inicial até as funcionalidades implementadas com testes, migrações e rastreabilidade até os REQ-IDs.**

![Etapa 3](https://img.shields.io/badge/Etapa-3%20%C2%B7%20Implementa%C3%A7%C3%A3o-171717?style=flat-square) ![Duração 100 min](https://img.shields.io/badge/Dura%C3%A7%C3%A3o-100%20min-737373?style=flat-square) ![Horário 15:30–17:10](https://img.shields.io/badge/Hor%C3%A1rio-15%3A30--17%3A10-A3A3A3?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | As responsabilidades de Desenvolvimento (TL + Developer) e QA (DBA + QA) lideram; o participante prepara a estrutura de CI |
| **Pré-requisitos** | Checkpoint C2 aceito; `spec.md`, `plan.md` e `tasks.md` prontos com REQ-IDs e `source_legacy:` |
| **Tempo estimado** | 100 min |
| **Etapa** | Etapa 3 — Implementação |
| **Resultado esperado** | Backend e frontend funcionais consultando no PostgreSQL dados reconciliados originados do Adabas; testes aprovados; commits com `Implements REQ-XXX` |

> [!IMPORTANT]
> Consulte o cronograma exato em [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md). Os badges mostram apenas a duração da etapa.

---

## Conceito: Monólito Modular

Um Monólito Modular é uma arquitetura na qual bounded contexts são módulos Java independentes dentro de uma única JVM, com limites explícitos entre eles. É o ponto de partida recomendado para modernizar o SIFAP antes de qualquer futura extração de microsserviços.

**Por que isso importa:** o SIFAP legado tem acoplamento implícito entre módulos por meio de memória compartilhada (Natural/Adabas). O Monólito Modular torna esse acoplamento explícito e controlado. Cada módulo expõe apenas a interface de que os outros módulos precisam.

**Strangler Fig:** um padrão de migração que envolve gradualmente o sistema legado. O protótipo da Etapa 3 não precisa substituir todo o SIFAP. Modernize um bounded context de cada vez, mantendo o sistema legado ativo nas partes que ainda não foram migradas.

---

## Conceito: Testcontainers

Testcontainers é uma biblioteca Java que inicia contêineres Docker reais durante os testes. Em vez de simular o PostgreSQL com um banco de dados em memória (C2), os testes usam o mecanismo real do banco de dados de produção.

**Por que isso importa:** testes com C2 podem passar e depois falhar com PostgreSQL devido a diferenças em SQL, tipos e comportamento de transações. Testcontainers elimina essa divergência.

**Erro comum:** esquecer de iniciar o Docker Desktop antes de executar `./mvnw test`. O erro é `Could not find a valid Docker environment`.

---

## Conceito: TDD (Test-Driven Development)

TDD é a prática de escrever o teste antes da implementação. O ciclo é: escrever um teste que falha (red), implementar o mínimo de código necessário para passar (green) e melhorar o código sem quebrar o teste (refactor).

**Aplique isto ao SIFAP:** escolha um requisito do `spec.md` do participante e escreva
um teste para seus critérios de aceitação aprovados antes de implementá-lo. O teste
falha até que a lógica especificada exista; este guia não fornece nenhum requisito pronto.

---

## Definition of Ready — antes de começar

> [!IMPORTANT]
> Confirme todos os itens antes de iniciar esta etapa:

- [ ] O PO aceitou o checkpoint C2.
- [ ] A persona `@builder` está selecionada no Copilot Chat.
- [ ] `.spec/<NNN>-<feature>/spec.md` tem REQ-IDs com entradas `source_legacy:` válidas.
- [ ] `.spec/<NNN>-<feature>/plan.md` contém as decisões necessárias para a primeira tarefa.
- [ ] O participante definiu os caminhos iniciais do protótipo (`backend/`, `frontend/` e, se necessário, `infra/`).
- [ ] DBA e arquitetos aprovaram a prontidão da origem, snapshot/extração, mapeamentos, ordem de carga, reexecução/retomada e recuperação do destino; QA definiu a reconciliação independente.
- [ ] O PO confirmou a cobertura completa dos beneficiários autorizados e os critérios de aceitação de listagem/pesquisa/detalhes.
- [ ] A branch `impl/<NNN>-<feature>` foi criada a partir da branch `develop` atualizada.

---

## Objetivo

Crie do zero o primeiro protótipo funcional do SIFAP 2.0 e implemente as funcionalidades priorizadas na Etapa 2. O kit não fornece codebase, conteinerização pronta nem symlink para protótipo. O participante cria a estrutura, implementa as funcionalidades e escreve testes. Toda funcionalidade deve ser rastreada até um REQ-ID.

A Etapa 3 é onde a especificação encontra a realidade. Um requisito EARS bem escrito na Etapa 2 se torna um teste que passa ou falha. Cada commit inclui uma referência `Implements REQ-XXX:` na mensagem. Sem ela, a rastreabilidade termina.

---

## Primeiros 15 minutos: criação da estrutura

### Passo 1 — Crie as pastas do protótipo

```bash
mkdir -p backend frontend
```

### Passo 2 — Crie a estrutura mínima

- **Backend:** Spring Boot 3.3, Java 21, Maven Wrapper e o pacote-base aprovado em `plan.md`.
- **Frontend:** Next.js 15 App Router, TypeScript strict e Tailwind CSS.
- **Banco de dados:** migrações Flyway em `backend/src/main/resources/db/migration/`.

O Flyway cria e evolui o schema; o DBA também implementa o pipeline aprovado de
migração de registros. Fixtures de teste podem apoiar testes isolados, mas nem
fixtures nem migrações apenas de schema substituem a população da origem.

> [!CAUTION]
> Não use código nem conteinerização de protótipos externos. O objetivo do workshop é que o participante construa o protótipo moderno a partir de sua leitura do sistema legado.

### Passo 3 — Verifique se a configuração mínima funciona

- Backend: `cd backend && ./mvnw test` deve passar assim que a estrutura existir.
- Frontend: `cd frontend && npm test` (ou o comando definido pelo participante) deve passar.
- Crie `infra/` somente quando o participante começar a descrever IaC ou composição local.

---

## Estrutura do backend

```text
backend/src/main/java/<approved/base/package>/
└── <feature>/
    ├── domain/
    ├── application/
    └── infrastructure/
```

### Camadas (de dentro para fora)

| Camada | Responsabilidade | Exemplos |
|---|---|---|
| **domain** | Regras de negócio puras, sem dependência de framework | Enums de status, interfaces de repositório, value objects |
| **application** | Casos de uso e orquestração | Services, DTOs de request/response |
| **infrastructure** | Detalhes técnicos e I/O | Controllers REST, entidades JPA, repositórios Spring Data |

> [!IMPORTANT]
> A camada `domain` nunca importa classes de `infrastructure`. O fluxo é sempre Controller → Service → Repository (interface em domain, implementação em infrastructure).

---

## Passo a passo: adicione uma funcionalidade

- [ ] **Releia o requisito EARS.** Abra `spec.md` e releia o REQ-ID a ser implementado.
- [ ] **Verifique a evidência do legado.** Confirme `source_legacy:` e releia o programa `.NSN` correspondente.
- [ ] **Revise o modelo.** Siga o mapeamento, os casos de uso e os contratos REST aprovados; devolva decisões não resolvidas para Arquitetura e DBA.
- [ ] **Escreva o teste primeiro.** Crie o teste de mapeamento/repositório ou de comportamento antes de implementar a alteração correspondente.
- [ ] **Crie a migração Flyway.** Adicione a alteração de schema revisada em `backend/src/main/resources/db/migration/`.
- [ ] **Implemente o código.** Controller → Service → Repository, seguindo as camadas.
- [ ] **Execute os testes.** `./mvnw test` deve passar com o Docker em execução.
- [ ] **Faça o commit da alteração.** Inclua `Implements REQ-XXX` na mensagem.

> [!CAUTION]
> Use Flyway. Nunca modifique migrações existentes. Sempre crie novas (`V2__`, `V3__` e assim por diante). Editar uma migração antiga corrompe o histórico do schema e interrompe os deployments.

---

## Fluxo com o Copilot Plan

Para implementar funcionalidades com rastreabilidade:

1. Selecione os arquivos relevantes no VS Code (Ctrl+clique).
2. Abra o Copilot no modo Plan.
3. Descreva a alteração em linguagem natural e solicite um plano antes da execução:
   > "Planeje a implementação do requisito EARS `REQ-XXX`. Liste os arquivos envolvidos, os riscos e os testes necessários. Ainda não implemente."
4. Revise o plano em relação à arquitetura aprovada; o modo Plan não implementa a alteração por conta própria.
5. Autorize o modo Agent local ou implemente manualmente; depois, revise o diff e execute os testes.

> [!TIP]
> Use Plan para a revisão de design e o modo Agent local para a implementação autorizada.
> A Etapa 4 explora o coding agent separado do GitHub, no fluxo de Issue para PR.

---

## Migração de dados: DBA lidera, QA verifica, Desenvolvimento integra

Siga o [guia de migração de dados](../docs/DATA-MIGRATION.md). Implemente estas tarefas
junto com o código da aplicação, não depois:

1. **Teste primeiro o contrato aprovado.** Cubra conversões, entradas inválidas, identificadores preservados da origem, ocorrências MU/PE e falhas com PostgreSQL 16.
2. **Extraia o snapshot acordado do Adabas.** Registre versão da origem, limite do snapshot, formato de exportação e evidências de integridade. Não grave nem redefina a origem.
3. **Prepare o staging e carregue.** Preserve a linhagem da origem, valide cada registro, carregue na ordem de dependência e registre rejeições com motivos acionáveis. Mantenha registros brutos e credenciais fora do Git e de logs públicos.
4. **Reconcilie de forma independente.** QA verifica a cobertura completa das chaves da origem, a contabilização de carregados/rejeitados, os relacionamentos, as conversões de campos e os agregados acordados usando o mesmo snapshot. Linhas filhas no destino podem superar as linhas da origem; explique-as pelos mapeamentos, em vez de comparar totais de tabelas não relacionadas.
5. **Conecte consultas reais.** Desenvolvimento implementa listagem, pesquisa e acesso a detalhes autorizados e paginados no PostgreSQL. Verifique a cobertura completa dos beneficiários entre páginas; não use mocks nem seeds de fallback no caminho de aceitação.
6. **Exercite reexecução e recuperação.** Reprocessar o mesmo snapshot não pode duplicar registros; uma interrupção deve ter um caminho testado de retomada ou limpeza. Teste a recuperação do destino sem alterar a origem.

Registre resultados sanitizados e referências de evidências nos
[registros de migração de dados](../docs/data-migration/). Resolva beneficiários
rejeitados antes de declarar a consulta completa; relatar uma rejeição explica uma
lacuna, mas não torna o beneficiário consultável. Não reduza a população para passar.

---

## Testes

### Execute todos os testes

```bash
cd backend
./mvnw test
```

**Pré-requisito:** o Docker deve estar em execução. Os testes usam Testcontainers para iniciar uma instância real do PostgreSQL.

### Tipos de teste esperados

| Tipo | Classe | O que testa |
|---|---|---|
| Unitário | `*ServiceTest.java` | Lógica de negócio isolada |
| Integração | `*ControllerTest.java` | Endpoint completo (HTTP → DB) |
| Repositório | `*RepositoryTest.java` | Consultas personalizadas |
| Migração de dados | Testes de integração definidos pelo participante | Leitura do snapshot, mapeamento da origem para o destino, reconciliação, rejeições, reexecução/retomada e recuperação do destino |
| Consulta de beneficiários | Testes de aceitação de API + UI | Listagem/pesquisa/detalhes autorizados e cobertura completa da população entre páginas |

---

## Frontend

### Execute o frontend localmente

```bash
cd frontend
npm install
npm run dev
```

Abra `http://localhost:3000`.

### Arquitetura do frontend

O frontend usa Next.js 15 com App Router e Server Components:

```text
src/app/
├── layout.tsx
├── page.tsx
└── <feature>/
    └── page.tsx
```

| Tipo de componente | Quando usar |
|---|---|
| **Server Component** (padrão) | Busca de dados no servidor; sem JavaScript no cliente |
| **Client Component** (`"use client"`) | Interatividade: formulários, modais e estado local |

---

## Rastreabilidade: requisito → código → teste

Documente a rastreabilidade de cada funcionalidade implementada:

| Requisito EARS | Arquivo de implementação | Arquivo de teste |
|---|---|---|
| `REQ-XXX` | `<!-- preencha -->` | `<!-- preencha -->` |

Todo commit que implementa um comportamento da especificação deve incluir `Implements REQ-XXX` na mensagem. Isso fecha o ciclo especificação → código → teste e permite que `/speckit.analyze` detecte desvios.

---

<details>
<summary><strong>Armadilhas comuns — expandir</strong></summary>

| Se você está fazendo isto | Faça isto |
|---|---|
| Uma branch enorme de oito horas | Use commits pequenos e PRs pequenas. Uma funcionalidade = uma PR |
| Implementar sem testes e planejar "fazê-los depois" | Escreva o teste junto com o código |
| Editar uma migração Flyway antiga | Nunca faça isso. Sempre crie uma nova migração (`V5__`, `V6__`...) |
| Criar um endpoint sem `@Valid` no DTO | Sempre use Bean Validation no controller |
| Misturar lógica de domínio no controller | O controller chama um service. A lógica pertence ao service ou ao domínio |
| Importar classes de infraestrutura entre contextos | Preserve os limites definidos pelo participante |
| Fazer commit sem `Implements REQ-XXX` | A rastreabilidade valida o trabalho da etapa anterior |

</details>

---

<details>
<summary><strong>Solução de problemas — expandir</strong></summary>

| Problema | Solução |
|---|---|
| O ambiente local não inicia | Verifique Java 21, Node, variáveis de ambiente e se as portas 5432/8080/3000 estão livres |
| O backend não consegue se conectar ao PostgreSQL | Verifique a URL configurada e se a instância PostgreSQL selecionada pelo participante está em execução |
| O frontend mostra "Failed to load" | O backend está em execução? Teste com `curl http://localhost:8080/actuator/health` |
| O teste com Testcontainers falha | Verifique o Docker Desktop e a configuração do teste. Testes unitários com Mockito não substituem o gate de migração/integração com PostgreSQL |
| A migração falha na inicialização | Nunca edite uma migração existente. Crie uma nova (`V5__`, `V6__`...) |
| Erro de import em `mvn test-compile` | Verifique se o pacote segue `domain/` → `application/` → `infrastructure/` |
| A Swagger UI não aparece | Tente `http://localhost:8080/swagger-ui/index.html` |

</details>

---

## Critérios de conclusão

- [ ] O fluxo priorizado pelo participante está implementado e documentado.
- [ ] A interface necessária para esse fluxo está disponível.
- [ ] Os testes definidos pelo participante passam com `./mvnw test`.
- [ ] A execução local está documentada no protótipo.
- [ ] Os contratos expostos estão documentados com Swagger/OpenAPI.
- [ ] A regra priorizada na Etapa 1 está implementada e testada.
- [ ] O PostgreSQL está populado a partir do snapshot aprovado do Adabas, com linhagem da origem e sem perda inexplicada de registros.
- [ ] DBA e QA reconciliaram chaves, relacionamentos, conversões, rejeições e agregados acordados; nenhuma lacuna não resolvida de beneficiários está oculta.
- [ ] Consultas autorizadas de listagem, pesquisa e detalhes cobrem todos os beneficiários da população acordada, incluindo registros além da primeira página.
- [ ] Reexecução/retomada e recuperação do destino foram testadas sem alterar a origem; extratos restritos permanecem fora do Git.
- [ ] Todo commit inclui `Implements REQ-XXX` na mensagem.

---

## Próximo passo

Durante o checkpoint C3 (por volta das 16:10), o participante usando `@builder` e `@dba`
entrega ao participante (Operações) o código funcional, o PostgreSQL populado e as evidências
de migração revisadas por QA. As responsabilidades de QA continuam a validação final dos dados
e das consultas. Um schema vazio, um seed de teste ou uma diferença de reconciliação não
resolvida bloqueia a aceitação dos dados, mesmo que os testes unitários passem.

Consulte [`../04-evolution/GUIDE.md`](../04-evolution/GUIDE.md) para a próxima etapa.

---

<details>
<summary><strong>Prompts úteis para o Copilot Chat — expandir</strong></summary>

1. "Crie um endpoint REST para [funcionalidade] seguindo a arquitetura existente."
2. "Escreva um teste de integração para o endpoint [endpoint]."
3. "Adicione Bean Validation ao DTO [classe]."
4. "Crie uma migração Flyway para adicionar [tabela/coluna]."
5. "Implemente a regra de negócio BR-XXX: [descrição da regra]."
6. "Crie um React Server Component para listar [entidade]."
7. "Adicione tratamento de erros para [cenário]."
8. "Refatore este service para separar a lógica de [responsabilidade]."

</details>

> [!TIP]
> Não tente implementar tudo. Priorize qualidade em vez de quantidade. Um endpoint bem construído, com testes, validação e documentação, vale mais do que cinco endpoints quebrados.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Etapa 2 — Especificação](../02-modern-spec/GUIDE.md)<br/><sub>14:50–15:30 · Escreva requisitos EARS, ADRs e diagramas C4.</sub> | [Etapa 4 — Evolução](../04-evolution/GUIDE.md)<br/><sub>não utilizada no desafio individual · Copilot Agent + Terraform + CI/CD.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
