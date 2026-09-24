---
name: "acquire-codebase-knowledge"
description: "Use quando a pessoa pedir explicitamente para mapear, documentar ou facilitar a integração em uma base de código existente, por exemplo: \"mapeie esta base de código\", \"documente esta arquitetura\", \"ajude-me a entender este repositório\" ou \"crie a documentação da base de código\". Não use em implementações rotineiras, correções de bugs ou alterações restritas, salvo quando o pedido também exigir descoberta em todo o repositório."
---
# Aquisição de conhecimento da base de código

Produza sete documentos preenchidos em `docs/codebase/` com as informações necessárias para trabalhar no projeto. Documente somente fatos verificáveis em arquivos ou na saída do terminal. Nunca faça inferências nem suposições.

## Quando invocar

- "Mapeie esta base de código e documente sua arquitetura."
- "Ajude-me a entender este repositório. Por onde começo?"
- "Crie a documentação da base de código para que uma nova pessoa contribua na primeira semana."
- "Documente a stack, a estrutura e as integrações deste projeto."

> [!NOTE]
> Neste workshop, a aplicação moderna só existe a partir da Etapa 3. Aponte esta skill para um projeto existente ou para o próprio kit. Trate tudo em `01-archaeology/legacy-sifap/` como evidência somente para leitura e nunca afirme o conteúdo de um programa ou campo legado sem verificá-lo. Registre como descobrir a informação e siga o gate de leitura em [`01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md`](../../../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md) e [`01-archaeology/legacy-sifap/HOW-TO-READ-NATURAL.md`](../../../01-archaeology/legacy-sifap/HOW-TO-READ-NATURAL.md).

## Procedimento

Copie e acompanhe este checklist:

```text
- [ ] Fase 1: executar a varredura e ler os documentos de intenção
- [ ] Fase 2: investigar cada área da documentação
- [ ] Fase 3: preencher os sete documentos em docs/codebase/
- [ ] Fase 4: validar os documentos, apresentar descobertas e resolver todos os itens [ASK USER]
```

### Modo de área de foco

Quando a pessoa indicar uma área de foco, por exemplo, "somente arquitetura" ou "testes e pontos de atenção":

1. Execute sempre a Fase 1 por completo.
2. Conclua primeiro os documentos da área de foco.
3. Nos documentos fora do foco ainda não analisados, mantenha as seções obrigatórias e marque informações desconhecidas com `[TODO]`.
4. Execute o ciclo de validação da Fase 4 nos sete documentos antes da resposta final.

### Fase 1: varrer e ler a intenção

1. Execute o script de varredura na raiz do projeto-alvo:

   ```bash
   python3 "$SKILL_ROOT/scripts/scan.py" --output docs/codebase/.codebase-scan.txt
   ```

   `$SKILL_ROOT` é o path absoluto da pasta da skill. O script funciona no Windows, macOS e Linux.

   **Início rápido:** quando o path estiver disponível:

   ```bash
   python3 /absolute/path/to/skills/acquire-codebase-knowledge/scripts/scan.py --output docs/codebase/.codebase-scan.txt
   ```

2. Procure arquivos `PRD`, `TRD`, `README`, `ROADMAP`, `SPEC` e `DESIGN` e leia-os.
3. Resuma a intenção declarada do projeto antes de ler o código-fonte.

### Fase 2: investigar

Use a saída da varredura para responder às perguntas dos sete templates. Carregue [`references/inquiry-checkpoints.md`](references/inquiry-checkpoints.md) para consultar a lista completa de perguntas por template.

Se a stack for ambígua, por exemplo, se houver vários manifestos, tipos de arquivo desconhecidos ou nenhum `package.json`, carregue [`references/stack-detection.md`](references/stack-detection.md).

### Fase 3: preencher os templates

Copie cada template de `assets/templates/` para `docs/codebase/`. Preencha-os nesta ordem:

