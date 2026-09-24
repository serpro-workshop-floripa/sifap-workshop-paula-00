---
description: "Use ao implementar ou revisar autenticação, autorização, criptografia, configuração segura, tratamento de secrets e código sensível à segurança."
applyTo: "backend/src/main/java/**/auth/**,backend/src/main/java/**/security/**,backend/src/main/java/**/config/**,backend/src/main/resources/**,frontend/**/auth/**,frontend/**/middleware.ts"
---

# Convenções de segurança — Autenticação, secrets e injeção

Este arquivo se aplica a `auth/`, `security/`, `config/`, `backend/src/main/resources/`, `frontend/**/auth/**` e `frontend/middleware.ts`. Ele orienta autenticação, autorização, validação, CORS, secrets e dados sensíveis conforme o OWASP Top 10. O formato REST está em [`backend.instructions.md`](backend.instructions.md), e o armazenamento de secrets do Terraform em [`infrastructure.instructions.md`](infrastructure.instructions.md).

## Autenticação (OAuth2/JWT)

O backend é um OAuth2 resource server stateless que valida JWTs com Spring Security. Nunca implemente parsing de token ou criptografia manualmente.

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
class SecurityConfig {

    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/actuator/health").permitAll()
                .anyRequest().authenticated())
            .oauth2ResourceServer(oauth -> oauth.jwt(Customizer.withDefaults()))
            .cors(Customizer.withDefaults())
            .csrf(csrf -> csrf.disable());
        return http.build();
    }
}
```

Se houver armazenamento de senhas, use argon2 ou bcrypt, nunca digest puro. Aplique rate limiting no login e MFA para administradores.

## Autorização

Autorize cada request, negue por padrão e aplique privilégio mínimo. Use method security para papéis e verifique explicitamente a propriedade do resource.

```java
@PreAuthorize("hasRole('AUDITOR')")
public AuditReport generate(UUID resourceId, Authentication principal) {
    Resource resource = resourceService.getOwned(resourceId, principal.getName());
    return AuditReport.of(resource);
}
```

## Validação de input e injeção

Valide cada fronteira com `@Valid`. Crie queries apenas com parâmetros vinculados em JPA/JPQL, escape HTML no output e valide tipo e tamanho de uploads.

> [!WARNING]
> Nunca concatene input do usuário em query, comando shell ou markup. Parameter binding é obrigatório.

## CORS

Configure origens permitidas explicitamente. O curinga `*` é proibido em produção.

```java
@Bean
CorsConfigurationSource corsConfigurationSource() {
    CorsConfiguration config = new CorsConfiguration();
    config.setAllowedOrigins(List.of("https://app.example.gov.br"));
    config.setAllowedMethods(List.of("GET", "POST", "PUT", "PATCH", "DELETE"));
    config.setAllowedHeaders(List.of("Authorization", "Content-Type"));
    UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
    source.registerCorsConfiguration("/api/**", config);
    return source;
}
```

## Secrets e configuração segura

Não fixe, versione nem registre secrets. Leia-os do ambiente ou do Key Vault. Use Managed Identity na autenticação entre serviços Azure. No frontend, apenas valores não secretos podem usar `NEXT_PUBLIC_`, pois esse prefixo envia o valor ao navegador.

## Dados sensíveis

> [!IMPORTANT]
> Mascare CPF e valores de benefícios em logs, erros e URLs. Nunca os coloque em query strings ou armazenamento sem criptografia. Sempre transmita por TLS.

```java
String masked = cpf.replaceAll("(\\d{3})\\d{6}(\\d{2})", "$1******$2");
```

## Fronteira de autenticação no frontend

Proteja rotas no middleware e nunca confie no cliente para impor acesso. Mantenha tokens e secrets no servidor.

```ts
import { NextResponse, type NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const session = request.cookies.get('session');
  if (!session) return NextResponse.redirect(new URL('/login', request.url));
  return NextResponse.next();
}

export const config = { matcher: ['/dashboard/:path*'] };
```

## Fronteiras de automação e agentes

Agentes de IA e automações nunca concedem novas permissões a si mesmos nem acessam banco de produção sem aprovação humana explícita. Alterações de autenticação, papéis ou secrets exigem revisão antes do merge.

## Convenções

| Regra | Motivo |
|---|---|
| OAuth2/JWT pelo Spring Security | Evita código de autenticação customizado e propenso a erros |
| Autorize cada request e negue por padrão | Aplica privilégio mínimo |
| Use apenas parâmetros vinculados | Elimina SQL injection |
| Configure origens CORS explícitas | Bloqueia abuso entre origens |
| Leia secrets do ambiente ou Key Vault | Evita credenciais no código e nos logs |
| Mascare CPF e valores | Protege dados regulados |

## Faça / Não faça

| Faça | Não faça |
|---|---|
| Use argon2 ou bcrypt para senhas | Armazene texto puro ou digest sem salt |
| Verifique papel e propriedade do resource | Considere o papel autorização suficiente |
| Mantenha secrets no servidor | Prefixe um secret com `NEXT_PUBLIC_` |
| Mascare campos antes do log | Coloque CPF ou valores em logs e query strings |

## Checklist antes de abrir um PR

- [ ] Endpoints autenticam pelo Spring Security, sem parsing customizado de token.
- [ ] Cada request é autorizada com negação por padrão e verificação de propriedade quando relevante.
- [ ] Queries usam parâmetros vinculados; uploads e inputs são validados.
- [ ] CORS lista origens explícitas e não usa `*` em produção.
- [ ] Nenhum secret está fixado, versionado ou registrado; Azure usa Managed Identity.
- [ ] CPF, valores e tokens estão mascarados em logs, erros e URLs.
