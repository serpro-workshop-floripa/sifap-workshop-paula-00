# Conjunto de dados legado sintético

> **Caminho:** [Kit da Equipe](../../README.md) › [Etapa 1](../README.md) › **Conjunto de dados legado sintético**

**Registros sintéticos para exercícios do SIFAP legado.** Esta pasta contém os arquivos de largura fixa usados para popular a instância Adabas autorizada antes das 14:00, permitindo comparar o comportamento legado com o sistema moderno.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual responsável por DBA, QA e implementação |
| **Pré-requisitos** | Ler os DDMs em [`legacy-sifap/adabas-ddms/`](../legacy-sifap/adabas-ddms/) |
| **Tempo estimado** | 15 min |
| **Etapa** | Etapa 1: Arqueologia; entrada para a Etapa 3 |
| **Resultado esperado** | Registros decodificados para validar o sistema moderno |

> [!IMPORTANT]
> **Dados 100% sintéticos.** Não contêm dados pessoais reais, CPF ou NIS atribuído a uma pessoa real nem registros de produção. Os dígitos verificadores são válidos somente para exercitar os validadores legados.

---

## Arquivos e volumes

| Arquivo | Registros | Bytes por registro (sem a quebra de linha) | Layout de origem |
|---|---:|---:|---|
| `beneficiary.dat` | 500 | 1739 | `layout-beneficiary.txt`, file 150 BENEFICIARY |
| `payment.dat` | 2000 | 855 | `layout-payment.txt`, file 152 PAYMENT |
| `social-program.dat` | 6 | 361 | `layout-social-program.txt`, file 151 SOCIAL-PROGRAM |
| `audit.dat` | 200 | 4995 | `layout-audit.txt`, file 153 AUDIT |

---

## Regeneração

Execute a partir da raiz do repositório:

```bash
python3 01-archaeology/legacy-seed-data/generate_seed.py
```

O gerador usa somente a biblioteca padrão do Python 3 e uma seed fixa, portanto sua saída é reproduzível byte a byte. Este README é gerado. Tradutores devem atualizar o texto dentro de `write_readme()`, não somente este arquivo gerado.

---

## Observações sobre o layout

Há um registro físico por linha. Campos alfanuméricos são preenchidos em ASCII com espaços à direita. Campos numéricos unpacked são preenchidos com zeros à esquerda.

> [!WARNING]
> Campos decimais packed são BCD binário, com a escala declarada no DDM/FDT. **Eles não podem ser lidos como texto e exigem decodificação antes de qualquer carga no PostgreSQL.** Pelo mesmo motivo, converter identificadores em números descarta zeros à esquerda de valores de CPF e NIS.

Grupos periódicos e campos MU são emitidos com o número máximo de ocorrências para que scripts ADACMP/ADALOD carreguem registros determinísticos de largura total. A quebra de linha não faz parte da largura do registro.

---

## Fixtures de aprendizagem

- Os dígitos verificadores de CPF e NIS usam os algoritmos de módulo 11 de [`SUBVALCP.NSN`](../legacy-sifap/natural-programs/SUBVALCP.NSN) e [`SUBVALNI.NSN`](../legacy-sifap/natural-programs/SUBVALNI.NSN).
- Alguns beneficiários têm CPF válido iniciado por `000` para o caminho de exceção de testes governamentais.
- Os valores de renda familiar atravessam as faixas de cálculo 300, 600, 1000 e 1500.
- Beneficiários da região `99` exercitam o ramo de elegibilidade internacional ou diplomática.
- Os dependentes abrangem situações sem dependentes, com vários, inativos e encerrados, além de um registro com o máximo de 10 ocorrências.
- Os pagamentos incluem estornos, reconciliação divergente, devoluções bancárias e linhas com valores bruto, de desconto e líquido deliberadamente desequilibrados para os laboratórios de relatórios.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Etapa 1: Arqueologia](../README.md)<br/><sub>Índice da etapa e seus artefatos.</sub> | [DDMs Adabas](../legacy-sifap/adabas-ddms/README.md)<br/><sub>Definições de campos que descrevem estes registros.</sub> |

<sub>[Voltar ao índice do Kit da Equipe](../../README.md)</sub>
