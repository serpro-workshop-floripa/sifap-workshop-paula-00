---
name: "create-spring-boot-java-project"
description: "Use quando a pessoa quiser iniciar um novo backend Spring Boot ou gerar um projeto-base. Crie um esqueleto Java 21 com Spring Boot 3.3 por start.spring.io, Maven, springdoc-openapi, ArchUnit, Testcontainers e PostgreSQL 16, pronto para execução com Docker Compose e alinhado à stack do kit."
---
# Criação de projeto Java com Spring Boot

Crie um esqueleto de backend com Spring Boot 3.3 e Java 21, fixado na stack do kit: PostgreSQL 16, Maven, springdoc-openapi, ArchUnit e Testcontainers. Execute todos os comandos no terminal integrado do VS Code, o único editor aprovado pelo kit. O prompt `/create-spring-boot-java-project` aplica os ajustes específicos do kit, como módulo de destino e dependências.

> [!IMPORTANT]
> O kit usa somente **PostgreSQL 16**, sem Redis nem MongoDB. Crie o módulo `backend/`, que ainda não existe e deve nascer na Etapa 3. Nunca grave credenciais no repositório. Forneça-as por variáveis de ambiente.

## Quando invocar

- "Inicie um novo backend Spring Boot."
- "Crie o esqueleto do módulo `backend/`."
- "Gere um projeto Spring Boot 3.3 com Java 21 e PostgreSQL."
- "Prepare a estrutura do projeto para começarmos a Etapa 3."

## Procedimento

### Pré-requisitos

Confirme a instalação das ferramentas:

| Ferramenta | Finalidade |
|------------|------------|
| Java 21 (JDK) | Compilar e executar a aplicação |
| Docker + Docker Compose | Executar PostgreSQL 16 localmente |
| VS Code | Editor aprovado pelo kit |

Para personalizar o nome do artefato ou pacote-base, altere `artifactId` e `packageName` em [Baixar o template do projeto Spring Boot](#baixar-o-template-do-projeto-spring-boot). Para mudar a versão do Spring Boot, altere `bootVersion` na mesma etapa e permaneça na linha 3.3.x do kit.

### Verificar a versão do Java

```shell
java -version
```

Confirme que a saída informa Java 21.

### Baixar o template do projeto Spring Boot

Baixe de start.spring.io um esqueleto Maven com Java 21 e as dependências do kit, sem Redis nem MongoDB.

Confirme antes se a release fixa do Boot 3.3 continua disponível. Se não estiver, registre o bloqueio e analise uma fonte compatível para o template. Não atualize silenciosamente a stack do workshop. Substitua o placeholder do nome do projeto e trabalhe em um novo diretório de saída aprovado.

```shell
PROJECT_NAME="<project-name>"
curl --fail --show-error --location https://start.spring.io/starter.zip \
  -d "artifactId=$PROJECT_NAME" \
  -d bootVersion=3.3.5 \
  -d dependencies=configuration-processor,web,data-jpa,postgresql,validation,testcontainers,flyway \
  -d javaVersion=21 \
  -d packageName=com.example \
  -d packaging=jar \
  -d type=maven-project \
  -o starter.zip
```

### Descompactar e limpar

```shell
unzip starter.zip -d "./$PROJECT_NAME"
rm -f starter.zip
cd "$PROJECT_NAME"
```

Continue somente depois de um download bem-sucedido. Verifique se a configuração Maven gerada inclui `flyway-core` e o módulo do Flyway específico para PostgreSQL exigido pela versão gerenciada pelo Boot. Adicione apenas dependências ausentes, sem duplicar o que o Initializr gerou:

```xml
<dependency>
  <groupId>org.flywaydb</groupId>
  <artifactId>flyway-core</artifactId>
</dependency>
<dependency>
  <groupId>org.flywaydb</groupId>
  <artifactId>flyway-database-postgresql</artifactId>
</dependency>
```

Use o gerenciamento de dependências do Spring Boot e documente a decisão. O suporte ao schema não carrega dados originados do Adabas.

### Adicionar springdoc-openapi e ArchUnit

Inclua as dependências `springdoc-openapi-starter-webmvc-ui` e `archunit-junit5` em `pom.xml`:

```xml
<dependency>
  <groupId>org.springdoc</groupId>
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
  <version>2.6.0</version>
</dependency>
<dependency>
  <groupId>com.tngtech.archunit</groupId>
  <artifactId>archunit-junit5</artifactId>
  <version>1.2.1</version>
  <scope>test</scope>
</dependency>
```

A linha 2.6 do springdoc é compatível com Boot 3.3. Verifique a [matriz de compatibilidade](https://springdoc.org/#what-is-the-compatibility-matrix-of-springdoc-openapi-with-spring-boot) e as versões de patch escolhidas pela equipe antes de declarar o build compatível. Não presuma a compatibilidade de um starter mais recente.

### Configurar SpringDoc e JPA

Adicione as configurações da UI do SpringDoc a `application.properties`:

```properties
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha
```

Adicione as configurações de datasource do PostgreSQL e do JPA. Leia a senha de uma variável de ambiente. Nunca a grave diretamente:

```properties
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.url=jdbc:postgresql://localhost:5432/postgres
spring.datasource.username=postgres
spring.datasource.******
spring.jpa.hibernate.ddl-auto=validate
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
```

> [!NOTE]
> Use `ddl-auto=validate`, não `update`, para que as migrações versionadas do Flyway sejam responsáveis pelo schema, conforme [`database.instructions.md`](../../instructions/database.instructions.md). Defina `POSTGRES_PASSWORD` no shell ou em um arquivo local `.env` ignorado pelo Git, nunca em `application.properties`.

### Adicionar Docker Compose somente com PostgreSQL 16

Crie `compose.yaml` na raiz do projeto com um único serviço PostgreSQL 16:

```yaml
services:
  postgres:
    image: postgres:16
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
```

Adicione o diretório de dados a `.gitignore`:

```gitignore
postgres_data
```

### Verificar o build

Testcontainers fornece um PostgreSQL 16 real aos testes. Assim, o build não depende de um banco iniciado manualmente:

```shell
./mvnw clean test
```

Para executar a aplicação com um banco local, inicie antes o serviço do Compose:

```shell
docker compose up -d
./mvnw spring-boot:run
docker compose down
```

## Modelo de saída

```markdown
### Criado
- `backend/`: esqueleto Spring Boot 3.3 (Java 21, Maven)
- Dependências: web, data-jpa, postgresql, validation, testcontainers, lombok, springdoc, archunit
- `compose.yaml`: somente o serviço PostgreSQL 16

### Build
`./mvnw clean test` -> BUILD SUCCESS
```

## Gate de qualidade

- [ ] O esqueleto usa Spring Boot 3.3.x e Java 21 e foi gerado em um novo módulo `backend/`.
- [ ] As dependências correspondem ao kit, sem Redis, MongoDB nem starter de cache.
- [ ] O arquivo Docker Compose define somente um serviço PostgreSQL 16.
- [ ] Nenhuma credencial está gravada diretamente; a senha do datasource vem de `POSTGRES_PASSWORD`.
- [ ] `./mvnw clean test` termina com `BUILD SUCCESS` antes da entrega do esqueleto.
