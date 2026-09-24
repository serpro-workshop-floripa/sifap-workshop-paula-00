# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`

**Created**: [DATE]

**Status**: Draft

**Input**: User description: "$ARGUMENTS"

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANTE: As histórias de usuário devem ser PRIORIZADAS como jornadas de
  usuário ordenadas por importância. Cada história/jornada de usuário deve ser
  TESTÁVEL DE FORMA INDEPENDENTE — isso significa que, se você implementar apenas
  UMA delas, ainda deverá ter um MVP (Produto Mínimo Viável) que entregue valor.

  Atribua prioridades (P1, P2, P3 etc.) a cada história, em que P1 é a mais
  crítica. Considere cada história como uma fatia independente de funcionalidade
  que possa ser:
  - Desenvolvida de forma independente
  - Testada de forma independente
  - Implantada de forma independente
  - Demonstrada aos usuários de forma independente
-->

### User Story 1 - [Brief Title] (Priority: P1)

[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently - e.g., "Can be fully tested by [specific action] and delivers [specific value]"]

**Acceptance Scenarios**:

1. **Given** [initial state], **When** [action], **Then** [expected outcome]
2. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

### User Story 2 - [Brief Title] (Priority: P2)

[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**Acceptance Scenarios**:

1. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

### User Story 3 - [Brief Title] (Priority: P3)

[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**Acceptance Scenarios**:

1. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

<!--
  AÇÃO NECESSÁRIA: O conteúdo desta seção representa placeholders.
  Preencha-os com os casos extremos adequados.
-->

- O que acontece quando [boundary condition]?
- Como o sistema trata [error scenario]?

## Requirements *(mandatory)*

<!--
  AÇÃO NECESSÁRIA: O conteúdo desta seção representa placeholders.
  Preencha-os com os requisitos funcionais adequados.
-->

### Functional Requirements

- **FR-001**: O sistema DEVE [specific capability, e.g., "allow users to create accounts"]
- **FR-002**: O sistema DEVE [specific capability, e.g., "validate email addresses"]
- **FR-003**: Os usuários DEVEM poder [key interaction, e.g., "reset their password"]
- **FR-004**: O sistema DEVE [data requirement, e.g., "persist user preferences"]
- **FR-005**: O sistema DEVE [behavior, e.g., "log all security events"]

*Exemplo de marcação de requisitos pouco claros:*

- **FR-006**: O sistema DEVE autenticar usuários por [NEEDS CLARIFICATION: auth method not specified - email/password, SSO, OAuth?]
- **FR-007**: O sistema DEVE reter os dados do usuário por [NEEDS CLARIFICATION: retention period not specified]

### Key Entities *(include if feature involves data)*

- **[Entity 1]**: [What it represents, key attributes without implementation]
- **[Entity 2]**: [What it represents, relationships to other entities]

## Success Criteria *(mandatory)*

<!--
  AÇÃO NECESSÁRIA: Defina critérios de sucesso mensuráveis.
  Eles devem ser independentes de tecnologia e mensuráveis.
-->

### Measurable Outcomes

- **SC-001**: [Measurable metric, e.g., "Users can complete account creation in under 2 minutes"]
- **SC-002**: [Measurable metric, e.g., "System handles 1000 concurrent users without degradation"]
- **SC-003**: [User satisfaction metric, e.g., "90% of users successfully complete primary task on first attempt"]
- **SC-004**: [Business metric, e.g., "Reduce support tickets related to [X] by 50%"]

## Assumptions

<!--
  AÇÃO NECESSÁRIA: O conteúdo desta seção representa placeholders.
  Preencha-os com as premissas adequadas, baseadas em padrões razoáveis
  escolhidos quando a descrição da funcionalidade não especificar determinados
  detalhes.
-->

- [Assumption about target users, e.g., "Users have stable internet connectivity"]
- [Assumption about scope boundaries, e.g., "Mobile support is out of scope for v1"]
- [Assumption about data/environment, e.g., "Existing authentication system will be reused"]
- [Dependency on existing system/service, e.g., "Requires access to the existing user profile API"]
