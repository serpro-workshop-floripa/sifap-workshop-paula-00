# Inventário do legado — Equipe PAULA SILVA

> **Trilha:** [Kit da Equipe](../README.md) › [Etapa 1](README.md) › **Inventário**

**Primeiro artefato da Etapa 1.** Examine a estrutura e conte os arquivos sem abrir nenhum programa — use somente nomes de arquivos e a estrutura de diretórios.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual realizando a varredura inicial |
| **Pré-requisitos** | Acesso ao diretório `legacy-sifap/` |
| **Etapa** | Etapa 1 — Arqueologia, Passo 1 |
| **Resultado esperado** | Contagens precisas de arquivos, padrões de nomenclatura observados e uma proposta de escopo de leitura |

> [!NOTE]
> Construa este inventário sem abrir nenhum programa. Trabalhe somente com nomes de arquivos e a estrutura de diretórios. Ele será revisado à medida que a equipe extrair regras, mapear dependências e registrar mistérios.

**Data:** 2026-09-24
**Participante responsável:** <!-- preencher -->
**Caminho examinado:** `01-archaeology/legacy-sifap/`
**Método:** enumeração de nomes de arquivos e diretórios. Nenhum programa, DDM, FDT ou documento legado foi aberto.

> [!IMPORTANT]
> **Primeira passagem.** Este inventário será revisado à medida que a leitura avançar. Nada aqui comprova leitura, conectividade entre membros ou comportamento. O registro de leitura está em [reading-coverage.md](reading-coverage.md).

---

## Estrutura de diretórios

```text
01-archaeology/legacy-sifap/                 (4 arquivos)
├── CHRONOLOGY.md
├── DECLARED-DRIFT.md
├── HOW-TO-READ-NATURAL.md
├── README.md
├── adabas-ddms/                             (6 arquivos)
│   ├── AUDIT.ddm
│   ├── BENEFIC.ddm
│   ├── FDT-150-BENEFICIARY.txt
│   ├── PAYMENT.ddm
│   ├── README.md
│   └── SOCPROG.ddm
├── legacy-docs/                             (7 arquivos)
│   ├── BUSINESS-RULES-2012.docx
│   ├── BUSINESS-RULES-2012.md
│   ├── ORIGINAL-ARCHITECTURE-1997.docx
│   ├── ORIGINAL-ARCHITECTURE-1997.md
│   ├── README.md
│   ├── TECHNICAL-MANUAL-SIFAP-2008.docx
│   └── TECHNICAL-MANUAL-SIFAP-2008.md
└── natural-programs/                        (25 arquivos)
    ├── BATCHCON.NSP
    ├── BATCHPGT.NSP
    ├── BATCHREL.NSP
    ├── CADBENEF.NSP
    ├── CADDEPEN.NSP
    ├── CADPROG.NSP
    ├── CALCBENF.NSN
    ├── CALCCORR.NSP
    ├── CALCDSCT.NSP
    ├── CCAUDIT.NSC
    ├── CCVALCPF.NSC
    ├── CONSBENF.NSP
    ├── LDASIFAP.NSL
    ├── PDACALC.NSA
    ├── PDAVALID.NSA
    ├── README.md
    ├── RELAUDIT.NSP
    ├── RELPGT.NSP
    ├── SIFAPJ01.jcl
    ├── SIFAPJ02.jcl
    ├── SUBVALCP.NSN
    ├── SUBVALNI.NSN
    ├── VALBENEF.NSN
    ├── VALDOCS.NSP
    └── VALELEG.NSN
```

| Medida | Valor |
|---|---|
| Diretórios (incluindo a raiz `legacy-sifap/`) | 4 |
| Subdiretórios | 3 |
| Profundidade máxima abaixo da raiz | 1 nível |
| Arquivos no total | 42 |

Verificação independente sugerida:

```bash
find 01-archaeology/legacy-sifap -type d | wc -l
find 01-archaeology/legacy-sifap -type f | wc -l
find 01-archaeology/legacy-sifap -type f | sed 's/.*\.//' | sort | uniq -c
```

---

## Contagem de arquivos por tipo

