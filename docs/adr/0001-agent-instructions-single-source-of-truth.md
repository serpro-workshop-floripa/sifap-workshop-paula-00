# ADR-0001: Fonte única de verdade para instruções de agentes (sem AGENTS.md na raiz)

> **Caminho:** [Kit da equipe](../../README.md) › [Documentação](../README.md) › [ADRs](README.md) › **ADR-0001**

| Campo | Valor |
|---|---|
| **Status** | accepted |
| **Data** | 2026-08-17 |
| **Autores** | Auditoria do harness |
| **Substitui** | N/A |

---

## Contexto

O GitHub Copilot lê vários tipos de arquivos de instruções personalizadas. Este repositório já fornece `.github/copilot-instructions.md` (para todo o repositório) e os arquivos `.github/instructions/*.instructions.md` com escopo por caminho. Ele **não** tem um `AGENTS.md` na raiz, e surgiu a dúvida sobre adicioná-lo, pois tanto a convenção aberta [agents.md](https://agents.md/) quanto o Copilot CLI leem `AGENTS.md`.

O risco a considerar é a divergência. Um segundo arquivo de instruções para todo o repositório pode divergir silenciosamente do primeiro. Assim, os agentes recebem orientações contraditórias conforme o arquivo carregado por cada superfície. Este kit aplica a regra da menor orientação útil: atualizar a fonte de verdade existente em vez de adicionar instruções duplicadas para todo o repositório.

Dois fatos fundamentam a decisão.

**1. Cobertura das superfícies: `AGENTS.md` não amplia o alcance neste caso.** Toda superfície do Copilot que lê `AGENTS.md` também lê `.github/copilot-instructions.md`:

| Superfície | Lê `.github/copilot-instructions.md` | Lê `AGENTS.md` |
|---|---|---|
| Copilot CLI (ferramenta opcional de terminal deste repositório) | Sim | Sim |
| VS Code — Copilot Chat | Sim | Sim |
| VS Code — cloud agent / code review | Sim | Sim |
| GitHub.com — cloud agent | Sim | Sim |
| GitHub.com — code review | Sim | Sim |
| GitHub.com — Copilot Chat | Sim | Não |

A saída de `/help` do próprio Copilot CLI lista `AGENTS.md` e `.github/copilot-instructions.md` como locais reconhecidos. O GitHub.com Copilot Chat lê `.github/copilot-instructions.md`, mas **não** `AGENTS.md`. Portanto, o arquivo para todo o repositório é o único respeitado por todas as superfícies.

**2. Precedência: o arquivo para todo o repositório já prevalece sobre `AGENTS.md`.** Quando mais de um arquivo se aplica, todos são fornecidos ao Copilot. Em caso de conflito, a ordem é (da maior para a menor precedência): pessoal → `.github/instructions/**` específico do caminho → **`.github/copilot-instructions.md` para todo o repositório** → **`AGENTS.md` do agente** → organização. Portanto, um novo `AGENTS.md` nunca prevaleceria em uma divergência com o arquivo existente. Ele só poderia divergir desse arquivo. Arquivos `AGENTS.md` aninhados são compatíveis (prevalece o mais próximo na árvore), o que ampliaria a superfície de divergência em vez de reduzi-la.

## Decisão

**Não** adicionaremos `AGENTS.md` à raiz (nem `CLAUDE.md` / `GEMINI.md`). `.github/copilot-instructions.md` permanece como fonte única de verdade para as instruções de agentes em todo o repositório, complementada pelos arquivos `.github/instructions/*.instructions.md` com escopo por caminho. A seção “Regras estritas” de `.github/copilot-instructions.md` proíbe adicionar um arquivo concorrente de instruções à raiz. Assim, a regra é aplicada no ponto em que uma pessoa colaboradora poderia violá-la.

## Alternativas consideradas

| Alternativa | Por que foi rejeitada |
|---|---|
| Adicionar um `AGENTS.md` completo que replique as instruções | Seria uma duplicação integral de um arquivo que todas as superfícies já leem. Duas fontes de verdade para todo o repositório divergiriam, exatamente a regressão que esta auditoria pretende evitar. |
| Adicionar um `AGENTS.md` mínimo que apenas aponte para `.github/copilot-instructions.md` | Adicionaria um arquivo a manter com benefício quase nulo: toda superfície que o lê já lê o destino, e o repositório proíbe assistentes que não sejam o Copilot. Isso elimina o valor entre ferramentas que é o principal atrativo de `AGENTS.md`. O link ainda poderia se tornar inválido. |

## Consequências

- **Mais fácil:** há um único local para editar, sem reconciliação entre dois arquivos para todo o repositório e sem orientações conflitantes entre superfícies.
- **Mais difícil:** uma pessoa colaboradora que espera encontrar `AGENTS.md` precisa aprender a convenção. A regra estrita explícita e esta ADR mitigam essa dificuldade.
- **Riscos:** se o GitHub tornar `AGENTS.md` o único arquivo lido por uma superfície obrigatória, esta decisão precisará ser revisitada.
- **Mitigações:** a regra estrita aponta para esta ADR. A verificação de divergência dos primitivos do Copilot (`.github/scripts/validate-copilot-primitives.py`, acompanhada separadamente) é o local apropriado para garantir que “não exista `AGENTS.md` avulso na raiz”, caso uma aplicação ativa seja necessária no futuro.

## Relacionados

- REQ-IDs: N/A
- ADRs: N/A
- Arquivos de instruções: `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`

## Referências

- GitHub Docs — Sobre a personalização das respostas do GitHub Copilot (precedência das instruções personalizadas): <https://docs.github.com/en/copilot/concepts/response-customization>
- GitHub Docs — Compatibilidade com diferentes tipos de instruções personalizadas (qual superfície lê cada arquivo): <https://docs.github.com/en/copilot/reference/custom-instructions-support>
- GitHub Docs — Adição de instruções personalizadas ao repositório (`AGENTS.md` aninhado, prevalece o mais próximo): <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- Convenção aberta agents.md: <https://agents.md/>

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [ADRs — Índice](README.md)<br/><sub>Índice das decisões registradas.</sub> | [Documentação](../README.md)<br/><sub>Índice dos recursos transversais do kit.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
