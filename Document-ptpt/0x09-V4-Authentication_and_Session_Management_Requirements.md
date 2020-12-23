# V4: Requisitos de Autenticação e Gestão da Sessão

## Objetivo de Controlo

Na grande maioria dos casos, a autenticação dos utilizadores em serviços remotos é uma parte integral da arquitetura da aplicação no geral. Ainda que a maior parte da lógica seja feita no ponto de acesso remoto, MASVS define alguns requisitos relativos à gestão da sessão e da conta dos utilizadores.

## Requisitos para a Verificação de Segurança

| # | MSTG-ID | Descrição| L1 | L2 |
 | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Se a aplicação providencia ao utilizador acesso a um serviço remoto, algum tipo de autenticação, como autenticação por nome de utilizador/palavra passe, é realizada no ponto de acesso remoto. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | Se a gestão da sessão é feita com persistência de estado, o acesso remoto deve fazer uso do identificador de sessão gerado aleatoriamente, para garantir a autenticação do cliente/utilizador a cada pedido ao servidor, sem que seja necessário o repetitivo fornecimento das credenciais do utilizador. | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | Se a gestão da sessão é baseada num passe (token), sem persistência de estado, o servidor providencia o passe assinado através de um algoritmo seguro. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | O ponto de acesso remoto termina a existente sessão quando o utilizador sai da aplicação (logout). | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | Ao nível do ponto de acesso, deve existir uma colecção de regras para a definição da palavra-passe. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | O ponto de acesso deve implementar um mecanismo que permita proteger a aplicação de uma submissão excessiva de tentativas de autenticação. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | As sessões devem ser invalidadas ao nível do ponto de acesso após um período de inactividade pré-definido, ao fim do qual, os passes de acesso (access token) expiram. | ✓ | ✓ |
| **4.8** | MSTG-AUTH-8 | A autenticação biométrica, se aplicável, não deve ser implementada através de uma API que retorna Verdadeiro ou Falso. Deve ser baseada no desbloqueio de um gestor de credenciais (keychain/keystore). | | ✓ |
| **4.9** | MSTG-AUTH-9 | Existe uma segunda autenticação (second factor authentication, 2FA) no ponto de acesso/ servidor e esse modo de autenticação é reforçado.  | | ✓ |
| **4.10** | MSTG-AUTH-10 | A transmissão de informação sensível deve ser feita após o reforço da autenticação. | | ✓ |
| **4.11** | MSTG-AUTH-11 | A aplicação informa o utilizador de qualquer actividade sensível efectuada com a sua conta. Aos utilizadores é providenciada uma lista de dispositivos onde a sua conta está a ser utilizada, assim como outras informações contextuais (localização, identificador respectivo à conexão da internet, entre outras), e também o bloqueio desses mesmos dispositivos. | | ✓ |
| **4.12** | MSTG-AUTH-12 | Os modelos de autorização devem ser definidos e aplicados ao nível do ponto de acesso. | ✓ | ✓ |

## Referências

O OWASP Mobile Security Testing Guide providencia instruções detalhadas para a verificação dos requisitos listados acima.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Para mais informação:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
