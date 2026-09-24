# Mapa de dados de origem

> **Caminho:** [Kit da Equipe](../README.md) > [Etapa 1](README.md) > **Mapa de dados**

**Definições e evidências de dados observadas na leitura dos 4 DDMs, da listagem FDT e dos 24 membros Natural/JCL.**

> [!IMPORTANT]
> Leitura estática assistida por `@archaeologist` em 2026-09-24, gerada com `/map-source-data`.
> Todo significado abaixo é **declarado** (comentário/remark da fonte) ou **observado** (instrução executável), nunca confirmado em runtime.
> Nenhuma contagem atual da origem foi medida. Nenhum mapeamento PostgreSQL foi decidido. Revisão humana do DBA e do QA está pendente.

| Campo | Evidência da equipe |
|---|---|
| Participante / evidência de revisão DBA-QA / data | <!-- preencher: participante --> / revisão DBA-QA pendente / 2026-09-24 |
| Versão da origem e escopo de leitura autorizado | Corpus local `01-archaeology/legacy-sifap/` (sem versão registrada). Escopo autorizado pelo participante: todos os DDMs, o FDT e todos os membros Natural/JCL |
| Cobertura de DDM/FDT e definições ausentes | 4/4 DDMs e 1/1 FDT lidos integralmente. Ausentes: FDT de FNR 151, 152 e 153; DDMs de FNR 154, 155 e 156 (citados em `AUDIT.ddm#L142-L145`) |
| Referência de evidência da população | **BLOQUEADO** — nenhuma medição atual. Os valores em trailers de DDM e no FDT são estatísticas arquivadas de 2018 |
| Status | Rascunho — aguardando revisão humana |

## Arquivos e identificadores de origem

| DDM / FDT | Vínculo de arquivo observado | Chaves / descritores declarados | Evidência de acesso pelo código | Questão em aberto |
|---|---|---|---|---|
| `BENEFIC.ddm` | DBID 057 / FNR 150 (`BENEFIC.ddm#L31-L32`); programas citam "FILE 150" (ex.: `CADBENEF.NSP#L11`) | Únicos: `AA` NUM-REGISTRATION (`#L39`), `AB` NUM-CPF (`#L40`), `AM` NUM-NIS (`#L52`), `AN` NUM-BENEFIT (`#L53`). Descritores: `AF`, `BG`, `BJ`, `CA`, `CB`, `CE`, `GA`, `HA`, `IA`, `IC`, `IG`, `JB`. Derivados: `PN`, `SA`, `S2`, `S3`, `H1` (`#L144-L153`). Sequência padrão `AA` (`#L31`) | `FIND ... NUM-CPF`: `CONSBENF.NSP#L149`, `CADBENEF.NSP#L206`, `CADDEPEN.NSP#L96`, `VALELEG.NSN#L84`, `CALCBENF.NSN#L166`, `CALCDSCT.NSP#L93`, `BATCHREL.NSP#L142`, `RELPGT.NSP#L154`. `FIND ... NUM-NIS`: `CONSBENF.NSP#L157`. `READ BY NUM-CPF`: `BATCHPGT.NSP#L250`. `STORE`: `CADBENEF.NSP#L295`. `UPDATE`: `CADBENEF.NSP#L318`, `CADDEPEN.NSP#L203` | Qual chave identifica o beneficiário na migração: `AA`, `AB` ou ISN? |
| `FDT-150-BENEFICIARY.txt` | ADAREP de DB 057 / FILE 150 (`FDT-150-BENEFICIARY.txt#L4`); RUN DATE 2018-03-14, LAST FDT CHANGE 2015-11-19 (`#L5-L6`) | Opções `DE`/`UQ`/`NU`/`FI`/`MU`/`PE` por campo (`#L13-L87`); derivados (`#L89-L95`); 21 descritores declarados (`#L134-L135`) | Nenhum programa lê o FDT; é listagem física | Por que `JA`/`JB` não aparecem (ver Q3)? |
| `SOCPROG.ddm` | DBID 057 / FNR 151 (`SOCPROG.ddm#L20-L21`); `BATCHPGT.NSP#L300` e `CADPROG.NSP#L109` citam "FILE 151"; `CADPROG.NSP#L10`, `VALELEG.NSN#L99` e `CALCBENF.NSN#L187` citam "FILE 155" | Único: `AA` COD-PROGRAM "PRIMARY KEY" (`#L28`). Descritores: `AD`, `AI`, `CJ`. Superdescritor `S2` (`#L102-L103`) | `FIND ... COD-PROGRAM`: `CADPROG.NSP#L111`, `VALELEG.NSN#L100`, `CALCBENF.NSN#L188`, `BATCHPGT.NSP#L302`. `STORE`: `CADPROG.NSP#L139` | Q1 — 151 ou 155? |
| `PAYMENT.ddm` | DBID 057 / FNR 152 (`PAYMENT.ddm#L26-L27`); programas citam "FILE 160" (`CALCBENF.NSN#L308`, `CALCDSCT.NSP#L76`, `CALCCORR.NSP#L10`, `CONSBENF.NSP#L14`, `BATCHCON.NSP#L12`) | Único: `AA` NUM-PAYMENT (`#L34`). Descritores: `AB`, `AD`, `AE`, `AF`, `DA`, `DB`, `EA`, `EF`, `EG`, `FF`, `GD`, `GH`. Derivados: `SA`, `S1`, `S2`, `S3` (`#L125-L132`) | `READ BY NUM-CPF`: `CONSBENF.NSP#L271`, `CALCCORR.NSP#L174`. `READ (1) BY NUM-PAYMENT DESCENDING`: `BATCHPGT.NSP#L240`. `FIND NUMBER ... SUPER-CPF-PERIOD`: `BATCHPGT.NSP#L294`. `FIND ... NUM-PAYMENT`: `CALCDSCT.NSP#L79`, `BATCHCON.NSP#L171`. `READ BY YEAR-MONTH-REF`: `BATCHREL.NSP#L125`, `RELPGT.NSP#L123`. `STORE`: `CALCBENF.NSN#L319`, `BATCHPGT.NSP#L488`. `UPDATE`: `CALCCORR.NSP#L208`, `CALCDSCT.NSP#L186`, `BATCHCON.NSP#L211` | Q1 — 152 ou 160? ISN não é chave estável (`#L162-L163`) |
| `AUDIT.ddm` | DBID 057 / FNR 153 (`AUDIT.ddm#L23-L24`); `CCAUDIT.NSC#L9-L10` cita "FILE 153"; `BATCHCON.NSP#L12` e `RELAUDIT.NSP#L13` citam "FILE 170" | Único: `AA` NUM-AUDIT (`#L31`). Descritores: `AB`, `AE`, `BA`, `CA`, `CB`, `CC`, `EA`, `EG`. Derivados: `SA`, `S1`, `S2`, `S3` (`#L98-L105`) | `READ (1) BY NUM-AUDIT DESCENDING`: `CCAUDIT.NSC#L66`, `BATCHCON.NSP#L116`. `STORE`: `CCAUDIT.NSC#L98`, `BATCHCON.NSP#L322`, `#L341`. `READ BY DT-EVENT`: `RELAUDIT.NSP#L111`. `HISTOGRAM`: `RELAUDIT.NSP#L260` | Q1 — 153 ou 170? Partições FNR 154–156 sem DDM (Q16) |

