# Software Architect — Kit de copiloto

> <x4/> <x5/> › <x6/> › <x7/>

<x2/> Lista os artefatos ativos, onde vivem sob <x3/>, e as melhores práticas específicas para esse papel.

| Campo | Valor |
|---|---|
|<x1/>|Pessoa agindo como Software Architect na workshop|
|<x1/>|Responsabilidade de arquitetura de software (coberto pelo participante)|
|<x1/>|Etapas 2-3: limites do módulo, RAMs e revisão do projeto de implementação|
|<x1/>|<x1/> lido|
|<x1/>|Kit validado, alertas acessíveis em Copilot Chat|

> [!Importante]
> Leia <x1/> antes de continuar. O perfil explica a missão, auto-check, e rubrics avaliação.

---

## Conceito

O Software Architect possui a estrutura interna do sistema. Este papel define como os módulos são organizados, onde os contextos delimitados (limites de Design Domain-Driven) começam e terminam, e quais abstrações são expostas. Em SIFAP (Sistema de Inspeção e Administração de Pagamentos), essa função produz a equipe técnica plan que será seguida — <x1/>, a estrutura do pacote e as RAMs de projeto interno.

---

## Kit da persona

|<x1/>| Tipo | Finalidade |
|---|---|---|
|<x1/>| Perfil |Responsabilidades, auto-controle, prompts e rubric|
|<x1/>| Skill |Arquitetura de software|
|<x1/>| Prompt |<x1/>|
|<x1/>| Prompt |<x1/>|
|<x1/>| Prompt |<x1/>|
|<x1/>| Instruções |Convenções de infra- estrutura|
|<x1/>| Instruções |Convenções de frontend|

---

## Onde ficam os artefatos

Os artefatos ativos estão consolidados sob o diretório raiz <x1/>:

|<x1/>| Caminho |
|---|---|
| Agentes |<x1/>|
| Prompts |<x1/>|
| Skills |<x1/>|
| Instruções |<x1/>|

Use esta pasta como referência. Arquivos ativos vivem apenas sob o diretório root <x1/> — editá-los lá quando a manutenção é necessária.

As integrações opcionais seguem o <x1/>; nenhum persona manifest é uma configuração de servidor instalável.

---

## Boas práticas

- Prefere composição sobre herança, limites claros sobre abstrações genéricas e dados claros sobre código inteligente.
- API contratos são um compromisso público; quebre-os apenas com versioning e um guia de migração.
- Mantenha as regras de negócios fora da base de dados e framework.
- Um diretório crescente <x1/> geralmente indica um contexto limitado em falta.

---

## Referências

- <x1/>
- <x1/>
- <x1/>
- <x1/>

---

### Continue lendo

| Anterior | Próximo |
|---|---|
|<x1/><x2/><x3/>Table das 10 personas.<x4/>|<x1/><x2/><x3/>Profile para esta persona. <x4/>|

<x1/><x2/><x3/>
