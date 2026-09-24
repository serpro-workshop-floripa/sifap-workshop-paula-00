---
name: "java-docs"
description: "Use ao escrever, revisar ou melhorar Javadoc e documentação de API em código Java. Aplique boas práticas para sentenças de resumo, `@param`, `@return`, `@throws`, blocos `{@code}`, `@since`, records e documentação herdada."
---
# Documentação Java com Javadoc

Escreva e revise Javadoc para o backend SIFAP 2.0, com Java 21 e Spring Boot 3.3, para que membros públicos e protegidos tenham contratos corretos e consistentes. Esta skill define as convenções de Javadoc. Ela documenta o comportamento, não decide o design do código e nunca inclui valores regulados reais, como CPF ou valores de benefícios, nos exemplos.

## Quando invocar

- "Escreva Javadoc para esta classe de serviço."
- "Revise o Javadoc deste pacote e corrija o que falta."
- "Documente a API pública deste módulo antes da publicação."
- "Adicione `@param`, `@return` e `@throws` a estes métodos."

## Procedimento

### O que documentar

| Visibilidade | Regra |
|--------------|-------|
| `public`, `protected` | Javadoc é obrigatório, pois esses membros formam o contrato da API |
| package-private | Documente quando o nome não revelar a intenção |
| `private` | Documente somente lógica realmente complexa; prefira código claro a comentários |

> [!NOTE]
> Documente o contrato no qual a pessoa que chama o código pode confiar, não a implementação. Nunca inclua CPF, valor de benefício, token ou outro dado sensível real em exemplos de Javadoc. Use placeholders claramente fictícios.

### Sentença de resumo

- A primeira frase é o resumo. Ela termina com ponto e usa uma locução verbal curta, como "Retorna..." ou "Registra...".
- Comece resumos de métodos com verbo na terceira pessoa, como "Calcula o imposto...", não com "Este método...".
- Mantenha o resumo centrado no contrato e mova detalhes para os parágrafos seguintes.

### Tags de bloco

| Tag | Quando usar | Regra de formato |
|-----|-------------|------------------|
| `@param name` | Cada parâmetro de método ou construtor | Descrição começa em minúscula e não termina com ponto |
| `@param <T>` | Cada parâmetro de tipo genérico | Mesma regra: minúscula e sem ponto final |
| `@return` | Cada método que retorna valor, exceto `void` | Descreva o valor e a semântica de `Optional` |
| `@throws` / `@exception` | Cada exceção verificada e cada exceção não verificada documentada | Declare a condição que a provoca |
| `@see` | Referências a tipos ou membros relacionados | Crie o link, sem repetir o conteúdo |
| `@since` | Quando o membro foi introduzido | Use a versão do projeto ou módulo |
| `@deprecated` | Membro programado para remoção | Indique o substituto e adicione `@Deprecated` ao código |

Inclua `@author` e `@version` somente quando a convenção da equipe exigir. Muitos guias omitem `@author` e usam o histórico do controle de versão.

> [!WARNING]
> Ordene as tags assim: `@param`, na ordem da declaração, depois `@return` e `@throws`. Um `@param` ausente ou fora de ordem é um defeito comum em revisões de Javadoc.

### Tags inline e código

- Use `{@code ...}` em identificadores, palavras-chave e literais inline, como `{@code null}` e `{@code Optional.empty()}`.
- Use `{@link Type#member}` para vincular outro elemento e `{@linkplain ...}` quando quiser texto simples no link.
- Use `<pre>{@code ... }</pre>` em exemplos de várias linhas para renderizar generics e sinais de maior ou menor literalmente.
- Use `{@inheritDoc}` para herdar o contrato do supertipo, mas documente novamente qualquer comportamento que seja diferente.

### Records do Java 21

Coloque o Javadoc de um record no tipo e documente cada componente com `@param`. Não crie métodos accessors somente para anexar Javadoc.

## Modelo de saída

```java
/**
 * Performs the behavior defined by the reviewed method contract.
 *
 * @param request the validated creation request; must not be {@code null}
 * @return the persisted resource as a response DTO
 * @throws ResourceConflictException when the reviewed conflict condition holds
 * @since 1.0.0
 * @see ResourceService#getById(java.util.UUID)
 */
ResourceResponse create(CreateResourceRequest request);

/**
 * Immutable request for the reviewed operation.
 *
 * @param label the value defined by the reviewed contract
 * @param amount the exact amount whose semantics and bounds come from the specification
 */
public record CreateResourceRequest(String label, BigDecimal amount) {}
```

O exemplo define o formato da documentação, não um contrato de negócio do SIFAP. Substitua tipos e condições genéricos pelo código inspecionado e pelos requisitos revisados. Não invente unicidade, positividade, limites de tamanho, existência de métodos nem sucesso na geração.

## Gate de qualidade

- [ ] Cada membro público e protegido tem uma sentença de resumo em Javadoc terminada com ponto.
- [ ] Cada parâmetro, inclusive parâmetros de tipo `<T>`, tem `@param`; cada método diferente de `void` tem `@return`.
- [ ] Cada exceção documentada tem `@throws` com a condição que a provoca.
- [ ] `{@code}` e `{@link}` envolvem identificadores, e as tags de bloco estão na ordem correta.
- [ ] Nenhum exemplo contém CPF, valor de benefício ou outro dado sensível real.
- [ ] `mvn javadoc:javadoc`, ou a tarefa `javadoc` do Gradle, termina sem avisos.