1. [STACK.md](assets/templates/STACK.md): linguagem, runtime, frameworks e todas as dependências
2. [STRUCTURE.md](assets/templates/STRUCTURE.md): layout dos diretórios, pontos de entrada e arquivos principais
3. [ARCHITECTURE.md](assets/templates/ARCHITECTURE.md): camadas, padrões e fluxo de dados
4. [CONVENTIONS.md](assets/templates/CONVENTIONS.md): nomenclatura, formatação, tratamento de erros e imports
5. [INTEGRATIONS.md](assets/templates/INTEGRATIONS.md): APIs externas, bancos de dados, autenticação e monitoramento
6. [TESTING.md](assets/templates/TESTING.md): frameworks, organização de arquivos e estratégia de mocks
7. [CONCERNS.md](assets/templates/CONCERNS.md): dívida técnica, bugs, riscos de segurança e gargalos de desempenho

Use `[TODO]` quando o código não permitir determinar uma informação. Use `[ASK USER]` quando a resposta depender da intenção da equipe.

### Fase 4: validar, corrigir e verificar

Execute este ciclo obrigatório antes de finalizar:

1. Valide cada documento conforme `references/inquiry-checkpoints.md`.
2. Confirme pelo menos uma referência de evidência para cada afirmação não trivial.
3. Se uma seção obrigatória estiver ausente ou sem sustentação:
   - corrija o documento;
   - execute novamente a validação.
4. Repita até que os sete documentos passem.

Depois, apresente um resumo dos sete documentos, liste cada item `[ASK USER]` como pergunta numerada e destaque divergências entre intenção e realidade identificadas na Fase 1.

Critérios de aprovação:

- Nenhuma afirmação sem sustentação.
- Nenhuma seção obrigatória vazia.
- Informações desconhecidas usam `[TODO]`, não suposições.
- Lacunas de intenção da equipe usam `[ASK USER]`.

### Cuidados

**Monorepos:** o `package.json` da raiz pode não conter código-fonte. Verifique `workspaces` e os diretórios `packages/` ou `apps/`. Cada workspace pode ter dependências e convenções próprias. Mapeie cada subpacote separadamente.

**README desatualizado:** o README costuma descrever a arquitetura pretendida, não a atual. Compare suas afirmações com a estrutura real de arquivos.

**Aliases de paths do TypeScript:** a configuração `paths` de `tsconfig.json` faz com que imports como `@/foo` não correspondam diretamente ao sistema de arquivos. Mapeie os aliases para paths reais antes de documentar a estrutura.

**Saída gerada ou compilada:** nunca documente padrões de `dist/`, `build/`, `generated/`, `.next/`, `out/` ou `__pycache__/`. Documente somente convenções do código-fonte.

**`.env.example` revela configurações obrigatórias:** secrets nunca devem estar no repositório. Leia `.env.example`, `.env.template` ou `.env.sample` para descobrir as variáveis de ambiente necessárias.

**`devDependencies` não são a stack de produção:** somente `dependencies`, ou equivalente como `[tool.poetry.dependencies]`, executa em produção. Documente linters, formatadores e frameworks de teste separadamente como ferramentas de desenvolvimento.

**TODOs de testes não são dívida de produção:** TODOs em `test/`, `tests/`, `__tests__/` ou `spec/` indicam lacunas de cobertura, não dívida técnica de produção. Separe-os em `CONCERNS.md`.

**Arquivos com muitas alterações são áreas frágeis:** os arquivos mais frequentes no histórico recente do Git têm maior taxa de modificação e podem ocultar complexidade. Registre-os em `CONCERNS.md`.

### Antipadrões

| Antipadrão | Ação correta |
|------------|--------------|
| "Usa Clean Architecture com camadas Domain/Data", sem esses diretórios | Declare somente o que a estrutura de diretórios demonstra. |
| "Este é um projeto Next.js", sem verificar `package.json` | Verifique primeiro `dependencies` e declare somente o que existe. |
| Deduzir o banco de dados de um nome de variável como `dbUrl` | Verifique no manifesto `pg`, `mysql2`, `mongoose`, `prisma` e similares. |
| Documentar padrões de nomes de `dist/` ou `build/` como convenções | Analise somente arquivos-fonte. |

