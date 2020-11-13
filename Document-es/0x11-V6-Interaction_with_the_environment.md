# V6: Requerimientos de Interacción con la Plataforma

## Objetivo de Control

Estos controles revisan que se utilicen las APIs de la plataforma y componentes estándar de una manera segura. Además, se cubre la comunicación entre aplicaciones (IPC).

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | La aplicación requiere la cantidad de permisos mínimamente necesaria. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | Todo dato ingresado por el usuario o cualquier fuente externa debe ser validado y, si es necesario, saneado. Esto incluye información recibida por la UI o mecanismos IPC como los Intents, URLs y datos provenientes de la red. | ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | La aplicación no expone ninguna funcionalidad sensible a través esquemas de URL salvo que dichos mecanismos estén debidamente protegidos. | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | La aplicación no expone ninguna funcionalidad sensible a través de mecanismos IPC salvo que dichos mecanismos estén debidamente protegidos. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | JavaScript se encuentra deshabilitado en los WebViews salvo que sea necesario. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | Las WebViews se configuran para permitir el mínimo de los esquemas (idealmente, sólo https). Esquemas peligrosos como file, tel y app-id están deshabilitados. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | Si objetos nativos son expuestos en WebViews, debe verificarse que cualquier componente JavaScript se carga exclusivamente desde el contenedor de la aplicación. | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | La serialización de objetos, si se realiza, debe implementarse utilizando API seguras. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | La aplicación se protege contra ataques de tipo screen overlay. (sólo Android) |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | La caché, el almacenamiento y los recursos cargados (JavaScript, etc.) de las WebViews deben de borrarse antes de destruir la WebView. |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | Verificar que la aplicación impide el uso de teclados de terceros siempre que se introduzca información sensible. (sólo iOS) |  | ✓ |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Para más información, ver también:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