| Extensão | Contagem | Diretório | Tipo geral de membro |
|---|---|---|---|
| `.NSP` | 12 | `natural-programs/` | Programa Natural |
| `.NSN` | 5 | `natural-programs/` | Subprograma Natural (`CALLNAT`) |
| `.NSA` | 2 | `natural-programs/` | PDA — Parameter Data Area (`PARAMETER USING`) |
| `.NSC` | 2 | `natural-programs/` | Copycode (`INCLUDE`) |
| `.NSL` | 1 | `natural-programs/` | LDA — Local Data Area (`LOCAL USING`) |
| `.jcl` | 2 | `natural-programs/` | Job Control Language (fora do Natural) |
| `.ddm` | 4 | `adabas-ddms/` | Data Definition Module (Adabas) |
| `.txt` | 1 | `adabas-ddms/` | Listagem FDT (pelo nome do arquivo) |
| `.docx` | 3 | `legacy-docs/` | Documento de época (Word) |
| `.md` | 10 | todos | 3 documentos de época em `legacy-docs/`, 3 READMEs de subdiretório, 4 documentos de orientação na raiz |
| **Total** | **42** | | |

| Agrupamento | Contagem | Observação |
|---|---|---|
| Membros Natural/JCL | 24 | `.NSP` + `.NSN` + `.NSA` + `.NSC` + `.NSL` + `.jcl` |
| Definições de dados | 5 | 4 DDMs + 1 listagem FDT |
| Documentação | 13 | Narrativa e orientação; não é evidência executável |

> [!NOTE]
> A divisão entre 15 membros atribuídos e 9 de apoio vem do [README de natural-programs](legacy-sifap/natural-programs/README.md), não dos nomes dos arquivos. O tipo de membro vem da extensão, conforme o [guia de leitura Natural/Adabas](../.github/instructions/natural-adabas.instructions.md); nenhum comportamento individual foi inferido.

---

## Padrões de nomenclatura

Os nomes não usam delimitadores (`-`, `_`); os prefixos abaixo foram agrupados pelas letras iniciais em comum. Todas as hipóteses são **não confirmadas** e se baseiam apenas em convenções gerais de nomes Natural e abreviações comuns em português.

| Prefixo | Contagem | Membros | Extensões | Hipótese (não confirmada) |
|---|---|---|---|---|
| `BATCH` | 3 | `BATCHCON`, `BATCHPGT`, `BATCHREL` | `.NSP` | Processamento batch |
| `CAD` | 3 | `CADBENEF`, `CADDEPEN`, `CADPROG` | `.NSP` | "Cadastro" (registro/manutenção) |
| `CALC` | 3 | `CALCBENF`, `CALCCORR`, `CALCDSCT` | 1 `.NSN`, 2 `.NSP` | "Cálculo" |
| `VAL` | 3 | `VALBENEF`, `VALDOCS`, `VALELEG` | 2 `.NSN`, 1 `.NSP` | "Validação" |
| `REL` | 2 | `RELAUDIT`, `RELPGT` | `.NSP` | "Relatório" |
| `SUB` | 2 | `SUBVALCP`, `SUBVALNI` | `.NSN` | Subprograma; o trecho `VAL` sugere validação — investigar |
| `CC` | 2 | `CCAUDIT`, `CCVALCPF` | `.NSC` | Prefixo coincide com o tipo copycode |
| `PDA` | 2 | `PDACALC`, `PDAVALID` | `.NSA` | Prefixo coincide com o tipo PDA |
| `SIFAPJ` | 2 | `SIFAPJ01`, `SIFAPJ02` | `.jcl` | Nome do sistema + `J` (job) + sequência |
| `CONS` | 1 | `CONSBENF` | `.NSP` | Padrão único; "consulta" é hipótese — investigar |
| `LDA` | 1 | `LDASIFAP` | `.NSL` | Padrão único; prefixo coincide com o tipo LDA |

| Padrão de sufixo/fragmento | Membros | Observação |
|---|---|---|
| `BENEF` / `BENF` | `CADBENEF`, `VALBENEF`, `CALCBENF`, `CONSBENF` | Duas grafias do mesmo fragmento; possivelmente o limite de 8 caracteres. Desconhecido — investigar |
| `VAL` no meio do nome | `SUBVALCP`, `SUBVALNI`, `CCVALCPF`, `PDAVALID` | Fragmento repetido fora do prefixo `VAL`; conectividade não estabelecida |
| Nome-base com ano | `BUSINESS-RULES-2012`, `ORIGINAL-ARCHITECTURE-1997`, `TECHNICAL-MANUAL-SIFAP-2008` | Documentos de época; cada nome-base aparece em `.md` e `.docx` |

| Arquivo | Nome-base | Hipótese (não confirmada) |
|---|---|---|
| DDMs | `AUDIT`, `BENEFIC`, `PAYMENT`, `SOCPROG` | Nomes em inglês/abreviados, diferentes do padrão português dos programas. Desconhecido — investigar |

---

## Itens incomuns (3 principais)

