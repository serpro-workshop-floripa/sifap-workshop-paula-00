# Antipadrões de SDD e EARS

Use este catálogo durante correções e validações. Corrija o defeito subjacente no requisito, na evidência ou na rastreabilidade, em vez de apenas aprimorar a prosa.

## Defeitos em requisitos

| Antipadrão | Por que falha | Ação corretiva |
| --- | --- | --- |
| História de usuário tratada como requisito | A intenção não é uma resposta normativa do sistema. | Preserve a história como contexto e derive um ou mais requisitos EARS. |
| `should`, `may`, `will` ou `must` vago | A obrigação ou o momento é ambíguo. | Use o padrão EARS apropriado com `shall`. |
| Resposta composta unida por `and` | Uma mudança ou teste pode passar enquanto o outro falha. | Divida em requisitos atômicos com IDs separados. |
| Sujeito pronominal como "it" | O limite do sistema responsável não está claro. | Nomeie o sistema ou componente. |
| Gatilho ou estado oculto | Revisores precisam inferir quando o comportamento se aplica. | Adicione cláusulas `when`, `while`, `where` ou `if...then`. |
| Tecnologia em requisito funcional | Comportamento e implementação ficam acoplados. | Mova uma escolha obrigatória com fonte para as restrições do NFRD; caso contrário, adie para o design. |
| Formulação vaga de qualidade | Termos como "rápido", "seguro" e "disponível" não podem ser verificados. | Adicione um envelope de medição sustentado por evidências ou um bloqueio. |
| Meta numérica inventada | O documento cria uma política operacional ou de negócio sem sustentação. | Cite a carga de trabalho medida ou a aprovação do responsável. |
| Comportamento indesejado ausente | O caminho feliz oculta obrigações de erro, timeout e recuperação. | Adicione requisitos EARS unwanted ou complex. |
| IDs instáveis ou duplicados | A rastreabilidade e o histórico de mudanças se rompem. | Preserve IDs e registre disposições de divisão, mesclagem, substituição ou retirada. |

## Defeitos em artefatos e no fluxo de trabalho

| Antipadrão | Por que falha | Ação corretiva |
| --- | --- | --- |
| Status `Approved` preenchido previamente | O artefato alega uma revisão que não ocorreu. | Comece como `Draft` ou `Ready for review`; vincule a evidência de aprovação depois. |
| Design primeiro sem requisitos recuperados | Escolhas arquiteturais tornam-se a fonte de verdade não revisada. | Derive e revise os requisitos antes do checkpoint C2. |
| Constituição local da funcionalidade em conflito com a governança do repositório | Duas autoridades podem impor regras incompatíveis. | Reutilize a constituição do repositório ou registre uma emenda explícita. |
| Texto completo do requisito copiado em cada artefato | As cópias divergem e criam várias fontes normativas. | Mantenha uma declaração canônica e vincule-a por ID estável. |
| Requisito sem design, tarefa ou verificação | A especificação não consegue orientar a implementação nem as evidências. | Adicione mapeamentos ou remova o item do escopo ativo. |
| Tarefa sem requisito | Trabalho entra no escopo sem uma necessidade aprovada. | Rastreie-o até um requisito ou classifique-o como governança ou habilitação com evidências. |
| `[P]` baseado apenas no texto da tarefa | O trabalho paralelo ainda pode conflitar em dependências ou arquivos. | Verifique a independência das dependências e da superfície de mudança. |
| Diagrama Mermaid com limites sem rótulos | Revisores não conseguem avaliar propriedade ou confiança. | Rotule atores, componentes, armazenamentos de dados, sistemas externos e limites de confiança. |
| NFR repetido entre contextos sem envelope de medição | Uma meta pode significar coisas diferentes em cada ambiente. | Defina carga de trabalho, ambiente, agregação, janela e instrumentação. |
| Status forte sem evidências | "Implemented" ou "Verified" vira uma ficção com aparência de sucesso. | Vincule evidências do repositório ou de execução e mantenha um status mais fraco caso contrário. |
| Regra arbitrária de quantidade de P0 | Limites mecânicos ocultam risco de entrega ou forçam classificação incorreta. | Justifique cada P0 e divida o incremento quando o conjunto não puder ser revisado. |
| Link relativo de recurso quebrado | A skill não consegue carregar a própria orientação após a instalação. | Use um path relativo ao pacote atual da skill e valide sua existência. |

## Perguntas de revisão

1. Existe exatamente uma declaração normativa canônica por ID de requisito ativo?
2. Um revisor consegue encontrar a fonte primária e o responsável por cada requisito?
3. Um testador consegue derivar uma verificação de aprovação ou reprovação sem inventar comportamento ausente?
4. Todo artefato posterior preserva o escopo e o significado?
5. Os bloqueios estão visíveis onde, de outro modo, surgiriam premissas sem sustentação?
