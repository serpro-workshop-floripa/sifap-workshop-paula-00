# Dicionário de declarações Natural

> **Caminho:** [Kit da Equipe](../README.md) > [Etapa 1](README.md) > **Dicionário de declarações**

**Registro técnico das declarações examinadas, separado da interpretação de negócio e da revisão humana.**

| Campo | Valor |
|---|---|
| Participante / papéis | A preencher pelo participante; revisão DBA/QA pendente |
| Leitor técnico / data | GitHub Copilot, nesta sessão, 2026-09-24 |
| Origem | Corpus local; revisão Git não identificada nesta sessão |
| Escopo solicitado | 24 membros Natural/JCL; dados relacionados no [mapa](data-map.md) |
| Cobertura efetiva | Somente os intervalos registrados em [reading-coverage.md](reading-coverage.md) |
| Limites | Sem compilação, execução Natural, medição da origem ou aprovação C1 |

> [!IMPORTANT]
> Formatos, ordem e dimensões são transcrições das declarações. Direções IN/OUT e significados em comentários são intenção declarada, não comportamento demonstrado. A leitura técnica não é leitura nem aprovação do participante. Autoria e datas históricas permanecem na [cronologia canônica](legacy-sifap/CHRONOLOGY.md).

## Registro de declarações do membro

### PDAVALID

Fonte: [PDAVALID.NSA](legacy-sifap/natural-programs/PDAVALID.NSA#L43). Contexto: `DEFINE DATA PARAMETER`; lista de nível 1, sem dimensões. Os exemplos de `USING` do cabeçalho não comprovam importações reais.

| Ordem | Variável / campo | Formato literal | Direção comentada | Significado declarado / limite |
|---|---|---|---|---|
| 1 | `#PV-TYPE-DOC` | `(A1)` | IN | C=CPF; N=NIS/PIS/PASEP |
| 2 | `#PV-CPF` | `(A11)` | IN | CPF sem máscara, preenchido à esquerda |
| 3 | `#PV-NIS` | `(A11)` | IN | NIS/PIS/PASEP sem máscara |
| 4 | `#PV-COD-RETURN` | `(N4)` | OUT | 0000=VALID |
| 5 | `#PV-MSG` | `(A60)` | OUT | Branco quando válido |
| 6 | `#PV-IND-SPECIAL` | `(A1)` | OUT | S=SPECIAL DOC; N=COMMON DOC |

Não há `INIT` explícito na lista. Os códigos comentados no cabeçalho não foram promovidos a regras candidatas.

### PDACALC

Fonte: [PDACALC.NSA](legacy-sifap/natural-programs/PDACALC.NSA#L49). Contexto: `DEFINE DATA PARAMETER`; lista de nível 1, sem dimensões. Preserve os formatos alfanuméricos das chaves e o ponto decimal, sem deduzir bytes físicos ou precisão SQL.

| Ordem | Variável / campo | Formato literal | Direção comentada | Significado declarado / limite |
|---|---|---|---|---|
| 1 | `#PC-CPF` | `(A11)` | IN | CPF sem máscara; comentário cita DDM AB |
| 2 | `#PC-COD-PROGRAM` | `(A4)` | IN | Código; comentário cita DDM AA |
| 3 | `#PC-PERIOD` | `(N6)` | IN | YYYYMM |
| 4 | `#PC-COD-REGION` | `(A2)` | IN | Comentário: 01-27 OR 99; domínio não confirmado |
| 5 | `#PC-FAMILY-INCOME` | `(P9.2)` | IN | DECLARED INCOME |
| 6 | `#PC-QTY-DEPEND` | `(N2)` | IN | NUMBER OF ACTIVE DEPENDENTS |
| 7 | `#PC-AGE` | `(N3)` | IN | AGE IN COMPLETED YEARS |
| 8 | `#PC-STAT-BENEF` | `(A1)` | IN | A/S/C/I/D, segundo comentário |
| 9 | `#PC-AMT-BASE` | `(P9.2)` | IN | PROGRAM BASE AMOUNT |
| 10 | `#PC-AMT-GROSS` | `(P9.2)` | OUT | CALCULATED GROSS AMOUNT |
| 11 | `#PC-AMT-DISC` | `(P9.2)` | OUT | TOTAL DEDUCTIONS |
| 12 | `#PC-AMT-BONUS` | `(P9.2)` | OUT | HOLIDAY BONUS |
| 13 | `#PC-AMT-NET` | `(P9.2)` | OUT | GROSS - DEDUCTION + BONUS, segundo comentário |
| 14 | `#PC-TYPE-PAYMENT` | `(A1)` | OUT | N=NORMAL; D=THIRTEENTH; T=THIRD, segundo comentário |
| 15 | `#PC-COD-RETURN` | `(N4)` | OUT | 0000=OK |
| 16 | `#PC-MSG` | `(A60)` | OUT | Branco quando OK |

Não há `INIT` explícito. O cabeçalho atribui conversões ao chamador; chamadas efetivas ainda precisam ser confrontadas com esta lista.

## Áreas importadas e declarações compartilhadas

Importações e contratos dos chamadores serão registrados somente após exame de instruções reais, não dos exemplos comentados das PDAs.

## Views e definições de origem

Os subconjuntos de views ainda não foram conferidos nesta retomada. O [mapa de dados existente](data-map.md) deve ser revisado junto às fontes, sem presumir que seus achados foram validados.

## Membros sem declarações

Copycodes e JCL serão distinguidos de áreas independentes após inspeção de cada membro.

## Verificações de conclusão

- [ ] Todos os 24 membros têm contexto de declaração ou justificativa de não aplicação registrada.
- [ ] Nomes, formatos, dimensões e ordem foram conferidos contra as fontes.
- [ ] Importações, views e requisitos de copycodes foram confrontados com os chamadores.
- [ ] O participante revisou significados e perguntas, sem aprovação presumida.
- [ ] Cobertura e limites constam do [registro de leitura](reading-coverage.md).
- [ ] Decisões do destino permanecem para a Etapa 2.