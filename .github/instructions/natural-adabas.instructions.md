---
description: "Use ao ler código legado Natural/Adabas, padrões da linguagem, estrutura FDT, nomenclatura e fluxos batch."
applyTo: "01-archaeology/legacy-sifap/**,**/*.NSP,**/*.nsp,**/*.NSN,**/*.nsn,**/*.NSS,**/*.nss,**/*.NSA,**/*.nsa,**/*.NSL,**/*.nsl,**/*.NSC,**/*.nsc,**/*.NSM,**/*.nsm,**/*.NSD,**/*.nsd,**/*.NAT,**/*.nat,**/*.CPY,**/*.cpy,**/*.DDM,**/*.ddm,**/*.jcl,**/*.JCL"
---

# Código legado Natural/Adabas — Guia de leitura

Este arquivo se aplica a programas Natural, DDMs Adabas, JCL, copycodes e arquivos em `01-archaeology/legacy-sifap/`. Ele orienta estrutura Natural, dependências `CALLNAT` e `INCLUDE`, FDTs, nomes, batch e packed decimals. Limites modernos e JPA pertencem a [`modular-monolith.instructions.md`](modular-monolith.instructions.md).

## Estrutura de programas Natural

```text
DEFINE DATA
  LOCAL
    01 #MY-VARIABLE  (A20)
    01 #COUNTER      (N5)
    01 #AMOUNT       (P9.2)
    01 #RATES        (N3.4/1:27)
  END-DEFINE
END
```

As fontes fornecidas e o gate de CI usam ponto em `(P9.2)` e `(N3.4)`. Isso não prova compilação ou execução. Confirme runtime e configuração decimal com o responsável pela origem. Preserve o corpus somente leitura e registre incertezas.

| Bloco | Finalidade |
|---|---|
| `DEFINE DATA LOCAL` | Variáveis locais |
| `DEFINE DATA PARAMETER` | Parâmetros de entrada/saída |
| `DEFINE DATA GLOBAL` | Dados compartilhados na sessão |
| `INPUT` | Entrada de terminal ou arquivo |
| `DISPLAY` / `WRITE` | Tela ou relatório |
| `MAP` | Layout de terminal |

## CALLNAT, PERFORM e INCLUDE

- `CALLNAT 'SUBPROG'` chama outro subprograma. Verifique parâmetros posicionais e PDA; não infira direção pelos nomes.
- `PERFORM` pode chamar subroutine interna ou externa. Localize a definição.
- `INCLUDE` insere copycode em compile time. Localize o membro para completar o layout.

Nunca ignore `CALLNAT`, `INCLUDE`, `PARAMETER USING` ou `LOCAL USING`.

## Extensões de membros

| Extensão | Tipo | Chamado por |
|---|---|---|
| `.NSP` | Programa | Sessão Natural ou batch |
| `.NSN` | Subprograma | `CALLNAT` |
| `.NSA` | PDA | `PARAMETER USING` |
| `.NSL` | LDA | `LOCAL USING` |
| `.NSC` | Copycode | `INCLUDE` |
| `.NSM` | Map | `INPUT USING MAP` |
| `.jcl` | Job Control Language | Scheduler batch |

Uma biblioteca Natural é plana e resolve membros pelo nome. Nomes têm até 8 caracteres. Preserve os nomes técnicos existentes.

## FDT Adabas

| Coluna | Significado |
|---|---|
| Level | Profundidade hierárquica |
| Name | Nome curto de dois caracteres |
| Format | Formato físico Adabas, como `A`, `U`, `P` ou `B` |
| Length | Tamanho em bytes |
| Descriptor | `DE`, `MU` ou `PE` |

MU contém vários valores por occurrence. PE repete um grupo de campos. Registre estrutura, identidade e ordem; DBA e architects escolhem o destino na Etapa 2. Um super-descriptor sugere padrão de acesso, não índice PostgreSQL automático.

## Convenções de nomes legadas

Prefixos como `BN-`, `BATCH-`, `PG-`, `PROG-`, `PS-`, `SUB-`, `AU-` e `AUT-` são pistas, não regras. `#` costuma marcar variável local. Verifique sempre a declaração e o uso.

## Padrões batch

Procure `READ WORK FILE`, `AT END OF DATA`, `AT BREAK`, `BEFORE BREAK PROCESSING`, reports, totais e cleanup. Leia também paths de erro e escape.

## Packed decimal

Packed decimal usa dois dígitos por byte e nibble final de sinal. Mapeie valores financeiros para `BigDecimal`, nunca `double` ou `float`. Não confunda precisão lógica `(P9.2)` com tamanho físico em bytes. Compare programa, DDM, storage e operações reais.

## Estratégia de leitura

1. Comece por `DEFINE DATA`.
2. Localize o `READ` ou `FIND` principal.
3. Rastreie cada `CALLNAT`.
4. Localize `INCLUDE`.
5. Verifique `AT BREAK` e `AT END OF DATA`.
6. Registre `ESCAPE` e `ON ERROR`.
7. Rastreie inicialização do buffer e `IF NO RECORDS FOUND`.
8. Verifique a forma de seleção, ordenação por descriptor e markers do DDM.

## Convenções

| Regra | Motivo |
|---|---|
| Preserve a notação decimal com ponto | Corresponde ao corpus e ao gate |
| Rastreie todas as dependências Natural | Um membro isolado está incompleto |
| Compare formatos com o DDM | Evita truncamento e overflow |
| Use `BigDecimal` para dinheiro | Preserva precisão |
| Verifique runtime e statements reais | Leitura estática não prova execução |
| Trate prefixos como pistas | Convenções variam |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Comece por `DEFINE DATA` | Interprete regra antes do layout |
| Localize `READ` ou `FIND` | Suponha o arquivo principal pelo nome |
| Rastreie dependências | Ignore subprogramas, PDAs, LDAs ou maps |
| Leia erros, breaks e end-of-data | Leia apenas o happy path |
| Rastreie buffers e no-record paths | Suponha limpeza automática do buffer |
| Inspecione seleção e descriptors | Afirme comportamento universal sem evidência |

## Checklist antes de abrir um PR

- [ ] Variáveis, arrays, parâmetros e formatos foram registrados.
- [ ] Paths de leitura, work files, reports e control breaks foram identificados.
- [ ] Dependências foram rastreadas ou registradas como abertas.
- [ ] Formatos foram comparados ao DDM, incluindo MU, PE e super-descriptors.
- [ ] Valores monetários usam ou indicam `BigDecimal`.
- [ ] Erros, escapes, no-records, end-of-data e defaults silenciosos foram incluídos.