### Seções adicionais da saída da varredura

O script `scan.py` produz estas seções além da saída original:

- **CODE METRICS**: total de arquivos, linhas de código por linguagem e maiores arquivos, que sinalizam complexidade
- **CI/CD PIPELINES**: GitHub Actions, GitLab CI, Jenkins, CircleCI e outros pipelines detectados
- **CONTAINERS & ORCHESTRATION**: configurações de Docker, Docker Compose, Kubernetes e Vagrant
- **SECURITY & COMPLIANCE**: Snyk, Dependabot, SECURITY.md, SBOM e políticas de segurança
- **PERFORMANCE & TESTING**: configurações de benchmark, marcadores de profiling e ferramentas de teste de carga

Use essas seções na Fase 2 para orientar as perguntas da investigação e identificar padrões específicos das ferramentas.

### Recursos incluídos

| Recurso | Quando carregar |
|---------|-----------------|
| [`scripts/scan.py`](scripts/scan.py) | Fase 1: execute antes de ler o código, requer Python 3.8+ |
| [`references/inquiry-checkpoints.md`](references/inquiry-checkpoints.md) | Fase 2: perguntas de investigação por template |
| [`references/stack-detection.md`](references/stack-detection.md) | Fase 2: somente quando a stack for ambígua |
| [`assets/templates/STACK.md`](assets/templates/STACK.md) | Fase 3, etapa 1 |
| [`assets/templates/STRUCTURE.md`](assets/templates/STRUCTURE.md) | Fase 3, etapa 2 |
| [`assets/templates/ARCHITECTURE.md`](assets/templates/ARCHITECTURE.md) | Fase 3, etapa 3 |
| [`assets/templates/CONVENTIONS.md`](assets/templates/CONVENTIONS.md) | Fase 3, etapa 4 |
| [`assets/templates/INTEGRATIONS.md`](assets/templates/INTEGRATIONS.md) | Fase 3, etapa 5 |
| [`assets/templates/TESTING.md`](assets/templates/TESTING.md) | Fase 3, etapa 6 |
| [`assets/templates/CONCERNS.md`](assets/templates/CONCERNS.md) | Fase 3, etapa 7 |

Modo de uso dos templates:

- Modo padrão: preencha somente as "Seções principais (obrigatórias)" de cada template.
- Modo estendido: adicione seções opcionais somente quando a complexidade do repositório justificar.

## Modelo de saída

Cada um dos sete arquivos em `docs/codebase/` apresenta primeiro as afirmações e depois as evidências. Exemplo em `STACK.md`:

```markdown
## Stack

| Camada | Tecnologia | Versão | Evidência |
|---|---|---|---|
| Linguagem | Java | 21 | backend/pom.xml |
| Framework | Spring Boot | 3.3.x | backend/pom.xml |
| Banco de dados | PostgreSQL | 16 | compose.yml, application.yml |

### Informações desconhecidas
- [TODO] Nenhuma camada de cache foi encontrada nos manifestos
- [ASK USER] Redis está planejado ou o cache deve permanecer em memória?

### Evidências
- backend/pom.xml
- compose.yml
```

## Gate de qualidade

- [ ] Existem exatamente sete arquivos em `docs/codebase/`, cada um com suas seções obrigatórias.
- [ ] Cada afirmação não trivial aponta para um arquivo, uma configuração ou uma saída do terminal.
- [ ] Informações desconhecidas usam `[TODO]`; decisões dependentes de intenção usam `[ASK USER]`.
- [ ] Cada documento contém uma lista concreta de evidências com paths reais.
- [ ] Saídas geradas, como `dist/`, `build/` e `.next/`, não sustentam afirmações sobre convenções.
- [ ] A resposta final apresenta perguntas `[ASK USER]` numeradas e cada divergência entre intenção e realidade.
