# Matriz de personas e agentes

![Tipo: referência](https://img.shields.io/badge/Type-Reference-171717?style=flat-square)
![Uso: quem faz o quê](https://img.shields.io/badge/Use-Who%20does%20what-737373?style=flat-square)

> **Caminho:** [Kit da equipe](../README.md) › [Documentação](README.md) › **Matriz de personas e agentes**

**Mapeia cada persona de papel aos agentes de etapa usados no desafio individual.** Um participante cobre todos os papéis; esta matriz é um checklist de papéis por etapa, não um quadro de atribuições.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participantes individuais do workshop |
| **Quando consultar** | No início de cada etapa e antes de cada checkpoint de autoverificação |
| **Resultado esperado** | Saber qual responsabilidade enfatizar ao usar o agente da etapa atual |

---

## Como ler esta matriz

1. Inicie o agente de etapa indicado para a etapa atual do desafio.
2. Leia a coluna de cima para baixo e aplique por conta própria as responsabilidades pertinentes dos papéis.
3. Use `@dba` sempre que houver descoberta, mapeamento, migração, reconciliação ou evidências de nova execução/recuperação de dados.
4. Pare em C1, C2 e C3 para verificar os artefatos antes de avançar.

> [!NOTE]
> **As linhas são skills; as colunas são agentes.** Você seleciona a coluna uma vez por etapa com `@name`. As linhas de papéis são carregadas automaticamente pelas descrições das skills e se compõem com o agente de etapa ativo. O DBA também é um agente porque seu ciclo de vida dos dados abrange todas as etapas. Consulte a [ADR-0002](adr/0002-team-roles-as-skills-not-agents.md) e a [ADR-0003](adr/0003-individual-challenge-format.md).

---

## A matriz do desafio

| # | Persona | Etapa 1 `@archaeologist` | Etapa 2 `@architect` | Etapa 3 `@builder` | Validação final do juiz |
|---|---|---|---|---|---|
| 01 | Product Owner | Confirmar o significado de negócio e a população-alvo de beneficiários | Decidir o escopo da v1 e os critérios de aceitação | Validar o comportamento real dos dados migrados | Aceitar ou registrar bloqueios |
| 02 | Requirements Engineer | Registrar regras candidatas com evidências | Escrever requisitos EARS com REQ-IDs e `source_legacy:` | Manter código/testes vinculados aos requisitos | Verificar a rastreabilidade |
| 03 | Enterprise Architect | Identificar sistemas externos, fontes batch e restrições | Validar decisões de contexto e integração | Verificar se a implementação ainda se ajusta ao contexto | Revisar bloqueios arquiteturais não resolvidos |
| 04 | Software Architect | Observar limites emergentes das evidências legadas | Definir limites dos módulos, ADRs e plano de implementação | Proteger os limites durante a geração de código | Confirmar que os desvios estão documentados |
| 05 | Technical Lead | Acompanhar riscos e sequência | Manter tarefas pequenas e implementáveis | Aplicar padrões e autorrevisão antes do PR | Confirmar a prontidão da submissão C3 |
| 06 | Developer | Entender o comportamento legado antes de programar | Estimar o caminho de implementação a partir das tarefas | Implementar o recorte Java/Next.js e os testes | Corrigir defeitos informados pelo juiz em caso de rejeição |
| 07 | DBA | Analisar campos DDM/FDT e população da fonte | Projetar mapeamento origem-destino e recuperação | Carregar o PostgreSQL, reconciliar e comprovar a segurança da nova execução | Comprovar que não há perdas inexplicadas |
| 08 | QA Engineer | Definir as evidências necessárias para aceitação | Definir testes e verificações de reconciliação | Executar caminhos de sucesso/erro e verificações de dados | Verificar todos os testes e evidências de dados obrigatórios |
| 09 | DevOps Engineer | Confirmar ferramentas locais e prontidão do pré-trabalho | Revisar restrições de execução | Manter verdes os jobs de CI obrigatórios para a submissão | Fornecer evidências da CI |
| 10 | Tech Writer | Manter o glossário e as notas de descoberta | Manter especificação/ADRs legíveis e consistentes | Atualizar README/notas de execução com comandos reais | Garantir que o checklist e o texto do PR estejam claros |

---

## Checklists das etapas

### Etapa 1 — `@archaeologist` + `@dba`

- Leia as fontes Natural/Adabas da capacidade fixa.
- Registre regras, termos do glossário, campos de dados, relacionamentos e questões em aberto com citações das fontes.
- Defina a população completa de beneficiários autorizados para migração e consulta.
- Não escreva requisitos sem evidências; registre as incógnitas com honestidade.

**Autoverificação C1:** os artefatos de descoberta citam as fontes, os fatos dos dados estão registrados e nenhuma regra é promovida sem evidências.

### Etapa 2 — `@architect` + `@dba`

- Converta regras confirmadas em requisitos EARS com REQ-IDs e `source_legacy:`.
- Defina escopo, fora de escopo, limites dos módulos e ADRs somente para decisões reais.
- Projete migração, tratamento de rejeições, reconciliação, nova execução/retomada e recuperação.
- Defina testes de listagem, pesquisa, detalhes e reconciliação dos dados antes de programar.

**Autoverificação C2:** os artefatos formais são rastreáveis, as tarefas de implementação são pequenas e a aceitação dos dados pode ser testada.

### Etapa 3 — `@builder` + `@dba`

- Implemente apenas a capacidade de consulta no escopo.
- Popule o PostgreSQL pela rota de origem aprovada; não substitua a migração por seed data de amostra.
- Execute `mvn verify` no backend e os testes do frontend, se houver frontend.
- Mantenha verde a CI obrigatória e documente comandos/resultados reais.

**Autoverificação C3:** CI verde, testes passando, todos os requisitos rastreáveis, contagem da origem = carregados + rejeições explicadas, nova execução sem duplicidades e listagem/pesquisa/detalhes cobrindo a população completa de beneficiários migrados.

---

## Ordem de leitura sugerida

- [ ] Leia [OVERVIEW.md](../05-personas/OVERVIEW.md) para ver o checklist de papéis para uma pessoa.
- [ ] Leia os arquivos `PERSONA.md` mais pertinentes à etapa atual.
- [ ] Abra o README do agente da etapa atual em [`06-stage-agents/`](../06-stage-agents/).
- [ ] Ative o agente de etapa no Copilot Chat e comece a trabalhar.

## Referências

- [Kits de agentes](../06-stage-agents/README.md)
- [Arquitetura dos agentes](4-agents-explained.md)
- [Fluxo do desafio](../00-TEAM-FLOW.md)
- [Kits de personas](../05-personas/README.md)

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Agentes explicados](4-agents-explained.md)<br/><sub>Por que o desafio usa agentes de etapa mais `@dba`.</sub> | [Fluxo do desafio](../00-TEAM-FLOW.md)<br/><sub>Cronograma e checkpoints de autoverificação.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