| # | Caminho do arquivo | O que o torna incomum | Investigação sugerida |
|---|---|---|---|
| 1 | [`adabas-ddms/FDT-150-BENEFICIARY.txt`](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt) | Única extensão `.txt`; único nome com número; único FDT para 4 DDMs; nome em inglês diferente de `BENEFIC.ddm` | Ler com o papel de DBA via `/map-source-data`; comparar com `BENEFIC.ddm`; tratar datas e contagens como observação histórica, não medição atual |
| 2 | [`natural-programs/LDASIFAP.NSL`](legacy-sifap/natural-programs/LDASIFAP.NSL) | Única extensão `.NSL`; único prefixo `LDA`; contém o nome do sistema | Localizar `LOCAL USING LDASIFAP` via `/map-dependencies` antes de ler o conteúdo |
| 3 | [`natural-programs/VALDOCS.NSP`](legacy-sifap/natural-programs/VALDOCS.NSP) e [`natural-programs/CALCBENF.NSN`](legacy-sifap/natural-programs/CALCBENF.NSN) | Famílias `VAL` e `CALC` misturam programa e subprograma: `VALDOCS` é o único `.NSP` entre os `VAL`; `CALCBENF` é o único `.NSN` entre os `CALC` | Verificar se são chamados por `CALLNAT` ou executados diretamente; registrar em `dependency-map.md` |

> [!NOTE]
> O critério "maior arquivo por tamanho" não foi aplicado: nenhuma medição de tamanho foi realizada nesta passagem. Execute `ls -lS 01-archaeology/legacy-sifap/natural-programs` para completá-lo. Os três pares `.md`/`.docx` em `legacy-docs/` também merecem atenção: a [cronologia](legacy-sifap/CHRONOLOGY.md) orienta tratar exportações do mesmo documento como uma única fonte.

---

## Ordem de leitura proposta

Ordem orientada à capacidade-alvo fixa do [guia da Etapa 1](GUIDE.md): listar, pesquisar e detalhar **todos** os beneficiários migrados, aplicando as regras legadas de validação. A escolha abaixo usa somente nomes e posição estrutural; a relevância real de cada membro só se confirma na leitura.

1. **DDMs e FDT, com o papel de DBA** (`/map-source-data`): `BENEFIC.ddm` e `FDT-150-BENEFICIARY.txt` primeiro; depois `SOCPROG.ddm`, `PAYMENT.ddm` e `AUDIT.ddm` na medida em que os dados relacionados forem exigidos pela consulta.
2. **Ponto de entrada de consulta:** `CONSBENF.NSP` (prefixo único `CONS`; hipótese de consulta a confirmar).
3. **Validação:** `VALBENEF.NSN`, `VALDOCS.NSP`, `VALELEG.NSN`.
4. **Membros de apoio, somente quando referenciados** por `USING`, `INCLUDE` ou `CALLNAT` nos membros acima: `PDAVALID.NSA`, `SUBVALCP.NSN`, `SUBVALNI.NSN`, `CCVALCPF.NSC`, `LDASIFAP.NSL`. A conectividade exige `/map-dependencies`.
5. **Cadastro — provisório:** `CADBENEF.NSP`, `CADDEPEN.NSP`, `CADPROG.NSP`, se trouxerem evidência de campos, identificadores ou registros relacionados.
6. **Pontos de entrada do batch, relatórios e cálculo — provisório:** `SIFAPJ01.jcl`, `SIFAPJ02.jcl`, `BATCHPGT.NSP`, `BATCHREL.NSP`, `BATCHCON.NSP`, `RELPGT.NSP`, `RELAUDIT.NSP`, `CALCBENF.NSN`, `CALCCORR.NSP`, `CALCDSCT.NSP`, `PDACALC.NSA`, `CCAUDIT.NSC` — somente se valores exibidos, auditoria ou população da origem exigirem evidência.
7. **Documentos de época por último:** `legacy-docs/*` para comparar narrativa e código, registrando divergências em `mysteries-found.md` (ver [desvios declarados](legacy-sifap/DECLARED-DRIFT.md)).

> [!IMPORTANT]
> Os itens 5 e 6 são extensões provisórias do escopo de leitura. A prontidão da origem populada e da rota de extração pertence ao `@dba`, registrada a partir do [template de prontidão](../docs/data-migration/source-readiness.template.md). Regras candidatas seguem para `/extract-business-rules`.

---

## Definição de pronto

- [ ] O inventário existe com contagens precisas.
- [ ] Somente padrões de nomenclatura observados e anomalias estruturais estão registrados.
- [ ] O registro de leitura foi inicializado sem marcar a enumeração de arquivos como leitura concluída.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIA da Etapa 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Catálogo de regras](business-rules-catalog.md)<br/><sub>Passo 2 — extração de regras.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
