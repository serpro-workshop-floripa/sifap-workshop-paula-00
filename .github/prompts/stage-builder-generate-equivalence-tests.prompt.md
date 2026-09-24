---
name: "generate-equivalence-tests"
description: "Gera testes JUnit que validam se a implementação Java moderna produz as mesmas saídas que o programa Natural original para as mesmas entradas."
argument-hint: "class=<java.package>.<Service> method=<method>"
agent: "builder"
tools: ["read", "search", "edit", "execute"]
---
# /generate-equivalence-tests

## Objetivo

Gerar testes parametrizados JUnit 5 que verifiquem se um método Java traduzido produz resultados de negócio equivalentes aos do programa Natural original para as mesmas entradas.

## Quando invocar

Antes de implementar o comportamento Java selecionado, usando a evidência
legada revisada e o requisito. Execute novamente durante a tradução e após alterações.

## Pré-condições

- O comportamento-alvo e a superfície de teste estão definidos; um esqueleto mínimo compilável pode existir, mas os testes precedem sua implementação
- O código-fonte Natural original está acessível em `01-archaeology/legacy-sifap/`
- O requisito e o método Java planejado referenciam arquivos-fonte e intervalos reais

## Inputs que a equipe deve fornecer

- A classe e o método Java a testar
- O path do arquivo Natural original (geralmente encontrado no Javadoc do método)
- Quaisquer dados de teste ou casos-limite conhecidos pela análise da Etapa 1 da equipe

## O que farei

- Ler o programa Natural original para identificar parâmetros de entrada e saídas esperadas
- Identificar cada branch (IF/ELSE, DECIDE) para determinar os casos de teste
- Gerar testes parametrizados JUnit 5 que cubram o happy path, branches, limites e valores nulos
- Executar os testes e relatar os resultados
- Listar qualquer branch não coberto

## O que NÃO farei

- Marcar um método como "equivalente" sem pelo menos um teste por branch identificado
- Ignorar condições de limite para entradas numéricas
- Fabricar valores esperados — todo valor esperado deve ser derivável da lógica do código Natural
- Ignorar paths de erro — branches de rejeição e erro também recebem testes

## Formato de saída

Arquivo de teste em `src/test/java/.../[ClassName]EquivalenceTest.java`

Use o package real em `backend/src/test/java/`. Classifique a evidência como
caracterização derivada do código-fonte ou comparação em runtime; raciocínio
estático e testes gerados a partir dele não comprovam que o Natural foi executado
com saídas idênticas.

## Definição de pronto

- [ ] Os testes cobrem os branches exigidos pelo recorte aprovado; valores esperados desconhecidos permanecem como bloqueios, em vez de assertions presumidas
- [ ] Os testes parametrizados cobrem: happy path, cada branch, valores-limite e entradas nulas/vazias
- [ ] Os testes compilam e executam
- [ ] Os resultados de aprovação/falha são relatados com a cobertura de branches
- [ ] Os testes com falha identificam qual branch divergiu da lógica Natural

## Corpo do prompt

Você é o `@builder`. A equipe está traduzindo um recorte legado revisado e
precisa de testes de caracterização antes da implementação.

**Passo 1 — Localize o código-fonte Natural.**
Leia o requisito aplicável e a referência de código-fonte do método; depois, abra
o intervalo Natural real e os callers/definições de dados necessários. Revise os
valores esperados de forma independente; não derive o oráculo de teste da nova implementação.

**Passo 2 — Identifique os branches no código Natural.**
Para o intervalo de linhas referenciado, liste cada branch condicional:

- Cada `IF...THEN...ELSE` cria 2+ paths
- Cada valor de `DECIDE ON` cria N paths
- Cada `AT BREAK` cria um path de control break

Para cada branch, registre:

- A condição (o que aciona esse path)
- A ação/saída esperada
- Os valores de entrada que acionariam esse path (derivados da condição)

**Passo 3 — Derive os casos de teste.**
Para cada branch, crie pelo menos um caso de teste:

```java
@ParameterizedTest
@CsvSource({
    "input1, input2, expectedOutput",  // Branch 1: [description]
    "input3, input4, expectedOutput",  // Branch 2: [description]
})
void should_produce_equivalent_output(Type param1, Type param2, Type expected) {
    // Arrange
    var service = new ServiceUnderTest(/* dependencies */);
    // Act
    var result = service.methodUnderTest(param1, param2);
    // Assert
    assertThat(result).isEqualTo(expected);
}
```

Adicione mais testes para:

- **Valores-limite**: mínimo/máximo para campos numéricos, strings vazias e strings de um único caractere
- **Entradas nulas/vazias**: o que acontece quando parâmetros opcionais são nulos?
- **Precisão de packed decimal**: verifique se os cálculos com `BigDecimal` correspondem à aritmética de packed decimal do Natural

**Passo 4 — Trate casos-limite.**
Se o código Natural tiver um branch que dependa do estado dos dados (por exemplo, "se o registro existir"), gere testes separados com respostas mockadas do repositório:

- O registro existe → comportamento esperado
- O registro não existe → erro/alternativa esperada

**Passo 5 — Execute os testes.**
Execute a suíte de testes usando a ferramenta `runTests`. Relate:

- Total de testes: N
- Aprovados: N
- Falharam: N (com detalhes de cada falha)
- Estimativa de cobertura de branches (branches com testes / total de branches identificados)

**Passo 6 — Registre a verificação não resolvida.**
Se o comportamento esperado de um branch for desconhecido, registre a fonte e o
bloqueio em `tasks.md` e no registro de mistérios da equipe. Não adicione um teste
desabilitado ou que sempre passa para fazer a suíte parecer completa. O requisito
afetado permanece não verificado até que sua expectativa seja revisada; trabalho
verificado não relacionado pode continuar.

## Exemplo de invocação

```
/generate-equivalence-tests class=<java.package>.<Service> method=<method>
```
