# ADR-XXX: Título da decisão

> **Caminho:** [Kit da equipe](../README.md) › [Etapa 2](README.md) › **Modelo de ADR**

> [!NOTE]
> Este arquivo é um modelo de apoio. Copie-o para `ADR-NNN-title.md` e preencha-o. Não edite o original.
> Use este modelo quando uma decisão arquitetural bloquear o `plan.md` da funcionalidade.

![Etapa 2](https://img.shields.io/badge/Etapa-2%20%C2%B7%20Especifica%C3%A7%C3%A3o-171717?style=flat-square) ![Tipo Modelo de ADR](https://img.shields.io/badge/Tipo-Modelo%20de%20ADR-737373?style=flat-square)

| Campo | Valor |
|---|---|
| **Data** | `YYYY-MM-DD` |
| **Status** | Proposta / Aceita / Rejeitada / Substituída pela ADR-YYY |
| **Responsáveis pela decisão** | Nomes dos participantes envolvidos |
| **Funcionalidade relacionada** | `.spec/<NNN>-<feature>/` |

---

## Conceito: ADR (Architecture Decision Record)

Uma ADR é o registro formal de uma decisão arquitetural significativa. Ela documenta o contexto que levou à decisão, as alternativas avaliadas, a opção selecionada e as consequências esperadas.

**Por que isso importa:** decisões técnicas tomadas verbalmente durante o workshop se perdem. Uma ADR de duas páginas garante que qualquer pessoa que revise a PR entenda por que o sistema foi projetado de determinada maneira, sem precisar perguntar a quem tomou a decisão às 14:30 de um dia corrido.

**Regra de ouro:** sempre liste o "caminho não escolhido". Sem isso, a ADR se torna uma descrição de implementação, em vez de um registro de decisão.

**Quando criar uma:** somente quando a decisão bloquear `plan.md`. Se a decisão couber em um comentário de commit, ela não precisa de uma ADR.

---

## Contexto

> Descreva o problema ou a necessidade que motivou esta decisão.
> Inclua restrições, requisitos e informações relevantes.
> Seja específico: "precisamos de um banco de dados" não é suficiente.

<!-- preencha -->

---

## Opções consideradas

### Opção 1: <!-- nome -->

| Aspecto | Avaliação |
|---|---|
| **Descrição** | Como funcionaria |
| **Vantagens** | Liste-as |
| **Desvantagens** | Liste-as |

### Opção 2: <!-- nome -->

| Aspecto | Avaliação |
|---|---|
| **Descrição** | Como funcionaria |
| **Vantagens** | Liste-as |
| **Desvantagens** | Liste-as |

### Opção 3: <!-- nome, opcional -->

| Aspecto | Avaliação |
|---|---|
| **Descrição** | Como funcionaria |
| **Vantagens** | Liste-as |
| **Desvantagens** | Liste-as |

---

## Decisão

**Decidimos** <!-- ação ou escolha selecionada -->.

---

## Justificativa

> Explique por que esta opção foi selecionada em vez das demais.
> Relacione-a aos requisitos, às restrições e ao contexto.

<!-- preencha -->

---

## Consequências

### Positivas

- <!-- consequência positiva 1 -->

### Negativas

- <!-- consequência negativa 1 e como mitigá-la -->

### Riscos

- <!-- risco identificado e plano de contingência -->

---

## Referências

- <!-- link ou documento relevante -->
- Requisito EARS relacionado: `REQ-XXX`

> [!IMPORTANT]
> Este modelo não contém nenhuma decisão aceita. O participante fornece evidências,
> alternativas, justificativa e status da revisão. Para migração de dados, arquitetos e
> DBA usam evidências medidas da origem e o [guia de migração de dados](../docs/DATA-MIGRATION.md).

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIA da Etapa 2](GUIDE.md)<br/><sub>Instruções passo a passo da etapa.</sub> | [GUIA da Etapa 2](GUIDE.md)<br/><sub>Conduza a decisão com o participante.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
