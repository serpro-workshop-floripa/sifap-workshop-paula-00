# FAQ — Perguntas frequentes

> **Caminho:** [Kit da equipe](../README.md) › [Documentação](README.md) › **FAQ**

**Respostas diretas para perguntas comuns sobre o workshop de modernização do SIFAP.**

| Campo | Valor |
|---|---|
| **Público-alvo** | Todas as pessoas participantes |
| **Como usar** | Pesquise a pergunta com `Ctrl+F`. Se ela não estiver aqui, consulte [troubleshooting.md](troubleshooting.md) |
| **Tempo estimado** | Leitura seletiva |

---

## Sobre o workshop

<details>
<summary><strong>Não programo. Posso participar?</strong></summary>

Sim. As personas Product Owner e Tech Writer, além de parte de QA, não exigem programação. Leia primeiro [`07-concepts/`](../07-concepts/) para conhecer os conceitos. Cada `PERSONA.md` inclui uma seção de orientações para emergências.

</details>

<details>
<summary><strong>Quanto tempo dura?</strong></summary>

O desafio individual ocorre das 14:00 às 17:40. O cronograma exato está em [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md).

</details>

<details>
<summary><strong>Quantas pessoas trabalham juntas?</strong></summary>

Uma. Cada participante trabalha individualmente e cobre as responsabilidades dos 10 papéis por meio das skills de papel.

</details>

<details>
<summary><strong>Posso escolher somente duas personas?</strong></summary>

Não há atribuição em duplas no desafio individual. Você cobre por conta própria as responsabilidades dos 10 papéis. As skills pertinentes são carregadas quando suas solicitações correspondem às descrições delas.

</details>

<details>
<summary><strong>O que é o SIFAP?</strong></summary>

