# Checklist de exploração do legado

> **Caminho:** [Kit da Equipe](../README.md) › [Etapa 1](README.md) › **Checklist de exploração**

**Gate obrigatório antes da Etapa 2.** Este checklist garante que o participante tenha lido os programas Natural e DDMs necessários à capacidade-alvo fixa e que as regras candidatas sejam rastreáveis ao código legado.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual; preencher durante a Etapa 1 |
| **Pré-requisitos** | Acesso a `legacy-sifap/natural-programs/` e `adabas-ddms/` |
| **Tempo estimado** | Preenchido ao longo da etapa de 50 minutos |
| **Etapa** | Etapa 1: Arqueologia |
| **Resultado esperado** | Matriz completa de leitura da capacidade e critérios C1 verificados |

> [!IMPORTANT]
> **Gate obrigatório antes da Etapa 2.** Nenhum requisito EARS é aceito sem referência a um programa Natural ou arquivo DDM. Requisitos greenfield (sem equivalente legado) devem ser marcados como `[GREENFIELD]` e justificados por escrito na especificação.

> [!WARNING]
> Na edição anterior do workshop, várias equipes pularam a exploração do legado e escreveram especificações baseadas somente no briefing de modernização. As especificações resultantes não preservaram as regras de negócio reais dos 29 anos de história do SIFAP como Payment Inspection and Administration System. Este gate é obrigatório.

---

## 1. A regra de rastreabilidade

Cada `REQ-ID` em `.spec/<NNN>-<feature>/spec.md` precisa de uma linha `source_legacy:` que aponte para uma destas opções:

- um membro Natural, como um arquivo `.NSP` ou `.NSN`, em `01-archaeology/legacy-sifap/natural-programs/` (preferencialmente com intervalo de linhas);
- um arquivo `.ddm` específico em `01-archaeology/legacy-sifap/adabas-ddms/`;
- `[GREENFIELD]` com uma justificativa de uma linha.

A CI rejeita PRs para `develop` quando algum `REQ-ID` não tem uma linha `source_legacy:`. A validação do juiz verifica isso após a submissão, e a autoavaliação C2 detecta o problema antes da implementação.

---

## 2. Capacidade-alvo fixa: o que ler

O participante lê somente os programas e DDMs necessários para consultar, pesquisar e visualizar detalhes de **todos os beneficiários migrados do Adabas para o PostgreSQL**, aplicando as regras legadas de validação descobertas. Todo membro de origem usado como evidência deve ter um intervalo de leitura registrado.

| Área de investigação | Evidência típica da origem | IDs de questões em aberto | Motivo |
|---|---|---|---|
| Cadastro e identidade do beneficiário | `CADBENEF.NSP`, `CADDEPEN.NSP`, `CADPROG.NSP` quando sustentarem campos ou relacionamentos de beneficiários | `SIFAP-M-01` … `M-04` | A lógica de cadastro define entidades e identificadores centrais. |
| Limites de batch e migração | `BATCHPGT.NSP`, `BATCHREL.NSP`, `BATCHCON.NSP` quando afetarem a população da origem ou a reconciliação | `SIFAP-M-05` … `M-08` | Fluxos batch revelam a movimentação da origem e os limites dos módulos. |
| Cálculo e valores derivados | `CALCBENF.NSN`, `CALCCORR.NSP`, `CALCDSCT.NSP` quando os valores precisarem ser exibidos ou reconciliados | `SIFAP-M-09` … `M-12` | Os cálculos explicam valores migrados e agregados de aceitação. |
| Validação | `VALBENEF.NSN`, `VALDOCS.NSP`, `VALELEG.NSN` | `SIFAP-M-13` … `M-16` | As validações se tornam testes e regras legadas para a consulta de beneficiários. |
| Consultas, relatórios e auditoria | `CONSBENF.NSP`, `RELPGT.NSP`, `RELAUDIT.NSP` quando definirem expectativas de lista/pesquisa/detalhe | `SIFAP-M-17` … `M-20` | Caminhos de leitura alimentam a API/UI de consulta, o glossário e o runbook. |

> [!IMPORTANT]
> **Há 20 espaços canônicos de questões em aberto.** Esta é a única meta numérica da Etapa 1. Os IDs e as áreas estão em [`mysteries-checklist.md`](mysteries-checklist.md); registre os relevantes à capacidade em [`mysteries-found.md`](mysteries-found.md). Achados fora da lista contam como bônus e **não** alteram o denominador.

### Checklist para cada programa