## Evidências no nível de campo

Formato lógico = DDM. Armazenamento físico = FDT (somente FNR 150). "Sem acesso observado" significa que nenhum dos 24 membros declara o campo em view e o usa em instrução executável.

### FNR 150 — `BENEFIC.ddm` × `FDT-150-BENEFICIARY.txt`

| Campo de origem / nome lógico | Formato / tamanho / escala declarados | Marcadores de armazenamento / descritor | Limites de grupo / ocorrência | Significado observado e evidência | Incerteza |
|---|---|---|---|---|---|
| `AA` NUM-REGISTRATION | DDM N 11 (`#L39`); FDT U 11 (`FDT#L13`) | DDM storage vazio, `U`; FDT `DE,UQ,FI` | Raiz | Remark "ALTERNATE ISN/REGISTRATION"; sequência padrão do DDM | Sem acesso observado. Diferença FI no FDT × vazio no DDM |
| `AB` NUM-CPF | A 11 (`#L40`); FDT A 11 (`FDT#L14`) | `U`; FDT `DE,UQ` | Raiz | "UNFORMATTED CPF". Escritores usam `MOVE EDITED ... (EM=99999999999)` (`CADBENEF.NSP#L205`) | `CONSBENF.NSP#L294-L300` cita CPF armazenado com comprimento variável (Q5) |
| `AC` FULL-NAME | A 60 (`#L41`); FDT `NU` (`FDT#L15`) | `N`; base do fonético `PN` (`#L144-L145`) | Raiz | "OFFICIAL LEGAL NAME". Escrito em `CADBENEF.NSP#L275-L318`; exibido em `CONSBENF.NSP` | — |
| `AD` MOTHER-NAME | A 60 (`#L42`); FDT `NU` | `N` | Raiz | Remark "(REQUIRED)" | Sem acesso observado. `NU` não prova obrigatoriedade |
| `AE` FATHER-NAME | A 60 (`#L43`); FDT `NU` | `N` | Raiz | "(OPTIONAL)" | Sem acesso observado |
| `AF` DT-BIRTH | N 8 (`#L44`); FDT U 8 `DE,NU` (`FDT#L18`) | DDM storage vazio, `D`; base de `SA` e `H1` | Raiz | "YYYYMMDD" | Q4: `NU` só no FDT; resíduos YYMMDD tratados em `BATCHPGT.NSP#L333-L346` |
| `AG` SEX | A 1 (`#L45`); FDT `FI` | `F` | Raiz | "M/F/I (I=UNDEFINED)" | `CADBENEF.NSP` aceita apenas M/F no cadastro |
| `AH` MARITAL-STAT | A 1 (`#L46-L47`); FDT `FI` | `F` | Raiz | S/C/D/V/U | Sem acesso observado |
| `AI` RG-NUMBER | A 15 (`#L48`); FDT `NU` | `N` | Raiz | Escrito em `CADBENEF.NSP`; declarado em view de `VALDOCS.NSP#L21` sem leitura | — |
| `AJ` RG-AGENCY / `AK` RG-UF / `AL` RG-DT-ISSUE | A 10 / A 2 / N 8 (`#L49-L51`); FDT `NU` (`FDT#L22-L24`) | `N` | Raiz | Órgão, UF e data de emissão | Sem acesso observado |
| `AM` NUM-NIS | N 11 (`#L52`); FDT U 11 `DE,UQ,NU` (`FDT#L25`) | `N`, `U` | Raiz | "NIS/PIS-PASEP (ADDED 2001)". `FIND` em `CONSBENF.NSP#L157`; teste `= 0` em `VALELEG.NSN#L249-L267` | Único e com supressão de nulos: vazio não é indexado (`FDT#L148-L150`) |
| `AN` NUM-BENEFIT | N 13 (`#L53`); FDT `DE,UQ,NU` (`FDT#L26`) | `N`, `U` | Raiz | "GRANT NUMBER (ADDED 2003)" | Sem acesso observado |
| `BA` GRP-ADDRESS | Grupo (`#L57`); FDT `GR` (`FDT#L27`) | — | Grupo nível 1 | Contém `BB`–`BJ` | Várias views declaram `UF`/`COD-REGION` fora do grupo (Q20) |
| `BB` STREET-ADDRESS | A 60 (`#L58`); FDT `NU` | `N` | `BA` | Escrito de `#ADDRESS (A80)` em `CADBENEF.NSP#L277-L279` | Truncamento declarado dos últimos 20 bytes (Q9) |
| `BC` NUMBER | A 10 (`#L59`) | `N` | `BA` | Lido em `CONSBENF.NSP#L208-L210` | Nenhum escritor observado |
| `BD` ADDRESS-COMPL | A 30 (`#L60`) | `N` | `BA` | Complemento | Sem acesso observado |
| `BE` DISTRICT | A 40 (`#L61`) | `N` | `BA` | Lido em `CONSBENF.NSP`; declarado em view de `CADBENEF.NSP` | Nenhum escritor observado |
| `BF` CITY | A 40 (`#L62`) | `N` | `BA` | Escrito em `CADBENEF.NSP`; exibido em `CONSBENF.NSP` | — |
| `BG` UF | A 2 (`#L63`); FDT `DE` | `D`; parte de `S2` (`#L148-L149`) | `BA` | "STATE ABBREVIATION"; validado contra 27 UFs em `VALBENEF.NSN#L73-L100` | — |
| `BH` CEP | N 8 (`#L64`); FDT `NU` | `N` | `BA` | "POSTAL CODE WITHOUT HYPHEN" | — |
| `BI` COD-IBGE | N 7 (`#L65`) | `N` | `BA` | Código IBGE | Sem acesso observado |
| `BJ` COD-REGION | A 2 (`#L66`); FDT `DE` | `D` | `BA` | "01-05 OR 99 (SPECIAL)"; escrito com `MOVE EDITED (EM=99)` em `CADBENEF.NSP` | Q6: `PDACALC.NSA#L59` diz "01-27 OR 99" |
| `CA` COD-PROGRAM | A 4 (`#L70`); FDT `DE` | `D`; parte de `S3` (`#L150-L151`) | Raiz | Código do programa; escrito com `MOVE EDITED (EM=9999)` | Zeros à esquerda dependem do escritor |
| `CB` DT-REGISTRATION | N 8 (`#L71`); FDT `DE` | `D` | Raiz | Escrito com `*DATN` na inclusão (`CADBENEF.NSP`) | — |
| `CC` DT-START-BENEF / `CD` DT-END-BENEF | N 8 / N 8 (`#L72-L73`) | — | Raiz | `CD`: "0 = NO END DATE" | Sem acesso observado; sentinela 0 |
| `CE` STAT-BENEFICIARY | A 1 (`#L74-L75`); FDT `DE,FI` | `F`, `D`; parte de `S2`/`S3` | Raiz | A/S/C/I/D. Rótulos de exibição em `CONSBENF.NSP#L228-L241` | `D`: DDM "DISCONNECTED", tela "TERMINATED" |
| `CF` REASON-STAT / `CG` DT-LAST-STAT | A 3 / N 8 (`#L76-L77`) | `N` | Raiz | Motivo em "INTERNAL TABLE" | Sem acesso observado; tabela interna ausente |
| `CH` AMT-FAMILY-INCOME | P 9,2 (`#L78`); FDT P **5 bytes** "9,2 PACKED" (`FDT#L44`) | `N` | Raiz | "DECLARED INCOME"; views declaram `(P9.2)` (ex.: `CONSBENF.NSP#L37`) | Q2: precisão lógica × 5 bytes físicos |
| `CI` QTY-FAMILY-MEMBERS | N 2 (`#L79`); FDT U 2 | — | Raiz | Membros do domicílio | Sem acesso observado |
| `CJ` IND-PERCAP-INCOME | P 7,2 (`#L80`); FDT P **4 bytes** (`FDT#L46`) | `N`; parte de `H1` | Raiz | "CALCULATED PER-CAPITA INCOME" | Nenhum cálculo ou escritor observado; Q2 |
| `CK` QTY-DEPEND | N 2 (`#L81-L82`); FDT `NU` | `N` | Raiz | "ACTIVE DEPENDENT COUNT (ADDED 2013)"; usado como índice em `CADDEPEN.NSP#L193` | Q8 |
| `CL` IND-DOCS-OK | A 1 (`#L83`); FDT `FI` | `F` | Raiz | "S/N (ADDED 2012)"; lido em `VALELEG.NSN#L84-L97` | Nenhum escritor observado |
| `DA` GRP-DEPEND | PE (`#L87`); FDT `PE` (`FDT#L55`) | — | **PE 1:10**; máximo 10 (`FDT#L119`) | Dependentes; view em `CADDEPEN.NSP#L19-L25` | Ordem e identidade das ocorrências (Q8) |
| `DB` CPF-DEPEND | A 11 (`#L88`) | `N` | `DA` | "CPF OR 00000000000" | Zero como ausência de CPF |
| `DC` NAME-DEPEND / `DD` DT-BIRTH-DEPEND | A 60 / N 8 (`#L89-L90`) | `N` | `DA` | Escritos em `CADDEPEN.NSP#L191-L203` | — |
| `DE` RELATION | A 2 (`#L91-L92`); FDT `FI` | `F` | `DA` | DDM: FI/CJ/NT/TU | Q7: `CADDEPEN.NSP#L126` aceita FI/CO/IR/OU |
| `DF` STAT-DEPEND / `DG` IND-DISABILITY | A 1 / A 1 (`#L93-L94`); FDT `FI` | `F` | `DA` | Declarados na view de `CADDEPEN.NSP` | Nenhum escritor observado |
| `EA` PHONE-LANDLINE / `EB` PHONE-MOBILE / `EC` EMAIL | A 14 / A 15 / A 80 (`#L98-L100`) | `N` | Raiz | `EB` escrito em `CADBENEF.NSP` | `EA`/`EC` sem acesso observado |
| `ED` NUM-PHONE | A 15 (`#L101`); FDT `MU,NU` (`FDT#L65`) | `N` | **MU 1:5**; máximo 5 (`FDT#L120`) | Telefones adicionais | Sem acesso observado |
| `FA`–`FD` biometria | A 1 / N 8 / A 6 / A 64 (`#L105-L108`) | `F` / `N` | Raiz | `FD`: "SHA-256 TEMPLATE (NOT IMPL.)" | Sem acesso observado |
| `GA` DT-INSERT / `GB` HR-INSERT / `GC` USR-INSERT | N 8 `D` / N 6 / A 8 (`#L112-L114`) | `GA` `DE` | Raiz | Controle de inserção | Nenhum escritor observado (Q22) |
| `GD` DT-LAST-UPDATE / `GE` / `GF` | N 8 / N 6 / A 8 (`#L115-L117`) | `N` | Raiz | `GD` escrito em `CADBENEF.NSP` | `GE`/`GF` sem escritor observado |
| `GG` NUM-VERSION | N 5 (`#L118`) | — | Raiz | "CONCURRENCY CONTROL" | Sem acesso observado |
| `HA`–`HE` dados bancários | A 3 `D` / A 6 / A 13 / A 1 / A 1 (`#L122-L126`) | `N`/`F` | Raiz | Banco, agência, conta, tipo, portabilidade | Sem acesso observado |
| `IA` IND-DEATH / `IB` DT-DEATH | A 1 `D` / N 8 (`#L130-L131`) | `F` / `N` | Raiz | "SISOBI CROSS-CHECK 2001"; `IB` "0=NOT PROVIDED" | Sem acesso observado |
| `IC` / `ID` / `IE` / `IG` bloqueio | A 2 `D` / A 1 / A 20 / N 5 `D` (`#L132-L135`) | `N`/`F` | Raiz | Bloqueio, decisão judicial, processo, órgão pagador | Sem acesso observado |
| `JA` IND-LEGAL-REPRESENTATIVE / `JB` CPF-REPRESENTATIVE | A 1 / A 11 `D` (`#L139-L140`) | `F` / `N` | Raiz | Representante legal (2009) | **Ausentes no FDT** (Q3) |
| `PN` / `SA` / `S2` / `S3` / `H1` | A 20 / N 4 / A 3 / A 5 / A 6 (`#L144-L153`); FDT `#L91-L95` | Derivados | — | `PN`=AC; `SA`=AF(1-4); `S2`=BG+CE; `S3`=CA+CE; `H1`=AF+CJ HYPEREXIT 03 | `SA`: DDM N, FDT U. Hyperexit 03 não está no corpus |

