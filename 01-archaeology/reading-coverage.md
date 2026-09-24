# Cobertura de leitura

> **Caminho:** [Kit da Equipe](../README.md) > [Etapa 1](README.md) > **Cobertura de leitura**

**Registre quem leu quais intervalos da origem, o que permanece não lido e o que foi revisado de forma independente.**

> [!NOTE]
> Inicializado por `/archaeology-kickoff` em 2026-09-24 a partir do [template](templates/reading-coverage.md).
> Nenhuma fonte foi lida até agora: a enumeração de arquivos do [inventário](inventory.md) não comprova leitura.
> Atualize somente os intervalos realmente examinados.

| Campo | Valor |
|---|---|
| Participante / data / versão da origem | <!-- preencher --> / 2026-09-24 / <!-- preencher --> |
| Escopo e denominador de leitura acordados | <!-- preencher: subconjunto do inventário necessário à consulta de beneficiários; o universo inventariado é 24 membros Natural/JCL + 4 DDMs + 1 FDT --> |
| Cobertura de leitura dos programas | 0 / <!-- preencher: denominador acordado --> |
| Cobertura de leitura de DDM/FDT | 0 / <!-- preencher: denominador acordado --> |
| Verificações de runtime realizadas | Não realizadas |

## Registro de leitura

| Membro / artefato de origem | Papel responsável | Intervalos realmente lidos | Intervalos não lidos | Observações / achados vinculados | Revisor / status |
|---|---|---|---|---|---|
| `adabas-ddms/BENEFIC.ddm` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `adabas-ddms/FDT-150-BENEFICIARY.txt` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `adabas-ddms/SOCPROG.ddm` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `adabas-ddms/PAYMENT.ddm` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `adabas-ddms/AUDIT.ddm` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/CONSBENF.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/VALBENEF.NSN` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/VALDOCS.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/VALELEG.NSN` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/CADBENEF.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/CADDEPEN.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/CADPROG.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/BATCHPGT.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/BATCHREL.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/BATCHCON.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/CALCBENF.NSN` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/CALCCORR.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/CALCDSCT.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/RELPGT.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |
| `natural-programs/RELAUDIT.NSP` | <!-- preencher --> | Nenhum | Membro inteiro | <!-- preencher --> | Não iniciado |

## Membros de apoio e fontes ausentes

| Artefato referenciado | Motivo para inspecionar | Disponível? | Leitor / evidência ou bloqueio |
|---|---|---|---|
| `natural-programs/PDAVALID.NSA` | <!-- preencher: referência encontrada via /map-dependencies --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/PDACALC.NSA` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/LDASIFAP.NSL` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/CCVALCPF.NSC` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/CCAUDIT.NSC` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/SUBVALCP.NSN` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/SUBVALNI.NSN` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/SIFAPJ01.jcl` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| `natural-programs/SIFAPJ02.jcl` | <!-- preencher --> | Sim (arquivo existe) | <!-- preencher --> |
| <!-- preencher: membro referenciado e ausente do corpus --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Limites da verificação

| Verificação | Planejada ou executada? | Evidência / resultado | O que não estabelece |
|---|---|---|---|
| Enumeração de arquivos e diretórios de `legacy-sifap/` | Executada em 2026-09-24 | 4 diretórios, 42 arquivos; ver [inventário](inventory.md) | Leitura, conteúdo, conectividade ou comportamento |
| Verificação independente das contagens com `find` | Planejada | <!-- preencher --> | Leitura de qualquer membro |
| Medição do tamanho dos arquivos | Não executada | <!-- preencher --> | — |
| Compilação ou execução Natural | Não executada | Sem runtime disponível no kit | Comportamento em runtime |
| População Adabas e rota de extração | Não executada; pertence ao `@dba` | <!-- preencher em docs/data-migration/source-readiness.md --> | Conteúdo atual da origem |

## Revisão da autoavaliação C1

| Papel / próxima etapa | Evidência revisada | Lacunas em aberto | Reconhecimento / data |
|---|---|---|---|
| <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher somente após a revisão real --> |

## Verificações de conclusão

- [ ] As contagens derivam do inventário selecionado e dos intervalos registrados.
- [ ] Leituras parciais, fontes ausentes e verificações não executadas permanecem visíveis.
- [ ] Nenhuma caixa marcada, assinatura, data, resultado de runtime ou aceitação C1 foi copiada de um exemplo.
- [ ] IDs de mistérios e achados da descoberta apontam para os registros do próprio participante.
