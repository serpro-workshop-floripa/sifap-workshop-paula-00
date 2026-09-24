---
name: "java-springboot"
description: "Use ao criar ou revisar código de backend Spring Boot e aplicar estrutura e convenções idiomáticas. Abrange organização por funcionalidade, injeção por construtor, DTOs e validação, transações na camada de serviço, Spring Data JPA e configuração segura. Complementa a stack Java 21 + Spring Boot 3.3 do kit."
---
# Boas práticas de Spring Boot

Crie e revise recortes idiomáticos do backend SIFAP 2.0 com Spring Boot 3.3, Java 21 e PostgreSQL 16. Use organização por funcionalidade, injeção por construtor, DTOs com records, transações na camada de serviço e Spring Data JPA. Esta skill oferece um checklist rápido. As convenções autoritativas aplicadas pela CI estão nestes arquivos:

- [`backend.instructions.md`](../../instructions/backend.instructions.md): controllers, DTOs, validação e tratamento de erros.
- [`modular-monolith.instructions.md`](../../instructions/modular-monolith.instructions.md): limites de módulos e mapeamento de FDTs Adabas para JPA.

## Quando invocar

- "Crie um novo recorte funcional com controller, service e repository."
- "Revise este código Spring Boot quanto à estrutura e às convenções."
- "Configure propriedades e secrets para este serviço."
- "Transforme esta entidade JPA em um endpoint baseado em DTOs."

## Procedimento

### Configuração e estrutura do projeto

- **Ferramenta de build:** use Maven (`pom.xml`) ou Gradle (`build.gradle`) para gerenciar dependências.
- **Starters:** use starters do Spring Boot, como `spring-boot-starter-web` e `spring-boot-starter-data-jpa`.
- **Estrutura de pacotes:** organize por funcionalidade ou domínio, como `com.example.app.order`, não por camada global, como `com.example.app.controller`.

### Injeção de dependência e componentes

- **Injeção por construtor:** use-a em todas as dependências obrigatórias para explicitar dependências e facilitar testes.
- **Imutabilidade:** declare campos de dependência como `private final`.
- **Estereótipos:** use `@Component`, `@Service`, `@Repository`, `@Controller` e `@RestController` conforme a responsabilidade do bean.

### Configuração

- **Configuração externa:** use `application.yml` ou `application.properties`. YAML costuma favorecer estruturas hierárquicas.
- **Propriedades type-safe:** use `@ConfigurationProperties` para vincular configuração a objetos Java fortemente tipados.
- **Profiles:** use Spring Profiles, como `application-dev.yml` e `application-prod.yml`, para configurações específicas de ambiente.
- **Secrets:** nunca grave secrets diretamente. Use variáveis de ambiente localmente e Azure Key Vault com Managed Identity no Azure. Nunca use `application.yml`, `locals` ou código-fonte. Consulte [`security.instructions.md`](../../instructions/security.instructions.md).

### Camada web

- **APIs REST:** use paths `/api/v1/{resource}`, verbos e status corretos, como `201`, `204` e `409`, além de anotações OpenAPI em cada endpoint.
- **DTOs com records:** exponha records do Java 21 nas fronteiras. Nunca retorne entidades JPA ao cliente.
- **Validação:** aplique Bean Validation, como `@Valid`, `@NotBlank`, `@Positive` e `@Size`, no record da request, na fronteira do controller.
- **Tratamento de erros:** centralize erros em um `@RestControllerAdvice` que retorne `ProblemDetail` conforme RFC 7807. Consulte [`backend.instructions.md`](../../instructions/backend.instructions.md).

### Camada de serviço

- **Lógica de negócio:** concentre-a em classes `@Service`.
- **Ausência de estado:** mantenha os serviços stateless.
- **Transações:** use `@Transactional` somente na camada de serviço, nunca em controllers ou repositories. Leituras usam `@Transactional(readOnly = true)`.
- **Sem retornos nulos:** represente ausência com `Optional`. Métodos públicos nunca retornam `null`.
- **Uniões de tipos:** use `sealed interface` com records para estados de domínio discriminados no Java 21.

### Camada de dados

- **Spring Data JPA:** estenda `JpaRepository` ou `CrudRepository` para operações padrão.
- **Consultas personalizadas:** use `@Query` ou JPA Criteria API em consultas complexas.
- **Projections:** use DTO projections para buscar somente os dados necessários.

### Logs

- Use a API SLF4J.
- Declare o logger como `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`.
- Use mensagens parametrizadas, como `logger.info("Processing user {}...", userId);`, em vez de concatenação.

### Testes

- Teste serviços e componentes com JUnit 5 e Mockito. Consulte [`java-junit`](../java-junit/SKILL.md).
- Use `@WebMvcTest`, `@DataJpaTest` e `@SpringBootTest` com Testcontainers e PostgreSQL 16 em testes slice e de integração. Consulte [`spring-boot-testing`](../spring-boot-testing/SKILL.md).

### Segurança

- Use Spring Security para autenticação e autorização com OAuth2/JWT.
- Gere hashes de senhas com um algoritmo forte, como BCrypt.
- Use Spring Data JPA ou JPQL, nunca SQL concatenado, e codifique saídas para evitar XSS. Consulte [`security.instructions.md`](../../instructions/security.instructions.md).

## Modelo de saída

```markdown
## Componente Spring implementado: <tarefa real>
| Ponto de atenção | Implementação baseada em evidências |
|---|---|
| Requisito / módulo | <REQ-ID aprovado e responsabilidade> |
| Controller / DTO | <path real e contrato revisado, se necessário> |
| Validação | <regras da especificação aprovada, sem limites inventados> |
| Serviço / transação | <fronteira real e comportamento de negócio> |
| Repository / mapeamento | <modelo de dados revisado pelo DBA> |
| Testes e build | <comando e resultado reais ou não executado> |
```

Gere Java a partir do design revisado pela equipe e use construtores explícitos. Não copie regras de pagamento, endpoints, valores ou limites de validação do SIFAP a partir de exemplos de sintaxe.

## Gate de qualidade

- [ ] O código está organizado por funcionalidade ou bounded context, e nenhum módulo importa detalhes internos de outro.
- [ ] Dependências usam injeção por construtor com `private final`, sem `@Autowired` em campos.
- [ ] Endpoints usam `/api/v1/{resource}`, status corretos, anotações OpenAPI e DTOs com records.
- [ ] `@Transactional` aparece somente em serviços, e nenhum método público retorna `null`.
- [ ] Erros passam por um `@RestControllerAdvice` como `ProblemDetail`, sem logs de secrets ou dados sensíveis.
- [ ] Testes unitários com Mockito e testes slice relevantes passam.
