# V4: Requisitos de Autenticação e Gerenciamento de Sessão

## Objetivo do Controle

Na maioria dos casos, o _login_ de usuários a um serviço remoto é parte integrante da arquitetura global das aplicações móveis. Embora a maior parte da lógica aconteça no terminal, o MASVS define alguns requisitos básicos sobre a forma como as contas e sessões dos usuários devem ser gerenciadas.

## Requisitos de Verificação de Segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Se o aplicativo fornecer aos usuários acesso a um serviço remoto, alguma forma de autenticação, como autenticação de nome de usuário e senha, será executada no terminal remoto. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | Se o gerenciamento de sessão com estado for usado _(stateful session management)_, o terminal remoto usará identificadores de sessão gerados aleatoriamente para autenticar as solicitações de clientes, sem que as credenciais do usuário sejam enviadas. | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | Se a autenticação baseada em _token_ sem estado for usada _(stateless token-based authentication)_, o servidor fornecerá um _token_ que foi assinado usando um algoritmo seguro. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | O _endpoint_ remoto termina a sessão existente quando o usuário efetuar _logout_. | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | Uma política de senha existe e é imposta no terminal remoto. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | O terminal remoto implementa um mecanismo para proteger contra o envio de credenciais em um número excessivo. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | As sessões são invalidadas pelo terminal remoto após um período predefinido de inatividade e os _tokens_ de acessos expiram. | ✓ | ✓ |
| **4.8** | MSTG-AUTH-8 | A autenticação biométrica, se houver, não é vinculada a eventos (ou seja, usando uma API que simplesmente retorna "verdadeiro" ou "falso"). Em vez disso, é baseado no desbloqueio do _keychain/keystore_ (armazenamento seguro). | | ✓ |
| **4.9** | MSTG-AUTH-9 | Existe um segundo fator de autenticação no terminal remoto e o requisito de 2FA é aplicado de maneira consistente. | | ✓ |
| **4.10** | MSTG-AUTH-10 | Transações confidenciais requerem autenticação adicional. | | ✓ |
| **4.11** | MSTG-AUTH-11 | O aplicativo informa o usuário de todas as atividades confidenciais com a sua conta. Os usuários podem visualizar uma lista de dispositivos, exibir informações contextuais (endereço IP, local etc.) e é capaz de bloquear dispositivos específicos. | | ✓ |
| **4.12** | MSTG-AUTH-12 | Os modelos de autorização devem ser definidos e aplicados no terminal remoto. | ✓ | ✓ |

## Referências

O Guia de Teste de Segurança de Aplicações Móveis da OWASP fornece instruções detalhadas para verificar os requisitos listados nesta seção (em inglês).

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Para mais informações, consulte também (em inglês):

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
