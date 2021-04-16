# V4: Requerimientos de Autenticación y Manejo de Sesiones

## Objetivo de Control

En la mayoría de los casos, una parte esencial de la arquitectura global de aplicaciones móviles es que los usuarios deben inician sesión en un servicio remoto. Aunque la mayor parte de la lógica ocurre en el servidor, MASVS define algunos requerimientos básicos sobre como manejar las cuentas y sesiones del usuario.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Si la aplicación provee acceso a un servicio remoto, un mecanismo aceptable de autenticación como usuario y contraseña es realizado en el servidor remoto. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | Si se utiliza la gestión de sesión por estado, el servidor remoto usa tokens de acceso aleatorios para autenticar los pedidos del cliente sin requerir el envío de las credenciales del usuario en cada uno. | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | Si se utiliza la autenticación basada en tokens sin estado, el servidor proporciona un token que se ha firmado utilizando un algoritmo seguro. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | Cuando el usuario cierra sesión se termina la sesión también en el servidor. | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | Existe una política de contraseñas y es aplicada en el servidor. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | El servidor implementa mecanismos, cuando credenciales de autenticación son ingresadas una cantidad excesiva de veces. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | Las sesiones y los tokens de acceso expiran luego de un tiempo predefinido de inactividad. | ✓  | ✓ |
| **4.8** | MSTG-AUTH-8 | La autenticación biométrica, si la hay, no está asociada a eventos (p. ej. usando una API que simplemente retorna "true" o "false"), sino basada en el desbloqueo del keychain/keystore (almacenamiento seguro). |   | ✓ |
| **4.9** | MSTG-AUTH-9 | El sistema remoto implementa un mecanismo de segundo factor de autenticación (2FA) y lo impone consistentemente. |   | ✓ |
| **4.10** | MSTG-AUTH-10 | Para realizar transacciones críticas se requiere una autenticación adicional (step-up). |   | ✓ |
| **4.11** | MSTG-AUTH-11 | La aplicación informa al usuario acerca de todas las actividades sensibles en su cuenta. El usuario es capaz de ver una lista de los dispositivos conectados, información contextual (dirección IP, localización, etc.), y es capaz de bloquear ciertos dispositivos. |  | ✓ |
| **4.12** | MSTG-AUTH-12 | Los modelos de autorización deberían de ser definidos e impuestos por el sistema remoto. | ✓ | ✓ |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- General - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Para más información, ver también:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
