# Lições aprendidas — erros comuns do desafio

![Tipo: referência](https://img.shields.io/badge/Type-Reference-171717?style=flat-square)
![Leitura de 5 min](https://img.shields.io/badge/Read-5%20min-737373?style=flat-square)

> **Caminho:** [Kit da equipe](../README.md) › [Documentação](README.md) › **Lições aprendidas**

**Dez padrões de falha aos quais prestar atenção**, com consequências plausíveis e ações preventivas. São riscos de aprendizagem, não resultados medidos de frequência ou tempo.

| Campo | Valor |
|---|---|
| **Público-alvo** | Todo participante, especialmente ao cobrir responsabilidades de Technical Lead |
| **Quando ler** | Antes do início do workshop |
| **Resultado esperado** | Reconhecer padrões de falha e conhecer a solução antes que ela seja necessária |

---

## Os dez erros mais comuns

### 1. “Não precisamos inspecionar o sistema legado — o briefing é suficiente”

- **Consequência:** requisitos podem não ter evidências válidas; a CI rejeita citações ausentes/inválidas, e revisores podem encontrar comportamentos sem respaldo mesmo quando a sintaxe passa.
- **Solução:** aplique o gate obrigatório da Etapa 1 — o facilitador o valida às 13:50. Consulte [`01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md`](../01-archaeology/LEGACY-EXPLORATION-CHECKLIST.md).

### 2. “Vou começar a programar enquanto outra pessoa escreve a especificação”

- **Consequência:** o código não corresponde aos requisitos EARS. A refatoração acontece no fim do dia e a aceitação permanece incompleta.
- **Solução:** a Etapa 3 começa somente depois que a autoverificação C2 confirmar que `spec.md`, `plan.md`, `tasks.md` e o design da migração estão prontos.

### 3. O Product Owner aprova tudo e nada fica fora do escopo

- **Consequência:** o participante tenta implementar 12 funcionalidades no timebox e não conclui nenhuma.
- **Solução:** PO e arquitetos escolhem com DBA/QA uma capacidade enxuta e respaldada por evidências. Adie explicitamente o trabalho não relacionado; não pré-selecione o ciclo de pagamentos nem invente uma cota de rejeições.

### 4. Cada pessoa usa o Copilot de um jeito

- **Consequência:** as respostas ficam inconsistentes. O participante debate com o assistente em vez de produzir artefatos.
- **Solução:** selecione no Chat o agente de etapa do bloco atual (`@archaeologist`, `@architect`, `@builder`, além de `@dba` para trabalho com dados).

### 5. Pular `/speckit.clarify` para economizar tempo

- **Consequência:** ambiguidades não resolvidas podem se tornar erros de implementação; este kit não atribui à clarificação uma economia de tempo medida.
- **Solução:** resolva com evidências as questões que bloqueiam o comportamento selecionado. Mantenha respostas indisponíveis como bloqueadas ou adie o escopo afetado mediante revisão.

### 6. Executar `git push --force` em `develop`

- **Consequência:** o trabalho de duas pessoas é perdido sem um caminho simples de recuperação.
- **Solução:** proteja `develop` (Etapa 4 de `00-SETUP.md`). Nunca use `--force` em uma branch compartilhada.

### 7. Editar uma migração antiga em vez de criar uma nova

- **Consequência:** o Flyway detecta incompatibilidade de checksum e o banco de dados deixa de iniciar.
- **Solução:** nunca edite um arquivo de migração já aplicado. Sempre crie `V<N+1>__description.sql`. Consulte [`docs/troubleshooting.md`](troubleshooting.md).

### 8. Delegar uma Issue vaga ao Copilot Agent

- **Consequência:** o pull request gerado não pode ser usado e o trabalho é descartado.
- **Solução:** vincule a Issue a evidências e critérios de aceitação verificáveis. Uma entrada clara melhora a revisabilidade, mas não garante um PR correto ou pontual.

### 9. Executar `terraform apply` em vez de `plan`

- **Consequência:** recursos do Azure são criados e cobrados imediatamente. O workshop não autoriza `apply`.
- **Solução:** não execute a infraestrutura da Etapa 4 durante o desafio individual. O trabalho de infraestrutura pós-desafio pode usar `terraform plan`; consulte [`04-evolution/GUIDE.md`](../04-evolution/GUIDE.md).

### 10. Tratar a criação do schema ou um seed de teste como migração de dados

- **Consequência:** a aplicação executa, mas não consegue contabilizar nem consultar a população original de beneficiários.
- **Solução:** o DBA lidera a prontidão da fonte e a migração desde o início; o QA reconcilia o snapshot de forma independente e verifica todas as consultas de beneficiários. Use [`DATA-MIGRATION.md`](DATA-MIGRATION.md) e mantenha os bloqueios em vez de inventar um resultado bem-sucedido.

---

## Cinco hábitos que distinguem boas submissões

1. **Checkpoint de autoverificação em cada limite de etapa** — C1, C2 e C3 são verificados antes de avançar.
2. **Todo pull request tem uma descrição** — use o modelo do GitHub e preencha o checklist.
3. **Commits pequenos incluem um REQ-ID** na mensagem de commit.
4. **A regra dos 20 minutos** — está bloqueado? Peça apoio do workshop e registre o bloqueio.
5. **Confie no processo** — não invente um fluxo de trabalho diferente no meio do dia.

---

## A regra fundamental

> **Modernização é arqueologia digital, não um projeto greenfield.**
> Tratar o SIFAP como greenfield arrisca perder comportamentos acumulados ao longo de aproximadamente 30 anos. Preserve as [evidências históricas](../README.md#cenário-cronologia-e-evidências) antes de tomar decisões modernas.
> A arqueologia sustenta um incremento defensável; a substituição em produção ainda exige evidências além deste exercício com tempo limitado.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Checklist do participante](CHECKLIST-LIDER.md)<br/><sub>Verificações ao longo do dia.</sub> | [Migração de dados](DATA-MIGRATION.md)<br/><sub>Migração e aceitação lideradas pelo DBA.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
