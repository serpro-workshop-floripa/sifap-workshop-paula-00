# Autochecklist do participante

![Checklist](https://img.shields.io/badge/Type-Checklist-171717?style=flat-square)
![Participante](https://img.shields.io/badge/Scope-Individual%20challenge-737373?style=flat-square)
![Duração](https://img.shields.io/badge/Duration-14%3A00%E2%80%9317%3A40-A3A3A3?style=flat-square)

> **Caminho:** [Kit da equipe](../README.md) › [Documentação](README.md) › **Autochecklist do participante**

**Checklist cronológico para um participante** — use-o em C1, C2, C3 e na linha de chegada. O cronograma completo está em [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md).

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual do workshop |
| **Pré-requisitos** | Setup concluído antes das 14:00; ler [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) |
| **Resultado esperado** | PR de submissão pronto para validação do juiz, com evidências honestas |

---

## Antes das 14:00 — somente pré-trabalho

- [ ] Git, VS Code, Copilot, Spec-Kit, Java 21, Node, Docker e acesso ao repositório estão prontos.
- [ ] O repositório está clonado e `develop` está disponível.
- [ ] A rota ou extração autorizada da fonte Adabas populada está pronta para a descoberta da Etapa 1.
- [ ] Você leu rapidamente a [visão geral das personas](../05-personas/OVERVIEW.md) e sabe que cobre por conta própria todos os 10 papéis.
- [ ] Você consegue selecionar `@archaeologist`, `@architect`, `@builder` e `@dba` no Copilot Chat.

---

## Etapa 1 — Arqueologia (`@archaeologist` + `@dba`)

- [ ] Leia os programas legados e as evidências DDM/FDT necessários para a capacidade fixa de consulta de beneficiários.
- [ ] Registre regras de negócio com citações das fontes; deixe interpretações não comprovadas como questões.
- [ ] Registre termos do glossário e significados dos campos legados.
- [ ] Analise a população completa de beneficiários autorizados e documente os fatos da fonte necessários para a migração.
- [ ] Aplique a regra dos 20 minutos: se estiver bloqueado, peça apoio do workshop e registre o bloqueio.

### Autoverificação C1 — antes de mudar para `@architect`

- [ ] Os artefatos de descoberta identificam os arquivos legados realmente lidos.
- [ ] As regras candidatas são respaldadas por evidências citadas ou marcadas explicitamente como não confirmadas.
- [ ] A descoberta de dados inclui população da fonte, chaves, campos, anomalias e premissas de extração.
- [ ] O escopo candidato é enxuto o bastante para a Etapa 3, mas não reduz a população migrada nem o padrão de verificação.

---

## Etapa 2 — Especificação (`@architect` + `@dba`)

- [ ] Escreva requisitos EARS com IDs `REQ-NNN` exclusivos.
- [ ] Inclua uma linha `source_legacy:` em cada requisito.
- [ ] Defina escopo e fora de escopo para listagem, pesquisa e detalhes de todos os beneficiários migrados.
- [ ] Documente decisões de arquitetura/módulo e ADRs somente quando houver uma escolha real.
- [ ] Projete o mapeamento origem-destino, tratamento de rejeições, reconciliação, nova execução/retomada e recuperação.
- [ ] Defina testes e verificações de aceitação antes do início da implementação.

### Autoverificação C2 — antes de mudar para `@builder`

- [ ] Todo requisito formal tem REQ-ID, redação EARS, critérios de aceitação e `source_legacy:`.
- [ ] As tarefas são pequenas o bastante para execução durante a Etapa 3.
- [ ] A aceitação dos dados consegue comprovar contagem da origem = carregados + rejeições explicadas.
- [ ] As verificações de listagem, pesquisa e detalhes abrangem a população migrada completa, não uma amostra.
- [ ] Nenhuma tarefa da Etapa 3 depende de ativos não publicados do instrutor nem de respostas ocultas.

---

## Etapa 3 — Implementação e migração de dados (`@builder` + `@dba`)

- [ ] Implemente o backend e o frontend no escopo somente conforme necessário para a capacidade de consulta de beneficiários.
- [ ] Mantenha os testes vinculados a REQ-IDs por comentários inline ou nomes claros.
- [ ] Carregue o PostgreSQL pela rota de origem aprovada; não substitua a migração por seed data.
- [ ] Reconcilie registros de origem, rejeições, chaves e agregados acordados.
- [ ] Verifique a segurança da nova execução: sem duplicidades e sem perdas inexplicadas.
- [ ] Atualize o README e as notas de execução com comandos e resultados reais.
- [ ] Mantenha verdes os jobs de CI obrigatórios do PR de submissão.

### Autoverificação C3 — antes de abrir o PR

- [ ] O `mvn verify` do backend passa.
- [ ] Os testes do frontend passam, se um frontend foi construído.
- [ ] A CI está verde, incluindo `legacy-traceability` e os jobs de teste.
- [ ] Todo requisito permanece rastreável às evidências legadas.
- [ ] Os dados reconciliam: contagem da origem = carregados + rejeições explicadas, sem perdas inexplicadas.
- [ ] Listagem, pesquisa e detalhes alcançam todos os beneficiários migrados, incluindo registros além da primeira página.
- [ ] A branch do PR é `impl/<NNN>-<feature>` e tem `develop` como destino.

---

## Linha de chegada — validação do juiz

- [ ] Abra o PR de submissão e preencha o checklist com honestidade.
- [ ] Notifique o juiz antes do prazo de submissão.
- [ ] Se houver rejeição, corrija o problema informado e reenvie; o novo timestamp de atualização do PR será considerado.
- [ ] Preserve evidências de qualquer trabalho inacabado ou bloqueio. Um incremento honesto e verificado é melhor que uma alegação não comprovada.

Os dois primeiros participantes cuja submissão passar na validação do juiz vencem. A verificação do juiz substitui a revisão cruzada e usa ativos privados de validação que não são publicados neste kit.

---

## Três perguntas para fazer a si mesmo a cada 20 minutos

```text
1. Am I blocked, guessing, or missing evidence?
2. Is the next C1/C2/C3 self-check still achievable?
3. Are CI, tests, and data reconciliation getting safer or riskier?
```

Se a resposta revelar um bloqueio, peça apoio do workshop e registre o problema em vez de ocultá-lo.

---

## Respostas de emergência

| Situação | Ação do participante |
|---|---|
| Você está sem direção há 15 minutos | Reafirme o objetivo da etapa atual e escolha o menor próximo passo respaldado por evidências. |
| A CI falha | Interrompa a expansão da funcionalidade e corrija a verificação obrigatória. |
| Novas evidências exigem mudança de escopo após C2 | Atualize spec/plano/tarefas e repita a autoverificação afetada; nunca oculte perda de dados reduzindo o escopo. |
| Você quer refatorar sem um teste existente | Pare. Primeiro adicione ou identifique o teste. |
| Restam trinta minutos e a reconciliação falha | Registre o bloqueio, priorize o defeito e não declare sucesso da migração. |
| O Copilot está indisponível | Use o Plano B em [troubleshooting.md](troubleshooting.md#plano-b--indisponibilidade-do-copilot). |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Fluxo do desafio](../00-TEAM-FLOW.md)<br/><sub>Cronograma completo das 14:00 às 17:40.</sub> | [Lições aprendidas](lessons-learned.md)<br/><sub>Erros comuns.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
