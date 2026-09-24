# Solução de problemas consolidada

> **Caminho:** [Kit da equipe](../README.md) › [Documentação](README.md) › **Solução de problemas**

**Um guia de diagnóstico e resolução para os erros mais comuns do workshop** — use `Ctrl+F` para procurar o sintoma.

| Campo | Valor |
|---|---|
| **Público-alvo** | Todo participante |
| **Como usar** | Use `Ctrl+F` para procurar o sintoma. Se não o encontrar, consulte [FAQ.md](FAQ.md) |
| **Resultado esperado** | O problema é resolvido seguindo as etapas descritas |

---

## Sumário

- [Configuração e ambiente](#configuração-e-ambiente)
- [Copilot, agentes e personas](#copilot-agentes-e-personas)
- [Spec-Kit e EARS](#spec-kit-e-ears)
- [Backend — Java e Spring Boot](#backend--java-e-spring-boot)
- [Frontend — Next.js e Node](#frontend--nextjs-e-node)
- [Docker](#docker)
- [Git e GitHub](#git-e-github)
- [Terraform e Azure](#terraform-e-azure)
- [Plano B — indisponibilidade do Copilot](#plano-b--indisponibilidade-do-copilot)

---

## Configuração e ambiente

### Ferramentas locais ausentes (Java, Node, Maven)

| Campo | Detalhes |
|---|---|
| **Sintoma** | Uma mensagem de erro "command not found" para `java`, `node` ou `mvn` |
| **Causa provável** | As ferramentas locais ainda não foram instaladas |
| **Correção** | Instale as versões especificadas em [`00-SETUP.md`](../00-SETUP.md) e valide-as com `java -version`, `node --version` e `git --version` |
| **Como confirmar** | Os três comandos retornam a versão esperada sem erros |

### "git: command not found" no terminal do VS Code (Mac)

| Campo | Detalhes |
|---|---|
| **Sintoma** | Ocorre um erro ao tentar executar qualquer comando `git` |
| **Causa provável** | As ferramentas de CLI do Xcode não estão instaladas |
| **Correção** | Execute `xcode-select --install` e siga as instruções do instalador |
| **Como confirmar** | `git --version` retorna uma versão sem erros |

---

## Copilot, agentes e personas

### O slash command não aparece no Chat

| Campo | Detalhes |
|---|---|
| **Sintoma** | `/write-ears-spec`, `/map-source-data` ou outro prompt fornecido não aparece |
| **Causa provável** | O VS Code não recarregou o diretório consolidado `.github/` ou a janela foi aberta fora da raiz do repositório |
| **Correção** | Confirme que `.github/prompts/` contém arquivos e recarregue a janela: `Cmd+Shift+P` → _Developer: Reload Window_ |
| **Como confirmar** | Os comandos aparecem quando você digita `/` no Chat |

> [!CAUTION]
> Mantenha uma única cópia ativa em `.github/`. A manutenção intencional de
> primitivos é permitida mediante revisão e uso do validador de primitivos;
> copiar uma segunda árvore ou presumir que pastas de guias instalam agentes
> causa divergências.

### "Não consigo selecionar `@archaeologist` no Chat"

| Campo | Detalhes |
|---|---|
| **Sintoma** | O agente `@archaeologist` não aparece no seletor do Chat |
| **Causa 1** | `.github/agents/archaeologist.agent.md` está ausente ou a raiz do workspace está incorreta |
| **Causa 2** | A extensão GitHub Copilot Chat está desatualizada |
| **Correção** | Verifique o arquivo do agente ativo em `.github/agents/`, seu frontmatter e a raiz do workspace; depois, recarregue ou atualize o Copilot |
| **Como confirmar** | O agente aparece na lista suspensa do Chat |

### O Copilot responde sem o contexto pertinente

| Campo | Detalhes |
|---|---|
| **Sintoma** | Respostas genéricas sem relação com o SIFAP (Sistema de Fiscalização e Administração de Pagamentos) ou com a etapa atual |
| **Causa provável** | Nenhum agente de etapa está selecionado ou o agente incorreto foi selecionado |
| **Correção** | Confirme a etapa atual e selecione o agente correspondente na lista suspensa do Chat |
| **Como confirmar** | As respostas passam a mencionar a etapa e o contexto do sistema legado |

### "Quero usar o modo Plan, mas somente Ask está disponível"

| Campo | Detalhes |
|---|---|
| **Sintoma** | O modo Plan não está disponível |
| **Causa provável** | A extensão do Copilot está desatualizada |
| **Correção** | Atualize a extensão GitHub Copilot Chat no VS Code |
| **Como confirmar** | O modo Plan aparece no seletor de modos |

---

## Spec-Kit e EARS

### "`specify version` retorna command not found"

| Campo | Detalhes |
|---|---|
| **Sintoma** | Ocorre um erro ao executar qualquer comando `specify` |
| **Causa provável** | O Spec-Kit não está instalado |
| **Correção** | Execute os comandos abaixo |
| **Como confirmar** | `specify version` retorna um número de versão |

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify version
```

### A CI rejeitou o PR: `missing source_legacy`

| Campo | Detalhes |
|---|---|
| **Sintoma** | A CI bloqueia o pull request com um erro de rastreabilidade |
| **Causa provável** | Um ou mais requisitos EARS não incluem uma linha `source_legacy:` |
| **Correção** | Adicione uma linha `source_legacy:` sem marcador nas 20 linhas seguintes ao requisito, com um path de fonte real e compatível e o trecho opcional `#L<start>-L<end>`, ou `[GREENFIELD] <justification>` |
| **Como confirmar** | A CI passa na execução seguinte |

Consulte [`07-concepts/05-ears-notation.md`](../07-concepts/05-ears-notation.md) para ver o formato correto.

### `/speckit.clarify` está fazendo perguntas demais

| Campo | Detalhes |
|---|---|
| **Sintoma** | O comando faz 10 perguntas ou mais |
| **Causa** | O escopo ou as evidências podem ser amplos demais ou estar incompletos; o comportamento do comando depende da versão instalada do Spec-Kit |
| **Ação** | Resolva com evidências as questões que bloqueiam o escopo. Não invente respostas; reduza o escopo da capacidade mediante revisão ou mantenha bloqueado o trabalho afetado |

---

## Backend — Java e Spring Boot

### O backend não inicia — erro de conexão com o Postgres

| Campo | Detalhes |
|---|---|
| **Sintoma** | Ocorre um erro `Connection refused` ou semelhante quando o backend inicia |
| **Causa provável** | O Postgres não está em execução ou a URL em `application.yml` está incorreta |
| **Correção** | Verifique `application.yml` e inicie o Postgres usando o método definido para a sua solução (local, Testcontainers ou Docker Compose) |
| **Como confirmar** | O backend inicia e responde em `/actuator/health` |

### Flyway: `Migration checksum mismatch`

| Campo | Detalhes |
|---|---|
| **Sintoma** | Ocorre um erro do Flyway quando o backend inicia |
| **Causa provável** | Um arquivo de migração existente foi editado depois de ser aplicado |
| **Correção** | Compare a migração aplicada com o histórico de versões, restaure somente o original verificado mediante revisão e adicione `V<N+1>__description.sql` |
| **Como confirmar** | O backend inicia sem erros do Flyway |

> [!CAUTION]
> Nunca edite arquivos de migração que já foram aplicados (V1, V2, V3...). Sempre crie um novo arquivo com o próximo número de versão.

### Testcontainers: `Could not find a valid Docker environment`

| Campo | Detalhes |
|---|---|
| **Sintoma** | Testes que usam Testcontainers falham com um erro de ambiente do Docker |
| **Causa provável** | O Docker não está em execução ou o socket usa um path não padrão |
| **Correção (macOS)** | Inicie o container runtime configurado e inspecione seu contexto/socket real. Não force um path de socket presumido nem substitua verificações de integração por mocks |
| **Como confirmar** | Os testes passam na execução seguinte |

---

## Frontend — Next.js e Node

### O frontend exibe `ECONNREFUSED localhost:8080`

| Campo | Detalhes |
|---|---|
| **Sintoma** | A página do frontend exibe um erro de conexão recusada |
| **Causa provável** | O backend não está em execução ou usa uma porta diferente |
| **Correção** | Confirme que o backend está em execução e que a URL do frontend aponta para a porta correta |
| **Como confirmar** | A página carrega os dados normalmente |

### `Module not found: shadcn/ui`

| Campo | Detalhes |
|---|---|
| **Sintoma** | Ocorre um erro de módulo não encontrado quando o frontend inicia |
| **Causa provável** | Um componente shadcn gerado ou seu alias de importação está ausente, ou as dependências fixadas não estão instaladas |
| **Correção** | Inspecione a importação e o alias reais do componente. Restaure o componente revisado ou instale com pnpm as dependências fixadas existentes; não presuma que `shadcn/ui` seja um pacote de runtime |
| **Como confirmar** | O frontend inicia sem erros de módulo |

---

## Docker

### `Cannot connect to the Docker daemon`

| Campo | Detalhes |
|---|---|
| **Sintoma** | Todos os comandos do Docker falham com um erro do daemon |
| **Causa provável** | O Docker Desktop está parado |
| **Correção** | Abra o Docker Desktop e aguarde até que o serviço inicie completamente |
| **Como confirmar** | `docker ps` retorna a lista de contêineres sem erros |

### `port is already allocated`

| Campo | Detalhes |
|---|---|
| **Sintoma** | O contêiner não inicia devido a um conflito de porta |
| **Causa provável** | A porta 5432, 8080 ou 3000 já está em uso por outro processo |
| **Correção** | Execute `lsof -i :8080` para identificar e interromper o processo ou altere a porta na configuração local |
| **Como confirmar** | O contêiner inicia sem erro de porta |

### O Docker Desktop informa `Out of memory`

| Campo | Detalhes |
|---|---|
| **Sintoma** | Os contêineres falham ou ficam lentos, e um aviso de memória aparece |
| **Causa provável** | O limite de RAM alocado ao Docker Desktop é muito baixo |
| **Correção** | Docker Desktop → Settings → Resources → Memory → 8 GB ou mais |
| **Como confirmar** | Os contêineres iniciam e respondem normalmente |

---

## Git e GitHub

### Push rejeitado: `protected branch`

| Campo | Detalhes |
|---|---|
| **Sintoma** | `git push` é rejeitado com uma mensagem de branch protegida |
| **Causa provável** | Houve uma tentativa de push direto para `main` ou `develop` |
| **Correção** | Crie uma branch e abra um pull request. Consulte [`00-GIT-WORKFLOW.md`](../00-GIT-WORKFLOW.md) |
| **Como confirmar** | O pull request é criado com sucesso |

### Conflito de merge

| Campo | Detalhes |
|---|---|
| **Sintoma** | Marcadores `<<<<<<<` aparecem nos arquivos durante um merge ou rebase |
| **Causa provável** | Alguém alterou o mesmo arquivo em `develop` antes de você |
| **Correção** | Execute o bloco abaixo, resolva os conflitos manualmente e conclua o rebase |
| **Como confirmar** | `git status` não mostra mais arquivos com conflitos |

```bash
git fetch origin
git rebase origin/develop
# Resolve conflicts in files containing markers
git add <file>
git rebase --continue
```

### Commit criado por engano diretamente em `develop`

```bash
git reset --soft HEAD~1
git stash
git checkout -b nova-branch
git stash pop
git commit -m "..."
```

### `gh: command not found`

| Campo | Detalhes |
|---|---|
| **Sintoma** | Ocorre um erro ao usar qualquer comando `gh` |
| **Causa provável** | A GitHub CLI não está instalada |
| **Correção** | `brew install gh && gh auth login` |
| **Como confirmar** | `gh --version` retorna uma versão sem erros |

---

## Terraform e Azure

### `Error: building AzureRM Client`

| Campo | Detalhes |
|---|---|
| **Sintoma** | O Terraform falha ao inicializar o provider do Azure |
| **Causa provável** | A sessão da Azure CLI expirou ou não foi iniciada |
| **Correção** | Execute `az login` |
| **Como confirmar** | `terraform plan` é executado sem erros de autenticação |

### `terraform plan` mostra centenas de novos recursos

| Campo | Detalhes |
|---|---|
| **Sintoma** | A saída do `plan` lista muitos recursos para criação |
| **Causa** | O arquivo de state está vazio — esse é o comportamento esperado na primeira execução |
| **Ação** | Revise o plano. Não execute `apply`. |

> [!CAUTION]
> O workshop autoriza somente `terraform plan`. Executar `terraform apply` cria recursos reais no Azure e gera custos imediatamente.

---

## Plano B — indisponibilidade do Copilot

Se o Copilot Chat parar de responder por mais de 5 minutos:

> [!WARNING]
> Não espere passivamente. O desafio individual dura das 14:00 às 17:40, e cada minuto ocioso tem um custo alto.

- [ ] **Recarregue** — tente `Cmd+Shift+P` → _Reload Window_. Se o Copilot voltar, continue normalmente.
- [ ] **Trabalhe manualmente** — se ele continuar offline, retome os modelos e artefatos que você já produziu.
- [ ] **Estruture o próximo artefato** — use as evidências disponíveis sem inventar dados.
- [ ] **Documente no PR** — escreva: _"Concluído manualmente em X min (Copilot offline)"_ — isso apoia a validação do juiz e a revisão de bloqueios.
- [ ] **Registre a limitação** — informe que o artefato pode estar menos refinado que o habitual porque o Copilot estava offline.

A CI continua validando as alterações mesmo quando o Copilot está offline. O trabalho não para.

| Artefato sem o Copilot | Próxima etapa |
|---|---|
| EARS na Etapa 2 | Use as descobertas rastreáveis e o fluxo de trabalho do [Spec-Kit](../09-cheat-sheets/spec-kit-workflow.md) |
| ADR na Etapa 2 | Preencha o [modelo de ADR](adr/0000-template.md) |
| Implementação na Etapa 3 | Revise os requisitos EARS priorizados, os DDMs e suas decisões |
| Issue da Etapa 4 pós-desafio | Escreva o contexto, os critérios de aceitação e a rastreabilidade da mudança |

---

## Quando nenhuma das soluções acima funcionar

| Tempo bloqueado | Ação |
|---|---|
| 5 min | Leia o erro novamente com atenção. Use o Copilot Ask: _"O que significa este erro: `<paste the error>`"_ |
| 10 min | Releia o guia da etapa pertinente e as evidências |
| 20 min | Levante a mão e chame o facilitador (regra da seção 6 de TEAM-FLOW) |
| 30 min | Pause esta tarefa e trabalhe em outra enquanto alguém ajuda |

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Kit em PT-BR](../README.md)<br/><sub>Hub principal.</sub> | [FAQ](FAQ.md)<br/><sub>Perguntas frequentes.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
