# QA Engineer — Kit de copiloto

> <x4/> <x5/> › <x6/> › <x7/>

<x1/>

<x1/>

| Campo | Valor |
|---|---|
|<x1/>|Pessoa que toma a persona QA Engineer na workshop|
|<x1/>|Gerando testes a partir de especificações EARS, cobrindo comportamento crítico, e mantendo o gasoduto verde|
|<x1/>|Etapas 1-3 mais validação final do juiz: projeto de teste, reconciliação e verificação de evidências|
|<x1/>|Conjunto de testes de passagem, pipeline verde CI e rastreabilidade do espetro ao teste garantida|

Ler primeiro: <x1/>.

---

## Conceito

O QA Engineer transforma os requisitos EARS em testes executáveis. Na modernização SIFAP (Sistema de Inspeção e Administração de Pagamentos), esta persona valida a equivalência funcional entre o comportamento legado Natural e o moderno código Java21, garantindo que cada REQ-ID tenha pelo menos um teste verificável e que o gasoduto GitHub Actions CI permaneça verde.

Por que importa: testes ausentes ou frágeis deixam o participante cego para regressões. Na modernização do legado, a equivalência funcional entre comportamento antigo e novo só pode ser comprovada por testes rastreáveis às exigências.

## Kit da persona

Todos os artefatos ativos vivem no diretório root do repositório <x2/>. Esta pasta é uma referência; edite os arquivos em <x3/> quando a manutenção for necessária.

|Arquivo| Tipo | Finalidade |
|---|---|---|
|<x1/>| Perfil |QA Engineer responsabilidades, etapas, alertas e rubricas|
|<x1/>| Skill |Geração de teste, análise de cobertura e portões de qualidade|
|<x1/>| Prompt |<x1/>|
|<x1/>| Prompt |<x1/>|
|<x1/>| Prompt |<x1/>|
|<x1/>| Instruções |Convenções de ensaio|

> [!Dica]
> Verificar ferramentas opcionais através do <x1/>. Os ganchos de amostras e os manifestos descritivos não são provas de aprovação do teste.

## Onde vivem os artefatos activos

- Agentes: <x1/>
- Perguntas: <x1/>
- Habilidades: <x1/>
- Instruções: <x1/>

## Boas práticas

- [ ] <x1/> Priorizar mais testes unitários, um número moderado de testes de integração e menos testes de ponta a ponta.
- [ ] <x1/> Isole, conserte ou remova; nunca ignore.
- [ ] <x1/> Cobertura de linhas sem uma afirmação significativa não valida o domínio.
- [ ] <x1/> Cada teste deve referenciar um REQ-ID em um comentário em linha.

## Aplicar o fluxo de trabalho para SIFAP

Durante a arqueologia, verificar de forma independente a fonte DBA basal e real
A ler provas. Na Fase 2, derivam-se testes da revisão do participante REQ-IDs e
mapeamentos de dados. Nos estágios 3-4, use PostgreSQL testes de integração e independentes
reconciliação para verificar cobertura completa source-key/field/relationship, real
Consultas do beneficiário e recuperação. Um resultado esperado copiado ou uma semente de teste é
não prova de migração. Utilizar o <x1/>;
O kit não fornece resultados de testes completos.

## Referências

- <x1/>
- <x1/>
- <x1/>
- <x1/>

---

### Continue lendo

| Anterior | Próximo |
|---|---|
|Lista de verificação para as 10 personas.|<x1/><x2/><x3/>Complete QA Engineer persona perfil.<x4/>|

<x1/><x2/><x3/>