### FNR 151 — `SOCPROG.ddm`

| Campo de origem / nome lógico | Formato / tamanho / escala declarados | Marcadores de armazenamento / descritor | Limites de grupo / ocorrência | Significado observado e evidência | Incerteza |
|---|---|---|---|---|---|
| `AA`–`AI` identificação | `AA` A 4 `U`; `AB` A 60; `AC` A 10; `AD` A 1 `D`; `AE` A 10; `AF` A 20; `AG`/`AH` N 8; `AI` A 1 `D` (`#L28-L37`) | `AD`/`AI` `F` | Raiz | `AD` A/T/P = ASSISTANCE/EMPLOYMENT/SOCIAL SECURITY; `AH` "0=ACTIVE"; `AI` A/I/E | `CADPROG.NSP#L18` comenta P=PENSION, T=WORK |
| `BA`–`BD` valores-base | P 7,2 / P 7,2 / P 9,2 / P 7,2 (`#L41-L44`) | — | Raiz | Valores mensais base, teto e piso | `CADPROG.NSP#L130` grava `#AMT-CALC (P9.2)` em `BA` (Q18) |
| `BE` PCT-ANNUAL-ADJUST / `BF` | P 3,2 / N 8 (`#L45-L46`) | `N` | Raiz | Percentual de reajuste | Sem acesso observado |
| `BG` FACTOR-K | P 5,4 (`#L47-L51`) | `N` | Raiz | ">>> UNDOCUMENTED <<<", inserido em 08/2008 | Q18: nenhuma leitura ou escrita observada |
| `BH` FACTOR-ADJUST | P 3,4 (`#L52`) | `N` | Raiz | "FACTOR ON BASE AMOUNT (2002)" | Aplicado em `CALCBENF.NSN#L262` e `BATCHPGT.NSP#L432` |
| `CA`–`CJ` elegibilidade | `CA` P 7,2; `CB`/`CC` N 3 ("0=NONE"); `CD`,`CF`–`CI` A 1; `CE` N 2; `CJ` A 5 `D` (`#L56-L65`) | `F`/`N` | Raiz | Critérios; `CJ` "SEE TICKET 4471/2012" | `CD`–`CI` sem acesso observado |
| `DA` GRP-CALC-BAND | `DB`/`DC`/`DE` P 7,2; `DD` P 3,4; `DF` A 1 (`#L69-L74`) | `N`/`F` | **PE 1:5** | Faixas de cálculo | Sem acesso observado; programas usam tabelas inline |
| `EA` TYPE-DISC-APPLIC | A 3 (`#L78-L83`) | `N` | **MU 1:8** | IR/JD/CS/PA/EM/TX/OU/EX | Sem acesso observado |
| `FA` GRP-REGIONAL-PARAM | `FB` A 2; `FC` P 3,4; `FD` P 7,2; `FE` A 1 (`#L86-L91`) | `N`/`F` | **PE 1:6** | "1=N 2=NE 3=CO 4=SE 5=S 6=ESP" | Sem acesso observado; Q6 |
| `GA`–`GD` controle / `S2` | N 8 / A 8 / N 8 / A 8 (`#L95-L98`); `S2`=AD+AI (`#L102-L103`) | — | Raiz | Inserção e atualização | Nenhum escritor observado |

