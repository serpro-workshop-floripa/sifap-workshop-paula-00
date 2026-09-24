---
description: "Use ao implementar ou revisar Next.js 15 App Router, TypeScript, Tailwind CSS, shadcn/ui e Server Components em frontend/."
applyTo: "frontend/app/**,frontend/components/**,frontend/src/app/**,frontend/src/components/**,frontend/**/*.ts,frontend/**/*.tsx"
---

# Especificação de frontend — Next.js 15 e TypeScript

Este arquivo orienta TypeScript, TSX, rotas App Router e componentes reutilizáveis em `frontend/`. A plataforma usa Next.js 15, Server Components, Server Actions, TypeScript strict, Tailwind CSS, shadcn/ui, acessibilidade e Vitest. [`frontend.instructions.md`](frontend.instructions.md) orienta construção e interação de componentes.

## Resumo da stack

| Camada | Tecnologia | Versão |
|---|---|---|
| Framework | Next.js App Router | 15 |
| Linguagem | TypeScript, strict mode | 5 |
| Estilo | Tailwind CSS | 3.4+ |
| Componentes | shadcn/ui | Versão compatível escolhida pela equipe |
| Estado cliente | React `useState` e Context | Nativo |
| Dados no servidor | Server Components e Server Actions | Nativo |
| Testes | Vitest e Testing Library | Versões compatíveis |

## Padrões do App Router

### Server Components por padrão

Server Components executam no servidor e não enviam o código do componente ao navegador. Podem usar `await`, mas não hooks de cliente, event handlers ou APIs do navegador.

- Busque dados pela fronteira backend configurada; `fetch` no servidor exige URL absoluta.
- Valide e tipe respostas na fronteira.
- Exponha falhas explicitamente; não substitua erro por lista vazia ou dados de exemplo.
- Mantenha autenticação, URLs internas e secrets no servidor.

### Client Components

Adicione `'use client'` apenas onde houver interatividade. Minimize a fronteira cliente. Comece com estado local e Context; outra dependência de estado ou cache exige ADR.

### Server Actions para mutações

Trate Server Actions como fronteiras públicas:

- Autentique e autorize cada operação.
- Valide `FormData` e tipos antes de chamar o backend.
- Use a URL de API configurada e propague erros significativos.
- Nunca coloque tokens em Client Components ou variables `NEXT_PUBLIC_`.
- Mantenha regras de domínio no backend.

## Convenções TypeScript

- Mantenha `strict: true`; não use `any`, `@ts-ignore` nem assertions inseguras.
- Use `unknown` com guards para input não confiável.
- Use named exports em componentes reutilizáveis. Arquivos de rota preservam default exports exigidos pelo Next.js.
- Prefira interfaces para objetos extensíveis.
- Reutilize `Pick`, `Omit` e `Partial`.

## Tailwind CSS e shadcn/ui

- Use Tailwind e shadcn/ui para elementos padrão.
- Reutilize design tokens da equipe.
- Evite outro framework de estilo ou CSS ad hoc sem revisão.
- Construa mobile-first com breakpoints `sm:`, `md:` e `lg:`.
- Preserve locale, moeda e datas aprovados.

## Baseline de acessibilidade

- Forneça texto alternativo adequado.
- Associe inputs a labels.
- Suporte teclado e foco visível.
- Não use somente cor para transmitir informação.
- Use um `h1` por página e hierarquia lógica.
- Exponha loading, vazio e falha de forma acessível.

## Consulta a dados migrados

Use o ciclo de dados revisado pelo DBA em [DATA-MIGRATION.md](../../docs/DATA-MIGRATION.md) e REQ-IDs aprovados. Consulte a aplicação real com PostgreSQL, não páginas baseadas apenas em fixtures. Verifique paginação estável, autorização, relações necessárias e cobertura além da primeira página. Não registre CPF ou valores.

## Vitest e Testing Library

Escreva testes durante a implementação para comportamento visível e falhas. Use nomes como `should_<behavior>_when_<condition>` ou `displays <what> when <condition>`.

## Convenções

| Regra | Motivo |
|---|---|
| Server Components por padrão | Reduz código cliente e protege dados |
| Tipos strict e fronteiras validadas | Detecta input inválido |
| Named exports reutilizáveis | Mantém imports consistentes |
| Server Actions autorizadas e validadas | Define fronteiras de mutation |
| Tailwind e shadcn/ui | Evita stacks de estilo concorrentes |
| Testes de comportamento | Verifica resultados observáveis |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Use named exports em componentes reutilizáveis | Remova defaults exigidos pelo Next.js |
| Restrinja `unknown` com guards | Ignore erros com `any` |
| Mantenha data loading no servidor | Adicione fetch cliente a Server Component |
| Mantenha secrets na configuração server-only | Exponha secrets em props ou variables públicas |
| Verifique cobertura completa com DBA/QA | Aceite telas baseadas apenas em amostra |

## Checklist antes de abrir um PR

- [ ] TypeScript permanece strict e dados de fronteira são validados.
- [ ] Código cliente está limitado a componentes interativos.
- [ ] Server Actions autorizam e validam antes de chamar o backend.
- [ ] Exports respeitam componentes reutilizáveis e rotas App Router.
- [ ] Estilo e acessibilidade seguem as convenções.
- [ ] Testes cobrem comportamento, falhas e queries aprovadas.
- [ ] Nenhum fallback de exemplo esconde falha de acesso a dados.