O SIFAP (Sistema de Fiscalização e Administração de Pagamentos) representa um
sistema governamental de pagamentos com aproximadamente 30 anos de história em
Natural/Adabas. O histórico fornecido começa em 1997; 2026 é o ano de referência
do workshop. Consulte a [cronologia](../README.md#cenário-cronologia-e-evidências).
Você moderniza um incremento limitado, não o sistema inteiro em um dia.

</details>

---

## Sobre o Copilot

<details>
<summary><strong>Qual modelo do Copilot devo usar?</strong></summary>

Sonnet 4.6 para a maioria das tarefas. Haiku para tarefas mecânicas e repetitivas. Opus para decisões arquiteturais complexas. Consulte [`09-cheat-sheets/model-routing.md`](../09-cheat-sheets/model-routing.md).

</details>

<details>
<summary><strong>Quando devo usar Ask, Plan ou Agent?</strong></summary>

- **Ask** — discutir e entender.
- **Plan** — planejar uma mudança em vários arquivos.
- **Agent** — delegar uma Issue completa.

Referência: [`07-concepts/04-3-copilot-modes.md`](../07-concepts/04-3-copilot-modes.md).

</details>

<details>
<summary><strong>O Agent pode fazer merge sozinho?</strong></summary>

Não. O Agent abre um pull request. Revise-o com o mesmo cuidado que você dedicaria à contribuição de uma pessoa.

</details>

<details>
<summary><strong>Posso usar Cursor, Codeium ou outro assistente?</strong></summary>

Não. A toolchain é fixa: use somente o GitHub Copilot. Consulte [`.github/copilot-instructions.md`](../.github/copilot-instructions.md).

</details>

---

## Sobre Spec-Kit e EARS

<details>
<summary><strong>Por que todo requisito EARS precisa de `source_legacy:`?</strong></summary>

Para garantir que você modernizou o sistema real, não somente o briefing. A CI rejeita pull requests sem esse campo. Consulte [`01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md`](../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md).

</details>

<details>
<summary><strong>E se a funcionalidade for nova e não tiver equivalente no legado?</strong></summary>

Use `source_legacy: "[GREENFIELD] <justification>"`. Confirme que a capacidade
selecionada não tem equivalente nas fontes legadas fornecidas. Somente o tipo
de terminal não estabelece qual autenticação o sistema usava.

</details>

<details>
<summary><strong>Posso pular `/speckit.clarify`?</strong></summary>

Não. Ignorá-lo transforma ambiguidades em defeitos da Etapa 3, quando o custo de correção é muito maior.

</details>

<details>
<summary><strong>O `/speckit.analyze` informa problemas. O que devo fazer?</strong></summary>

Resolva-os antes da implementação. Cada apontamento evita retrabalho posterior.

</details>

---

## Sobre Git e branches

<details>
<summary><strong>Posso fazer commit diretamente em `main`?</strong></summary>

Não. Sempre use um pull request. Consulte a regra 1 em [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md).

</details>

<details>
<summary><strong>Qual prefixo de branch devo usar?</strong></summary>

- `spec/<NNN>-<feature>` na Etapa 2
- `impl/<NNN>-<feature>` na Etapa 3

As duas branches de funcionalidade nascem de `develop`. Prefixos de branch `infra/` não são usados no desafio individual. Consulte a tabela completa em [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md).

</details>

<details>
<summary><strong>Como meu PR é aprovado?</strong></summary>

CI verde e validação do juiz. O PR de submissão é `impl/<NNN>-<feature>` → `develop` no seu repositório, com o checklist preenchido.

</details>

<details>
<summary><strong>Posso executar `git push --force`?</strong></summary>

Somente na sua própria branch e somente com `--force-with-lease`. Nunca em `develop` ou `main`.

</details>

---

## Sobre Terraform e Azure

<details>
<summary><strong>Posso executar `terraform apply`?</strong></summary>

> [!CAUTION]
> Não. Somente `terraform plan` é autorizado durante o workshop. Executar `apply` cria recursos reais no Azure e gera custos.

</details>

<details>
<summary><strong>Onde devo armazenar secrets?</strong></summary>

No Azure Key Vault. Nunca em `variables.tf` nem em arquivos `.env` versionados. Ao criar `infra/`, modele secrets por meio do Key Vault e de Managed Identity.

</details>

---

## Sobre etapas e checkpoints de autoverificação

<details>
<summary><strong>O que são os checkpoints de autoverificação C1, C2 e C3?</strong></summary>

São pontos de autoverificação em cada troca de agente. Antes de avançar, você verifica os mesmos artefatos antes revisados nos limites entre as etapas. Os detalhes estão em [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md).

</details>

<details>
<summary><strong>Posso iniciar a Etapa 2 enquanto a Etapa 1 ainda está em andamento?</strong></summary>

Não. Sem concluir a arqueologia da Etapa 1, os requisitos EARS não terão `source_legacy:` e a CI rejeitará o pull request.

</details>

<details>
<summary><strong>Quem conduz cada etapa?</strong></summary>

Consulte [`05-personas/OVERVIEW.md`](../05-personas/OVERVIEW.md). Resumo:

- Etapa 1 — você trabalha com `@archaeologist` e usa `@dba` para a descoberta de dados
- Etapa 2 — você trabalha com `@architect` e usa `@dba` para o projeto da migração
- Etapa 3 — você trabalha com `@builder` e `@dba`
- Validação final — o juiz valida a submissão

A Etapa 4 não faz parte do desafio individual.

</details>

<details>
<summary><strong>Quem vence o desafio individual?</strong></summary>

Vencem os dois primeiros participantes cujas submissões passarem na validação do juiz. Uma submissão é o PR `impl/<NNN>-<feature>` → `develop` no repositório do participante, com o checklist preenchido e o juiz notificado. O horário de criação do PR é o timestamp. Submissões rejeitadas podem ser corrigidas e reenviadas com um novo timestamp.

</details>

<details>
<summary><strong>O que conta como conclusão?</strong></summary>

A CI deve estar verde, todo requisito deve ter REQ-ID, EARS e `source_legacy:`, os testes devem passar, os dados da origem devem reconciliar, novas execuções devem evitar duplicidades e a listagem/pesquisa/detalhes devem cobrir toda a população de beneficiários migrados.

</details>

<details>
<summary><strong>Posso usar subagentes paralelos ou um orquestrador?</strong></summary>

Não. Use os modos Ask, Plan e Agent do Copilot com os agentes de etapa. Fan-out do Copilot CLI, harnesses de workers e orquestração paralela de subagentes não são permitidos no desafio individual.

</details>

<details>
<summary><strong>A Etapa 4 está incluída?</strong></summary>

Não. O desafio individual termina na Etapa 3 e na validação do juiz. Os arquivos da Etapa 4 permanecem no kit somente para atividades após o desafio.

</details>

---

## Sobre bloqueios

<details>
<summary><strong>Estou com um bloqueio. O que devo fazer?</strong></summary>

Use a regra dos 20 minutos ([`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) §6):

| Tempo de bloqueio | Ação |
|---|---|
| 5 min | Tente resolver por conta própria |
| 10 min | Releia o guia e as evidências pertinentes |
| 20 min | Peça apoio do workshop e registre o bloqueio |
| 30 min | Reduza a amplitude da capacidade, nunca a população migrada nem o padrão de verificação |

</details>

<details>
<summary><strong>Como peço ajuda com eficiência?</strong></summary>

Use três linhas: (1) Objetivo, (2) O que tentei, (3) O bloqueio. Consulte o exemplo em [`00-TEAM-FLOW.md`](../00-TEAM-FLOW.md) §6.

</details>

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Solução de problemas](troubleshooting.md)<br/><sub>Erros comuns e soluções.</sub> | [Kit em PT-BR](../README.md)<br/><sub>Hub principal.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
