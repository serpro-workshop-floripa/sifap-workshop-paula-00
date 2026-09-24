# Guia de configuração: preparação para o desafio individual

> **Trilha:** [Kit do desafio individual](README.md) › **Configuração**

Conclua estas verificações antes das 14:00. O desafio cronometrado começa diretamente em `@archaeologist`; a configuração é uma atividade prévia.

![Configuração](https://img.shields.io/badge/Configura%C3%A7%C3%A3o-00-171717?style=flat-square) ![Duração: 45 min](https://img.shields.io/badge/Dura%C3%A7%C3%A3o-45%20min-737373?style=flat-square) ![Quando: antes das 14:00](https://img.shields.io/badge/Quando-Antes%20das%2014%3A00-A3A3A3?style=flat-square)

| Campo | Valor |
|---|---|
| **Público-alvo** | Um participante em seu próprio computador |
| **Pré-requisitos** | Conta do GitHub com o Copilot habilitado |
| **Tempo estimado** | 45 minutos depois que as ferramentas e os acessos estiverem disponíveis |
| **Resultado esperado** | Computador, repositório, Copilot, Spec-Kit e preparação dos dados de origem verificados |

> [!WARNING]
> Usuários do Windows: blocos de terminal com heredoc ou `for` pressupõem Git Bash ou WSL. Não use PowerShell nem CMD para esses blocos.

---

## 1. Verifique os pré-requisitos do computador

| Ferramenta | Versão mínima | Como verificar | Se estiver ausente |
|---|---|---|---|
| Git | 2.40+ | `git --version` | <https://git-scm.com/downloads> |
| GitHub CLI | 2.40+ | `gh --version` | <https://cli.github.com> |
| VS Code | Versão Stable ou Insiders atualmente suportada | Help -> About; verifique Ask, Plan, Agent e agentes personalizados | <https://code.visualstudio.com/download> |
| Docker Desktop | 4.30+ | `docker --version` e abra o aplicativo | <https://www.docker.com/products/docker-desktop> |
| Java 21 JDK | 21 | `java -version` | <https://learn.microsoft.com/java/openjdk/download> |
| Node.js | 20, conforme a versão fixada na CI fornecida | `node --version` | <https://nodejs.org/en/download> |
| pnpm | 9, conforme a CI de frontend fornecida | `pnpm --version` | <https://pnpm.io/installation> |

Essas versões são a linha de base do exercício, não uma declaração de suporte para produção. Avalie o suporte de runtime separadamente antes de qualquer implantação real.

---

## 2. Crie seu repositório de participante

Use o kit público como template para seu próprio repositório privado.

1. Abra o [kit público](https://github.com/workshop-gbb/datacorp-sifap-modernization-team-kit/tree/main).
2. Clique em **Use this template** -> **Create a new repository**.
3. Escolha a organização do workshop indicada pelos facilitadores.
4. Use o nome de repositório atribuído a você.
5. Defina a visibilidade como **Private**.
6. Deixe **Include all branches** desmarcado, a menos que os facilitadores orientem o contrário.

Nunca faça push para o kit público. Seu trabalho ocorre somente em seu repositório privado.

---

## 3. Clone e crie `develop`

```bash
mkdir -p ~/Code && cd ~/Code
git clone --branch main https://github.com/<WORKSHOP_ORG>/<YOUR-REPO>.git
cd <YOUR-REPO>
ls 01-archaeology/legacy-sifap .github/agents .github/prompts .github/instructions .github/skills
git checkout -b develop
git push -u origin develop
```

Proteja `main` e `develop` caso as permissões de seu repositório permitam. Exija PRs, resolução de conversas e as verificações reais da CI assim que elas tiverem sido executadas.

---

## 4. Ative o GitHub Copilot no VS Code

1. Abra a raiz do repositório com `code .`.
2. Entre no GitHub Copilot pelo VS Code.
3. Abra o Copilot Chat.
4. Verifique se os modos Ask, Plan e Agent estão disponíveis.
5. Pergunte:

```text
What stack are we using in this project?
```

A resposta deve incluir Java 21, Spring Boot 3.3, Next.js 15, PostgreSQL 16 e o contexto de modernização do SIFAP. Caso contrário, confirme se `.github/copilot-instructions.md` foi carregado e recarregue o VS Code.

---

## 5. Valide os agentes de etapa e as skills de função

```bash
ls .github/agents .github/prompts .github/instructions .github/skills
```

Abra estes itens antes das 14:00:

- [`06-stage-agents/README.md`](06-stage-agents/README.md)
- [`05-personas/`](05-personas/)
- [`09-cheat-sheets/copilot-3-modes.md`](09-cheat-sheets/copilot-3-modes.md)

Você cobre sozinho todas as responsabilidades das funções. Não adicione uma lista de participantes às instruções carregadas globalmente.

---

## 6. Instale o Spec-Kit oficial

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
specify version
```

Substitua `vX.Y.Z` pela versão aprovada pelos facilitadores. Confirme as opções dos comandos com `--help`; elas podem mudar entre versões.

Inicialize uma vez na raiz do repositório caso `.specify/` ainda não esteja presente:

```bash
specify init . --integration copilot
```

Não execute novamente a inicialização sem verificar os artefatos existentes.

---

## 7. Entenda a estratégia de branches do desafio

```text
main                    <- stable, protected
develop                 <- integration branch
spec/NNN-feature        <- Stage 2 specification work
impl/NNN-feature        <- Stage 3 implementation and judged submission
```

Somente os prefixos `spec/` e `impl/` são usados durante o desafio cronometrado. O PR final de envio é `impl/<NNN>-<feature>` -> `develop`. Consulte [`00-GIT-WORKFLOW.md`](00-GIT-WORKFLOW.md).

---

## 8. Preparação dos dados de origem antes das 14:00

Os fontes Natural locais, DDMs, FDT e documentos históricos são evidências somente para leitura. Eles não constituem um banco de dados Adabas em execução nem uma exportação atual de registros.

- [ ] Confirme o proprietário autorizado da origem, a versão, a procedência do conjunto de dados sintéticos e a população medida.
- [ ] Confirme se o acesso do participante permite consultas somente para leitura e extração suportada.
- [ ] Estabeleça uma rota de extração suportada e um limite consistente para o snapshot.
- [ ] Defina a população completa e autorizada de beneficiários e os dados relacionados necessários para a consulta.
- [ ] Registre contagens de referência, consultas de leitura representativas, anomalias e locais restritos de evidências sem copiar dados pessoais para o Git.

Se a origem estiver vazia, indisponível ou não puder ser extraída de maneira consistente, registre o bloqueio. A leitura dos fontes pode continuar, mas a aceitação da migração permanece bloqueada.

---

## 9. Teste rápido antes do desafio

- [ ] O repositório abre no VS Code pela raiz.
- [ ] `git status` funciona em `develop`.
- [ ] `gh auth status` é executado com sucesso.
- [ ] As versões de Java, Node, pnpm, Docker e Specify estão visíveis.
- [ ] O Copilot responde com a stack e o contexto corretos do projeto.
- [ ] Os comandos `/speckit.*` aparecem no Copilot caso o Spec-Kit esteja inicializado.
- [ ] Ao abrir **New issue** no GitHub, os templates fornecidos são exibidos.
- [ ] `.github/agents`, `.github/prompts`, `.github/instructions` e `.github/skills` estão presentes.
- [ ] [`00-TEAM-FLOW.md`](00-TEAM-FLOW.md) e [`00-START-HERE.md`](00-START-HERE.md) foram lidos.
- [ ] A preparação dos dados de origem foi verificada ou explicitamente bloqueada.

Quando essas verificações estiverem concluídas, você estará pronto para abrir `@archaeologist` às 14:00.

---

## Solução de problemas

### O Copilot não lê as instruções do projeto

- Abra o VS Code na raiz do repositório.
- Reinicie ou recarregue o VS Code.
- Confirme se `github.copilot.chat.useProjectInstructions` está habilitado.

### `specify init` falha ou os comandos não aparecem

- Confirme se `uv`, Python 3.11+ e Git estão instalados.
- Execute `specify version`.
- Inspecione `.specify/` antes de executar novamente a inicialização.
- Recarregue o VS Code.

### O Docker está indisponível quando necessário

Verifique as portas e interrompa somente o processo específico que estiver causando conflito:

```bash
lsof -i :5432 -i :8080 -i :3000
kill <PID>
```

Não use comandos que encerrem processos de maneira abrangente.

### Permissão negada ao fazer push para `main`

A proteção de branch está funcionando. Faça push de uma branch `spec/` ou `impl/` e abra um PR.

---

### Continue a leitura

| Anterior | Próximo |
|---|---|
| [Comece aqui](00-START-HERE.md)<br/><sub>Atividades prévias e início às 14:00.</sub> | [Fluxo de trabalho Git](00-GIT-WORKFLOW.md)<br/><sub>Regras de branch e envio.</sub> |

<sub>[Voltar ao índice do kit](README.md)</sub>
