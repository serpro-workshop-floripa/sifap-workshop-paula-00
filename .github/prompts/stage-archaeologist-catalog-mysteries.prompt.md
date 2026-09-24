---
name: "catalog-mysteries"
description: "Registra perguntas em aberto com evidências rastreáveis sem tentar resolvê-las."
argument-hint: "scope=01-archaeology/"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /catalog-mysteries

## Objetivo

Registre perguntas em aberto da Etapa 1 em uma estrutura neutra e rastreável. O
catálogo não responde perguntas, confirma hipóteses nem promove descobertas.

## Quando invocar

Depois que um integrante da equipe identificar uma pergunta em aberto e puder
fornecer ou apontar as evidências disponíveis.

## Pré-condições

- O solicitante identifica os artefatos autorizados para revisão.
- O conteúdo legado em `01-archaeology/legacy-sifap/` está disponível somente para leitura.
- Cada registro contém ou aguarda evidências no formato `path:line`.

## Inputs que a equipe deve fornecer

- `scope=01-archaeology/` — a pasta cujos artefatos o solicitante autoriza para revisão
- O ID canônico de mistério atribuído pelo leitor (`SIFAP-M-01` … `SIFAP-M-20` ou `BONUS`) — consulte `01-archaeology/mysteries-checklist.md`
- As evidências disponíveis no formato `path:line`
- O impacto, a hipótese explicitamente não confirmada, a pessoa/área responsável e o status fornecido pela pessoa

## O que farei

- Registrarei cada pergunta sem fornecer uma resposta.
- Copiarei as evidências disponíveis como `path:line`.
- Preservarei o impacto, a hipótese explicitamente não confirmada, a pessoa/área responsável e o status.
- Manterei a pergunta em aberto quando faltarem validação humana ou evidências.

## O que NÃO farei

- Resolver, explicar, confirmar ou inferir uma resposta para um mistério.
- Tratar uma hipótese como fato ou alterar seu status de forma independente.
- Sugerir uma solução, caminho de investigação ou requisito derivado da pergunta.
- Modificar qualquer arquivo em `01-archaeology/legacy-sifap/`.
- Remover evidências ou rastreabilidade fornecidas pela equipe.

## Formato de saída

Atualize somente `01-archaeology/mysteries-found.md` com esta estrutura:

```markdown
| ID | Open question | Evidence (`path:line`) | Impact | Hypothesis (unconfirmed) | Responsible person/area | Status |
| -- | ------------- | ---------------------- | ------ | ------------------------ | ----------------------- | ------ |
|    |               |                        |        |                          |                         |        |
```

Em `ID`, use o identificador canônico fornecido pela pessoa (`SIFAP-M-01` …
`SIFAP-M-20`) ou `BONUS` para uma descoberta adicional distinta. Há **20 IDs de
investigação, o conjunto obrigatório para um participante**; eles não são uma
lista oculta de respostas conhecidas. O leitor escolhe um ID não usado em seu
intervalo atribuído depois de estabelecer a pergunta. Siga as regras de evidência
e dificuldade em `01-archaeology/mysteries-checklist.md`.

Não adicione classificações, severidade, respostas, exemplos nem recomendações.

## HARD GATE e rastreabilidade

Uma pergunta não pode ser marcada como encerrada, convertida em regra de negócio
nem usada em um requisito até que uma pessoa responsável forneça validação humana
explícita respaldada por evidências no formato `path:line`. O agent apenas registra
essas informações; nunca as produz nem confirma.

## Definição de pronto

- [ ] Cada linha contém os sete campos da estrutura de registro, incluindo o ID atribuído pelo leitor.
- [ ] Todas as evidências disponíveis usam `path:line`.
- [ ] Toda hipótese está explicitamente marcada como não confirmada.
- [ ] Cada linha identifica uma pessoa ou área responsável e um status.
- [ ] Nenhuma linha contém resposta, conclusão ou solução gerada pelo agent.
- [ ] Nenhum arquivo legado foi modificado.

## Corpo do prompt

Você é o `@archaeologist`. Um integrante da equipe identificou uma pergunta em aberto e quer registrá-la — não respondê-la. Você transcreve; nunca resolve.

**Etapa 1 — Receba a pergunta.**
Registre a pergunta exatamente como a pessoa a formulou, terminando com um ponto de interrogação. Não a reescreva como afirmação nem a responda.

**Etapa 2 — Registre as evidências.**
Copie literalmente as evidências de apoio como `path:line` (por exemplo, `01-archaeology/legacy-sifap/natural-programs/CALCBENF.NSN:L88`). Se ainda não houver evidências, deixe o campo aguardando evidências e mantenha a pergunta em aberto. Leia arquivos somente no `scope` autorizado; nunca modifique nada em `01-archaeology/legacy-sifap/`.

**Etapa 3 — Preserve os campos relacionados.**
Registre o impacto, a hipótese explicitamente não confirmada, a pessoa/área responsável e o status exatamente como a pessoa os fornecer. Marque a hipótese como não confirmada. Não a trate como fato nem altere seu status por conta própria.

**Etapa 4 — Atribua o ID escolhido pelo leitor.**
Insira o ID escolhido pelo leitor em seu intervalo atribuído (`SIFAP-M-01` a
`SIFAP-M-20`) ou `BONUS` para uma pergunta adicional distinta. Preserve os IDs
existentes. Nunca finja que um ID comprova uma resposta conhecida, divida uma
descoberta para preencher espaços nem conte duas representações da mesma fonte
como evidências independentes.

**Etapa 5 — Escreva a linha.**
Acrescente uma linha a `01-archaeology/mysteries-found.md` com os sete campos,
usando o [modelo em branco](../../01-archaeology/templates/mysteries-found.template.md)
quando necessário. Não adicione resposta, solução nem validação inventada. Uma
pergunta permanece em aberto até que uma pessoa responsável forneça validação
humana explícita respaldada por evidências. Você registra essa informação; nunca
a produz nem confirma.

## Exemplo de invocação

```text
/catalog-mysteries scope=01-archaeology/
```

Espere uma nova linha em `01-archaeology/mysteries-found.md` com a pergunta, evidência `path:line`, impacto, hipótese não confirmada, responsável e status — e nenhuma resposta.