Para cada programa ou DDM usado como evidência, registre anotações de leitura suficientes para confirmar que ele foi examinado:

- [ ] **Identifique o programa.** Registre nome, autor e ano da última modificação.
- [ ] **Mapeie as entradas.** Registre quais DDMs ele lê.
- [ ] **Mapeie as saídas.** Registre em quais DDMs ele grava.
- [ ] **Registre as chamadas.** Registre outros programas chamados por `CALLNAT`.
- [ ] **Catalogue regras candidatas.** Quando o programa contiver uma regra relevante ao escopo, registre-a em `business-rules-catalog.md` com `Programa de origem` e intervalo de linhas.

> [!WARNING]
> Uma linha sem `Programa de origem` não sustenta um requisito EARS.

---

## 3. Os quatro DDMs: mapeamento de campos

O participante assume as responsabilidades de DBA e QA e registra evidências para os DDMs exigidos pela capacidade de consulta.

| DDM | Responsável | Artefato-alvo no PostgreSQL |
|---|---|---|
| `BENEFIC.ddm` | Participante | <!-- definir a partir das evidências --> |
| `PAYMENT.ddm` | Participante | <!-- definir a partir das evidências --> |
| `SOCPROG.ddm` | Participante | <!-- definir a partir das evidências --> |
| `AUDIT.ddm` | Participante | <!-- definir a partir das evidências --> |

Revise os DDMs exigidos pela funcionalidade selecionada. O mapeamento PostgreSQL completo pertence ao planejamento e à implementação; ele não é pré-requisito para iniciar a especificação.

O participante também inventaria a população medida dos arquivos relevantes. Use os [registros de migração de dados](../docs/data-migration/) para diferenciar contagens atuais de documentação histórica ou definições de seed. Registre chaves, registros relacionados, achados de qualidade de dados e a rota de snapshot/extração suportada. A autoavaliação C1 confirma a cobertura de todos os beneficiários autorizados e preserva restrições para o mapeamento e o planejamento da migração.

---

## 4. Registro de questões em aberto

Use [`mysteries-checklist.md`](mysteries-checklist.md) para registrar questões em aberto sem antecipar respostas. O registro é um catálogo de incertezas, não um gabarito nem uma fonte de regras.

Registre em `mysteries-found.md` somente questões que afetem o escopo. Cada entrada deve conter:

| Campo | Descrição |
|---|---|
| Questão em aberto | O texto da questão, sem conclusão |
| Evidência | `caminho:linha` |
| Impacto | Efeito no escopo |
| Hipótese | Explicitamente marcada como não confirmada |
| Responsável | Pessoa ou área que pode validá-la |
| Status | `aberta` / `aguardando validação humana` / `encerrada após validação humana` |

Uma questão só pode ser encerrada ou usada como base para uma regra após validação humana explícita sustentada pelas evidências registradas.

---

## 5. Verificação C1 antes de iniciar a Etapa 2

Às 14:50, o participante confere o próprio trabalho com esta matriz. Uma linha vermelha bloqueia o avanço para a Etapa 2 até ser registrada como bloqueio ou corrigida.

| Verificação | Critério do gate |
|---|---|
| Leitura da capacidade | O participante confirmou que leu os membros de origem necessários à consulta de beneficiários e às regras de validação. |
| Catálogo de regras | Toda regra candidata no escopo tem `Programa de origem` preenchido. |
| Escopo | O relatório de descoberta identifica uma funcionalidade pequena e o que foi adiado. |
| Questões em aberto | Incertezas relevantes foram registradas sem se tornarem requisitos. |
| Dados de origem | O trabalho prévio confirmou uma origem Adabas autorizada e populada e uma rota de extração suportada e consistente; o participante registrou evidências de linha de base para verificação do juiz. |
| Cobertura da população | O PO confirmou todos os beneficiários autorizados e os dados relacionados necessários; nenhuma amostra substituiu a população acordada. |

---

## 6. Formato obrigatório da Etapa 2

Escreva requisitos EARS somente em `.spec/<NNN>-<feature>/spec.md`, usando Spec-Kit. Todo `REQ-ID` precisa de um padrão EARS, critérios Given/When/Then e `source_legacy:`. Não finalize um requisito até o participante confirmar a origem ou a justificativa greenfield durante o C2.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Guia da Etapa 1](GUIDE.md)<br/><sub>Cronograma.</sub> | [Templates](templates/)<br/><sub>Modelos preenchíveis para os artefatos da etapa.</sub> |

<sub>[Voltar ao índice do Kit da Equipe](../README.md)</sub>
