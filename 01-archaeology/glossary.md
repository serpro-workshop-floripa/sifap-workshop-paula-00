# Glossário do SIFAP legado

> **Trilha:** [Kit da Equipe](../README.md) › [Etapa 1](README.md) › **Glossário**

**Artefato preenchido pela equipe durante a Etapa 1.** Uma tabela de todos os termos, abreviações e acrônimos encontrados no código Natural/Adabas — a base da linguagem ubíqua para a Etapa 2.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual contribuindo com termos dos membros de origem lidos |
| **Pré-requisitos** | Abrir os arquivos `.NSN`, `.NSP` e `.ddm` necessários à capacidade fixa |
| **Etapa** | Etapa 1 — Arqueologia |
| **Resultado esperado** | 30 ou mais termos com programa de origem e status CONFIRMADO/HIPÓTESE |

> [!NOTE]
> Guia passo a passo: [`GUIDE.md`](GUIDE.md).

---

## Por que o glossário é importante

Sistemas legados têm vocabulário próprio, raramente documentado em um local acessível — ele vive em nomes de variáveis, abreviações de campos e comentários do código. Se o trabalho da Etapa 2 não souber o significado de `DSCT`, `BENF`, `PE` ou `CTC`, escreverá uma especificação baseada em suposições sobre esses termos.

O glossário transforma abreviações de 3 a 6 caracteres em uma linguagem ubíqua compartilhada entre os artefatos do participante — e fornece a base para nomes de entidades e atributos no modelo de domínio da Etapa 3.

**Erro comum:** marcar um termo como CONFIRMADO sem evidência literal no código ou na documentação histórica. Se você inferiu o significado pelo contexto, marque-o como HIPÓTESE e identifique quem é responsável pela validação.

---

## Como preencher

| Coluna | O que registrar |
|---|---|
| **Termo** | A abreviação ou o acrônimo exatamente como aparece no código. |
| **Expansão** | O significado completo do termo. |
| **Programa** | O arquivo `.NSN` ou `.ddm` em que o termo foi encontrado. |
| **Contexto** | Explicação breve de como e onde o termo é usado. |
| **Status** | `CONFIRMADO` — evidência literal no código ou na documentação. `HIPÓTESE` — inferido pelo contexto e aguardando validação. |

### Dica de extração com o Copilot Chat

Antes de usar o prompt abaixo, cole no chat os trechos relevantes dos arquivos `.NSN`, `.NSP` ou `.ddm`:

> "Liste todas as abreviações e acrônimos usados neste código Natural. Para cada um, sugira a expansão e marque como 'CONFIRMADO' ou 'HIPÓTESE'."

Compare a sugestão do Copilot com o que você observou diretamente no código. Se coincidirem, registre como CONFIRMADO; caso contrário, registre como HIPÓTESE.

---

## Termos encontrados

| # | Termo | Expansão | Programa | Contexto | Status |
|---|---|---|---|---|---|
| 1 | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| 2 | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |
| 3 | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

> [!NOTE]
> Organize por domínio (cadastro, cálculo, batch, validação) se isso facilitar a navegação. Adicione quantas linhas forem necessárias — a meta é 30 ou mais termos.

---

## Definição de pronto

- [ ] 30 ou mais termos registrados.
- [ ] Todo termo tem um programa de origem.
- [ ] Todo termo tem status CONFIRMADO ou HIPÓTESE.
- [ ] Hipóteses marcadas para validação com um facilitador.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIA da Etapa 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Relatório de descoberta](discovery-report.md)<br/><sub>Consolidação final da etapa.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
