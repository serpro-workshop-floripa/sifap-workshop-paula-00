# Notação EARS

EARS, Easy Approach to Requirements Syntax, restringe requisitos em linguagem natural a uma ordem previsível de cláusulas. Use-a em requisitos normativos funcionais e não funcionais para que um revisor identifique o gatilho, o sistema, a resposta e o alvo de verificação sem inferir comportamentos ocultos.

## Sintaxe genérica

A ordem genérica das cláusulas é:

```text
While <optional precondition>, when <optional trigger>, the <system name> shall <system response>.
```

Nesta skill, mantenha uma resposta observável do sistema por requisito, mesmo que as regras gerais de EARS permitam várias respostas. Requisitos atômicos produzem rastreabilidade, impacto de mudança e resultados de teste mais claros.

## Seis padrões

| Padrão | Modelo canônico | Use quando |
| --- | --- | --- |
| Ubiquitous | `The <system> shall <response>.` | O comportamento ou a restrição de qualidade está sempre ativo. |
| Event-driven | `When <trigger>, the <system> shall <response>.` | Um evento discreto causa uma resposta. |
| State-driven | `While <state>, the <system> shall <response>.` | O comportamento permanece válido durante um estado. |
| Optional | `Where <feature or configuration is present>, the <system> shall <response>.` | O comportamento aplica-se apenas a uma capacidade incluída. |
| Unwanted | `If <undesired condition>, then the <system> shall <mitigation>.` | O sistema precisa detectar, rejeitar, recuperar ou degradar com segurança. |
| Complex | `While <state>, when <trigger>, the <system> shall <response>.` | Uma pré-condição e um evento regem a resposta. |

Um requisito complexo unwanted pode combinar cláusulas:

```text
While <state>, if <undesired condition>, then the <system> shall <mitigation>.
```

Classifique uma declaração como complex somente quando mais de uma palavra-chave EARS for necessária. Não adicione cláusulas apenas para fazer o requisito parecer detalhado.

## Registro do requisito

```markdown
### REQ-NNN: <short title>

- Pattern: <ubiquitous|event-driven|state-driven|optional|unwanted|complex>
- Priority: <P0|P1|P2|P3>
- Status: <proposed|ready-for-review|approved|implemented|verified|retired>
- Source: <optional supplementary SRC-NNN>
source_legacy: <actual supported source path or [GREENFIELD] with justification>
- Rationale: <why this behavior is needed>

> <Canonical EARS statement.>

**Acceptance signals**
- AC-REQ-NNN-NN: <observable pass/fail outcome>

**Verification**
- <test|inspection|analysis|measurement>: <planned evidence>
```

Requisitos não funcionais também usam `REQ-NNN`; registre sua categoria separadamente.
Seu sinal de aceitação também define o envelope de medição. Siga o
[vínculo com o kit](../SKILL.md#vínculo-com-este-kit-do-participante) e preserve os IDs existentes.

## Regras de escrita

1. Nomeie um sistema ou componente concreto como sujeito. Evite pronomes como "it".
2. Use `shall` na resposta normativa. Evite `should`, `may`, `could`, `would` e o `will` preditivo.
3. Escreva uma resposta por requisito. Separe conjunções ocultas, como "validate and notify".
4. Torne a resposta externamente observável ou objetivamente inspecionável.
5. Mantenha escolhas de implementação fora dos requisitos funcionais.
6. Declare pré-condições e gatilhos explicitamente e na ordem canônica.
7. Defina termos de modo consistente. Vincule termos de domínio ambíguos a um glossário ou definição de dados.
8. Dê a cada requisito ID estável, fonte, justificativa, prioridade, sinal de aceitação, método de verificação e status do ciclo de vida.
9. Use uma meta numérica somente quando ela vier de evidências ou de um responsável.
10. Registre comportamentos de erro, timeout, entrada inválida, falha de dependência e recuperação com padrões unwanted ou complex, quando aplicável.

## Método de classificação

1. Se o comportamento estiver sempre ativo, use ubiquitous.
2. Se um evento discreto iniciar o comportamento, use event-driven.
3. Se o comportamento permanecer válido enquanto um estado for verdadeiro, use state-driven.
4. Se o comportamento existir apenas com uma funcionalidade ou configuração selecionada, use optional.
5. Se a condição for indesejada e exigir mitigação, use unwanted.
6. Se duas cláusulas necessárias regerem o comportamento, use complex.

Registre exatamente uma classificação para cada requisito, inclusive variantes complexas.

## Exemplos

Estas ilustrações genéricas de sintaxe não são requisitos do SIFAP, evidências de fonte,
decisões aceitas nem soluções dos exercícios do participante.

- Ubiquitous: `The audit service shall record the actor, action, target, outcome, and timestamp for each privileged operation.`
- Event-driven: `When a user submits valid credentials, the identity service shall create an authenticated session.`
- State-driven: `While an order is awaiting payment confirmation, the order service shall prevent shipment creation.`
- Optional: `Where single sign-on is enabled, the identity service shall redirect unauthenticated users to the configured identity provider.`
- Unwanted: `If an uploaded file exceeds the approved size limit, then the upload service shall reject the file and identify the violated limit.`
- Complex: `While an account is locked, when a login attempt occurs, the identity service shall deny authentication without validating the submitted password.`

## Defeitos comuns

| Defeito | Exemplo ruim | Correção |
| --- | --- | --- |
| Qualidade vaga | "The system shall be fast." | Defina uma métrica e um envelope de medição com fonte ou mantenha um bloqueio explícito. |
| Resposta composta | "The system shall validate the order and email the user." | Separe validação e notificação em requisitos distintos. |
| Comportamento passivo | "Authentication shall be supported." | Nomeie o sistema e a resposta de autenticação observável. |
| Condição oculta | "The system shall show an error." | Declare o evento ou a condição indesejada que causa o erro. |
| Vazamento de implementação | "The system shall store sessions in Redis." | Declare o comportamento de sessão exigido; mova uma restrição tecnológica com fonte para o NFRD. |
| Limite sem responsável | "The API shall respond in 500 ms." | Cite evidências da carga de trabalho ou um SLO aprovado pelo responsável. |
| Declaração sem rastreabilidade | Uma frase correta sem ID ou fonte | Adicione os metadados do registro do requisito e o mapeamento da fonte. |

## Referências

- Alistair Mavin, [visão geral de EARS e definições dos padrões](https://alistairmavin.com/ears/), revisado em 2026-08-25.
- A. Mavin, P. Wilkinson, A. Harwood, and M. Novak, "Easy Approach to Requirements Syntax (EARS)," *17th IEEE International Requirements Engineering Conference*, 2009, pp. 317-322, [doi:10.1109/RE.2009.9](https://doi.org/10.1109/RE.2009.9).
- University of Manchester Research Explorer, [registro bibliográfico de "Easy Approach to Requirements Syntax (EARS)"](https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/), revisado em 2026-08-25.
