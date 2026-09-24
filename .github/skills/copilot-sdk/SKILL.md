---
name: "copilot-sdk"
description: "Use ao criar aplicações agênticas com o GitHub Copilot SDK: incorporar agents, criar ferramentas personalizadas, transmitir respostas, gerenciar sessões, conectar servidores MCP ou criar agents personalizados. Antes de gerar código, verifique a versão instalada do SDK, a configuração de modelo controlada pela pessoa usuária, as permissões limitadas e a limpeza de recursos."
---
# GitHub Copilot SDK

Use o SDK oficial para incorporar fluxos do Copilot em uma aplicação ou extensão de ferramenta solicitada explicitamente. O SDK não é necessário para usar os agents de etapa do workshop no VS Code e não fornece uma implementação pronta do SIFAP.

## Quando invocar

- "Incorpore um agent do Copilot à nossa aplicação com o SDK."
- "Adicione uma ferramenta personalizada com uma política de permissões limitada."
- "Transmita a resposta de um agent na aplicação."
- "Conecte um servidor MCP aprovado e persista sessões com segurança."

## Procedimento

### Escopo e pré-requisitos

- Inspecione a aplicação, a linguagem, as versões instaladas do SDK e da CLI e os testes existentes antes de propor código. Não suponha que uma aplicação exista.
- O SDK usa a Copilot CLI. Confirme disponibilidade e autenticação. Nunca copie credenciais para código, prompts ou logs.
- Verifique compatibilidade de runtime e pacotes na versão escolhida do SDK. Não trate o requisito de runtime de um tutorial antigo como evidência atual.
- Siga a stack aprovada do kit nos trabalhos do SIFAP. Uma extensão separada exige escopo e decisão de dependência próprios.
- Mantenha `01-archaeology/legacy-sifap/**` somente para leitura. Não anexe código-fonte bruto, registros de produção, secrets nem arquivos não relacionados à sessão.

### Implementação baseada na versão

Use os tipos instalados e a documentação oficial da release como contrato da API. Assinaturas de métodos, formatos de eventos, transporte, callbacks de permissão e persistência de sessão podem mudar. Não copie trechos de outra linguagem ou versão e afirme que compilam.

| Área | O que verificar antes da implementação |
|------|-----------------------------------------|
| Cliente | Ciclo de vida da CLI, transporte, contexto de autenticação e responsabilidade |
| Sessão | ID do modelo controlado pela pessoa, instruções do sistema, ferramentas permitidas e cancelamento |
| Streaming | Nomes reais dos eventos, tratamento de final/idle/erro e remoção de listeners |
| Ferramentas personalizadas | Schema tipado, validação de entrada, autorização e falhas explícitas |
| MCP | Identidade aprovada do servidor, transporte, ferramentas permitidas e conectividade |
| Agents personalizados | Schema real de configuração e limites de permissão herdados |
| Persistência | IDs de sessão autorizados, isolamento por tenant/usuário, retenção e exclusão |
| Encerramento | Limpeza após sucesso, falha, cancelamento e erro na criação da sessão |

### Limites de permissões e dados

Nunca use `approveAll` irrestrito como política padrão da aplicação.

1. Defina as operações e os paths acessíveis pela tarefa.
2. Valide cada request conforme esse limite e a pessoa autenticada responsável.
3. Negue requests fora do limite e exija aprovação humana quando a política determinar. Uma justificativa gerada pelo modelo não é autorização.
4. Preserve negações, falhas e cancelamentos como resultados distintos.
5. Registre metadados de auditoria higienizados, não secrets nem conteúdo bruto de requests ou arquivos.

As ferramentas personalizadas também aplicam autorização internamente. Um callback de permissão não substitui a validação de argumentos, consultas ao banco ou acessos a serviços externos.

Anexos exigem aprovação explícita e classificação dos dados. Use somente material sintético ou higienizado autorizado. Um nome genérico, como o de um CSV, não autoriza leitura ou transmissão.

### Modelos e configuração