### FNR 152 — `PAYMENT.ddm`

| Campo de origem / nome lógico | Formato / tamanho / escala declarados | Marcadores de armazenamento / descritor | Limites de grupo / ocorrência | Significado observado e evidência | Incerteza |
|---|---|---|---|---|---|
| `AA`–`AF` chaves | `AA` N 15 `U`; `AB` A 11 `D`; `AC` N 11; `AD` A 4 `D`; `AE` N 6 `D`; `AF` N 6 `D` (`#L34-L39`) | `AC` `N` | Raiz | `AA` "UNIQUE SEQUENCE" = último + 1 (`BATCHPGT.NSP#L240`, `#L475`); `AB` CPF; `AE` YYYYMM | Q13: `CALCBENF.NSN#L308-L319` grava sem `AA`. `AC` sem acesso observado |
| `BA`–`BD` valores | P 9,2 / P 9,2 / **P 7,2** / P 9,2 (`#L43-L46`) | `BC`/`BD` `N` | Raiz | Bruto, líquido, total de descontos, abono | Q12: `BC` recebe `#AMT-DISC (P9.2)` |
| `CA` GRP-DISC | `CB` A 3; `CC` P 7,2; `CD` P 3,2; `CE` A 20; `CF`/`CG` N 8 (`#L50-L56`) | `N` | **PE 1:8** | Descontos aplicados; `CG` "0=UNDEFINED" | Q11: `CALCDSCT.NSP#L22-L23`, `#L45` usa códigos de 1 caractere |
| `DA`–`DG` status | `DA` A 1 `D`; `DB` N 8 `D`; `DC` N 6; `DD`–`DF` N 8; `DG` A 3 (`#L60-L68`) | `F`/`N` | Raiz | `DA` P/G/E/C/D/X/R | Q10 |
| `EA`–`EG` bancário | A 3 `D` / A 6 / A 13 / A 1 / A 3 / N 8 `D` / A 1 `D` (`#L72-L80`) | `N`/`F` | Raiz | `EF` "(ADDED 1999 - NOT DB)" com `D`; `EG` N/R/A/C | Q10; Q14 (`BATCHCON.NSP#L209`) |
| `FA`–`FG` SIAFI e lote | A 12 / A 12 / A 6 / A 5 / A 1 / N 8 `D` / N 6 (`#L84-L90`) | `N`/`F` | Raiz | `FF`/`FG` escritos em `BATCHPGT.NSP` | `FA`–`FE` sem acesso observado |
| `GA`–`GK` conciliação e estorno | `GC`/`GI` P 9,2; `GD` A 2 `D`; `GH` N 15 `D`; demais A/N (`#L94-L105`) | `N`/`F` | Raiz | `GH` "ORIGINAL PAYMENT (2003)"; `GI`–`GK` escritos em `CALCCORR.NSP#L203-L208` | `GG`/`GH` sem acesso observado |
| `HA`/`HB` hashes / `HC` COD-OCCURRENCE | A 64 / A 64 / A 3 (`#L109-L112`) | `N` | `HC` **MU 1:10** | Hashes SHA-256 e ocorrências bancárias | Sem acesso observado |
| `IA`–`IF` controle | N 8 / N 6 / A 8 / N 8 / N 6 / A 8 (`#L116-L121`) | — | Raiz | `IC` "USUALLY 'BATCH'" | Nenhum escritor observado |
| `SA` / `S1` / `S2` / `S3` | N 4 / A 17 / A 11 / A 7 (`#L125-L132`) | Derivados | — | `S1` = CPF + YYYYMM, usado em `BATCHPGT.NSP#L294` | — |

