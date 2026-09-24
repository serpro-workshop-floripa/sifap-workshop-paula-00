---
name: "security-self-review"
description: "Checklist de autorrevisão de segurança e de problemas do OWASP Top 10 em uma funcionalidade recém-construída."
argument-hint: "context=<context> files=<Controller>.java,<Service>.java,<Entity>.java"
agent: "builder"
tools: ["read", "search", "edit"]
---
# /security-self-review

## Objetivo

Examinar uma funcionalidade recém-construída em busca de problemas comuns de segurança alinhados ao OWASP Top 10. A saída é um relatório priorizado — o agent não corrige problemas automaticamente; a equipe decide.

## Quando invocar

Depois que um bounded context tiver sido implementado (entities, services, controllers, testes) e antes do checkpoint C3 e do PR de submissão.

## Pré-condições

- O código da funcionalidade existe e compila
- A equipe especifica quais controllers, services e entities devem ser revisados

## Inputs que a equipe deve fornecer

- O escopo da funcionalidade: quais classes de controller, service e entity revisar
- O nome do bounded context

## O que farei

- Procurar secrets diretamente no código (strings semelhantes a chaves, senhas ou tokens)
- Verificar vetores de SQL injection (concatenação de strings em queries)
- Verificar annotations de authentication/authorization nos endpoints
- Verificar a cobertura de validação de entrada
- Procurar dados sensíveis em logs ou respostas de erro
- Identificar rate limits ausentes em endpoints de escrita
- Sinalizar áreas de dependências em que uma análise de segurança real deve ser executada

## O que NÃO farei

- Executar um scanner de segurança real (realizo análise estática pela leitura do código)
- Corrigir problemas automaticamente — a equipe revisa e decide o que corrigir
- Fabricar classificações de severidade — cada classificação é justificada pelo achado
- Garantir completude — esta é uma autorrevisão, não uma auditoria formal

## Formato de saída

Um relatório Markdown em `03-implementation/security-review-[context].md`:

```markdown
# Security Self-Review — [Bounded Context]
## Summary
Findings: N total | High: N | Medium: N | Low: N
## Findings
| # | Severity | Category | File:Line | Description | Remediation |
## Areas Requiring External Scanning
## Approval
```

## Definição de pronto

- [ ] Todo endpoint de controller foi verificado quanto a annotations de authentication
- [ ] Toda query foi verificada quanto a SQL injection
- [ ] Nenhum secret diretamente no código foi encontrado (ou todos estão sinalizados)
- [ ] A cobertura de validação de entrada foi avaliada para cada endpoint
- [ ] O relatório tem classificações de severidade justificadas pelos achados
- [ ] Pelo menos uma "área que exige análise externa" foi identificada

## Corpo do prompt

Você é o `@builder` realizando uma autorrevisão de segurança. Esta não é uma auditoria formal — é uma verificação rápida antes que o participante alcance o checkpoint C3 e abra o PR de submissão.

**Passo 1 — Procure secrets diretamente no código.**
Pesquise nos arquivos especificados padrões que sugiram secrets diretamente no código:

- Strings contendo "password", "secret", "key", "token" ou "api_key" (sem diferenciar maiúsculas de minúsculas)
- Strings semelhantes a tokens codificados em Base64 (strings alfanuméricas longas)
- Propriedades ou referências a variáveis de ambiente definidas com valores literais em vez de `${ENV_VAR}`
- Arquivos chamados `.env` commitados no repositório

Para cada achado: path do arquivo, número da linha, padrão suspeito (mascarado caso pareça ser um secret real) e severidade (Alta).

**Passo 2 — Verifique SQL injection.**
Pesquise:

- Concatenação de strings em queries SQL (`"SELECT..." + variable`)
- Annotations `@Query` com interpolação de strings em vez de parâmetros nomeados
- Qualquer uso de `nativeQuery = true` (sinalize para revisão manual; não rejeite automaticamente)
- Uso de `JdbcTemplate` com concatenação de strings

Para cada achado: arquivo, linha, padrão vulnerável e remediação (use parâmetros nomeados ou derived queries).

**Passo 3 — Verifique authentication e authorization.**
Para cada endpoint de `@RestController`:

- Verifique se `@PreAuthorize`, `@Secured` ou method-level security está presente
- Verifique se o controller está em um path coberto pelas filter chains do Spring Security
- Sinalize qualquer endpoint acessível publicamente sem justificativa aparente

Para cada endpoint desprotegido: arquivo, linha, método e path do endpoint e severidade (Alta se modificar dados, Média se for somente leitura).

**Passo 4 — Verifique a validação de entrada.**
Para cada endpoint que aceita um request body:

- Verifique se `@Valid` está presente no parâmetro
- Verifique se o DTO de request tem annotations Bean Validation
- Procure qualquer campo `String` sem constraints `@Size` ou `@Pattern`

Para cada lacuna: arquivo, linha, campo não validado e remediação.

**Passo 5 — Verifique a exposição de dados sensíveis.**
Pesquise:

- Instruções de logging que possam emitir campos sensíveis (senhas, tokens, dados pessoais)
- Respostas de erro que exponham stack traces ou detalhes internos
- DTOs de response que incluam campos como `password`, `token` ou `ssn`

**Passo 6 — Identifique oportunidades de rate limiting.**
Sinalize qualquer endpoint de escrita (POST, PUT, DELETE) sem rate limiting. Observação: a equipe pode não implementar rate limiting durante o workshop, mas ele deve ser documentado como uma preocupação de produção.

**Passo 7 — Compile o relatório.**
Escreva em `03-implementation/security-review-[context].md`, com todos os achados ordenados por severidade (Alta primeiro). Inclua uma contagem resumida e uma seção que liste as áreas em que um scanner real (SAST/DAST) deve ser executado.

Este relatório informa a prontidão para C3. O participante decide quais achados corrigir agora e quais adiar.

## Exemplo de invocação

```
/security-self-review context=<context> files=<Controller>.java,<Service>.java,<Entity>.java
```
