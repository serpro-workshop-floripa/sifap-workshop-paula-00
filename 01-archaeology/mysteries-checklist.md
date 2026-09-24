# Checklist de questões em aberto: Etapa 1

> **Caminho:** [Kit da Equipe](../README.md) › [Etapa 1](README.md) › **Checklist de questões em aberto**

**Rastreie as incertezas antes da Etapa 2.** Este checklist garante que toda questão em aberto seja registrada com evidências, uma hipótese marcada como não confirmada e um responsável identificado.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual; preencher durante a Etapa 1 |
| **Pré-requisitos** | Ler os programas e DDMs necessários à capacidade-alvo fixa |
| **Etapa** | Etapa 1: Arqueologia |
| **Resultado esperado** | Uma lista de questões sem resposta, com rastreabilidade e responsável |

> [!IMPORTANT]
> **Gate de rastreabilidade.** Uma questão permanece em aberto até receber validação humana explícita sustentada por evidências. Ela não pode se tornar resposta, regra ou requisito sem essa validação.

---

## O denominador é 20

O SIFAP, Payment Inspection and Administration System, contém **20 espaços canônicos de questões em aberto**: regras de negócio, contradições e decisões que nunca foram documentadas e existem somente no código. Eles estão agrupados por área de investigação e dificuldade para que um participante individual possa usar os IDs relevantes à capacidade fixa de consulta.

| Regra | Valor |
|---|---|
| Total de questões em aberto canônicas do grupo | **20** (`SIFAP-M-01` … `SIFAP-M-20`) |
| Por área de investigação | **4** |
| Escopo da capacidade | IDs relevantes à lista/pesquisa/detalhe de beneficiários consultados e às regras de validação |
| Registro completo do desafio | IDs relevantes registrados, com bloqueios explícitos para áreas não lidas |

> [!NOTE]
> **Por que usar um número fixo.** Sem um denominador, participantes relatam quantidades diferentes após ler o mesmo material, dependendo da granularidade de agregação e de quantos artefatos abrem. O denominador **não muda**: achados fora da lista são **bônus** reconhecidos no debriefing, mas não substituem uma questão canônica ausente, e os facilitadores não criam IDs canônicos durante o workshop.

Oito das 20 são **bilaterais**: contam somente com ambas as evidências (código **e** DDM, ou código **e** documento legado). A comparação das fontes é obrigatória.

### Onde procurar por área de investigação

Os rótulos indicam a **área** da questão em aberto, nunca o achado.

| Área | Domínio | IDs | Programas |
|---|---|---|---|
| Cadastro | Cadastro | `M-01` … `M-04` | `CADBENEF`, `CADDEPEN`, `CADPROG` |
| Batch | Batch | `M-05` … `M-08` | `BATCHPGT`, `BATCHREL`, `BATCHCON` |
| Cálculo | Cálculo | `M-09` … `M-12` | `CALCBENF`, `CALCCORR`, `CALCDSCT`\* |
| Validação | Validação | `M-13` … `M-16` | `VALBENEF`, `VALDOCS`, `VALELEG` |
| Consultas e relatórios | Consultas e relatórios | `M-17` … `M-20` | `CONSBENF`, `RELPGT`, `RELAUDIT` |

\* `CALCDSCT.NSP` é uma leitura de apoio para evidências de cálculo. Não contém nenhuma questão canônica em aberto, mas vale perguntar por que existe.

> [!TIP]
> **Se você ficar bloqueado por mais de 20 minutos, peça apoio no workshop e registre o bloqueio.** Uma dica não custa pontos; permanecer bloqueado tira você do exercício.

---

## Para cada questão em aberto

- [ ] A questão está registrada sem resposta ou conclusão.
- [ ] A evidência contém `caminho:linha`.
- [ ] O impacto está registrado.
- [ ] A hipótese está explicitamente marcada como **não confirmada**.
- [ ] Uma pessoa ou área responsável está identificada.
- [ ] O status está registrado.

---

## Estrutura do registro

| Questão em aberto | Evidência (`caminho:linha`) | Impacto | Hipótese (não confirmada) | Pessoa/área responsável | Status |
|---|---|---|---|---|---|
| <!-- preencher --> | <!-- preencher: caminho:linha --> | <!-- preencher --> | <!-- preencher: não confirmada --> | <!-- preencher --> | <!-- preencher: aberta / aguardando validação humana / encerrada após validação humana --> |

---

## Quadro de acompanhamento da capacidade

Preencha esta tabela com os IDs relevantes aos membros de origem que você leu para a capacidade fixa.

| ID canônico | Encontrado | Registrado em `mysteries-found.md` |
|---|---|---|
| `SIFAP-M-__` | [ ] | [ ] |
| `SIFAP-M-__` | [ ] | [ ] |
| `SIFAP-M-__` | [ ] | [ ] |
| `SIFAP-M-__` | [ ] | [ ] |

**Achados adicionais (bônus):** <!-- liste aqui; não mudam o denominador -->

---

## Métodos para encontrar questões em aberto

Nenhuma destas dicas revela um achado. Todas são técnicas reutilizáveis de leitura de código legado.

1. **Leia os comentários antes do código.** Em um código de 29 anos, um comentário costuma ser o único lugar em que alguém tentou explicar o *porquê*. Um comentário com nome e data é especialmente valioso.
2. **Leia o cabeçalho do programa.** Linhas como `* CHANGED: yyyy-mm-dd - NAME - reason` contam a história do sistema em ordem cronológica.
3. **Compare o código com a documentação.** Quando `legacy-docs/` e o código divergem, você encontrou algo.
4. **Compare o código com o DDM.** Tipo, tamanho e domínio de valores devem coincidir entre o programa e `adabas-ddms/`, mas nem sempre coincidem.
5. **Procure literais numéricos.** Todo número sem explicação em um cálculo levanta questões: de onde veio, quem o decidiu e o que falha se ele mudar?
6. **Pergunte: "Quem grava neste campo?"** Escolha um campo DDM e encontre todos os programas que gravam nele. Às vezes, a resposta é nenhum.
7. **Leia código comentado.** Blocos desativados revelam o que o sistema fazia e por que parou.
8. **Questione `ESCAPE`, um `IF` sem `ELSE` e atribuições incondicionais.** Saídas antecipadas e regras que sempre se aplicam ocultam decisões que ninguém registrou.
9. **Faça referências cruzadas entre os programas e DDMs relevantes.** Várias questões em aberto aparecem somente quando dois arquivos são comparados.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Guia da Etapa 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Registro de questões em aberto](mysteries-found.md)<br/><sub>Registro detalhado com evidências e responsável.</sub> |

<sub>[Voltar ao índice do Kit da Equipe](../README.md)</sub>
