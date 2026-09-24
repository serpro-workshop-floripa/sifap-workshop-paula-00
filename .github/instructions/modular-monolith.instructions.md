---
description: "Use ao projetar ou revisar arquitetura de Monólito Modular, limites por funcionalidade, mapeamento JPA e migração Strangler Fig."
applyTo: "backend/src/main/java/**,backend/pom.xml,backend/build.gradle*"
---

# Guia de arquitetura de Monólito Modular

Este arquivo define a arquitetura de destino: um **Monólito Modular**, não microsserviços, com package-by-feature, bounded contexts, mapeamento FDT Adabas para JPA, Spring Boot 3.3 e Strangler Fig. Controllers e DTOs pertencem a [`backend.instructions.md`](backend.instructions.md), segurança a [`security.instructions.md`](security.instructions.md), schema a [`database.instructions.md`](database.instructions.md) e leitura legada a [`natural-adabas.instructions.md`](natural-adabas.instructions.md).

## Princípio central: um deployable, vários módulos

O sistema é uma única aplicação Spring Boot com limites internos claros. Cada bounded context possui domínio, interfaces de repositório e serviços.

- **Restrição do workshop:** a janela do desafio não comporta coordenação de sistemas distribuídos.
- **Orçamento de complexidade:** um deployable reduz coordenação enquanto a equipe estabelece ownership e comportamento de migração.
- **Caminho de migração:** um Monólito Modular bem estruturado pode ser separado depois, se necessário.

## Estrutura package-by-feature

Organize por capacidade de negócio, não por camada técnica.

```text
src/main/java/com/example/app/
├── <feature>/
│   ├── domain/
│   ├── application/
│   └── infrastructure/
├── shared/
│   ├── audit/
│   └── exception/
└── Application.java
```

- Um módulo nunca importa diretamente internals de outro; use interfaces ou eventos.
- `shared/` contém apenas temas transversais.
- Adicione repositórios, serviços e controllers apenas onde o comportamento aprovado exigir.

## Limites de bounded contexts

Pergunte quem possui os dados, o que muda junto e o que precisa de isolamento. Identificadores de arquivos Adabas são inventário de origem, não bounded contexts prontos. Architects e DBA definem ownership por padrões de acesso, relações e evidências de negócio.

## Arquitetura de migração de dados

Siga [DATA-MIGRATION.md](../../docs/DATA-MIGRATION.md). O DBA responde por prontidão, profiling, extração, carga e evidências; architects definem contratos; QA reconcilia de forma independente.

- Use origem Adabas autorizada e populada com snapshot consistente.
- Defina contrato de extração, linhagem de chaves, mapeamentos, staging, ordem de carga, rejeições, retomada e recuperação.
- Preserve identificadores, zeros à esquerda, precisão, datas, null, encoding e ocorrências MU/PE.
- Separe Flyway da migração de registros.
- Mantenha dados importados atrás das interfaces do módulo responsável.
- A aceitação cobre toda a população autorizada com listagem, busca e detalhes.
- Exija reconciliação independente e rerun/recovery testados antes de C3.

## Mapeamento JPA a partir do FDT

| Formato Adabas | Tipo Java | Anotação JPA |
|---|---|---|
| `A` | `String` | `@Column(length = N)` |
| `N` inteiro | `Long` ou `Integer` | `@Column` |
| `N` decimal | `BigDecimal` | `@Column(precision = P, scale = S)` |
| `P` | `BigDecimal` | `@Column(precision = P, scale = S)` |
| `D` | `LocalDate` | `@Column` |
| `T` | `LocalDateTime` | `@Column` |
| `B` | `byte[]` | `@Column` ou `@Lob` |

Normalize MU em tabela relacionada ou `@ElementCollection` quando a semântica revisada permitir. JSONB exige evidência. Mapeie PE com relação como `@OneToMany`, preservando identidade e ordem quando necessário.

## Convenções Spring Boot 3.3

- Use injeção por construtor.
- Use records para DTOs.
- Valide no controller com `@Valid`.
- Use `@Transactional` apenas em serviços.
- Retorne `Optional`, nunca `null`.
- Use sealed interfaces para uniões de tipos.
- Retorne `ProblemDetail` RFC 7807 em erros.

## Padrão Strangler Fig

Quando moderno e legado coexistirem:

1. Requests passam por uma camada de roteamento.
2. Funcionalidades migradas seguem para módulos Spring Boot.
3. Funcionalidades não migradas permanecem no legado.
4. Cada rota muda gradualmente para o moderno.

Documente a fronteira do incremento. Não invente proxy HTTP legado nem implemente facade sem requisito.

## Convenções

| Regra | Motivo |
|---|---|
| Um deployable Spring Boot com módulos internos | Mantém velocidade e limites explícitos |
| Package por capacidade de negócio | Alinha módulos a bounded contexts |
| Acesso entre módulos por interfaces ou eventos | Evita acoplamento oculto |
| Mapeamento FDT deliberado | Evita truncamento e perda de precisão |
| Transações em serviços e injeção por construtor | Explicita fronteiras |
| `ProblemDetail` para erros | Padroniza respostas |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Mantenha uma aplicação com módulos claros | Crie um microsserviço por contexto |
| Coloque lógica de negócio em serviços Java | Mova regras para stored procedures |
| Use JPA/JPQL ou queries derivadas | Concatene SQL |
| Retorne `Optional` quando puder faltar | Retorne `null` |
| Suporte migração parcial com Strangler Fig | Suponha migração total de uma vez |

## Checklist antes de abrir um PR

- [ ] O código está em um deployable e organizado por capacidade.
- [ ] Módulos não importam internals uns dos outros.
- [ ] Tipos FDT preservam precisão, MU, PE e descriptors.
- [ ] DBA e architects revisaram extração, linhagem, carga e recuperação.
- [ ] QA verificou reconciliação e queries sobre toda a população.
- [ ] Transações estão apenas em serviços e métodos públicos não retornam `null`.
- [ ] O design pode coexistir com paths legados por Strangler Fig.