Obtenha identificador de modelo, endpoints, configuração MCP e opções de runtime da configuração controlada pela pessoa. Verifique disponibilidade na conta e política reais. Não grave um provider ou modelo diretamente nem faça fallback silencioso. Configuração ausente ou inválida é um erro explícito de setup.

Mantenha secrets no servidor e fora de configurações públicas do frontend. Não registre requests e respostas completas do modelo quando puderem conter dados sensíveis.

### Ciclo de vida do cliente e da sessão

1. Valide a configuração antes de iniciar o cliente.
2. Prepare a limpeza em torno da inicialização do cliente e da criação da sessão.
3. Crie a sessão com a política de permissão revisada e as ferramentas selecionadas.
4. Registre somente os listeners necessários.
5. Envie a request com política explícita de timeout e cancelamento.
6. Trate resposta final, erros, negações, cancelamento e ausência de resposta de forma distinta.
7. Remova listeners e encerre ou descarte sessões e clientes em todos os caminhos, inclusive falha de inicialização ou criação de sessão.

Use `try/finally`, `defer` ou o mecanismo real de descarte da linguagem. Não invente uma API nem suponha que o encerramento do processo limpe tarefas em segundo plano.

### Ferramentas, streaming e trabalho em vários turnos

- Crie schemas de ferramentas a partir do limite real da tarefa, não de formatos inventados pelo modelo. Retorne resultados tipados e falhas explícitas.
- Mantenha deltas de streaming separados da resposta final. Um sinal `idle` não comprova sucesso.
- Reutilize sessões somente dentro do limite autorizado de pessoa e tarefa. Retomar uma sessão não pode cruzar usuários ou tenants.
- Teste cancelamentos, timeouts, permissões negadas e falhas de ferramentas, além do caminho feliz.
- Em conexões MCP, teste o subconjunto permitido de ferramentas. Não exponha todas as ferramentas nem suponha que uma integração existe porque foi nomeada.

## Modelo de saída

Gere a implementação solicitada e seus testes. Depois, informe:

```markdown
## Integração com Copilot SDK: <tarefa aprovada>
| Ponto de atenção | Configuração real ou evidência |
|---|---|
| Linguagem / SDK / CLI / runtime | <versões verificadas> |
| Configuração do modelo | <identificador selecionado e disponibilidade> |
| Limite de permissão | <operações/paths aprovados e comportamento de negação> |
| Ferramentas / MCP | <schemas, autorização e endpoints configurados, sem secrets> |
| Anexos / persistência | <dados aprovados, isolamento e retenção> |
| Streaming / erros / cancelamento | <comportamento implementado e testes> |
| Limpeza | <limpeza verificada em sucesso/falha/inicialização> |
| Verificação | <comandos e resultados reais, ou não executado> |
```

Não preencha saídas do modelo, testes bem-sucedidos, concessões de permissão ou resultados do runtime. Um esboço de código não é uma integração verificada.

## Gate de qualidade

- [ ] O contrato do SDK, CLI e runtime selecionados foi inspecionado antes da geração do código.
- [ ] Modelos e endpoints permanecem configuráveis pela pessoa; não existe aprovação irrestrita de permissões.
- [ ] Acesso a ferramentas e anexos é autorizado, validado e limitado explicitamente.
- [ ] Erros, respostas ausentes, negações e cancelamentos não são ocultados.
- [ ] Isolamento de sessão, remoção de listeners e descarte do cliente funcionam em caminhos de falha.
- [ ] Os testes cobrem comportamento e limites solicitados com a toolchain existente.
- [ ] Evidência end-to-end real foi registrada antes de declarar a integração concluída.

### Referências

- [Repositório e releases oficiais do SDK](https://github.com/github/copilot-sdk)
- [Tutorial da primeira aplicação](https://github.com/github/copilot-sdk/blob/main/docs/tutorials/first-app.md)
- [Exemplos oficiais](https://github.com/github/copilot-sdk/tree/main/samples)
- [Servidor GitHub MCP](https://github.com/github/github-mcp-server)
- [Padrão de primitivos do kit](../../PRIMITIVE-STANDARD.md)
