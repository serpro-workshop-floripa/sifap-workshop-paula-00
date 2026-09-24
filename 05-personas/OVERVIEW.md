# Visão geral das 10 personas

> <x4/> <x5/> › <x6/> › <x7/>

<x1/> No desafio individual, um participante cobre cada papel como checklist de responsabilidade enquanto troca de agentes de palco.

| Campo | Valor |
|---|---|
|<x1/>|Participantes individuais das workshops|
|<x1/>|Nenhum|
|<x1/>|5 min|
|<x1/>|Você entende que responsabilidade aplicar em cada etapa|

> [!Importante]
> O desafio é individual. Você cobre todos os 10 papéis você mesmo; papéis carregam como habilidades automaticamente. Selecione apenas o estágio atual agent (<x4/>, <x5/>, <x6/>) e consulte <x7/> para descoberta de dados, projeto de migração e reconciliação.

---

## As 10 responsabilidades de papel

<x1/>

|<x1/>| Persona | Foco no desafio | Estágio(s) mais ativo(s) | Apoia | Padrão quando houver bloqueio |
|---|---|---|---|---|---|
|01|<x1/>|Âmbito, valor e aceitação de dados migrados|1, 2, validação final|3|Uma característica fina; preservar dados e portões de verificação|
|02|<x1/>|Requisitos EARS e rastreabilidade|1, 2|3|Rastreie todos os requisitos para evidências legadas|
|03|<x1/>|Dependências externas e decisões de âmbito|1, 2|3|Gravar explicitamente alternativas e pressupostos|
|04|<x1/>|Limites do módulo, técnicas plan, RAMs|2|3|Validar os pressupostos de concepção contra os elementos de prova|
|05|<x1/>|Padrões, sequenciamento e auto-revisão|3|1, 2|Implementar a exigência priorizada EARS|
|06|<x1/>|Java/TypeScript código, testes e integração|3|2|Complete uma capacidade de ponta a ponta com testes|
|07|<x1/>|Preparação da fonte, migração, reconciliação, recuperação|1, 2, 3|Todos os estágios|Reconcile os registros de origem; nunca substitua a migração por uma semente|
|08|<x1/>|Testes, verificações independentes de dados, portões de qualidade|2, 3|1|Caminho feliz + caminho de erro para crítico REQ-IDs|
|09|<x1/>|Execução local e CI verde para submissão|3|1, 2|Corrigir a verificação necessária antes de adicionar escopo|
|10|<x1/>|Glossário, clareza README, ADR/spec legibilidade|1, 2, 3|Todos os estágios|Registre a decisão agora, com provas|

---

## Checklist de responsabilidades por estágio

Use isto como uma lista de uma pessoa. Os orçamentos estão resumidos em <x1/>, a fonte da verdade para o calendário de desafios 14:00-17:40.

| Estágio |Agent| Checklist de responsabilidades |
|---|---|---|
|<x1/>|<x2/> + <x3/>|Leia as fontes legadas para a capacidade de destino; capture regras, termos glossários, perguntas abertas, campos de dados e evidências de população-fonte.|
|<x1/>|—|Verificar os artefatos de descoberta citaram evidências de legado e dados suficientes para suportar requisitos.|
|<x1/>|<x2/> + <x3/>|Converta evidências em requisitos EARS com REQ-IDs e <x1/>, defina escopo, arquitetura, projeto de migração de dados, testes e tarefas.|
|<x1/>|—|Verifique se cada requisito formal é rastreável e as tarefas de implementação são pequenas o suficiente para a Etapa 3.|
|<x1/>|<x2/> + <x3/>|Implementar a fatia fina, migrar todos os dados de beneficiários acordados, conciliar as contagens de código-alvo, executar testes e manter CI verde.|
|<x1/>|—|Verificar CI, testes, rastreabilidade, reconciliação de dados e cobertura listing/search/detail antes de abrir a RP para <x1/>.|

---

## Padrões de emergência (resumo)

Cada <x1/> detalha uma seção "Quando preso". Aqui está uma linha por papel:

- <x1/> Escolha uma capacidade fina e proteja a população migrada e o padrão de verificação.
- <x1/> Rastreie cada requisito EARS de evidência e registre lacunas para esclarecimento.
- <x1/> Use uma RAM apenas para escolhas reais; registre alternativas e consequências.
- <x1/> Mantenha os limites do módulo simples e valide suposições antes da codificação.
- <x1/> Pare de refatorar sem testes; foque na porta de submissão.
- <x1/> Um endpoint completo e o caminho do teste são melhores do que várias parciais quebradas.
- <x2/> Siga o <x3/>; concilie os registros de origem e o comportamento de repetição.
- Verificar um caminho feliz e um caminho de erro para cada REQ-ID crítico.
- <x1/> Mantenha os empregos obrigatórios CI verdes para a RP de submissão.
- <x1/> Ask você mesmo: "Que decisão ou termo acabei de usar que ainda não está escrito?"

---

### Continue lendo

| Anterior | Próximo |
|---|---|
|<x1/><x2/><x3/>Pre-work configuração antes das 14:00.<x4/>|<x1/><x2/><x3/>Read o sistema legado e regras de negócios de catálogo.<x4/>|

<x1/><x2/><x3/>
