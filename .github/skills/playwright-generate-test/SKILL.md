---
name: "playwright-generate-test"
description: "Use quando a pessoa pedir para criar ou gravar um teste de navegador ou E2E com Playwright para um fluxo web. Explore o cenário passo a passo com o servidor Playwright MCP, gere uma spec TypeScript com `@playwright/test` e execute-a até que passe de forma confiável."
---
# Geração de teste end-to-end com Playwright

Gere um teste end-to-end (E2E) em TypeScript explorando o fluxo descrito com o servidor Playwright MCP, uma etapa por vez. Depois, crie uma spec com `@playwright/test` e execute-a até que passe. Esta skill cobre regressões no navegador para o frontend SIFAP 2.0 com Next.js 15. Testes unitários e de componentes permanecem em Vitest + Testing Library, conforme [`tests.instructions.md`](../../instructions/tests.instructions.md).

## Quando invocar

- "Gere um teste Playwright para este fluxo."
- "Grave um teste end-to-end que faça login e abra o dashboard."
- "Crie um teste de regressão no navegador para este cenário."
- "Transforme esta jornada de usuário em uma spec Playwright."

## Procedimento

> [!NOTE]
> Esta skill controla o **servidor Playwright MCP**, que precisa estar instalado, em execução e conectado a um frontend acessível. Se ele não estiver disponível, instale-o e inicie-o antes de usar a skill. Não escreva o teste somente a partir da descrição do cenário.

Nunca escreva o código do teste antes de observar o DOM real com o MCP.

1. **Obtenha o cenário.** Se nenhum fluxo tiver sido descrito, solicite um. Confirme a URL base do frontend em execução.
2. **Explore etapa por etapa.** Controle o fluxo com as ferramentas do Playwright MCP, como navegação, clique, preenchimento e assertion. Use cada estado observado para decidir a próxima ação.
3. **Prefira locators acessíveis.** Selecione elementos por role, label ou texto, com `getByRole` e `getByLabel`. Evite CSS frágil ou `data-testid` quando existir uma role.
4. **Gere a spec.** Somente depois de confirmar todas as etapas, crie um teste TypeScript com `@playwright/test`, baseado nas interações observadas. Estruture-o com Arrange-Act-Assert e inclua `// REQ-NNN` quando o fluxo rastrear um requisito.
5. **Salve o arquivo** no diretório `tests/` do frontend como `<feature>.spec.ts`.
6. **Execute e ajuste.** Rode `npx playwright test <name>` e corrija locators ou esperas até que o teste passe de forma confiável. Não deixe uma spec falhando ou instável.

> [!WARNING]
> Não inclua secrets nem dados específicos do ambiente na spec. Leia URLs base e credenciais de variáveis de ambiente ou da configuração do Playwright.

### Limites de escopo

| Camada | Ferramenta | Responsável |
|--------|------------|-------------|
| End-to-end no navegador | Playwright | Esta skill |
| Componente e interação | Vitest + Testing Library | [`tests.instructions.md`](../../instructions/tests.instructions.md) |
| Unidade e lógica pura | Vitest no frontend ou JUnit 5 no backend | [`test-strategy`](../test-strategy/SKILL.md) |

## Modelo de saída

```markdown
## Verificação da UI: <fluxo revisado>
- REQ-ID aplicável: <requisito real>
- Pré-condições / ator: <escopo aprovado>
- Ações e seletores acessíveis: <estrutura observada da página>
- Resultado esperado: <critério de aceitação revisado>
- Path do teste: <arquivo real gerado>
- Comando / resultado da execução: <evidência real ou não executado>
```

Resultado da execução:

```text
Comando: <comando real do teste direcionado>
Resultado: <aprovações/falhas observadas, duração e ambiente, ou não executado>
```

O template não pressupõe fluxo de aprovação de pagamento, papel, transição de estado nem execução bem-sucedida. Use Playwright somente quando já estiver disponível ou tiver aprovação explícita. Vitest e Testing Library continuam como padrão do kit para testes de frontend.

## Gate de qualidade

- [ ] O fluxo foi explorado etapa por etapa com o Playwright MCP antes da escrita do código.
- [ ] A spec usa `@playwright/test` e está no diretório `tests/` do frontend.
- [ ] Os elementos são selecionados por role ou label acessível, não por seletores frágeis.
- [ ] Fluxos baseados em requisitos contêm um comentário inline `// REQ-NNN`.
- [ ] O teste passa e não é instável; nenhum secret está gravado diretamente.
- [ ] A cobertura unitária e de componentes permanece em Vitest + Testing Library.