### FNR 153 — `AUDIT.ddm`

| Campo de origem / nome lógico | Formato / tamanho / escala declarados | Marcadores de armazenamento / descritor | Limites de grupo / ocorrência | Significado observado e evidência | Incerteza |
|---|---|---|---|---|---|
| `AA`–`AE` evento | N 15 `U` / N 8 `D` / N 6 / N 14 / A 8 `D` (`#L31-L35`) | `AD`/`AE` `N` | Raiz | `AA` sequência = último + 1 (`CCAUDIT.NSC#L64-L70`); `AD` YYYYMMDDHHMMSS | `BATCHCON.NSP#L311-L343` numera fora de `CCAUDIT` |
| `BA` COD-ACTION / `BB` / `BC` | A 2 `D` / A 8 / A 80 (`#L39-L51`) | `BA` `F` | Raiz | `BA`: IN/AL/EX/CO/LG/LO/BT/ER/AU/RE (`#L39-L49`) | Q15: `DV` e `CN` usados, ausentes do domínio |
| `CA` TYPE-ENTITY / `CB` ID-ENTITY / `CC` NUM-CPF-AFFECTED | A 4 `D` / A 15 `D` / A 11 `D` (`#L55-L57`) | `CC` `N` | Raiz | BENF/PGTO/PROG/ADMN/SIST | `CB` recebe CPF, período ou NUM-PAYMENT conforme o escritor |
| `DA` GRP-BEFORE / `DD` GRP-AFTER | `DB`/`DE` A 30; `DC`/`DF` A 80 (`#L61-L66`) | `N` | Grupos com **MU 1:20** paralelos | Estado anterior e posterior | Correspondência por índice não declarada; sem acesso observado |
| `DG` AMT-PREV / `DH` AMT-NEW | A 60 / A 60 (`#L67-L70`) | `N` | Raiz | "SCALAR (ADDED 2014)"; recebem valores numéricos em `BATCHCON.NSP#L326-L343` | Valor monetário em campo alfanumérico |
| `EA`–`EH` usuário e origem | A 8 `D` / A 40 / A 3 / A 10 / A 15 / A 20 / A 8 `D` / A 8 (`#L74-L81`) | — | Raiz | `EC` ADM/OPR/CON/AUD/SUP | `EC` nunca preenchido (`CCAUDIT.NSC#L50-L51`) |
| `FA`–`FE` batch / `GA`–`GB` correlação | N 6 / N 10 / A 16 / A 1 / A 120; A 36 / N 3 (`#L85-L94`) | `N`/`F` | Raiz | `FC`/`FD` preenchidos só com ação BT (`CCAUDIT.NSC#L91-L95`) | Demais sem acesso observado |
| `SA` / `S1` / `S2` / `S3` | N 6 / A 10 / A 27 / A 16 (`#L98-L105`) | Derivados | — | `S2` = entidade + chave + data | "HEAVY QUERIES MUST USE S2" (`#L18`) |

