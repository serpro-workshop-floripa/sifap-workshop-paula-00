# Referência para detecção da stack

Carregue este arquivo quando a stack de tecnologia for ambígua, por exemplo, quando houver vários manifestos, extensões desconhecidas ou nenhum `package.json` ou `go.mod` evidente.

---

## Arquivo de manifesto por ecossistema

| Arquivo | Ecossistema | Campos principais para leitura |
|---------|-------------|-------------------------------|
| `package.json` | Node.js / JavaScript / TypeScript | `dependencies`, `devDependencies`, `scripts`, `main`, `type`, `engines` |
| `go.mod` | Go | Path do módulo, versão do Go, bloco `require` |
| `requirements.txt` | Python (pip) | Lista de pacotes com versões fixadas |
| `Pipfile` | Python (pipenv) | `[packages]`, `[dev-packages]`, versão do Python em `[requires]` |
| `pyproject.toml` | Python (poetry / uv / hatch) | `[tool.poetry.dependencies]`, `[project]`, `[build-system]` |
| `setup.py` / `setup.cfg` | Python (setuptools, legado) | `install_requires`, `python_requires` |
| `Cargo.toml` | Rust | `[dependencies]`, `[[bin]]`, `[lib]` |
| `pom.xml` | Java / Kotlin (Maven) | `<dependencies>`, `<artifactId>`, `<groupId>`, `<java.version>` |
| `build.gradle` / `build.gradle.kts` | Java / Kotlin (Gradle) | `dependencies {}`, `sourceCompatibility` |
| `composer.json` | PHP | `require`, `require-dev` |
| `Gemfile` | Ruby | Declarações `gem`, restrição de versão do `ruby` |
| `mix.exs` | Elixir | `deps/0`, `elixir: "~> X.Y"` |
| `pubspec.yaml` | Dart / Flutter | `dependencies`, `dev_dependencies`, `environment.sdk` |
| `*.csproj` | .NET / C# | `<PackageReference>`, `<TargetFramework>` |
| `*.sln` | Solução .NET | Referências a vários projetos `.csproj` |
| `deno.json` / `deno.jsonc` | Deno (runtime TypeScript) | `imports`, `tasks` |
| `bun.lockb` | Bun (runtime JavaScript) | Lockfile binário, consulte `package.json` para as dependências |

---

## Detecção da versão do runtime da linguagem

| Linguagem | Onde encontrar a versão |
|-----------|-------------------------|
| Node.js | `.nvmrc`, `.node-version`, `engines.node` em `package.json`, `FROM node:X` no Docker |
| Python | `.python-version`, `pyproject.toml [requires-python]`, `FROM python:X` no Docker |
| Go | Primeira linha de `go.mod` (`go 1.21`) |
| Java | `<java.version>` em `pom.xml`, `sourceCompatibility` em `build.gradle`, `FROM eclipse-temurin:X` no Docker |
| Ruby | `.ruby-version`, `ruby 'X.Y.Z'` em `Gemfile` |
| Rust | `rust-toolchain.toml`, arquivo `rust-toolchain` |
| .NET | `<TargetFramework>` em `.csproj`, por exemplo, `net8.0` |

---

## Detecção de frameworks (Node.js / TypeScript)

| Dependência em `package.json` | Framework |
|-------------------------------|-----------|
| `express` | Express.js (servidor HTTP mínimo) |
| `fastify` | Fastify (servidor HTTP de alto desempenho) |
| `next` | Next.js (SSR/SSG com React, verifique o diretório `pages/` ou `app/`) |
| `nuxt` | Nuxt.js (SSR/SSG com Vue) |
| `@nestjs/core` | NestJS (framework opinativo para Node.js com DI) |
| `koa` | Koa (focado em middleware, sem router integrado) |
| `@hapi/hapi` | Hapi |
| `@trpc/server` | tRPC (API type-safe sem schemas REST/GraphQL) |
| `routing-controllers` | routing-controllers (wrapper do Express baseado em decorators) |
| `typeorm` | TypeORM (ORM SQL com decorators) |
| `prisma` | Prisma (ORM type-safe, verifique `prisma/schema.prisma`) |
| `mongoose` | Mongoose (ODM do MongoDB) |
| `sequelize` | Sequelize (ORM SQL) |
| `drizzle-orm` | Drizzle (ORM SQL leve) |
| `react` sem `next` | SPA React sem framework, verifique `react-router-dom` |
| `vue` sem `nuxt` | SPA Vue sem framework |

---

## Detecção de frameworks (Python)

| Pacote | Framework |
|--------|-----------|
| `fastapi` | FastAPI (REST assíncrono, documentação OpenAPI automática) |
| `flask` | Flask (framework web WSGI mínimo) |
| `django` | Django (inclui recursos integrados, verifique `settings.py`) |
| `starlette` | Starlette (ASGI, geralmente usado como base do FastAPI) |
| `aiohttp` | aiohttp (cliente e servidor HTTP assíncronos) |
| `sqlalchemy` | SQLAlchemy (ORM SQL, verifique migrações `alembic`) |
| `alembic` | Alembic (ferramenta de migração do SQLAlchemy) |
| `pydantic` | Pydantic (validação de dados, base do FastAPI) |
| `celery` | Celery (fila distribuída de tarefas) |

---

## Detecção de monorepo

Verifique estes sinais na ordem:

1. `pnpm-workspace.yaml`: workspaces do pnpm
2. `lerna.json`: monorepo Lerna
3. `nx.json`: monorepo Nx, verifique também `workspace.json`
4. `turbo.json`: Turborepo
5. `rush.json`: Rush, gerenciador de monorepo da Microsoft
6. `moon.yml`: Moon
7. `package.json` com `"workspaces": [...]`: workspaces do npm/yarn
8. Presença dos diretórios `packages/`, `apps/`, `libs/` ou `services/` com seus próprios arquivos `package.json`

Se detectar um monorepo, considere que cada workspace pode ter dependências e convenções independentes. Mapeie cada subpacote separadamente em `STACK.md` e registre a estrutura do monorepo em `STRUCTURE.md`.

---

## Detecção de aliases de paths do TypeScript

Se `tsconfig.json` tiver uma chave `paths`, os imports com prefixos não relativos são aliases. Mapeie-os antes de documentar a estrutura.

```json
// exemplo de tsconfig.json
"paths": {
  "@/*": ["./src/*"],
  "@components/*": ["./src/components/*"],
  "@utils/*": ["./src/utils/*"]
}
```

Imports como `import { foo } from '@/utils/bar'` resolvem para `src/utils/bar`. Documente como `src/utils/bar`, não como `@/utils/bar`.

---

## Imagem base do Docker por runtime

Se não houver manifesto, mas existir um `Dockerfile`, a linha `FROM` revela o runtime:

| Padrão da linha FROM | Runtime |
|----------------------|---------|
| `FROM node:X` | Node.js X |
| `FROM python:X` | Python X |
| `FROM golang:X` | Go X |
| `FROM eclipse-temurin:X` | Java X (Eclipse Temurin JDK) |
| `FROM mcr.microsoft.com/dotnet/aspnet:X` | .NET X |
| `FROM ruby:X` | Ruby X |
| `FROM rust:X` | Rust X |
| `FROM alpine` isolado | Verifique o que foi instalado com `RUN apk add` |
