# V2: Requerimientos de Almacenamiento de datos y Privacidad

## Objetivo de Control

La protección de datos sensibles, como las credenciales del usuario y la información privada, es un aspecto clave de la seguridad móvil. En primer lugar, los datos confidenciales pueden exponerse involuntariamente a otras aplicaciones que se ejecutan en el mismo dispositivo si se utilizan de forma inadecuada mecanismos de comunicación entre procesos del sistema operativo. Los datos también pueden filtrarse involuntariamente en el almacenamiento en la nube, las copias de seguridad o la caché del teclado. Además, los dispositivos móviles pueden perderse o robarse más fácilmente que otros tipos de dispositivos, por lo que un adversario que obtiene acceso físico al mismo es un escenario más probable. En ese caso, se pueden implementar protecciones adicionales para dificultar la recuperación de los datos sensibles.

El MASVS se centra en las aplicaciones y por esto no cubre políticas para el dispositivo como Mobile Device Managment (MDM) (<https://gsuite.google.com/products/admin/mobile/>) o Enter (EDM). Igualmente se recomienda utilizar estas soluciones en contextos empresariales.

### Definición de Datos Sensibles

Los datos sensibles en el contexto del MASVS se refieren tanto a las credenciales de usuario como a cualquier otro dato que se considere sensible en el contexto particular, por ejemplo:

- Información de identificación personal que puede ser usada para el robo de identidad: números de seguro social, números de tarjetas de crédito, números de cuentas bancarias, información médica;
- Datos altamente confidenciales que, en caso de que se comprometieran, ocasionarían daños a la reputación y/o costes financieros: información contractual, información cubierta por acuerdos de confidencialidad, información de gestión;
- Cualquier dato que debe ser protegido por ley o por razones de conformidad.

## Requerimientos de Verificación de Seguridad

La gran mayoría de las cuestiones relativas a la divulgación de datos pueden prevenirse siguiendo reglas sencillas. La mayoría de los controles enumerados en este capítulo son obligatorios para todos los niveles de verificación.

| # | MSTG-ID | Descripción | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | Las funcionalidades de almacenamiento de credenciales del sistema deben de ser utilizadas para almacenar información sensible, tal como información personal, credenciales de usuario o claves criptográficas. | ✓ | ✓ |
| **2.2** | MSTG-STORAGE-2 | No se debe almacenar información sensible fuera del contenedor de la aplicación o del almacenamiento de credenciales del sistema. | ✓ | ✓ |
| **2.3** | MSTG-STORAGE-3 | No se escribe información sensible en los registros (logs) de la aplicación. | ✓ | ✓ |
| **2.4** | MSTG-STORAGE-4 | No se comparte información sensible con servicios externos salvo que sea una necesidad de la arquitectura. | ✓ | ✓ |
| **2.5** | MSTG-STORAGE-5 | Se desactiva la caché del teclado en los campos de texto que contienen información sensible. | ✓ | ✓ |
| **2.6** | MSTG-STORAGE-6 | No se expone información sensible mediante mecanismos de comunicación entre procesos (IPC). | ✓ | ✓ |
| **2.7** | MSTG-STORAGE-7 | No se expone información sensible como contraseñas y números de tarjetas de crédito a través de la interfaz o capturas de pantalla. | ✓ | ✓ |
| **2.8** | MSTG-STORAGE-8 | No se incluye información sensible en las copias de seguridad generadas por el sistema operativo. |   | ✓ |
| **2.9** | MSTG-STORAGE-9 | La aplicación elimina toda información sensible de la vista cuando la aplicación pasa a un segundo plano. |  | ✓ |
| **2.10** | MSTG-STORAGE-10 | La aplicación no conserva ninguna información sensible en memoria más de lo necesario y la memoria se limpia trás su uso. |  | ✓ |
| **2.11** | MSTG-STORAGE-11 | La aplicación obliga a que exista una política mínima de seguridad en el dispositivo, como que el usuario deba configurar un código de acceso. |  | ✓ |
| **2.12** | MSTG-STORAGE-12 | La aplicación educa al usuario acerca de los tipos de información personal que procesa y de las mejores prácticas en seguridad que el usuario debería seguir al utilizar la aplicación. |  | ✓ |
| **2.13** | MSTG-STORAGE-13 | No se guarda ningún tipo de información sensible de forma local en el dispositivo móvil. En su lugar, esa información debería ser obtenida desde un sistema remoto sólo cuando es necesario y únicamente residir en memoria. |  | ✓ |
| **2.14** | MSTG-STORAGE-14 | En caso de ser necesario guardar información sensible de forma local, ésta debe de ser cifrada usando una clave derivada del hardware de almacenamiento seguro, el cual debe requerir autenticación previa. |  | ✓ |
| **2.15** | MSTG-STORAGE-15 | El almacenamiento local de la aplicación debe de ser borrado trás un número excesivo de intentos fallidos de autenticación. |  | ✓ |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

Para más información, ver también:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M2 (Insecure Data Storage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage>
- CWE 117 (Improper Output Neutralization for Logs) - <https://cwe.mitre.org/data/definitions/117.html>
- CWE 200 (Information Exposure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 276 (Incorrect Default Permissions) - <https://cwe.mitre.org/data/definitions/276.html>
- CWE 311 (Missing Encryption of Sensitive Data) - <https://cwe.mitre.org/data/definitions/311.html>
- CWE 312 (Cleartext Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/312.html>
- CWE 316 (Cleartext Storage of Sensitive Information in Memory) - <https://cwe.mitre.org/data/definitions/316.html>
- CWE 359 (Exposure of Private Information ('Privacy Violation')) - <https://cwe.mitre.org/data/definitions/359.html>
- CWE 522 (Insufficiently Protected Credentials) - <https://cwe.mitre.org/data/definitions/522.html>
- CWE 524 (Information Exposure Through Caching) - <https://cwe.mitre.org/data/definitions/524.html>
- CWE 530 (Exposure of Backup File to an Unauthorized Control Sphere) - <https://cwe.mitre.org/data/definitions/530.html>
- CWE 532 (Information Exposure Through Log Files) - <https://cwe.mitre.org/data/definitions/532.html>
- CWE 534 (Information Exposure Through Debug Log Files) - <https://cwe.mitre.org/data/definitions/534.html>
- CWE 634 (Weaknesses that Affect System Processes) - <https://cwe.mitre.org/data/definitions/634.html>
- CWE 798 (Use of Hard-coded Credentials) - <https://cwe.mitre.org/data/definitions/798.html>
- CWE 921 (Storage of Sensitive Data in a Mechanism without Access Control) - <https://cwe.mitre.org/data/definitions/921.html>
- CWE 922 (Insecure Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/922.html>
