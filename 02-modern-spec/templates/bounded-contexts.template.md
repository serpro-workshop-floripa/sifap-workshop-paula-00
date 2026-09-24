---

title: "Modelo: Bounded Contexts"
description: "Estrutura para definições de bounded contexts por meio de /carve-bounded-contexts"
author: "Paula Silva, AI-Native Software Engineer, Americas Global Black Belt at Microsoft"
date: "2026-04-29"
version: "1.0.0"
status: "aprovado"
tags: ["modelo", "bounded-contexts", "architect", "etapa-2"]
---

<!-- Como usar: execute /carve-bounded-contexts. Clone o bloco de contexto para cada contexto. -->

# Mapa de bounded contexts

![Modelo de bounded contexts](https://img.shields.io/badge/Modelo-bounded--contexts-737373?style=flat-square) ![Copie — não edite o original](https://img.shields.io/badge/Copie-n%C3%A3o%20edite%20o%20original-A3A3A3?style=flat-square)

> **Caminho:** [Kit da equipe](../../README.md) › [Etapa 2](../README.md) › Modelos › **bounded-contexts**

> [!NOTE]
> Este arquivo é um MODELO. Copie-o para o repositório do participante e preencha-o com dados reais. Não edite o original.

---

## Conceito: Bounded Context

Um bounded context é um limite explícito dentro do qual um modelo de domínio é válido e consistente. O termo vem de Domain-Driven Design (DDD) e fornece a base para definir os módulos de um Monólito Modular.

**Por que isso importa:** no SIFAP, o módulo de pagamentos usa o termo "beneficiário" de uma forma, enquanto o módulo de fiscalização pode usar o mesmo termo com regras diferentes. Definir bounded contexts impede que um único modelo seja distorcido para atender a todos os contextos ao mesmo tempo, o que causa acoplamento indesejado e dificulta a evolução.

**Monólito Modular:** uma arquitetura na qual bounded contexts são módulos Java independentes dentro de uma única JVM. Cada módulo tem suas próprias camadas (`domain/`, `application/`, `infrastructure/`) e se comunica com outros módulos apenas por interfaces públicas definidas.

**Strangler Fig:** um padrão de migração incremental no qual o sistema moderno cresce ao redor do sistema legado e substitui funcionalidades uma de cada vez. O SIFAP 2.0 não precisa substituir tudo de uma só vez. Cada bounded context pode ser modernizado de forma independente.

---

## Avaliações de hipóteses

### <!-- espaço reservado: Nome --> — <!-- espaço reservado: ACEITA / REJEITADA -->

| Critério | Avaliação | Evidência |
|---|---|---|
| Coesão | <!-- espaço reservado --> | <!-- espaço reservado --> |
| Acoplamento | <!-- espaço reservado --> | <!-- espaço reservado --> |
| Frequência de mudança | <!-- espaço reservado --> | <!-- espaço reservado --> |

---

## Bounded contexts finais

### <!-- espaço reservado: Nome do contexto -->

| Campo | Valor |
|---|---|
| **Responsabilidade** | <!-- espaço reservado --> |
| **Dados sob responsabilidade** | <!-- espaço reservado --> |
| **Interface pública** | <!-- espaço reservado --> |
| **Por que é um contexto próprio** | <!-- espaço reservado --> |

---

## Comunicação entre contextos

| De | Para | Mecanismo | Dados |
|---|---|---|---|
| <!-- espaço reservado --> | <!-- espaço reservado --> | <!-- espaço reservado --> | <!-- espaço reservado --> |

```mermaid
%%{init: {'theme':'neutral','themeVariables':{'fontFamily':'ui-sans-serif, system-ui, sans-serif','primaryColor':'#F5F5F5','primaryTextColor':'#171717','primaryBorderColor':'#171717','lineColor':'#525252','secondaryColor':'#FFFFFF','tertiaryColor':'#FAFAFA','background':'#FFFFFF'}}}%%
flowchart LR
    classDef ctx fill:#F5F5F5,stroke:#171717,color:#171717

    CTX1["Contexto 1"]:::ctx -->|"chama"| CTX2["Contexto 2"]:::ctx
```

---

> [!IMPORTANT]
> Definition of Done: hipóteses avaliadas, rejeições documentadas, 2 a 5 contextos nomeados e diagrama Mermaid renderizado sem erros.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIA da Etapa 2](../GUIDE.md)<br/><sub>Instruções passo a passo.</sub> | [Modelo de ADR](ADR.template.md)<br/><sub>Modelo de ADR.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
