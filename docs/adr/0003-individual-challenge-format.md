# ADR-0003: O workshop é um desafio individual da Etapa 1 à Etapa 3

> **Caminho:** [Kit da equipe](../../README.md) › [Documentação](../README.md) › [ADRs](README.md) › **ADR-0003**

| Campo | Valor |
|---|---|
| **Status** | accepted |
| **Data** | 2026-09-24 |
| **Autores** | Mantenedores do kit |
| **Substitui** | O formato de equipe/duplas descrito em `00-TEAM-FLOW.md` antes desta data |

---

## Contexto

O kit foi projetado para cinco participantes trabalhando como cinco duplas de
papéis ao longo de um dia de oito horas. Ele tinha quatro etapas, com 260 minutos
de trabalho, além de três handoffs ao vivo (H1, H2, H3) entre as duplas.

O evento agora ocorre das 14:00 às 17:40 (220 minutos). Cada participante
trabalha sozinho e realiza toda a modernização. Os dois primeiros participantes
que comprovarem um resultado correto vencem. Com esse formato:

- o orçamento de etapas baseado em equipe não cabe;
- duplas e handoffs entre pessoas diferentes deixam de existir;
- o QA independente não pode vir de um segundo participante;
- a Etapa 4 (evolução com o coding agent) não cabe no tempo disponível.

Também avaliamos um orquestrador paralelo de subagentes para a Etapa 3. Seu ganho
é limitado pelo trabalho serial (migração de dados, reconciliação, execução de
testes). Isso tornaria injusta a comparação entre participantes e ocultaria o
exercício por trás da automação.

## Decisão

1. **Formato individual.** Cada participante cobre todos os 10 papéis. Os papéis
   continuam como skills ([ADR-0002](0002-team-roles-as-skills-not-agents.md)); o
   participante alterna apenas os agentes de etapa.
2. **Cronograma.** O participante começa diretamente em `@archaeologist` às 14:00.

   | Horário | Etapa | Agente |
   |---|---|---|
   | 14:00-14:50 | Etapa 1 - Arqueologia | `@archaeologist` + `@dba` |
   | 14:50-15:30 | Etapa 2 - Especificação | `@architect` + `@dba` |
   | 15:30-17:10 | Etapa 3 - Implementação e migração de dados | `@builder` + `@dba` |
   | 17:10-17:40 | Validação final do juiz | Juiz |

   O setup e a fonte Adabas autorizada e populada são pré-trabalho, concluído
   antes das 14:00.
3. **A Etapa 4 está fora do desafio.** Seus arquivos permanecem no kit, marcados
   como não utilizados.
4. **Handoffs tornam-se checkpoints de autoverificação** C1, C2 e C3. Eles usam
   os mesmos artefatos e a mesma definição de pronto de antes. C3 é a submissão.
5. **Capacidade-alvo fixa.** Todos devem listar, pesquisar e mostrar os detalhes
   de **todos** os beneficiários migrados do Adabas para o PostgreSQL, aplicando
   as regras de validação legadas que descobrirem.
6. **Linha de chegada.** A CI está verde (incluindo `legacy-traceability`), todo
   requisito tem REQ-ID, EARS e `source_legacy:`, os testes passam, os dados estão
   reconciliados (origem = carregados + rejeições explicadas; chaves e agregados
   correspondem; nova execução sem duplicidades) e as consultas cobrem toda a população.
7. **Vencedores.** As duas primeiras submissões que passarem na validação do juiz
   vencem. O timestamp é o da criação do PR `impl/<NNN>-<feature>` -> `develop`.
   17:10 é o prazo de submissão. Uma submissão rejeitada pode ser corrigida e
   reenviada com um novo timestamp.
8. **Independência.** A verificação do juiz substitui a revisão entre duplas e o
   QA independente. Scripts do juiz e valores esperados permanecem no repositório
   privado do instrutor.
9. **Sem orquestrador.** A orquestração paralela de subagentes não é permitida.

## Consequências

- Execução mais rápida e comparação fácil: uma capacidade fixa e uma linha de
  chegada objetiva.
- Menos prática de colaboração e delegação. O conteúdo da Etapa 4 permanece
  disponível para uma sessão posterior.
- O juiz se torna um ponto único de verificação, portanto valida continuamente
  à medida que as submissões chegam.
- A regra “reduza a abrangência da capacidade, nunca a população migrada nem o
  padrão de verificação” continua válida. Uma submissão incompleta não vence.
