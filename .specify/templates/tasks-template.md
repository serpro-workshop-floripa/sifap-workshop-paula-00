---

description: "Template de lista de tarefas para implementação de funcionalidade"
---

# Tasks: [FEATURE NAME]

**Input**: Documentos de design em `/specs/[###-feature-name]/`

**Prerequisites**: plan.md (obrigatório), spec.md (obrigatório para histórias de usuário), research.md, data-model.md, contracts/

**Tests**: Os exemplos abaixo incluem tarefas de teste. Os testes são OPCIONAIS — inclua-os somente se forem solicitados explicitamente na especificação da funcionalidade.

**Organization**: As tarefas são agrupadas por história de usuário para permitir a implementação e o teste independentes de cada história.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Pode ser executada em paralelo (arquivos diferentes, sem dependências)
- **[Story]**: Indica a qual história de usuário esta tarefa pertence (por exemplo, US1, US2, US3)
- Inclua caminhos exatos de arquivos nas descrições

## Path Conventions

- **Projeto único**: `src/`, `tests/` na raiz do repositório
- **Aplicação web**: `backend/src/`, `frontend/src/`
- **Dispositivo móvel**: `api/src/`, `ios/src/` ou `android/src/`
- Os caminhos mostrados abaixo pressupõem um projeto único — ajuste-os com base na estrutura de plan.md

<!--
  ============================================================================
  IMPORTANTE: As tarefas abaixo são TAREFAS DE EXEMPLO apenas para fins
  ilustrativos.

  O comando /speckit.tasks DEVE substituí-las por tarefas reais baseadas em:
  - Histórias de usuário de spec.md (com suas prioridades P1, P2, P3...)
  - Requisitos da funcionalidade em plan.md
  - Entidades de data-model.md
  - Endpoints de contracts/

  As tarefas DEVEM ser organizadas por história de usuário para que cada
  história possa ser:
  - Implementada de forma independente
  - Testada de forma independente
  - Entregue como um incremento do MVP

  NÃO mantenha estas tarefas de exemplo no arquivo tasks.md gerado.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Inicialização do projeto e estrutura básica

- [ ] T001 Criar a estrutura do projeto conforme o plano de implementação
- [ ] T002 Inicializar o projeto [language] com dependências de [framework]
- [ ] T003 [P] Configurar ferramentas de lint e formatação

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Infraestrutura principal que DEVE estar concluída antes da implementação de QUALQUER história de usuário

**⚠️ CRITICAL**: Nenhum trabalho em histórias de usuário pode começar até que esta fase esteja concluída

Exemplos de tarefas fundamentais (ajuste conforme o seu projeto):

- [ ] T004 Configurar o schema do banco de dados e o framework de migrações
- [ ] T005 [P] Implementar o framework de autenticação/autorização
- [ ] T006 [P] Configurar o roteamento da API e a estrutura de middleware
- [ ] T007 Criar os modelos/entidades base dos quais todas as histórias dependem
- [ ] T008 Configurar a infraestrutura de tratamento de erros e logs
- [ ] T009 Configurar o gerenciamento de configurações de ambiente

**Checkpoint**: Fundação pronta — a implementação das histórias de usuário pode começar em paralelo

---

## Phase 3: User Story 1 - [Title] (Priority: P1) 🎯 MVP

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Escreva estes testes PRIMEIRO e confirme que FALHAM antes da implementação**

- [ ] T010 [P] [US1] Teste de contrato para [endpoint] em tests/contract/test_[name].py
- [ ] T011 [P] [US1] Teste de integração para [user journey] em tests/integration/test_[name].py

### Implementation for User Story 1

- [ ] T012 [P] [US1] Criar o modelo [Entity1] em src/models/[entity1].py
- [ ] T013 [P] [US1] Criar o modelo [Entity2] em src/models/[entity2].py
- [ ] T014 [US1] Implementar [Service] em src/services/[service].py (depende de T012, T013)
- [ ] T015 [US1] Implementar [endpoint/feature] em src/[location]/[file].py
- [ ] T016 [US1] Adicionar validação e tratamento de erros
- [ ] T017 [US1] Adicionar logs para as operações da história de usuário 1

**Checkpoint**: Neste ponto, a História de Usuário 1 deve estar totalmente funcional e ser testável de forma independente

---

## Phase 4: User Story 2 - [Title] (Priority: P2)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Teste de contrato para [endpoint] em tests/contract/test_[name].py
- [ ] T019 [P] [US2] Teste de integração para [user journey] em tests/integration/test_[name].py

### Implementation for User Story 2

- [ ] T020 [P] [US2] Criar o modelo [Entity] em src/models/[entity].py
- [ ] T021 [US2] Implementar [Service] em src/services/[service].py
- [ ] T022 [US2] Implementar [endpoint/feature] em src/[location]/[file].py
- [ ] T023 [US2] Integrar com os componentes da História de Usuário 1 (se necessário)

**Checkpoint**: Neste ponto, as Histórias de Usuário 1 E 2 devem funcionar de forma independente

