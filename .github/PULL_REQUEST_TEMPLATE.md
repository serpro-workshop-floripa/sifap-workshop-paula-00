# Pull request

## Descrição

<!-- Descreva o que foi implementado neste PR. -->

## Etapa

- [ ] Etapa 1 - Evidências de arqueologia
- [ ] Etapa 2 - Especificação moderna
- [ ] Etapa 3 - Implementação e migração de dados
- [ ] PR de submissão: `impl/<NNN>-<feature>` -> `develop`

## Participante responsável

<!-- Seu nome ou identificador do GitHub. No desafio individual, você cobre todas as responsabilidades dos papéis. -->

## REQ-IDs atendidos

<!-- Exemplo: REQ-001, REQ-003 -->

## Checklist de submissão

- [ ] A CI está verde, incluindo `legacy-traceability` e os jobs de teste.
- [ ] Cada requisito tem um REQ-ID, texto EARS e `source_legacy:`.
- [ ] `mvn verify` passa no backend.
- [ ] Os testes de frontend passam, caso um frontend tenha sido criado.
- [ ] A reconciliação comprova: contagem da origem = registros carregados + rejeições explicadas.
- [ ] As chaves de origem e os agregados acordados reconciliam sem perdas inexplicadas.
- [ ] A reexecução da migração termina sem duplicidades.
- [ ] A listagem cobre toda a população migrada de beneficiários, não apenas uma amostra ou a primeira página.
- [ ] A busca cobre toda a população migrada de beneficiários.
- [ ] A visualização de detalhes funciona para beneficiários migrados selecionados da população completa.
- [ ] Nenhum dado sensível aparece em logs, capturas de tela, commits ou no corpo do PR.
- [ ] Alterações de workflow, quando houver, usam permissões de privilégio mínimo e actions fixadas por SHA.

## Como validar

<!-- Liste os comandos exatos e os locais das evidências que o juiz deve usar. -->
