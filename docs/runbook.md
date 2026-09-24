# Modelo de runbook do participante

![Tipo: runbook](https://img.shields.io/badge/Type-Runbook-171717?style=flat-square)
![Responsável: DevOps](https://img.shields.io/badge/Owner-DevOps-737373?style=flat-square)

> **Caminho:** [Kit da equipe](../README.md) › [Documentação](README.md) › **Runbook**

**Modelo para documentar como executar, verificar e diagnosticar a solução do próprio participante.**
Preencha-o com os comandos e as evidências do participante; ele não descreve nem concede acesso aos ambientes do instrutor.

| Campo | Valor |
|---|---|
| **Público-alvo** | Participante, especialmente ao cobrir responsabilidades de DevOps |
| **Pré-requisitos** | Setup local concluído conforme [`00-SETUP.md`](../00-SETUP.md) |
| **Resultado esperado** | Ambiente local funcional, CI legível e escalonamento correto |

---

## Verificações iniciais (primeiro uso)

- [ ] **Verifique os pré-requisitos** — execute cada linha e confirme que não ocorrem erros:

```bash
git --version
java -version
node --version
docker --version
specify version
```

> [!NOTE]
> O kit não inclui um protótipo pronto. Quando você criar `backend/`, `frontend/` e, se necessário após o desafio, `infra/`, registre aqui os comandos reais de execução.

Depois de criar o protótipo, documente:

| Serviço | URL / Comando |
|---|---|
| Health do backend | — |
| Swagger UI | — |
| Frontend local | — |
| Como configurar a autenticação local, sem registrar senhas | — |

---

## Rotina diária

- [ ] **Verifique o estado do repositório:**

```bash
git status
```

- [ ] **Execute os testes do backend** (quando `backend/` existir):

```bash
(cd backend && ./mvnw test)
```

- [ ] **Execute os testes do frontend** (quando `frontend/` existir):

```bash
(cd frontend && pnpm test)
```

---

## Operações de migração de dados (responsabilidade do DBA, verificação do QA)

Preencha esta tabela usando seus [registros de migração de dados](data-migration/)
e o [ciclo de vida aprovado](DATA-MIGRATION.md). Estas são instruções não
preenchidas para o participante, não comandos para administrar o ambiente de origem.

| Item | Comando sob responsabilidade do participante ou referência de evidência sanitizada |
|---|---|
| Versão da fonte autorizada, população medida e identificador do snapshot | — |
| Extração compatível e verificação de integridade | — |
| Versão do schema de destino e execução de staging/carga | — |
| Contabilização de registros, rejeições e reconciliação independente | — |
| Verificações completas de listagem/pesquisa/detalhes de beneficiários | — |
| Nova execução/retomada do mesmo snapshot sem duplicidades | — |
| Recuperação do destino sem alterar a origem | — |
| Retenção e limpeza de evidências restritas | — |
| DBA responsável, revisor de QA e aceitação ou bloqueios do PO | — |

Não faça commit de registros de origem, dados pessoais, secrets nem endereços de
acesso. Diferenças de dados não resolvidas bloqueiam a aceitação; seeds de teste
e builds aprovados não substituem a população migrada.

---

## CI — Entenda os workflows

Use as definições reais dos workflows como fonte de verdade para gatilhos e
comandos. Os jobs da aplicação são filtrados por path; uma execução verde apenas
de documentação não comprova que backend, frontend ou migração foram testados.

| Arquivo de workflow | O que verifica | Quando executa |
|---|---|---|
| [`ci.yml`](../.github/workflows/ci.yml) | Proteção de formato Natural; `./mvnw -B verify` condicional no backend, verificações pnpm no frontend e validação Terraform | Pushes e PRs nas branches configuradas; jobs da aplicação dependem dos paths alterados |
| [`spec-quality.yml`](../.github/workflows/spec-quality.yml) | Validação de Markdown/primitivos, gate bloqueante de referência à fonte e relatório não bloqueante de referência a testes | Pushes nas branches configuradas e PRs filtrados por path |

- [ ] **Quando a CI falhar** — abra a aba Actions no GitHub, selecione a execução com falha e leia o log.
- [ ] **Corrija localmente** — reproduza o erro com os comandos do protótipo criado antes de fazer novo push.

---

## Infraestrutura criada pelo participante — Etapa 4 pós-desafio

> [!NOTE]
> Não é usada no desafio individual (14:00-17:40). O desafio termina na Etapa 3 e na validação do juiz. Consulte a [ADR-0003](../docs/adr/0003-individual-challenge-format.md).

O kit não inclui recursos provisionados, arquivos de state nem uma assinatura configurada. Se o escopo pós-desafio incluir infraestrutura, siga o [guia da Etapa 4](../04-evolution/GUIDE.md) e documente apenas o que você criar.

- [ ] Registre os módulos e arquivos de configuração que realmente existem.
- [ ] Registre os comandos de validação e o resultado da revisão do plano.
- [ ] Registre permissões e limites de planejamento; não faça deployment nem provisionamento durante este workshop.
- [ ] Descreva a autenticação sem fazer commit de secrets, tokens ou arquivos de state.
- [ ] Se nada foi implantado, declare essa limitação em vez de apresentar um ambiente como pronto.

---

## Problemas comuns

| Sintoma | Causa provável | Correção | Como confirmar |
|---|---|---|---|
| O ambiente local trava | Uma porta necessária pode estar em uso | Identifique o responsável pelo processo e a configuração de porta aprovada; não pare o processo de outro participante | O serviço selecionado inicia sem erro de porta |
| `mvn verify` falha no Testcontainers | O Docker não está em execução | Inicie o Docker Desktop | Os testes passam na próxima execução |
| `pnpm test` falha nos snapshots | Uma mudança intencional de comportamento ou uma regressão | Compare com o requisito aprovado; atualize apenas expectativas revisadas, nunca aceite em massa para forçar o verde | Os testes e a revisão confirmam o comportamento pretendido |
| O plano de infraestrutura é rejeitado | A configuração não atende aos limites ou políticas autorizados | Leia o diagnóstico e revise o plano antes do deployment | O plano revisado passa na validação |
| O GitHub Actions não consegue acessar o Azure | A autenticação não corresponde ao repositório, branch ou ambiente | Verifique a configuração OIDC autorizada e peça ajuda ao responsável pelo acesso | O workflow autentica sem secrets em commits |

---

## Quando escalar para o facilitador

- [ ] O build falhou por mais de 20 minutos sem solução.
- [ ] A assinatura do Azure parece estar suspensa.
- [ ] Alguma ação irreversível foi executada por engano, como `terraform destroy`.

Use o formato de escalonamento em três linhas da [regra dos 20 minutos](../00-TEAM-FLOW.md#6-a-regra-dos-20-minutos).

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [FAQ](FAQ.md)<br/><sub>Perguntas frequentes.</sub> | [Solução de problemas](troubleshooting.md)<br/><sub>Erros comuns e soluções.</sub> |

<sub>[Voltar ao índice do kit](README.md)</sub>
