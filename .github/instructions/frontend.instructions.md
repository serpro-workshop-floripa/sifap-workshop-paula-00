---
description: "Use ao construir componentes e páginas de frontend, interações, estado, acessibilidade e fluxos voltados ao usuário."
applyTo: "frontend/app/**,frontend/components/**,frontend/src/app/**,frontend/src/components/**"
---

# Convenções de frontend — Componentes e interação

Este arquivo se aplica à UI em `frontend/app/**` e `frontend/components/**`. Ele define comportamento de componentes, interação, estado e acessibilidade. O contrato de Next.js 15, TypeScript strict, Tailwind/shadcn, Server Components e Server Actions está em [`frontend-spec.instructions.md`](frontend-spec.instructions.md).

> [!NOTE]
> `frontend/` ainda não existe. A equipe o cria na Etapa 3 e aplica estas convenções desde o início.

## Construção de componentes

Crie componentes pequenos, com uma responsabilidade, named exports e props tipadas. Prefira composição a listas crescentes de props. Não busque dados em componentes apenas de apresentação.

```tsx
export function ResourceCard({ resource }: { resource: ResourceDto }) {
  return (
    <article className="rounded-lg border p-4">
      <h3 className="font-semibold">{resource.label}</h3>
      <p className="text-muted-foreground">{formatBRL(resource.amount)}</p>
    </article>
  );
}
```

Mantenha `'use client'` na menor superfície possível. O Server Component busca dados e passa-os a um Client Component pequeno.

## Estado de componentes

Comece com `useState` local. Eleve o estado ao parent comum mais próximo quando siblings precisarem compartilhá-lo. Use Context apenas para estado realmente compartilhado. Uma biblioteca de estado exige ADR.

Inputs são controlados com `value` e `onChange`. Derive valores durante o render em vez de copiar props para state.

## Interação e fluxos assíncronos

Mutações usam Server Actions, não `fetch` no cliente. Use `useTransition` para estado pending/disabled e reflita-o com `aria-busy`.

Toda view assíncrona apresenta estados explícitos de loading, vazio e erro. Confirme ações destrutivas e formate valores e datas com locale explícito.

## Acessibilidade (WCAG 2.1 AA)

| Requisito | Como atender |
|---|---|
| Labels | Cada input tem `<label htmlFor>` ou `aria-label` |
| Teclado | Elementos interativos funcionam por Tab, Enter e Space |
| Foco | Dialog recebe foco ao abrir e devolve ao trigger ao fechar |
| Contraste | Texto ≥ 4.5:1; texto grande ≥ 3:1 |
| Estrutura | Um `<h1>` por página, headings lógicos e landmarks |
| Cor | Nunca é o único sinal; acompanhe com texto ou ícone |

Prefira elementos semânticos antes de ARIA. Adicione ARIA apenas quando a semântica nativa não bastar.

## Convenções

| Regra | Motivo |
|---|---|
| Named exports | Mantém imports consistentes |
| Props tipadas, sem `any` | Detecta falhas na compilação |
| `useState` local; Context apenas quando compartilhado | Mantém estado previsível |
| Teste ao lado do componente | Aproxima comportamento e cobertura |
| Estados loading, vazio e erro | Evita becos sem saída |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Restrinja `'use client'` ao menor leaf | Marque a página inteira como client |
| Mute por Server Action | Faça mutation com `fetch` no cliente |
| Rotule cada controle | Use placeholder como label |
| Formate valores e datas com locale | Mostre números brutos ou datas ISO |

## Checklist antes de abrir um PR

- [ ] Componentes usam named exports e props totalmente tipadas.
- [ ] `'use client'` está restrito ao menor componente interativo.
- [ ] Context só é usado quando justificado.
- [ ] Views assíncronas exibem loading, vazio e erro.
- [ ] Inputs são rotulados, operáveis por teclado e atendem contraste AA.
- [ ] Um teste Testing Library cobre a interação.
