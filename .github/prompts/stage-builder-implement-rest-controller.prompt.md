---
name: "implement-rest-controller"
description: "Implementa um controller REST Spring a partir da definição de um endpoint OpenAPI e o conecta aos serviços do bounded context."
argument-hint: "endpoint=\"<METHOD /api/v1/resource>\" context=<context> service=<Service>"
agent: "builder"
tools: ["read", "search", "edit", "execute"]
---
# /implement-rest-controller

## Objetivo

Gerar um controller REST Spring Boot a partir da definição de um endpoint OpenAPI. O controller é um adaptador fino: valida a entrada, delega a um serviço e retorna a resposta. Ele não contém lógica de negócio.

## Quando invocar

Depois que a camada de serviço de um bounded context existir, quando a equipe estiver pronta para expô-la como uma API REST.

## Pré-condições

- A definição OpenAPI criada pela equipe contém o endpoint
- A classe de serviço do bounded context (ou sua interface) existe
- Os DTOs de request/response estão definidos (ou serão gerados como records)

## Inputs que a equipe deve fornecer

- O endpoint a implementar (método + path da definição OpenAPI)
- O bounded context e o package de destino
- A classe de serviço à qual delegar

## O que farei

- Ler a definição OpenAPI do endpoint especificado
- Gerar uma classe `@RestController` com as annotations apropriadas
- Criar DTOs record de request/response com Jakarta Bean Validation
- Conectar o controller ao serviço por meio de constructor injection
- Adicionar tratamento de erros com `@ControllerAdvice` se ainda não existir
- Executar um build para verificar a compilação

## O que NÃO farei

- Colocar lógica de negócio no controller — ele delega à camada de serviço
- Ignorar a validação de entrada — todo endpoint tem `@Valid` em seu request body
- Usar field injection com `@Autowired` — usar apenas constructor injection
- Colocar mensagens de erro diretamente no código — usar respostas RFC 7807 `ProblemDetail`
- Fabricar comportamento de endpoint não definido na especificação OpenAPI

## Formato de saída

Arquivos Java:

1. Controller em `src/main/java/[package]/api/[Name]Controller.java`
2. DTOs de request/response em `src/main/java/[package]/api/dto/[Name]Request.java` e `[Name]Response.java`
3. Handler global de exceções em `src/main/java/[package]/shared/exception/GlobalExceptionHandler.java` (se não existir)

## Definição de pronto

- [ ] O controller compila sem erros
- [ ] O `operationId` da OpenAPI é referenciado no Javadoc
- [ ] O DTO de request tem annotations Jakarta Bean Validation (`@NotNull`, `@Size` etc.)
- [ ] A resposta usa os HTTP status codes corretos (201 para POST, 200 para GET, 204 para DELETE)
- [ ] O corpo do controller não contém lógica de negócio — apenas validação, delegação e mapeamento da resposta
- [ ] As respostas de erro usam RFC 7807 `ProblemDetail`
- [ ] Os REQ-IDs relacionados estão documentados no Javadoc

## Corpo do prompt

Você é o `@builder`. A equipe precisa de um controller REST para um endpoint definido na especificação OpenAPI.

**Passo 1 — Leia a definição OpenAPI.**
Abra a definição OpenAPI identificada pela equipe. Encontre o endpoint especificado. Extraia:

- Método HTTP e path
- Operation ID e resumo
- Schema do request body (se houver)
- Schema da resposta
- Parâmetros de path/query
- REQ-IDs relacionados (da descrição ou das tags)

**Passo 2 — Gere os records de request/response.**
Crie records Java para a request e a response:

```java
public record [RequestName](
    @NotNull [FieldType] [requiredField],
    @Size(max = [maxLength]) String [optionalTextField]
) {}

public record [ResponseName](
    [FieldType] [field]
) {}
```

Use annotations Jakarta Bean Validation com base nos tipos dos campos e em quaisquer constraints do schema OpenAPI.

**Passo 3 — Gere o controller.**
Crie a classe do controller:

```java
@RestController
@RequestMapping("/api/v1/[context]")
@Tag(name = "[Context]", description = "[de OpenAPI]")
public class [Name]Controller {

    private final [Service] service;

    public [Name]Controller([Service] service) {
        this.service = service;
    }

    /**
    * [OpenAPI operation summary].
     *
     * <p>OpenAPI operationId: {@code [operationId]}</p>
    * <p>Implements: REQ-NNN</p>
     */
    @PostMapping  // or @GetMapping, etc.
    @Operation(summary = "[summary]", operationId = "[operationId]")
    public ResponseEntity<[Response]> [methodName](@Valid @RequestBody [Request] request) {
        var result = service.[method](/* map request to domain */);
        return ResponseEntity.status(HttpStatus.CREATED).body(/* map domain to response */);
    }
}
```

**Passo 4 — Garanta que exista tratamento de erros.**
Verifique se `GlobalExceptionHandler` existe no package compartilhado. Caso contrário, gere-o com handlers para:

- `MethodArgumentNotValidException` → 400 com detalhes da validação
- `EntityNotFoundException` → 404
- `IllegalStateException` → 409 (conflito)
- `Exception` → 500 (catch-all com uma mensagem de erro segura e sem stack trace exposta)

Todas as respostas de erro usam `ProblemDetail` (RFC 7807).

**Passo 5 — Verifique a compilação.**
Execute `mvn compile` (ou o comando de build equivalente). Relate e corrija quaisquer erros.

Se a interface de serviço ainda não existir, gere uma interface mínima com a assinatura de método exigida e uma implementação TODO. A equipe preencherá a lógica.

## Exemplo de invocação

```
/implement-rest-controller endpoint="<METHOD /api/v1/resource>" context=<context> service=<Service>
```
