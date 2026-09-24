# Mapa de dependências — SIFAP legado

> **Trilha:** [Kit da Equipe](../README.md) › [Etapa 1](README.md) › **Mapa de dependências**

**Artefato preenchido pela equipe durante a Etapa 1 — Passo 3.** Registra as dependências entre programas Natural e DDMs Adabas que sustentam o escopo selecionado.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual responsável por Arquitetura |
| **Pré-requisitos** | Catálogo de regras com origens identificadas |
| **Etapa** | Etapa 1 — Arqueologia |
| **Resultado esperado** | Diagrama Mermaid e tabelas de arestas com evidências `arquivo:linha` |

> [!IMPORTANT]
> Mapeie somente dependências que expliquem o escopo selecionado: programas `.NSN` que chamam outros programas (`CALLNAT`, `FETCH`) e programas que acessam DDMs (`READ`, `FIND`, `STORE`, `UPDATE`, `DELETE`). Toda aresta deve ser sustentada por `arquivo:linha` — nenhuma inferência sem evidências. Este mapa orienta as hipóteses de recorte em [`discovery-report.md`](discovery-report.md).

> [!NOTE]
> Guia passo a passo: [`GUIDE.md`](GUIDE.md).

**Participante**: <!-- preencher -->
**Escopo**: programas e DDMs que sustentam a funcionalidade selecionada

---

## Diagrama Mermaid

```mermaid
%%{init: {'theme':'neutral','themeVariables':{'fontFamily':'ui-sans-serif, system-ui, sans-serif','primaryColor':'#F5F5F5','primaryTextColor':'#171717','primaryBorderColor':'#171717','lineColor':'#525252','secondaryColor':'#FFFFFF','tertiaryColor':'#FAFAFA','background':'#FFFFFF'}}}%%
flowchart TD
    classDef step fill:#F5F5F5,stroke:#171717,color:#171717
    classDef alt fill:#FFFFFF,stroke:#525252,color:#171717
    classDef muted fill:#FAFAFA,stroke:#A3A3A3,color:#404040
    classDef result fill:#FFFFFF,stroke:#171717,color:#171717,stroke-width:2px

    %% preencher: nós = programas e DDMs; arestas = chamadas e acesso a dados
    %% exemplo de sintaxe:
    %% PROGRAMA1 -->|"CALLNAT"| PROGRAMA2
    %% PROGRAMA1 -->|"READ"| DDM1[("DDM1")]
```

---

## Arestas Programa → Programa

| # | De | Para | Tipo (`CALLNAT`/`FETCH`) | Evidência (`arquivo:linha`) |
|---|---|---|---|---|
| 1 | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

---

## Arestas Programa → DDM

| # | Programa | DDM | Operação (`READ`/`FIND`/`STORE`/`UPDATE`/`DELETE`) | Evidência (`arquivo:linha`) |
|---|---|---|---|---|
| 1 | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

---

## Observações

- **Programas mais conectados (hubs):** <!-- preencher -->
- **Programas isolados ou código morto:** <!-- preencher -->
- **Ordem de dependência do batch:** <!-- preencher -->

---

## Definição de pronto

- [ ] Toda aresta relevante ao escopo cita `arquivo:linha`.
- [ ] Diagrama Mermaid gerado com o cabeçalho `%%{init:...}%%` e uma paleta neutra.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Catálogo de regras](business-rules-catalog.md)<br/><sub>Passo 2 — extração de regras.</sub> | [Questões em aberto](mysteries-found.md)<br/><sub>Passo 4 — registro de incertezas.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