## Relacionamentos e acesso

| Relacionamento de origem | Evidência de leitura / gravação | Declarado ou observado? | Integridade não estabelecida | Responsável |
|---|---|---|---|---|
| BENEFIC `AB` NUM-CPF → PAYMENT `AB` NUM-CPF | `CONSBENF.NSP#L271`; `BATCHREL.NSP#L142`; `RELPGT.NSP#L154`; gravação `BATCHPGT.NSP#L476` | Observado | `RELPGT.NSP#L155-L157` ignora beneficiário ausente: pagamentos órfãos são possíveis | DBA |
| BENEFIC `AA` → PAYMENT `AC` NUM-REGISTRATION | Remark "BENEFICIARY REGISTRATION" (`PAYMENT.ddm#L36`) | Declarado (remark) | Nenhum leitor ou escritor observado | DBA |
| BENEFIC `CA` COD-PROGRAM → SOCPROG `AA` | `BATCHPGT.NSP#L302`; `CALCBENF.NSN#L188`; `VALELEG.NSN#L100` | Observado | `BATCHPGT.NSP#L303-L312` trata programa inexistente como rejeição | DBA |
| PAYMENT `AD` COD-PROGRAM → SOCPROG `AA` | Gravado a partir do beneficiário em `BATCHPGT.NSP` e `CALCBENF.NSN#L310` | Observado | Programa do pagamento pode divergir do atual do beneficiário | DBA |
| PAYMENT `GH` → PAYMENT `AA` | Remark "ORIGINAL PAYMENT (2003)" (`PAYMENT.ddm#L102`) | Declarado | Nenhum acesso observado | DBA |
| AUDIT `CA`+`CB` → entidade | `CADBENEF.NSP` (BENF/CPF), `CADPROG.NSP` (PROG/código), `BATCHPGT.NSP#L540-L545` (PGTO/período), `BATCHCON.NSP` (PGTO/NUM-PAYMENT), `CALCCORR.NSP` (PGTO/CPF) | Observado | Chave polimórfica sem tipagem | DBA |
| AUDIT `CC` → BENEFIC `AB` | `CCAUDIT.NSC#L90` | Observado | Vazio para PROG e BT | DBA |
| BENEFIC `DA` (PE) → dependente | Embutido no registro; nenhum `FIND` por `CPF-DEPEND` | Observado | Dependente não é registro independente | DBA |

### Campos exibidos pela consulta legada

`CONSBENF.NSP` é a única consulta online de beneficiário observada. Seleção por CPF (`#L149`) ou NIS (`#L157`); exibição em `#L243-L260`; histórico de pagamentos em `#L263-L288`.

| Dado exibido | Campo de origem | Evidência | Observação |
|---|---|---|---|
| CPF mascarado | BENEFIC `AB` | `CONSBENF.NSP#L199-L205`, `#L298-L311` | Máscara depende do valor numérico (Q5) |
| Nome, nascimento, sexo | `AC`, `AF`, `AG` | `CONSBENF.NSP#L243-L260` | Data exibida sem formatação |
| Endereço, cidade/UF, CEP, região | `BB`, `BC`, `BE`, `BF`, `BG`, `BH`, `BJ` | `CONSBENF.NSP#L207-L210` | `COMPRESS` de rua, número e bairro |
| Status e descrição | `CE` | `CONSBENF.NSP#L228-L241` | `NONE` → "UNKNOWN" |
| Programa, renda familiar, dependentes, NIS, data de cadastro | `CA`, `CH`, `CK`, `AM`, `CB` | `CONSBENF.NSP#L243-L260` | — |
| Até 12 pagamentos: período, bruto, líquido, status, tipo | PAYMENT `AE`, `BA`, `BB`, `DA`, `EG` | `CONSBENF.NSP#L271-L284` | Q23: título "LAST 12", leitura ascendente por CPF |

## População e qualidade

