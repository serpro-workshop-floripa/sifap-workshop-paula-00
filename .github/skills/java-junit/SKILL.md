---
name: "java-junit"
description: "Use ao escrever ou revisar testes unitários JUnit 5 para lógica de negócio Java. Abrange estrutura Arrange-Act-Assert, ciclo de vida, testes parametrizados, assertions, isolamento com Mockito e organização. Para testes slice ou de integração do Spring Boot, como `@WebMvcTest`, `@DataJpaTest` e Testcontainers, use `spring-boot-testing`."
---
# Boas práticas de JUnit 5

Escreva testes unitários JUnit 5 focados na lógica de negócio do backend SIFAP 2.0, com Java 21 e Spring Boot 3.3. Cubra abordagens padrão e orientadas a dados, com isolamento por Mockito e assertions do AssertJ. Para testes slice ou de integração do Spring Boot, use a skill [`spring-boot-testing`](../spring-boot-testing/SKILL.md). Para o ciclo red-green-refactor, consulte [`tdd-workflow`](../tdd-workflow/SKILL.md).

## Quando invocar

- "Escreva testes JUnit 5 para este serviço."
- "Adicione um teste parametrizado para estes valores-limite."
- "Revise estes testes unitários quanto a isolamento e nomenclatura."
- "Cubra os caminhos de erro deste método de negócio."

## Procedimento

### Configuração do projeto

- Use o layout padrão do Maven ou Gradle e coloque os testes em `src/test/java`.
- `spring-boot-starter-test` já inclui JUnit 5, `junit-jupiter-params`, Mockito e AssertJ na stack do kit. Não adicione outra dependência de testes.
- Execute os testes com `./mvnw test` ou `./gradlew test`.

### Estrutura dos testes

- Nomeie classes de teste com o sufixo `Test`, por exemplo, `CalculatorTest` para `Calculator`.
- Use `@Test` nos métodos de teste.
- Siga o padrão Arrange-Act-Assert (AAA).
- Use nomes descritivos, como `methodName_should_expectedBehavior_when_scenario`.
- Use `@BeforeEach` e `@AfterEach` para setup e teardown por teste.
- Use `@BeforeAll` e `@AfterAll` para setup e teardown por classe. Esses métodos devem ser estáticos.
- Use `@DisplayName` para nomes legíveis de classes e métodos de teste.
- Referencie o requisito testado com um comentário `// REQ-NNN`.

### Testes padrão

- Mantenha cada teste focado em um comportamento.
- Evite verificar várias condições independentes no mesmo método.
- Torne os testes independentes e idempotentes para que executem em qualquer ordem.
- Não crie dependências entre testes.

### Testes orientados a dados

Marque o método com `@ParameterizedTest` em vez de `@Test` e forneça argumentos com uma anotação de origem:

| Origem | Uso |
|--------|-----|
| `@ValueSource` | Um parâmetro com literais simples, como strings, ints e longs |
| `@CsvSource` | Linhas inline de valores separados por vírgula, com vários parâmetros |
| `@CsvFileSource` | Linhas carregadas de um arquivo CSV no classpath |
| `@MethodSource` | Argumentos criados por um factory method que retorna `Stream` ou `Collection` |
| `@EnumSource` | Todas as constantes, ou um subconjunto nomeado, de um enum |

### Assertions

- Prefira `assertThat(...)` do AssertJ para mensagens de falha legíveis.
- Os métodos de `org.junit.jupiter.api.Assertions`, como `assertEquals`, `assertTrue` e `assertNotNull`, também permanecem disponíveis.
- Use `assertThrows` ou `assertThatThrownBy` para verificar exceções.
- Agrupe assertions relacionadas com `assertAll` para executar todas antes da falha do teste.
- Use mensagens descritivas para esclarecer falhas.

### Mocks e isolamento

- Use Mockito para criar mocks das dependências.
- Use `@Mock` e `@InjectMocks` para simplificar criação e injeção.
- Use interfaces para facilitar mocks.

### Organização

- Agrupe testes por funcionalidade ou componente usando pacotes.
- Use `@Tag` para categorizá-los, como `@Tag("fast")` e `@Tag("integration")`.
- Use `@TestMethodOrder(MethodOrderer.OrderAnnotation.class)` e `@Order` somente quando forem indispensáveis.
- Use `@Disabled` para ignorar temporariamente uma classe ou método e sempre informe o motivo.
- Use `@Nested` para agrupar testes relacionados em uma classe interna.

## Modelo de saída

```java
// REQ-042: tax is zero for a tax-exempt customer
@ExtendWith(MockitoExtension.class)
class TaxCalculatorTest {

    @Mock TaxRateProvider rateProvider;
    @InjectMocks TaxCalculator calculator;

    @Test
    @DisplayName("returns zero tax for a tax-exempt customer")
    void returnsZeroForTaxExemptCustomer() {
        // Arrange
        var customer = new Customer(Status.TAX_EXEMPT);
        // Act
        var tax = calculator.taxFor(customer);
        // Assert
        assertThat(tax).isEqualTo(Money.ZERO);
    }

    @ParameterizedTest(name = "income {0} -> tax {1}")
    @CsvSource({ "1000, 100", "2000, 200" })
    void appliesFlatRate(BigDecimal income, BigDecimal expected) {
        when(rateProvider.ratePercent()).thenReturn(new BigDecimal("10"));
        assertThat(calculator.taxFor(income)).isEqualByComparingTo(expected);
    }
}
```

## Gate de qualidade

- [ ] Cada teste verifica um comportamento e executa independentemente dos demais, em qualquer ordem.
- [ ] Os nomes descrevem o comportamento e a classe contém um comentário de rastreabilidade `// REQ-NNN`.
- [ ] Valores-limite e caminhos de erro estão cobertos, não somente o caminho feliz.
- [ ] Mockito isola colaboradores; testes unitários não acessam banco de dados, relógio ou rede reais.
- [ ] As assertions são significativas, como `assertThat`, e não apenas "não lança exceção".
- [ ] `./mvnw test` passa localmente antes da abertura do PR.
