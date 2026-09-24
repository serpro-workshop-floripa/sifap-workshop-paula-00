# Pontos de verificação da investigação

Perguntas de investigação por template para a Fase 2 do fluxo de `acquire-codebase-knowledge`. Em cada área, procure primeiro as respostas na saída da varredura. Depois, leia os arquivos-fonte para preencher as lacunas.

---

## 1. STACK.md: stack de tecnologia

- Qual é a linguagem principal e sua versão exata? Verifique `.nvmrc`, `go.mod`, `pyproject.toml` e a linha `FROM` do Docker.
- Qual gerenciador de pacotes é usado? Exemplos: `npm`, `yarn`, `pnpm`, `go mod`, `pip` e `uv`.
- Quais são os principais frameworks de runtime? Considere servidor web, ORM e contêiner de DI.
- O que `dependencies` (produção) e `devDependencies` (ferramentas de desenvolvimento) contêm?
- Existe uma imagem Docker? Qual imagem base ela usa?
- Quais são os principais scripts em `package.json`, `Makefile` ou `pyproject.toml`?

## 2. STRUCTURE.md: layout dos diretórios

- Onde fica o código-fonte? Em geral, ele está em `src/`, `lib/` ou na raiz do projeto em Go.
- Quais são os pontos de entrada? Verifique `main` em `package.json`, `scripts.start`, `cmd/main.go` e `app.py`.
- Qual é a finalidade declarada de cada diretório do nível superior?
- Existem diretórios menos evidentes, como `eng/`, `platform/` ou `infra/`?
- Existem diretórios ocultos de configuração, como `.github/`, `.vscode/` ou `.husky/`?
- Quais convenções nomeiam os diretórios? Exemplos: camelCase, kebab-case, por domínio ou por camada.

## 3. ARCHITECTURE.md: padrões

- O código está organizado por camada, como controllers, services e repos, ou por funcionalidade?
- Qual é o fluxo de dados principal? Rastreie uma request ou um comando desde a entrada até o armazenamento.
- Existem singletons, padrões de injeção de dependência ou requisitos explícitos de ordem de inicialização?
- Existem workers em segundo plano, filas ou componentes orientados a eventos?
- Quais padrões de design aparecem repetidamente? Exemplos: Factory, Repository, Decorator e Strategy.

## 4. CONVENTIONS.md: padrões de código

- Qual é a convenção de nomes de arquivos? Verifique pelo menos 10 arquivos para identificar camelCase, kebab-case ou PascalCase.
- Qual é a convenção de nomes de funções e variáveis?
- Métodos ou campos privados usam prefixos, como `_methodName` ou `#field`?
- Quais linter e formatador estão configurados? Verifique `.eslintrc`, `.prettierrc` e `golangci.yml`.
- Quais opções de rigor do TypeScript estão ativas, como `strict` e `noImplicitAny`?
- Como cada camada trata erros? Ela lança exceções ou retorna um erro estruturado?
- Qual biblioteca de logs é usada? Qual é o formato das mensagens?
- Como os imports são organizados? Considere barrel exports, aliases de paths e regras de agrupamento.

## 5. INTEGRATIONS.md: serviços externos

- Quais APIs externas são chamadas? Procure `axios.`, `fetch(`, `http.Get(` e URLs base em constantes.
- Como as credenciais são armazenadas e acessadas? Considere `.env`, gerenciador de secrets e variáveis de ambiente.
- Quais bancos de dados são acessados? Verifique no manifesto `pg`, `mongoose`, `prisma`, `typeorm` e `sqlalchemy`.
- Existe API gateway, service mesh ou proxy entre a aplicação e os serviços externos?
- Quais ferramentas de monitoramento ou observabilidade são usadas? Considere APM, Prometheus e pipelines de logs.
- Existem filas de mensagens ou barramentos de eventos, como Kafka, RabbitMQ, SQS ou Pub/Sub?

## 6. TESTING.md: configuração de testes

- Qual test runner está configurado? Verifique `scripts.test` em `package.json`, `pytest.ini` e `go test`.
- Onde ficam os arquivos de teste? Junto ao código, em `tests/` ou em `__tests__/`?
- Qual biblioteca de assertions é usada? Exemplos: Jest expect, Chai e pytest assert.
- Como as dependências externas são simuladas? Considere `jest.mock`, injeção de dependência e fixtures.
- Existem testes de integração que acessam serviços reais? Quais testes unitários usam mocks?
- Existe um limite de cobertura obrigatório? Verifique `jest.config.js`, `.nycrc` e `pyproject.toml`.

## 7. CONCERNS.md: problemas conhecidos

- Quantos TODOs, FIXMEs e HACKs existem no código de produção? Consulte a saída da varredura.
- Quais arquivos tiveram mais alterações no Git nos últimos 90 dias? Consulte a saída da varredura.
- Existem arquivos com mais de 500 linhas que misturam várias responsabilidades?
- Algum serviço faz chamadas sequenciais que poderiam ser paralelizadas?
- Existem valores gravados diretamente no código, como URLs, IDs ou números mágicos, que deveriam ser configuração?
- Quais riscos de segurança existem? Considere ausência de validação de entrada, erros brutos expostos aos clientes e verificações de autenticação ausentes.
- Existem padrões de desempenho que não escalam, como consultas N+1 ou caches em memória usados em várias instâncias?
