---
name: "code-modernization"
description: "Use ao modernizar um sistema legado com um fluxo disciplinado que preserve o comportamento. Acione para pedidos sobre modernização, código legado, COBOL, extração de regras de negócio, avaliação antes de reescrita e transformação com equivalência comportamental."
---
# Modernização de código

Use esta skill para orientar a modernização de sistemas legados com preservação de comportamento. O fluxo é dividido em etapas para que a equipe compreenda o sistema antes de transformá-lo.

## Quando invocar

- "Planeje a modernização deste módulo legado."
- "Avalie esta base de código antes de reescrever qualquer parte."
- "Extraia as regras de negócio ocultas neste programa."
- "Transforme este módulo preservando seu comportamento."

## Procedimento

1. **Brief**: defina o que será modernizado, o motivo, as restrições, os itens fora do escopo e os critérios de sucesso.
2. **Assess**: inventarie linguagens, módulos, integrações, build, cobertura de testes, complexidade e riscos.
3. **Extract rules**: transforme a lógica procedural oculta em cartões de regras de negócio com evidências da fonte.
4. **Map**: relacione módulos legados a domínios, pacotes, serviços e sequência de migração no destino.
5. **Reimagine**: projete API, modelo de dados, runtime e modelo operacional de destino.
6. **Transform**: reescreva um módulo por vez em `backend/` e `frontend/`, com testes que fixem o comportamento legado.
7. **Harden**: revise segurança, testes, tratamento de erros, observabilidade e preparo para implantação.

### Primitivos do GitHub Copilot

| Necessidade | Primitivo |
|-------------|-----------|
| Descoberta profunda do legado | Agent [`@archaeologist`](../../agents/archaeologist.agent.md), Etapa 1 |
| Extração de regras de negócio | Prompt [`/extract-business-rules`](../../prompts/stage-archaeologist-extract-business-rules.prompt.md) |
| Design de destino e ADRs | Agent [`@architect`](../../agents/architect.agent.md), Etapa 2 |
| Tradução de módulos e testes | Agent [`@builder`](../../agents/builder.agent.md), Etapa 3 |
| Reforço de segurança e entrega | Agent [`@evolution`](../../agents/evolution.agent.md), mantido para trabalho após o desafio e não usado no desafio individual |
| Leitura segura do código legado | Instructions [`natural-adabas`](../../instructions/natural-adabas.instructions.md) |

### Contrato de pastas

- `01-archaeology/legacy-sifap/**`: evidência da fonte legada e do comportamento. Somente leitura.
- `01-archaeology/**` e `.spec/<NNN>-<feature>/`: briefs, avaliações, mapas, catálogos de regras, especificações EARS e relatórios.
- `backend/**` e `frontend/**`: implementação transformada ou substituta e seus testes.

### Regras

- Não transforme código antes da avaliação e da extração das regras de negócio.
- Cite os arquivos-fonte de cada descoberta. Quando não houver números de linha, cite o arquivo e explique o motivo.
- Diferencie comportamento observado de intenção inferida.
- Prefira vários artefatos focados a um relatório extenso.
- Use testes de caracterização para preservar o comportamento legado antes de alterações intencionais.
- Não invente métricas de complexidade, custo, runtime ou risco. Use valores medidos ou identifique as suposições.

### Validação

- Execute ferramentas de inventário disponíveis, como `scc`, `cloc` ou analisadores da linguagem.
- Execute as suítes de testes disponíveis antes e depois da transformação.
- Nos módulos transformados, forneça evidências de testes que comparem ou fixem o comportamento legado.
- Na etapa de reforço, informe descobertas por severidade e inclua correções concretas.

## Modelo de saída

Registre cada módulo modernizado como uma nota de avaliação em `01-archaeology/`, vinculada ao destino em `backend/` ou `frontend/`:

```markdown
## Registro de modernização: <módulo legado>

| Campo | Valor |
|---|---|
| Fonte legada | 01-archaeology/legacy-sifap/natural-programs/<FILE>.NSN |
| Módulo de destino | backend/src/main/java/<package>/ |
| Etapa alcançada | Brief / Assess / Extract / Map / Reimagine / Transform / Harden |
| Evidência de comportamento | <path do teste de caracterização> |
| Rastreia | REQ-NNN |

### Comportamento observado
- <fato obtido no código legado, com evidência path:line>

### Perguntas em aberto
- <dúvida que exige validação humana>
```

## Gate de qualidade

- [ ] A avaliação e a extração das regras de negócio ocorreram antes de qualquer transformação.
- [ ] Cada descoberta cita um arquivo-fonte legado e, quando disponíveis, números de linha.
- [ ] O comportamento observado está separado da intenção inferida.
- [ ] Testes de caracterização fixam o comportamento legado antes de alterações intencionais.
- [ ] Nenhuma métrica de complexidade, custo, runtime ou risco foi inventada. Os valores foram medidos ou marcados como suposições.
