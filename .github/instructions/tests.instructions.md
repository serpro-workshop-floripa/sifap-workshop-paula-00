---
description: "Use ao criar ou revisar testes automatizados, estratégia, lacunas de cobertura, regressões e gates de qualidade em qualquer stack."
applyTo: "**/*.test.*,**/*.spec.*,**/test_*.py,**/*_test.*,**/*Test.java,**/*Tests.cs,**/tests/**,**/test/**,**/__tests__/**"
---

# Convenções de testes — Estrutura, rastreabilidade e cobertura

Este arquivo se aplica a testes de backend e frontend. Ele orienta estrutura, nomenclatura, ferramentas, rastreabilidade por REQ-ID e cobertura. Escreva testes durante a implementação. Detalhes de assertions JUnit estão em [java-junit5-assertions.instructions.md](java-junit5-assertions.instructions.md).

## Pirâmide de testes

| Camada | O que comprova | Proporção |
|---|---|---|
| Unitário | Regras de negócio sem I/O | Maior |
| Integração | Comportamento com dependências reais ou renderização | Menor |
| End to end | Fluxo crítico do usuário | Poucos |

## Ferramentas de referência

| Stack | Unitário | Integração | E2E |
|---|---|---|---|
| JavaScript/TypeScript | `node:test`, Vitest ou Jest | Supertest, Testcontainers | Playwright |
| Frontend | Vitest + Testing Library | Testing Library + MSW | Playwright |
| Java | JUnit 5 + AssertJ | Testcontainers | Playwright |
| Python | pytest | pytest + Testcontainers | Playwright |
| .NET | xUnit ou NUnit | Testcontainers | Playwright |

Adote apenas ferramentas já usadas pelo projeto ou aprovadas em ADR.

## Estrutura Arrange-Act-Assert

Cada teste tem três fases visíveis e verifica um comportamento. Mocke apenas fronteiras externas, nunca a classe ou função testada.

```ts
describe('calculateTotal', () => {
  it('should_apply_discount_when_coupon_is_valid', () => { // REQ-002
    const items = [{ price: 100 }, { price: 50 }];            // Arrange
    const total = calculateTotal(items, { coupon: 'OFF10' }); // Act
    expect(total).toBe(135);                                  // Assert
  });
});
```

## Nomenclatura

Use `should_<expected behavior>_when_<condition>` ou intenção equivalente em `it(...)` ou `@DisplayName`. Mantenha um idioma por projeto.

## Dependências reais e test doubles

- Quando o comportamento dos dados importar, use a dependência real em container.
- Use doubles apenas para collaborators lentos, não determinísticos ou inexistentes.
- Não mocke tipos externos diretamente; envolva-os em uma abstração fina.

## Frontend

Consulte elementos por role ou label, nunca por `data-testid` quando houver role. Use `user-event` e evite testes apenas de snapshot.

## Rastreabilidade e TDD

Cada teste que verifica requisito cita o ID na mesma linha ou logo acima: `// REQ-NNN` ou `# NFR-NNN`.

Para cada regra de negócio, a tarefa RED executa primeiro e falha pela ausência do comportamento. `python3 .github/scripts/validate-red-phase.py -- <test command>` comprova a falha antes da tarefa GREEN.

## Metas de cobertura

Use os limites definidos pelo projeto. Sem limite, proponha e registre uma decisão. Configure a ferramenta para falhar abaixo do mínimo.

> [!NOTE]
> Cobertura é piso, não objetivo. Uma branch sem assertion permanece sem teste mesmo quando a linha aparece coberta.

## Convenções

| Regra | Motivo |
|---|---|
| Arrange-Act-Assert e um comportamento por teste | Facilita leitura e diagnóstico |
| Mock apenas em fronteiras externas | Dependências reais encontram bugs reais |
| Nomes `should_<behavior>_when_<condition>` | Expõem intenção no relatório |
| Comentário `REQ-NNN` ou `NFR-NNN` | Mantém rastreabilidade viva |
| RED comprovado antes de GREEN | Um teste que nunca falhou não comprova nada |
| Testes escritos durante a implementação | Código sem teste não está integrado |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Use dependência real em container quando os dados importarem | Troque banco real por substituto com outra semântica |
| Consulte elementos por role ou label | Use `data-testid` quando houver role |
| Verifique comportamento e edge cases | Confie apenas em snapshots ou cobertura de linhas |
| Escreva teste junto com o código | Adicione testes depois da funcionalidade pronta |
| Enfraqueça teste apenas com issue e justificativa | Pule teste para deixar a pipeline verde |

## Checklist antes de abrir um PR

- [ ] Novo comportamento tem teste unitário; persistência tem integração real quando aplicável.
- [ ] Testes seguem Arrange-Act-Assert e a convenção de nomes.
- [ ] Testes de requisitos citam `REQ-NNN` ou `NFR-NNN`.
- [ ] Regras cobrem sucesso, validação e autorização quando aplicável.
- [ ] A cobertura atende ao mínimo.
- [ ] Apenas fronteiras externas usam mocks.