---

## Phase 5: User Story 3 - [Title] (Priority: P3)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T024 [P] [US3] Teste de contrato para [endpoint] em tests/contract/test_[name].py
- [ ] T025 [P] [US3] Teste de integração para [user journey] em tests/integration/test_[name].py

### Implementation for User Story 3

- [ ] T026 [P] [US3] Criar o modelo [Entity] em src/models/[entity].py
- [ ] T027 [US3] Implementar [Service] em src/services/[service].py
- [ ] T028 [US3] Implementar [endpoint/feature] em src/[location]/[file].py

**Checkpoint**: Agora, todas as histórias de usuário devem funcionar de forma independente

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Melhorias que afetam várias histórias de usuário

- [ ] TXXX [P] Atualizar a documentação em docs/
- [ ] TXXX Limpar e refatorar o código
- [ ] TXXX Otimizar o desempenho em todas as histórias
- [ ] TXXX [P] Adicionar testes unitários (se solicitados) em tests/unit/
- [ ] TXXX Reforçar a segurança
- [ ] TXXX Executar a validação de quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Configuração (Fase 1)**: Sem dependências — pode começar imediatamente
- **Fundamental (Fase 2)**: Depende da conclusão da configuração — BLOQUEIA todas as histórias de usuário
- **Histórias de usuário (Fase 3+)**: Todas dependem da conclusão da fase fundamental
  - Depois, as histórias de usuário podem prosseguir em paralelo (se houver equipe)
  - Ou sequencialmente, por ordem de prioridade (P1 → P2 → P3)
- **Polimento (Fase final)**: Depende da conclusão de todas as histórias de usuário desejadas

### User Story Dependencies

- **História de Usuário 1 (P1)**: Pode começar após a fase fundamental (Fase 2) — sem dependências de outras histórias
- **História de Usuário 2 (P2)**: Pode começar após a fase fundamental (Fase 2) — pode integrar-se à US1, mas deve ser testável de forma independente
- **História de Usuário 3 (P3)**: Pode começar após a fase fundamental (Fase 2) — pode integrar-se à US1/US2, mas deve ser testável de forma independente

### Within Each User Story

- Os testes (se incluídos) DEVEM ser escritos e FALHAR antes da implementação
- Modelos antes de serviços
- Serviços antes de endpoints
- Implementação principal antes da integração
- Conclua a história antes de avançar para a próxima prioridade

### Parallel Opportunities

- Todas as tarefas de configuração marcadas com [P] podem ser executadas em paralelo
- Todas as tarefas fundamentais marcadas com [P] podem ser executadas em paralelo (na Fase 2)
- Após a conclusão da fase fundamental, todas as histórias de usuário podem começar em paralelo (se a capacidade da equipe permitir)
- Todos os testes de uma história de usuário marcados com [P] podem ser executados em paralelo
- Os modelos de uma história marcados com [P] podem ser executados em paralelo
- Histórias de usuário diferentes podem ser trabalhadas em paralelo por integrantes diferentes da equipe

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for [endpoint] in tests/contract/test_[name].py"
Task: "Integration test for [user journey] in tests/integration/test_[name].py"

# Launch all models for User Story 1 together:
Task: "Create [Entity1] model in src/models/[entity1].py"
Task: "Create [Entity2] model in src/models/[entity2].py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Conclua a Fase 1: Configuração
2. Conclua a Fase 2: Fundamental (CRÍTICA — bloqueia todas as histórias)
3. Conclua a Fase 3: História de Usuário 1
4. **PARE e VALIDE**: Teste a História de Usuário 1 de forma independente
5. Implante/demonstre se estiver pronta

### Incremental Delivery

1. Conclua Configuração + Fundamental → fundação pronta
2. Adicione a História de Usuário 1 → teste de forma independente → implante/demonstre (MVP!)
3. Adicione a História de Usuário 2 → teste de forma independente → implante/demonstre
4. Adicione a História de Usuário 3 → teste de forma independente → implante/demonstre
5. Cada história agrega valor sem quebrar as histórias anteriores

### Parallel Team Strategy

Com vários desenvolvedores:

1. A equipe conclui Configuração + Fundamental em conjunto
2. Quando a fase fundamental estiver concluída:
   - Pessoa desenvolvedora A: História de Usuário 1
   - Pessoa desenvolvedora B: História de Usuário 2
   - Pessoa desenvolvedora C: História de Usuário 3
3. As histórias são concluídas e integradas de forma independente

---

## Notes

- Tarefas [P] = arquivos diferentes, sem dependências
- O rótulo [Story] associa a tarefa a uma história de usuário específica para rastreabilidade
- Cada história de usuário deve poder ser concluída e testada de forma independente
- Confirme que os testes falham antes de implementar
- Faça commit após cada tarefa ou grupo lógico
- Pare em qualquer checkpoint para validar a história de forma independente
- Evite: tarefas vagas, conflitos no mesmo arquivo e dependências entre histórias que prejudiquem a independência
