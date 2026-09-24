# Índice de prompts

Este diretório contém os arquivos de prompt do GitHub Copilot para o workshop.

> [!IMPORTANT]
> Mantenha os arquivos `*.prompt.md` diretamente em `.github/prompts/`. O local de workspace documentado pelo Copilot é plano (`.github/prompts/*.prompt.md`). A organização por etapa/persona é representada pelo prefixo do nome do arquivo e por este índice.

## Convenção de nomes

| Prefixo | Uso |
| --- | --- |
| `stage-<agent>-<task>.prompt.md` | Prompts para agents de etapa (`archaeologist`, `architect`, `builder`; os prompts de `evolution` são preservados, mas não usados no desafio individual). |
| `persona-<persona>-<task>.prompt.md` | Prompts para papéis da equipe (`product-owner`, `developer`, `qa-engineer` etc.). Cada um se vincula ao agent de etapa responsável por seu momento e começa carregando a skill do papel. |

## Prompts de etapa

| Agent | Arquivos |
| --- | --- |
| `archaeologist` | `stage-archaeologist-*.prompt.md` |
| `architect` | `stage-architect-*.prompt.md` |
| `builder` | `stage-builder-*.prompt.md` |
| `evolution` | `stage-evolution-*.prompt.md` (não usados no desafio individual) |

## Prompts de persona

### Rota de descoberta e migração de dados

| Fase | Prompt / agent | Resultado |
|---|---|---|
| Leitura orientada da Etapa 1 | [/map-source-data](stage-archaeologist-map-source-data.prompt.md) com `@archaeologist` + DBA | Mapa da fonte, dicionário e registro real de leitura gerados pela equipe |
| Incertezas da Etapa 1 | [/catalog-mysteries](stage-archaeologist-catalog-mysteries.prompt.md) | IDs atribuídos pelo leitor e perguntas sem resposta; nenhuma solução |
| Síntese do C1 | [/discovery-report](stage-archaeologist-discovery-report.prompt.md) | Relatório baseado em evidências com o estado real da revisão |

Siga o [ciclo de vida dos dados](../../docs/DATA-MIGRATION.md). Os modelos
permanecem em branco; os prompts preenchem artefatos da equipe somente com
evidências reais dos participantes.

### Grupos de arquivos por persona

| Persona | Arquivos |
| --- | --- |
| Responsável pelo Produto | `persona-product-owner-*.prompt.md` |
| Engenheiro de Requisitos | `persona-requirements-engineer-*.prompt.md` |
| Arquiteto Corporativo | `persona-enterprise-architect-*.prompt.md` |
| Arquiteto de Software | `persona-software-architect-*.prompt.md` |
| Líder Técnico | `persona-technical-lead-*.prompt.md` |
| Desenvolvedor | `persona-developer-*.prompt.md` |
| DBA | `persona-dba-*.prompt.md` |
| Engenheiro de QA | `persona-qa-engineer-*.prompt.md` |
| Engenheiro de DevOps | `persona-devops-engineer-*.prompt.md` |
| Redator Técnico | `persona-tech-writer-*.prompt.md` |

## Regras de manutenção

- Todo prompt deve ter frontmatter YAML válido.
- Prefira campos explícitos `description`, `name`, `argument-hint` (quando houver inputs), `agent` e `tools`.
- Evite ferramentas em excesso; use o menor conjunto necessário para a tarefa.
- As ferramentas definidas no prompt substituem, em vez de ampliar, as ferramentas do agent personalizado; declare todas as permissões necessárias no próprio prompt.
- Prefira aliases portáveis do VS Code (`read`, `search`, `edit`, `execute`, `agent`, `web`, `todo`) a IDs específicos da implementação.
- Não especifique capacidade nem provider no prompt. O usuário decide como executar a tarefa.
- Ao usar um agent personalizado, referencie seu `name` em `.github/agents/` (por exemplo, `archaeologist`, não o nome de exibição no corpo do arquivo).
- Ao adicionar um novo prompt, use um dos prefixos acima para preservar a descoberta e a organização.