Use o [template de prontidão da origem](../docs/data-migration/source-readiness.template.md) com `@dba`. Nenhum registro de beneficiário foi copiado para este documento.

| População de origem | Método / horário da medição | Contagem / cobertura | Observação de qualidade | Referência de evidência / bloqueio |
|---|---|---|---|---|
| FNR 150 BENEFICIARY | Não medido | **unknown** | Arquivado: 4.201.884 em ADAREP 14/03/2018 (`BENEFIC.ddm#L169`; `FDT#L115`) — não é medição atual | BLOQUEADO — prontidão com `@dba` |
| FNR 151 SOCIAL-PROGRAM | Não medido | **unknown** | Arquivado: 45 (`SOCPROG.ddm#L119`) | BLOQUEADO |
| FNR 152 PAYMENT | Não medido | **unknown** | Arquivado: 611.902.774 (`PAYMENT.ddm#L148`) × cabeçalho "APPROX. 180 MILLION" (`#L18`) | BLOQUEADO |
| FNR 153 AUDIT (+154–156) | Não medido | **unknown** | Arquivado: 417.884.120 (`AUDIT.ddm#L122`); partições sem DDM (`#L142-L145`) | BLOQUEADO |
| Qualidade prevista por leitura de código | Estática | — | Endereços truncados (Q9), datas YYMMDD (Q4), CPF com comprimento variável (Q5), domínios divergentes (Q6, Q7, Q10, Q11, Q15) | Confirmar por profiling da origem |
| Dataset sintético `legacy-seed-data/` | Não lido nesta sessão | — | Receita de seed não comprova o conteúdo atual | — |

## Questões entre fontes

IDs de mistério ainda não atribuídos. Registre-os com `/catalog-mysteries` usando os IDs canônicos ou `BONUS`.

| Questão | Evidência no código | Evidência DDM/FDT ou histórica | Impacto / responsável | Referência no registro de mistérios |
|---|---|---|---|---|
| Q1. Qual FNR cada programa acessa: 151/152/153 ou 155/160/170? | `CALCBENF.NSN#L13`, `#L187`, `#L308`; `VALELEG.NSN#L11`; `CADPROG.NSP#L10` × `#L109`; `BATCHPGT.NSP#L300`; `RELAUDIT.NSP#L13`; `BATCHCON.NSP#L12` | `SOCPROG.ddm#L21`; `PAYMENT.ddm#L27`; `AUDIT.ddm#L24` | Identidade da origem de extração / DBA | A atribuir |
| Q2. Qual a precisão real de `CH` P 9,2 (5 bytes) e `CJ` P 7,2 (4 bytes)? | Views `(P9.2)`, ex.: `CONSBENF.NSP#L37` | `BENEFIC.ddm#L78`, `#L80`, `#L161`; `FDT#L44`, `#L46` | Escala e overflow na carga / DBA | A atribuir |
| Q3. Por que o FDT não lista `JA`/`JB` e declara 21 descritores com 15 `DE` elementares visíveis? | — | `BENEFIC.ddm#L139-L140`; `FDT#L13-L87`, `#L134-L135` | Extração do representante legal / DBA | A atribuir |
| Q4. Existem nascimentos ainda em YYMMDD? `AF` é `NU` no físico? | `BATCHPGT.NSP#L333-L346`; janelas comentadas em `VALBENEF.NSN#L290-L300`, `CALCBENF.NSN`, `CADBENEF.NSP` | `BENEFIC.ddm#L44`; `FDT#L18`; `LDASIFAP.NSL#L88-L96` | Conversão de datas e rejeições / DBA, QA | A atribuir |
| Q5. Todos os CPFs estão com 11 posições e zeros à esquerda? | `CONSBENF.NSP#L294-L300`; `MOVE EDITED (EM=99999999999)` em `CADBENEF.NSP#L205` | `BENEFIC.ddm#L40`, `#L88` | Preservação de chave / DBA | A atribuir |
| Q6. Qual o domínio de COD-REGION: 01–05, 01–25 ou 01–27, mais 99? | `PDACALC.NSA#L59`; `CALCBENF.NSN`; `BATCHREL.NSP`; `LDASIFAP.NSL#L34-L46` | `BENEFIC.ddm#L66`; `SOCPROG.ddm#L86-L88` | Exibição e validação de região / PO | A atribuir |
| Q7. Qual o domínio de RELATION: FI/CJ/NT/TU ou FI/CO/IR/OU? | `CADDEPEN.NSP#L23`, `#L126` | `BENEFIC.ddm#L91-L92` | Exibição de dependentes / PO | A atribuir |
| Q8. `QTY-DEPEND` corresponde às ocorrências do PE? Limite 5 ou 10? | `CADDEPEN.NSP#L117`, `#L193` | `BENEFIC.ddm#L81-L82`, `#L87`; `FDT#L119` | Contagem e ordem de dependentes / DBA, QA | A atribuir |
| Q9. Quantos endereços foram truncados? Quem escreve `NUMBER` e `DISTRICT`? | `CADBENEF.NSP#L277-L279` | `BENEFIC.ddm#L58-L61` | Qualidade de dados / DBA | A atribuir |
| Q10. Quais os domínios reais de TYPE-PAYMENT e STAT-PAYMENT? | `CALCBENF.NSN#L42`; `PDACALC.NSA#L75`; `RELPGT.NSP`; `BATCHREL.NSP#L186`; `BATCHCON.NSP` | `PAYMENT.ddm#L60-L62`, `#L79-L80` | Exibição e agregados por status / PO, QA | A atribuir |
| Q11. TYPE-DISC usa códigos de 2 ou de 1 caractere? | `CALCDSCT.NSP#L22-L23`, `#L45` | `PAYMENT.ddm#L51`; `SOCPROG.ddm#L78-L83` | Detalhe de descontos / DBA | A atribuir |
| Q12. `AMT-DISC-TOTAL` P 7,2 comporta os valores gravados de campos P9.2? | `BATCHPGT.NSP`; `CALCBENF.NSN`; `CALCDSCT.NSP` | `PAYMENT.ddm#L45` | Overflow e truncamento / DBA | A atribuir |
| Q13. `CALCBENF` e `BATCHPGT` gravam dois pagamentos por beneficiário e período? | `BATCHPGT.NSP#L381`, `#L475-L488`; `CALCBENF.NSN#L308-L319` | `PAYMENT.ddm#L34` (`AA` único) | Duplicidade e chaves ausentes na população / DBA, QA | A atribuir |
| Q14. Por que COD-BANK A 3 recebe o numérico 1? | `BATCHCON.NSP#L209` | `PAYMENT.ddm#L72` | Qualidade de dados / DBA | A atribuir |
| Q15. O que significam `CO`, `CN` e `DV` na auditoria? | `CONSBENF.NSP#L172`; `BATCHCON.NSP#L318`, `#L333`; `RELAUDIT.NSP#L170-L175` | `AUDIT.ddm#L39-L49`, `#L126-L136`; `CCAUDIT.NSC#L45-L48` | Semântica do histórico de auditoria / PO | A atribuir |
| Q16. Onde estão as definições de FNR 154–156? | — | `AUDIT.ddm#L142-L145` | Completude do histórico, se estiver no escopo / DBA | A atribuir |
| Q17. `RELAUDIT.NSN` e `BENEFICIARY.DDM` citados existem com outro nome? | `RELAUDIT.NSP#L130` (filtro `EX`) | `AUDIT.ddm#L138-L140`; `FDT#L151` | Rastreabilidade de fontes / leitor | A atribuir |
| Q18. O que FACTOR-K representa? A base gravada em `CADPROG` já está ajustada? | `CADPROG.NSP#L124`, `#L130`; `CALCBENF.NSN#L262`; `BATCHPGT.NSP#L432` | `SOCPROG.ddm#L47-L52` | Valores exibidos e reconciliados / PO | A atribuir |
| Q19. As estatísticas arquivadas refletem o volume atual? | — | `PAYMENT.ddm#L18` × `#L148`; `BENEFIC.ddm#L169` | Linha de base da migração / DBA | A atribuir |
| Q20. Views com `UF`/`COD-REGION` fora de `GRP-ADDRESS` compilam e leem o mesmo campo? | `CALCBENF.NSN#L28-L29`; `BATCHPGT.NSP#L40-L41`; `BATCHREL.NSP#L39-L40`; `CADBENEF.NSP#L35`; `CALCDSCT.NSP#L34` | `BENEFIC.ddm#L57-L66` | Evidência de runtime ausente / leitor | A atribuir |
| Q21. `NUM-REGISTRATION` (`AA`) é preenchido na origem? | Nenhum acesso nos 24 membros | `BENEFIC.ddm#L31`, `#L39`; `PAYMENT.ddm#L36` | Linhagem de chave alternativa / DBA | A atribuir |
| Q22. Quem preenche `GA` DT-INSERT, `GC` USR-INSERT e `GG` NUM-VERSION? | `CADBENEF.NSP` grava só `CB` e `GD` | `BENEFIC.ddm#L112-L118` | Campos de controle na carga / DBA | A atribuir |
| Q23. O histórico "LAST 12" mostra os 12 mais antigos ou os mais recentes? | `CONSBENF.NSP#L263-L284` | `PAYMENT.ddm#L35` (`AB` descritor) | Aceitação do detalhe do beneficiário / PO, QA | A atribuir |

