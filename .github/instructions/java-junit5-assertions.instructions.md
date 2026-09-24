---
description: "Use ao escrever ou revisar assertions JUnit 5 em testes Java do backend: ordem expected/actual, mensagens lazy, assertAll, exceções, timeouts e assertInstanceOf."
applyTo: "**/*Test.java,**/*IT.java,**/*Steps.java,**/*StepDefs.java"
---

# Assertions JUnit 5 — Convenções do Jupiter

Este arquivo orienta o uso de `org.junit.jupiter.api.Assertions` em Java 21. Estratégia, slices, mocks e cobertura estão nas skills `java-junit`, `spring-boot-testing` e em [`tests.instructions.md`](tests.instructions.md).

> [!NOTE]
> Para chains fluentes e objetos complexos, prefira AssertJ. Use as assertions Jupiter para agrupamento, exceções, timeouts, tipos exatos e igualdade simples.

## Imports estáticos

Importe assertions estaticamente e sempre de `org.junit.jupiter.api.Assertions`. Nunca misture `org.junit.Assert` do JUnit 4.

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertAll;
```

## Expected antes de actual

Em `assertEquals`, `expected` é o primeiro argumento e `actual` o segundo.

```java
assertEquals(2, resourceService.count());
assertEquals(0.3, 0.1 + 0.2, 1e-9);
```

> [!WARNING]
> `BigDecimal.equals` considera scale. Compare valores monetários com `compareTo` ou AssertJ `isEqualByComparingTo`.

## Mensagens de falha

Use `Supplier<String>` para mensagens caras, de modo que sejam construídas apenas na falha. Literais constantes podem usar `String`.

```java
assertEquals(expected, actual,
    () -> "expected %s but got %s".formatted(expected, actual));
```

## Agrupamento com assertAll

Use `assertAll` para várias propriedades de um resultado. Todas as assertions executam, mesmo se uma falhar.

```java
assertAll("payment view",
    () -> assertEquals("ACME LTDA", view.beneficiary()),
    () -> assertEquals(0, new BigDecimal("1500.00").compareTo(view.amount())),
    () -> assertEquals(PaymentStatus.APPROVED, view.status())
);
```

## Exceções

`assertThrows` aceita subclasses e retorna a exceção. Use `assertThrowsExactly` quando a classe exata fizer parte do contrato.

```java
ResourceConflictException ex = assertThrows(
    ResourceConflictException.class,
    () -> resourceService.create(request));
assertEquals("alpha", ex.conflictingLabel());
```

Use `assertDoesNotThrow` apenas quando a ausência de exceção for o contrato.

## Timeouts

Use `assertTimeout` sem interromper o trabalho. Use `assertTimeoutPreemptively` apenas quando precisar abortar.

> [!WARNING]
> `assertTimeoutPreemptively` executa em outra thread. `ThreadLocal`, `EntityManager` transacional e contexto de segurança não são propagados.

## Verificação de tipos

Prefira `assertInstanceOf` a `assertTrue(x instanceof T)`, pois retorna o valor convertido e produz mensagem melhor.

## Coleções e arrays

Use `assertIterableEquals` e `assertArrayEquals` para obter diffs por elemento.

## Convenções

| Regra | Motivo |
|---|---|
| `expected` antes de `actual` | Produz mensagem de falha correta |
| Compare `BigDecimal` por valor | `equals` considera scale |
| Use `Supplier<String>` para mensagens caras | Evita trabalho quando o teste passa |
| Agrupe checks com `assertAll` | Relata todas as diferenças |
| Escolha deliberadamente entre `assertThrows` e `assertThrowsExactly` | Reflete o contrato de tipo |
| Use apenas imports Jupiter | Evita ordens de argumentos incompatíveis |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Coloque `expected` antes de `actual` | Inverta-os |
| Compare dinheiro com `compareTo` | Use `BigDecimal.equals` |
| Use `assertEquals` para valores | Use `assertTrue(result == 2)` |
| Verifique o valor real | Pare em `assertNotNull` |
| Mantenha timeout preemptivo fora de código transacional | Perda o contexto da thread |
| Deixe assertions falharem claramente | Capture `AssertionError` |

## Checklist antes de abrir um PR

- [ ] Cada `assertEquals` usa `expected` antes de `actual`.
- [ ] Valores monetários são comparados por valor.
- [ ] Checks de várias propriedades usam `assertAll`.
- [ ] Testes de exceção escolhem a assertion adequada e verificam a exceção retornada.
- [ ] `assertTimeoutPreemptively` não envolve código transacional.
- [ ] Imports são apenas Jupiter.
- [ ] Testes de requisitos mantêm comentário `// REQ-NNN`.
