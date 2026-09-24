# @evolution — Etapa 4: Evolução

> **Caminho:** [Kit da equipe](../../README.md) › [Agentes de etapa](../README.md) › **@evolution**

**O agente `@evolution` orienta o participante a transformar o trabalho local da Etapa 3 em uma entrega revisável: Issues bem escritas para o modo Agente do Copilot, revisão de PR, registros de CI/CD e um relatório de experiência.**

| Campo | Valor |
|---|---|
| **Público-alvo** | Líder Técnico (líder), Engenheiro de DevOps, Redator Técnico, Desenvolvedor e Engenheiro de QA |
| **Pré-requisitos** | Checkpoint da Etapa 3 com backend/frontend funcional e testes relevantes |
| **Tempo estimado** | Não utilizada no desafio individual |
| **Etapa** | Etapa 4 — Evolução |
| **Resultado esperado** | Issue criada ou esboçada, PR revisado ou próximo passo registrado e relatório de experiência concluído |

![Etapa 4](https://img.shields.io/badge/Stage-4%20%C2%B7%20Evolution-171717?style=flat-square)
![Abordagem operacional](https://img.shields.io/badge/Approach-Operational-404040?style=flat-square)

---

## Quando usar

Use este agente quando o protótipo existir e o participante precisar transformar o trabalho local em uma entrega revisável: Issues, PRs, CI/CD, IaC, runbook e relatório final.

- **Liderança:** Líder Técnico
- **Apoio importante:** Engenheiro de DevOps, Redator Técnico, Desenvolvedor e Engenheiro de QA
- **Pré-requisito obrigatório:** protótipo com backend/frontend funcional e testes relevantes

---

## O que o agente faz

- Ajuda a estruturar Issues pequenas e revisáveis para o modo Agente do Copilot
- Orienta a revisão de PR com ênfase em bugs, riscos, regressões e testes ausentes
- Cria workflows do GitHub Actions para build, teste e validação do Terraform
- Converte comandos individuais em um runbook de operações
- Produz o relatório de experiência do modo Agente (`agent-experience-report.md`)

---

## O que o agente NÃO faz

- Não delega uma Issue vaga ao modo Agente; exige contexto, escopo e critérios de aceitação
- Não aprova um PR gerado por IA sem revisão humana explícita
- Não cria novas funcionalidades na Etapa 4; adiciona-as ao backlog
- Não oculta trabalhos pendentes; documenta riscos e registra o próximo passo

---

## Entradas

| Entrada | Local |
|---|---|
| Backend/frontend da Etapa 3 | `backend/`, `frontend/` |
| Trabalho pendente conhecido | Notas do checkpoint da Etapa 3 |
| `spec.md` da funcionalidade | `.spec/<NNN>-<feature>/spec.md` |
| Plano técnico | `.spec/<NNN>-<feature>/plan.md` |
| ADRs de apoio | Registros reais vinculados no plano |

---

## Saídas esperadas

| Artefato | Local |
|---|---|
| Issue para o modo Agente | GitHub Issues do repositório |
| Revisão de PR (se disponível) | GitHub Pull Requests |
| Workflow de CI/CD (se relevante) | `.github/workflows/` |
| Runbook (se relevante) | `docs/runbook.md` |
| Relatório de experiência do agente | `04-evolution/agent-experience-report.md` |

---

## Como selecionar o agente no Copilot Chat

- [ ] **Abra o Copilot Chat** no VS Code (`Ctrl+Alt+I` / `Cmd+Alt+I`).
- [ ] **Selecione `@evolution`** no seletor de agentes.
- [ ] **Abra a lista de trabalhos pendentes da Etapa 3** no editor.
- [ ] **Cole o prompt inicial** abaixo e pressione Enter.

```text
I am starting Stage 4 — Evolution.
We have a prototype with a backend, frontend, and tests.
Help review a small Issue for Copilot Agent and record the delegation
outcome. Do not invent requirements, architecture, or criteria.
```

---

## Exemplos de prompts

| Situação | Prompt útil |
|---|---|
| Issue para o modo Agente | "Escreva uma Issue pequena com contexto, arquivos relevantes, critérios de aceitação e itens fora do escopo." |
| Revisão de PR | "Revise este PR priorizando bugs, riscos, regressões e testes ausentes." |
| CI/CD | "Crie um workflow do GitHub Actions para build, teste e validação do Terraform." |
| Runbook | "Transforme estes comandos em um runbook para um novo membro participante de operações." |
| Relatório final | "Escreva o `agent-experience-report` com o que funcionou, o que falhou e o que aprendemos." |

---

## Definição de pronto

- [ ] Uma Issue pequena foi criada ou deixada como rascunho revisável, com contexto, escopo e critérios de aceitação.
- [ ] Um PR disponível recebeu revisão humana; se não houver PR, o próximo passo está documentado.
- [ ] O status de CI/IaC foi registrado sem criar infraestrutura apenas para cumprir uma meta.
- [ ] O relatório de experiência do modo Agente está completo.
- [ ] DBA/QA transferem evidências reais de reconciliação, consulta e recuperação após a alteração, ou bloqueios, para a validação integrada das 17:10–17:40; não há aceitação final prematura.

---

## Erros comuns

| Sintoma | Causa | Correção |
|---|---|---|
| O modo Agente produz um resultado fora do escopo | Issue vaga sem critérios explícitos | Reescreva a Issue com contexto, arquivos relevantes e itens fora do escopo |
| PR gerado por IA é integrado sem revisão | Confiança excessiva no resultado do agente | Revise-o exatamente como revisaria um PR humano |
| Nova funcionalidade aparece no final | Controle de escopo inadequado | Adicione-a ao backlog; não a implemente na Etapa 4 |
| Trabalho pendente ocultado para alegar aceitação | Medo de julgamento | Documente o risco e o bloqueio; transparência é o objetivo |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [@builder](../03-builder/README.md)<br/><sub>Etapa 3: construa a implementação rastreável.</sub> | [Agentes de etapa — visão geral](../README.md)<br/><sub>Visão geral dos 4 agentes e do cronograma do workshop.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
