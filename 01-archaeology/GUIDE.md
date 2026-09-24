# Etapa 1: Arqueologia digital (50 min)

> **Caminho:** [Kit da Equipe](../README.md) › [Etapa 1](README.md) › **GUIA**

**Um cronograma de 50 minutos para ler somente os programas Natural e DDMs necessários à capacidade fixa de consulta, registrar evidências rastreáveis e preparar o C1.**

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante individual responsável por arqueologia, DBA, QA, Visão e Arquitetura |
| **Pré-requisitos** | Ler [`README.md`](README.md), acessar o diretório `legacy-sifap/` e concluir antes das 14:00 o trabalho prévio de prontidão dos dados de origem |
| **Tempo estimado** | 50 min (14:00–14:50) |
| **Etapa** | Etapa 1: Arqueologia |
| **Resultado esperado** | Catálogo de regras candidatas, linha de base de dados medida, relatório de descoberta e autoavaliação C1 concluída |

> [!IMPORTANT]
> **Gate obrigatório.** Antes de escrever requisitos EARS na Etapa 2, o participante deve ler os programas Natural e DDMs necessários à capacidade-alvo fixa e ter evidências para cada comportamento selecionado. Cada requisito formal posterior precisa de um `source_legacy:` válido ou de um marcador `[GREENFIELD]` justificado. O gate não é uma meta quantitativa.

---

## Objetivo

Ler os programas Natural e DDMs necessários à capacidade-alvo fixa, registrar evidências rastreáveis e definir o recorte de consulta de beneficiários que pode se tornar uma funcionalidade. O objetivo não é explicar todo o SIFAP Payment Inspection and Administration System, produzir documentação enciclopédica nem resolver questões em aberto.

O sistema moderno deverá posteriormente armazenar e exibir os registros legados da população de beneficiários acordada, e não apenas reproduzir suas regras. A origem Adabas autorizada e populada e a rota de extração fazem parte do trabalho prévio concluído antes das 14:00; durante a Etapa 1, registre a linha de base de dados medida da qual partirá a migração da Etapa 3.

---

## Cronograma

| Horário | Atividade | Resultado mínimo |
|---|---|---|
| 14:00–14:05 | Comece diretamente em `@archaeologist`; confirme a capacidade-alvo fixa e as evidências prévias de prontidão da origem. | Escopo e evidências de prontidão ou bloqueio registrados. |
| 14:05–14:30 | Leitura orientada: programas de consulta, regras de validação, DDMs, entradas, saídas, chamadas e decisões de domínio necessárias para listar, pesquisar e detalhar todos os beneficiários. | Anotações com caminhos e intervalos de linhas. |
| 14:30–14:40 | Registre regras candidatas e questões sem inferir comportamentos ausentes. | Evidências no catálogo e itens em aberto explícitos. |
| 14:40–14:47 | Consolide somente evidências que sustentem a consulta de beneficiários e a prontidão da migração. | Catálogo e relatório de descoberta atualizados. |
| 14:47–14:50 | Conclua a autoavaliação C1 antes de mudar para `@architect`. | Fontes, escopo, evidências de dados e bloqueios revisados conforme o checklist C1. |

---

## Escopo de leitura

O participante lê somente os programas e DDMs necessários à capacidade-alvo fixa: consultar, pesquisar e visualizar detalhes de **todos os beneficiários migrados do Adabas para o PostgreSQL**, aplicando as regras legadas de validação descobertas na origem. Concentre-se nas decisões de domínio e na rastreabilidade. Não tente traduzir todos os comandos Natural nesta etapa.

Comece pelos caminhos de consulta e validação; depois, adicione membros de cadastro, dependência, pagamento, programa, auditoria ou batch somente quando fornecerem evidências sobre campos, filtros, validação, registros relacionados ou prontidão da migração. Revise os DDMs necessários às evidências selecionadas. Mapear todos os campos ou propor o esquema PostgreSQL completo não é necessário nesta etapa.

O participante registra o inventário de dados dos arquivos Adabas relevantes: população medida, chaves, registros relacionados, achados de qualidade de dados e a rota de snapshot/extração suportada. Registre-os nos [registros de migração de dados](../docs/data-migration/). O [conjunto de dados legado sintético](legacy-seed-data/README.md) documenta os registros usados para popular a origem; ele não comprova o conteúdo atual da origem.

---

## O que registrar

Use os [templates](templates/) como apoio. Para cada regra candidata no escopo, registre pelo menos:

