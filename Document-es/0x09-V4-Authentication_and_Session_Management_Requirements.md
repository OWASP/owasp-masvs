# V4: Requerimientos de Autenticación y Manejo de Sesiones

## Objetivo de control

En la mayoría de los casos, una parte esencial de la arquitectura global de aplicaciones móviles es que los usuarios deben inician sesión en un servicio remoto. Aunque la mayor parte de la lógica ocurre en el servidor, MASVS define algunos requerimientos básicos sobre como manejar las cuentas y sesiones del usuario.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción | L1 | L2 |
| --- | --- | --- | --- | --- |
| **4.1** | MSTG‑AUTH‑1 | Si la aplicación provee acceso a un servicio remoto, un mecanismo aceptable de autenticación como usuario y contraseña es realizado en el servidor remoto. | ✓ | ✓ |
| **4.2** | MSTG‑AUTH‑2 | Si se utiliza la gestión de sesión por estado, el servidor remoto usa tokens de acceso aleatorios para autenticar los pedidos del cliente sin requerir el envío de las credenciales del usuario en cada uno. | ✓ | ✓ |
| **4.3** | MSTG‑AUTH‑3 | Si se utiliza la autenticación basada en tokens sin estado, el servidor proporciona un token que se ha firmado utilizando un algoritmo seguro. | ✓ | ✓ |
| **4.4** | MSTG‑AUTH‑4 | Cuando el usuario cierra sesión se termina la sesión también en el servidor. | ✓ | ✓ |
| **4.5** | MSTG‑AUTH‑5 | Existe una política de contraseñas y es aplicada en el servidor. | ✓ | ✓ |
| **4.6** | MSTG‑AUTH‑6 | El servidor implementa mecanismos, cuando credenciales de autenticación son ingresadas una cantidad excesiva de veces. | ✓ | ✓ |
| **4.7** | MSTG‑AUTH‑7 | Las sesiones y los tokens de acceso expiran luego de un tiempo predefinido de inactividad. | ✓  | ✓ |
| **4.8** | MSTG‑AUTH‑8 | La autenticación biométrica, si hay, no está atada a un evento (usando una API que simplemente retorna "true" o "false"). Sino que está basado en el desbloqueo del keychain (iOS) o un keystore (Android). |   | ✓ |
| **4.9** | MSTG‑AUTH‑9 | Existe un mecanismo de segundo factor de autenticación (2FA) en el servidor y es aplicado consistentemente. |   | ✓ |
| **4.10** | MSTG‑AUTH‑10 | Para realizar transacciones se requiere una re-autenticación. |   | ✓ |
| **4.11** | MSTG‑AUTH‑11 | La aplicación informa al usuario acerca de los accesos a su cuenta. El usuario es capaz de ver una lista de los dispositivos conectados y bloquear el acceso desde ciertos dispositivos. |  | ✓ |

<div style="page-break-after: always;"></div>

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- General - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Para Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- Para iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M4 - Autenticación Insegura: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M4-Insecure_Authentication>
- OWASP Top 10 Móvil: M6 - Autorización Insegura: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M6-Insecure_Authorization>
- CWE:  <https://cwe.mitre.org/data/definitions/287.html>