## Autoavaliação C1 para Arquitetura

| Evidência ou bloqueio | Efeito no planejamento posterior da migração | Papel responsável | Resultado da autoavaliação |
|---|---|---|---|
| Definições lógicas dos 4 DDMs lidas | Base para o mapeamento na Etapa 2; nenhum modelo aprovado aqui | DBA | <!-- preencher somente após a autoavaliação real --> |
| FDT físico somente para FNR 150; `JA`/`JB` ausentes | Layout físico de 151–153 desconhecido | DBA | <!-- preencher --> |
| Precisão packed ambígua (Q2) | Bloqueia a decisão de `NUMERIC(p,s)` até haver evidência de runtime | DBA | <!-- preencher --> |
| Domínios divergentes (Q6, Q7, Q10, Q11, Q15) | Regras de exibição e validação exigem decisão do PO | PO | <!-- preencher --> |
| População atual não medida | Gate de prontidão de dados bloqueado | DBA | <!-- preencher --> |

## Verificações de conclusão

- [ ] Toda linha preenchida cita evidências de leitura ou medição real.
- [ ] Campos não lidos e definições físicas ausentes permanecem explícitos.
- [ ] Receitas de seed, estatísticas FDT arquivadas e medições atuais da população estão diferenciadas.
- [ ] Ocorrências MU/PE, identificadores, semântica numérica/de datas e lacunas de qualidade de dados estão registrados sem escolher silenciosamente uma solução.
- [ ] As responsabilidades de DBA e QA foram revisadas com base em evidências; nenhum modelo PostgreSQL ou aprovação C1 foi fabricado.

## Referências

- [Guia da Etapa 1](GUIDE.md)
- [Ciclo de vida da migração de dados](../docs/DATA-MIGRATION.md)
- [Dicionário de declarações](program-data-dictionary.md)
- [Cobertura de leitura](reading-coverage.md)
