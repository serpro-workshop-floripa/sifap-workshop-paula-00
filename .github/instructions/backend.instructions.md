---
description: "Use ao implementar APIs, serviços, controllers, validação de requests, tratamento de erros e fronteiras de serviços de negócio no backend."
applyTo: "backend/src/main/java/**,backend/src/test/java/**"
---

# Convenções de backend — Controllers, serviços e validação

Este arquivo se aplica a fontes e testes Java em `backend/`. Ele orienta controllers, DTOs, serviços, validação de requests e respostas de erro em Java 21 + Spring Boot 3.3. Limites de módulos e mapeamento JPA/FDT pertencem a [`modular-monolith.instructions.md`](modular-monolith.instructions.md). Autenticação pertence a [`security.instructions.md`](security.instructions.md).

> [!NOTE]
> `backend/` ainda não existe. A equipe o cria do zero na Etapa 3. Aplique estas convenções desde o primeiro código.

## Camadas e fronteiras

As requests percorrem a fronteira aprovada do módulo: controller, application service, comportamento de domínio e interface/adapter de repositório. Mantenha controllers finos e invariantes de domínio fora de HTTP e persistência.

- Use `@Transactional` apenas na camada de serviço. Leituras usam `@Transactional(readOnly = true)`.
- Métodos públicos nunca retornam `null`; represente ausência com `Optional`.
- Mantenha internals privados quando a visibilidade Java permitir. Exponha a outros módulos apenas a interface aprovada e teste essa fronteira.

## Controllers e endpoints REST

Use `/api/v1/{resource}`, com resource no plural e kebab-case quando tiver mais de uma palavra. Cada endpoint inclui anotações OpenAPI e retorna o status correto: `201` ao criar, `204` ao excluir, `409` em conflito e `PATCH` em atualizações parciais.

```java
@RestController
@RequestMapping("/api/v1/resources")
class ResourceController {

    private final ResourceService resourceService;

    ResourceController(ResourceService resourceService) {
        this.resourceService = resourceService;
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(summary = "Register a resource")
    @ApiResponse(responseCode = "201", description = "Created")
    @ApiResponse(responseCode = "409", description = "Duplicate resource")
    ResourceResponse create(@Valid @RequestBody CreateResourceRequest request) {
        return resourceService.create(request);
    }
}
```

## DTOs e validação

Exponha DTOs como `record` do Java 21, nunca entidades JPA. Valide o record da request na fronteira do controller com Bean Validation.

```java
public record CreateResourceRequest(
    @NotBlank @Size(max = 120) String label,
    @NotNull @Positive BigDecimal amount) {}
```

## Camada de serviço

O serviço coordena a transação, aplica invariantes e converte resultados de persistência em DTOs.

```java
@Service
class ResourceService {

    private final ResourceRepository resourceRepository;

    ResourceService(ResourceRepository resourceRepository) {
        this.resourceRepository = resourceRepository;
    }

    @Transactional(readOnly = true)
    ResourceResponse getById(UUID id) {
        return resourceRepository.findById(id)
            .map(ResourceResponse::from)
            .orElseThrow(() -> new ResourceNotFoundException(id));
    }
}
```

## Tratamento de erros

Retorne `ProblemDetail` RFC 7807 por um único `@RestControllerAdvice`. Mapeie falhas de validação para `400` e inclua um correlation ID para relacionar logs e respostas.

```java
@RestControllerAdvice
class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    ProblemDetail handleNotFound(ResourceNotFoundException ex) {
        return problem(HttpStatus.NOT_FOUND, "Resource not found");
    }

    private ProblemDetail problem(HttpStatus status, String detail) {
        ProblemDetail body = ProblemDetail.forStatusAndDetail(status, detail);
        body.setProperty("correlationId", MDC.get("correlationId"));
        return body;
    }
}
```

## Logs e dados sensíveis

> [!WARNING]
> Nunca registre CPF, valores de benefícios, tokens ou outros dados sensíveis. Registre identificadores e o correlation ID. Mascare campos regulados antes de chegarem a logs ou mensagens de erro.

```java
log.info("payment processed correlationId={} resourceId={}", correlationId, id);
```

## Convenções

| Regra | Motivo |
|---|---|
| Controllers em `PascalCase`; rotas em `/api/v1/{resource}` | Mantém a superfície HTTP previsível e versionada |
| `@Transactional` apenas em serviços | Preserva fronteiras explícitas de efeitos colaterais |
| Records para DTOs | Cria contratos imutáveis |
| `@Valid` + Bean Validation no controller | Rejeita input inválido antes da lógica de negócio |
| `Optional` para resultados ausentes | Evita `NullPointerException` em APIs públicas |
| `ProblemDetail` para erros | Padroniza o formato legível por máquina |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Retorne `201`, `204` e `409` quando aplicável | Retorne `200` para todo resultado |
| Lance exceções de domínio mapeadas no advice | Exponha stack traces ou erros `Map<String,Object>` |
| Injete dependências pelo construtor | Use `@Autowired` em campos |
| Mascare CPF e valores nos logs | Registre entidades, request bodies ou tokens |

## Checklist antes de abrir um PR

- [ ] Cada endpoint usa `/api/v1/{resource}`, verbo e status corretos.
- [ ] Cada endpoint tem anotações OpenAPI e request `record` validada.
- [ ] `@Transactional` aparece apenas em serviços e nenhum método público retorna `null`.
- [ ] Erros passam pelo `@RestControllerAdvice` como `ProblemDetail` com correlation ID.
- [ ] Dados sensíveis não aparecem em logs nem payloads de erro.
- [ ] Testes cobrem sucesso, falha de validação e falha de autorização.