- uma descrição breve do comportamento observado;
- o caminho do `.NSN` ou `.ddm` e, quando possível, o intervalo de linhas;
- a questão que ainda impede uma conclusão, sem transformá-la em requisito;
- o impacto da regra na funcionalidade priorizada.

O arquivo `business-rules-catalog.md` é a entrada da especificação formal. Use o [template do catálogo](templates/business-rules-catalog.template.md) se o arquivo ainda não existir. Você pode enriquecer o glossário, o mapa de dependências e o registro de questões em aberto quando ajudarem a definir o escopo, mas metas numéricas não bloqueiam a transição.

> [!IMPORTANT]
> **Exceção: questões em aberto têm um denominador fixo.** O SIFAP contém **20 espaços canônicos de questões em aberto** agrupados por área de investigação. Use os IDs relevantes para a capacidade que você realmente leu e registre-os em [`mysteries-found.md`](mysteries-found.md). Achados fora da lista são bônus e não alteram o denominador.

---

## Descoberta de dados versus projeto da migração

- **Etapa 1:** registre definições da origem, chaves, declarações reais, relacionamentos, população atual medida e incertezas.
- **Etapa 2:** DBA e arquitetos decidem, no plano formal, os mapeamentos para PostgreSQL, snapshot/extração, ordem de carga, tratamento de rejeições, recuperação e aceitação de QA.
- **Etapa 3:** implemente e execute a carga aprovada da origem para o destino, reconcilie-a e exponha consultas reais.

Siga o [ciclo de vida dos dados](../docs/DATA-MIGRATION.md). A Etapa 4 não faz parte do desafio individual; a validação do juiz após a Etapa 3 substitui o antigo bloco de verificação pós-alteração. A leitura da origem pode continuar offline, mas uma origem Adabas vazia ou indisponível, ou uma rota de extração não verificada, mantém bloqueado o gate de prontidão dos dados. Arquivos seed e contagens FDT arquivadas não são medições atuais do banco de dados. Mantenha registros restritos fora do Git.

---

## Autoavaliação C1

Nos minutos finais, o participante verifica os itens a seguir antes de mudar para `@architect`:

1. a funcionalidade enxuta selecionada e o que permanece fora do escopo, sem reduzir silenciosamente a população autorizada de beneficiários;
2. as regras que podem se tornar requisitos, com caminhos legados;
3. as questões em aberto que **não podem** se tornar requisitos EARS;
4. referências a DDMs e dependências somente quando afetarem a funcionalidade;
5. as evidências de dados: população medida da origem, população de beneficiários acordada, lacunas de qualidade de dados e prontidão da extração ou seu bloqueio.

Se as evidências forem insuficientes para iniciar `.spec/<NNN>-<feature>/spec.md`, registre o bloqueio e reduza a amplitude da capacidade sem reduzir a população de beneficiários migrada nem inventar uma origem.

---

## Definição de pronto

- [ ] O participante leu os programas Natural e DDMs necessários à consulta de beneficiários e às regras legadas de validação.
- [ ] O comportamento selecionado tem evidências em um arquivo `.NSN` ou `.ddm`, ou está explicitamente separado como proposta greenfield.
- [ ] O catálogo identifica a origem de cada regra candidata.
- [ ] O relatório de descoberta registra o escopo e as questões relevantes.
- [ ] A população medida da origem e a prontidão da extração estão registradas; evidências ausentes permanecem como bloqueio.
- [ ] A população autorizada de beneficiários está confirmada; a funcionalidade não a reduz a uma amostra.
- [ ] A autoavaliação C1 está concluída até as 14:50.

---

## Referências

- [Checklist de exploração do legado](LEGACY-EXPLORATION-CHECKLIST.md): verificação do gate C1 e critérios da capacidade fixa.
- [Guia de migração de dados](../docs/DATA-MIGRATION.md): ciclo de vida dos dados e gates de aceitação, da prontidão da origem à reconciliação.
- [Guia da Etapa 2](../02-modern-spec/GUIDE.md): o próximo passo após o C1.
- [Como ler Natural](legacy-sifap/HOW-TO-READ-NATURAL.md): tutorial de sintaxe para não desenvolvedores.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [README da Etapa 1](README.md)<br/><sub>Visão geral da etapa.</sub> | [Checklist de exploração do legado](LEGACY-EXPLORATION-CHECKLIST.md)<br/><sub>Gate obrigatório antes da Etapa 2.</sub> |

<sub>[Voltar ao índice do Kit da Equipe](../README.md)</sub>
