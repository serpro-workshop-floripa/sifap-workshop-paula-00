---
description: "Use ao criar, editar ou revisar diagramas draw.io e XML mxGraph em arquivos .drawio, .drawio.svg ou .drawio.png."
applyTo: "**/*.drawio,**/*.drawio.svg,**/*.drawio.png"
---

# Diagramas draw.io — Convenções e restrições

Este arquivo define estrutura, estilo e nomenclatura para `.drawio`, `.drawio.svg` e `.drawio.png`. Os arquivos devem abrir corretamente no VS Code com `hediet.vscode-drawio`. O procedimento de criação, receitas XML e validação pertencem à skill `draw-io-diagram-generator`.

## Invariantes estruturais

- `id="0"` e `id="1"` são as duas primeiras cells de cada `<diagram>`, nessa ordem, e nunca representam conteúdo.
- Cada `id` é exclusivo na página.
- Cada vertex tem `<mxGeometry ... as="geometry">` com `x`, `y`, `width` e `height`.
- Cada edge aponta `source` e `target` para vertices existentes ou usa `sourcePoint` e `targetPoint`.
- Toda cell, exceto `id="0"`, tem `parent` válido.
- Filhos de containers usam coordenadas relativas ao parent.

```xml
<root>
  <mxCell id="0" />
  <mxCell id="1" parent="0" />
</root>
```

> [!WARNING]
> Um arquivo em branco no VS Code geralmente não tem as root cells `id="0"`/`id="1"` ou contém edge com `source`/`target` inválido. Verifique primeiro essas invariantes.

## Paleta semântica

| Papel | fillColor | strokeColor |
|---|---|---|
| Primário/informação | `#dae8fc` | `#6c8ebf` |
| Sucesso/início/positivo | `#d5e8d4` | `#82b366` |
| Alerta/decisão | `#fff2cc` | `#d6b656` |
| Erro/fim/perigo | `#f8cecc` | `#b85450` |
| Neutro/interface | `#f5f5f5` | `#666666` |
| Externo/parceiro | `#e1d5e7` | `#9673a6` |

## Arquivo, nome e layout

| Tema | Convenção |
|---|---|
| Extensão | `.drawio` para versionamento; `.drawio.svg` para inclusão em Markdown |
| Nome | `kebab-case`, como `payment-flow.drawio` |
| Local | Ao lado do código documentado, em `docs/` ou `architecture/` |
| Grid | Coordenadas alinhadas ao grid de 10 px |
| Espaçamento | 40–60 px na mesma linha; 80–120 px entre camadas |
| Página | A4 paisagem `1169 × 827` px |
| Densidade | Máximo de 40 cells por página |
| Título | Uma cell de título no topo de cada página |

## Validação

Execute o checker `validate-drawio.py` documentado na skill e abra o arquivo no VS Code antes do commit.

## Convenções

| Regra | Motivo |
|---|---|
| `id="0"` e `id="1"` primeiro | São as roots reservadas pelo draw.io |
| Vertex usa `whiteSpace=wrap;html=1` | Mantém labels legíveis |
| Connectors usam `edgeStyle=orthogonalEdgeStyle` | Mantém rotas claras |
| Use a paleta semântica | Preserva significado das cores |
| Arquivos em `kebab-case` ao lado do código | Facilita descoberta e diff |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Coloque as root cells antes do conteúdo | Reutilize `0` ou `1` |
| Aponte edges para vertices existentes | Deixe `source` ou `target` pendente |
| Reutilize a paleta semântica | Invente cores ad hoc |
| Vincule a skill para o procedimento | Duplique as receitas da skill |
| Divida diagramas grandes em páginas | Coloque mais de 40 cells por página |

## Checklist antes de abrir um PR

- [ ] As root cells são as duas primeiras cells de cada página.
- [ ] IDs são exclusivos e cada `parent` resolve.
- [ ] Cada edge resolve seus endpoints ou usa points flutuantes.
- [ ] Cada vertex tem geometry e filhos usam coordenadas relativas.
- [ ] Paleta e estilo de vertex são consistentes.
- [ ] O arquivo usa `kebab-case`, tem título e fica em `docs/` ou `architecture/`.
- [ ] O checker passa e o arquivo renderiza no VS Code.
