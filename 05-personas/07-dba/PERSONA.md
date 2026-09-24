# Persona - DBA

> <x5/> <x6/> > <x7/> > <x8/> > <x9/>

<x1/>

| Campo | Valor |
|---|---|
| Escopo do papel |Responsabilidade pelo ciclo de vida dos dados (coberto pelo participante com <x1/>)|
| Estágios ativos |Preparação e cada etapa|
|Entradas|Fonte real definitions/records, evidência de leitura de equipe, requisitos revistos e arquitetura|
|Saídas|Fonte readiness/map/dictionary, mapeamento e carga plan, esquema e pipeline de registro, evidência de reconciliação e recuperação|
|Controlo automático|Dados de evidência C1 para arquitetura; projeto C2 com architects/QA; alvo C3 povoado e consultas verificadas para operações|

## Onde você trabalha

| Estágio |A sua responsabilidade|Colaboradores|
|---|---|---|
|Preparação|Coordene a população fonte com seu proprietário autorizado; verifique a capacidade de extração e dados atuais|Propriedade do código fonte, DevOps, QA|
|1 - Arqueologia|Leia DDM/FDT e declarações de programas, dados de perfil, incerteza de registro e cobertura real|Leitores, RE, QA|
|2 - Especificação|Desenho do mapeamento fonte-alvo, snapshot/extraction, staging/load, rejeita, replay/resume e recuperação|Arquitetos, PO/RE, QA|
|3 - Execução|Crie o esquema e execute a carga aprovada derivada da fonte com testes e linhagem|Developer, QA|
|4 - validação final|Verifique novamente a reconciliação, consultas reais, recuperação e aceitação após alterações|QA, PO, DevOps, Tech Writer|

Siga o <x1/>. Toda a descoberta
a documentação é gerada durante a arqueologia a partir da leitura real; o kit
Fornece modelos em branco, não o catálogo de campo completo ou o modelo-alvo.

## Princípios fundamentais

- Normalizar o modelo relacional; não simplesmente copiar Adabas layouts de arquivos.
- Mantenha o dinheiro exato e preservar identificadores, zeros principais, codificação, dates/nulls e ocorrências significativas MU/PE.
- Mantenha-se aplicado Flyway versões imutáveis. Esquema histórico e histórico de execução de dados são diferentes.
- Tornar as cargas de dados limitadas, replay-safe, reutilizáveis e recuperáveis.
- Escolha índices e restrições de consultas reais e evidência revisada.
- Parâmetros de consulta de ligação e preservar o histórico de auditoria somente do anexo.
- Nunca reparar silenciosamente inconsistências da fonte ou tratar os beneficiários rejeitados como estando disponíveis com sucesso.

## Perguntas por fase

|Estágio / intenção| Prompt |
|---|---|
|Confirmar origem povoada e extração suportada|<x1/>|
|Ler as definições e declarações da fonte com os participantes|<x2/> com <x3/>|
|Gravar perguntas sem resposta com IDs atribuídos ao leitor|<x1/>|
|Design mapeamentos, cargas e recuperação com arquitetura|<x1/>|
|Aplicar tarefas de migração revistas|<x1/>|
|Verificar independentemente o movimento de dados executado|<x1/>|
|Verificar os caminhos reais de pesquisa do beneficiário|<x1/>|

O <x1/> liga cada prompt e as instruções do banco de dados.
Use Ask para compreensão, Plan para decisões e execução autorizada apenas para
trabalho revisto. Nunca assuma que um ambiente ou ferramenta de banco de dados esteja disponível.

## Provas e auto-controle

|Revisão|O que eles precisam de ti|
|---|---|
|PO / RE|População autorizada, cobertura de consultas e questões não resolvidas business/data|
|Arquitetos|Definições de origem, relações observadas, lacunas de qualidade e restrições de migração|
|Developer|Mapas de alvos revistos e contratos pipeline/query, tabelas não adivinhadas|
|QA|Identidade de instantâneo fonte, resultados esperados independentes, contabilidade de carga e procedimento de recuperação|
|DevOps / Tech Writer|Comandos higiénicos e evidências para a solução do participante, sem detalhes ou segredos da administração da fonte|

## Quando bloqueado

|Bloqueador|Resposta correcta|
|---|---|
|Fonte vazia ou indisponível|Titular do registro e bloqueador de prontidão; não gerar dados substitutos PostgreSQL|
|Nenhum contrato de extração suportado|Resolver com o proprietário da fonte e arquitetos antes da aceitação da migração|
|DDM/FDT/program discordância|Preservar ambas as fontes e uma pergunta não confirmada; não escolher uma resposta conveniente|
|Precisão desconhecida ou semântica do identificador|Estabelecer formato com evidência source/runtime antes do mapeamento|
|Carga de dados quebrada|Utilização testada checkpoint/resume ou recuperação de alvo isolada; nunca reiniciar Adabas|
|Diferença inexplicável ou beneficiário em falta|Aceitação em bloco e investigar com QA|

## Controlos de conclusão

- [ ] São evidenciadas disponibilidade e cobertura de leitura de fonte.
- [ ] Mapeamentos-alvo e tratamento de ambiguidades foram revisados.
- [ ] PostgreSQL é povoada a partir do instantâneo de origem aprovado, não sementes de ensaio.
- [ ] QA chaves reconciliadas independentemente, campos, relacionamentos e agregados acordados.
- [ ] Todos os beneficiários autorizados podem ser listados, pesquisados e consultados.
- [ ] Replay/resume e a recuperação do alvo foram testadas independentemente da Flyway.
- [ ] Nenhum registro bruto, registros sensíveis, credenciais ou aprovações fabricadas entrou em Git.

## Continue lendo

- <x1/>
- <x1/>
- <x1/>
