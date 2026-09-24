# Template: Mapa de dados de origem

> **Caminho:** [Kit da Equipe](../../README.md) > [Etapa 1](../README.md) > **Templates** > **Mapa de dados**

**Registro sob responsabilidade do DBA das definições e da população de dados que a equipe realmente investiga na Etapa 1.**

> [!NOTE]
> Use `/map-source-data` com `@archaeologist` e o DBA após a leitura orientada da origem.
> Registre os achados em `01-archaeology/data-map.md`, não neste template.
> Nenhum mapeamento de campo, contagem, interpretação ou aprovação é fornecido aqui.

| Campo | Evidência da equipe |
|---|---|
| Participante / evidência de revisão DBA-QA / data | <!-- preencher --> |
| Versão da origem e escopo de leitura autorizado | <!-- preencher --> |
| Cobertura de DDM/FDT e definições ausentes | <!-- preencher --> |
| Referência de evidência da população | <!-- preencher: origem medida ou BLOQUEADO; não uma estimativa da seed --> |
| Status | <!-- preencher: rascunho / aguardando evidências / pronto para revisão --> |

## Arquivos e identificadores de origem

| DDM / FDT | Vínculo de arquivo observado | Chaves / descritores declarados | Evidência de acesso pelo código | Questão em aberto |
|---|---|---|---|---|
| <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher: caminho:linha real --> | <!-- preencher --> |

## Evidências no nível de campo

Duplique linhas para os campos realmente examinados. Mantenha separados o formato lógico,
o armazenamento físico e as declarações dos programas. Não infira precisão SQL a partir
de um tamanho packed ambíguo nem trate a supressão de nulos como regra de valor obrigatório.

| Campo de origem / nome lógico | Formato / tamanho / escala declarados | Marcadores de armazenamento / descritor | Limites de grupo / ocorrência | Significado observado e evidência | Incerteza |
|---|---|---|---|---|---|
| <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher: caminho:linha da origem --> | <!-- preencher --> |

## Relacionamentos e acesso

| Relacionamento de origem | Evidência de leitura / gravação | Declarado ou observado? | Integridade não estabelecida | Responsável |
|---|---|---|---|---|
| <!-- preencher --> | <!-- preencher: caminho:linha --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## População e qualidade

Use o [template de prontidão da origem](../../docs/data-migration/source-readiness.template.md)
para autorização, contagens medidas, capacidade de snapshot/extração e referências
restritas de evidências. Nunca copie registros de beneficiários para este documento.

| População de origem | Método / horário da medição | Contagem / cobertura | Observação de qualidade | Referência de evidência / bloqueio |
|---|---|---|---|---|
| <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> |

## Questões entre fontes

| Questão | Evidência no código | Evidência DDM/FDT ou histórica | Impacto / responsável | Referência no registro de mistérios |
|---|---|---|---|---|
| <!-- preencher: questão, não resposta --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher --> | <!-- preencher: ID atribuído pelo leitor ou BONUS --> |

## Autoavaliação C1 para Arquitetura

| Evidência ou bloqueio | Efeito no planejamento posterior da migração | Papel responsável | Resultado da autoavaliação |
|---|---|---|---|
| <!-- preencher --> | <!-- preencher: nenhum projeto-alvo aprovado aqui --> | <!-- preencher --> | <!-- preencher somente após a autoavaliação real --> |

## Verificações de conclusão

- [ ] Toda linha preenchida cita evidências de leitura ou medição real.
- [ ] Campos não lidos e definições físicas ausentes permanecem explícitos.
- [ ] Receitas de seed, estatísticas FDT arquivadas e medições atuais da população estão diferenciadas.
- [ ] Ocorrências MU/PE, identificadores, semântica numérica/de datas e lacunas de qualidade de dados estão registrados sem escolher silenciosamente uma solução.
- [ ] As responsabilidades de DBA e QA foram revisadas com base em evidências; nenhum modelo PostgreSQL ou aprovação C1 foi fabricado.

## Referências

- [Guia da Etapa 1](../GUIDE.md)
- [Ciclo de vida da migração de dados](../../docs/DATA-MIGRATION.md)
- [Template de dicionário de declarações](program-data-dictionary.md)
