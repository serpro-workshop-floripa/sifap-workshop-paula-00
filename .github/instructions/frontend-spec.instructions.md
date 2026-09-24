---
description: "Use when implementing or reviewing Next.js 15 App Router, TypeScript, Tailwind CSS, shadcn/ui, and Server Components under frontend/."
applyTo: "frontend/app/**,frontend/components/**,frontend/src/app/**,frontend/src/components/**,frontend/**/*.ts,frontend/**/*.tsx"
---
# Frontend Specification - Next.js 15 and TypeScript

This file governs TypeScript, TSX, App Router routes, and reusable components in
`frontend/`. It defines the modern SIFAP platform: Next.js 15, Server Components,
Server Actions, strict TypeScript, Tailwind CSS, shadcn/ui, accessibility, and
Vitest. [frontend.instructions.md](frontend.instructions.md) covers component
construction, client interaction, state coordination, and user-facing flows.

## Stack Summary

| Layer | Technology | Version |
|---|---|---|
| Framework | Next.js App Router | 15 |
| Language | TypeScript, strict mode | 5 |
| Styling | Tailwind CSS | 3.4+ |
| Components | shadcn/ui | Team-selected compatible version |
| Client state | React `useState` and Context when needed | Built-in |
| Server data | Server Components and Server Actions | Built-in |
| Testing | Vitest and Testing Library | Team-selected compatible versions |

## App Router Patterns

### Server Components by Default

Server Components execute on the server and do not ship their component code
to the browser. They can use `await` for server-side data access; they cannot
use client hooks, event handlers, or browser APIs.

- Fetch through the configured server-side backend boundary; server-side `fetch` needs an absolute URL, not a browser-relative `/api/...` URL.
- Validate and type responses at the boundary before rendering.
- Surface failures explicitly; do not replace failed requests with empty successful lists or sample data.
- Keep authentication, internal URLs, and secrets on the server.

### Client Components

Add `'use client'` only where interactivity is required:

```tsx
'use client';

import { useId, useState } from 'react';

export function ResourceFilter({ onFilter }: { onFilter: (term: string) => void }) {
  const [term, setTerm] = useState('');
  const inputId = useId();
  return (
    <div>
      <label htmlFor={inputId}>Filter resources</label>
      <input
        id={inputId}
        value={term}
        onChange={event => {
          setTerm(event.target.value);
          onFilter(event.target.value);
        }}
      />
    </div>
  );
}
```

Minimize the client boundary: keep data-loading pages on the server and isolate
interactive forms and filters. Start with local state and Context; add another
state or cache dependency only with an ADR.

### Server Actions for Mutations

Use Server Actions for form mutations when appropriate to the reviewed design.
Treat them as public input boundaries:

- Authenticate and authorize each operation.
- Validate `FormData` and request types before calling the backend.
- Bind the configured server-side API URL and propagate meaningful errors.
- Never put tokens in client components or `NEXT_PUBLIC_` variables.
- Keep domain rules in the backend, not duplicated in UI actions.

## TypeScript Conventions

- Keep `strict: true`; do not use `any`, `@ts-ignore`, or unsafe type assertions to bypass boundary validation.
- Use `unknown` with guards for untrusted input.
- Prefer named exports for reusable components. App Router route files retain Next.js-required default exports.
- Prefer interfaces for extensible object shapes.
- Reuse `Pick`, `Omit`, and `Partial` rather than duplicating types.

```tsx
interface ResourceLabel {
  label: string;
}

export function ResourceCard({ resource }: { resource: ResourceLabel }) {
  return <div>{resource.label}</div>;
}
```

## Tailwind CSS and shadcn/ui

- Use Tailwind utilities and shadcn/ui for standard UI elements.
- Reuse team-defined design tokens for spacing and colors.
- Avoid separate styling frameworks or ad hoc CSS unless indispensable and reviewed.
- Build mobile-first with appropriate `sm:`, `md:`, and `lg:` breakpoints.
- Preserve approved locale, currency, and date semantics. Translating documentation does not change business data formats.

## Accessibility Baseline

- Give images appropriate alternative text.
- Associate form inputs with labels.
- Support keyboard navigation and visible focus.
- Do not communicate information through color alone.
- Use one page-level `h1` and a logical heading hierarchy.
- Expose loading, empty, and failure states accessibly.

## Migrated-Data Consultation

Use the [DBA-reviewed data lifecycle](../../docs/DATA-MIGRATION.md) and approved
REQ-IDs for beneficiary listing, search, and detail flows. Query the real
PostgreSQL-backed application, not fixture-only pages. Verify stable pagination,
authorization, required related data, and coverage beyond the first page with QA.
Do not expose CPF or benefit amounts in logs.

## Vitest and Testing Library

Write component tests during implementation for visible behavior and failures.
Use names such as `should_<behavior>_when_<condition>` or
`displays <what> when <condition>`.

```tsx
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { ResourceCard } from './ResourceCard';

describe('ResourceCard', () => {
  it('displays the resource label when a resource is provided', () => {
    render(<ResourceCard resource={{ label: 'Example' }} />);
    expect(screen.getByText('Example')).toBeInTheDocument();
  });
});
```

These generic syntax examples do not supply SIFAP page behavior or acceptance
results; the team derives those from its specification.

## Convenções

| Rule | Rationale |
|---|---|
| Server Components by default | Minimize client code and protect server data access |
| Strict types and validated boundaries | Detect invalid input before it reaches rendering or mutations |
| Named reusable exports | Consistent imports without breaking App Router requirements |
| Authorized, validated Server Actions | Explicit mutation boundaries |
| Tailwind and shadcn/ui | Consistent UI without competing styling stacks |
| Behavior-focused tests | Verify observable outcomes and failure handling |

## Faça / Não faça

| Do | Do not |
|---|---|
| Use named exports for reusable components | Remove required Next.js route defaults |
| Narrow `unknown` with guards | Bypass typing with `any` or ignored errors |
| Use `async`/`await` | Hide errors in chained success fallbacks |
| Keep data loading on the server | Add client fetching to a Server Component |
| Keep secrets in server-only configuration | Expose secrets through client props or public variables |
| Verify full query coverage with DBA/QA | Accept sample-only screens as migrated-data consultation |

## Checklist antes de abrir um PR

- [ ] TypeScript stays strict and boundary data is validated.
- [ ] Client code is limited to components that require interaction.
- [ ] Server Actions authorize and validate before backend calls.
- [ ] Export conventions match reusable components and App Router routes.
- [ ] UI styling and accessibility follow the reviewed conventions.
- [ ] Tests cover the changed behavior, failures, and approved query coverage.
- [ ] No sample fallback or sensitive logging hides a data-access failure.
