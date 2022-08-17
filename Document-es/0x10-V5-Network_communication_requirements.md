# V5: Requisitos de Comunicación a través de la red

## Objetivo de la Categoría V5

Los controles enumerados en esta categoría tienen el objetivo de asegurar la confidencialidad e integridad de la información intercambiada entre la aplicación móvil y los servicios del servidor. Como mínimo se deben utilizar canales seguros y cifrados utilizando el protocolo TLS con las configuraciones apropiadas. En el nivel 2 se establecen medidas en profundidad como fijación de certificados SSL.

## Requisitos de Verificación de Seguridad

| # | MSTG-ID | Descripción | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | La información se debe enviar cifrada utilizando TLS. El canal seguro es usado consistentemente en la aplicación. | x | x |
| **5.2** | MSTG-NETWORK-2 | Las configuraciones del protocolo TLS deben seguir las buenas prácticas de la industria, o deben hacerlo lo mejor posible en caso de que el sistema operativo del dispositivo no soporte los estándares recomendados. | x | x |
| **5.3** | MSTG-NETWORK-3 | La aplicación debe verificar el certificado X.509 del sistema remoto al establecer el canal seguro y sólo se deben aceptar certificados firmados por una entidad certificadora (CA) de confianza. | x | x |
| **5.4** | MSTG-NETWORK-4 | La aplicación debe utilizar su propio almacén de certificados o realiza _pinning_ del certificado o la clave pública del servidor. Bajo ningún concepto establecerá conexiones con servidores que ofrecen otros certificados o claves, incluso si están firmados por una entidad certificadora (CA) de confianza. |   | x |
| **5.5** | MSTG-NETWORK-5 | La aplicación no debe depender de un único canal de comunicaciones inseguro (email o SMS) para operaciones críticas como registro de usuarios o recuperación de cuentas. |  | x |
| **5.6** | MSTG-NETWORK-6 | La aplicación sólo debe depender de bibliotecas de conectividad y seguridad actualizadas. |  | x |

<!-- \pagebreak -->

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Para más información, ver también:

- OWASP Mobile Top 10: M3 (Insecure Communication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Improper Certificate Validation) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Improper Following of a Certificate's Chain of Trust) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Improper Validation of Certificate with Host Mismatch) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Improper Validation of Certificate Expiration) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Cleartext Transmission of Sensitive Information) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Use of RSA Algorithm without OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Improper Verification of Source of a Communication Channel) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Incorrectly Specified Destination in a Communication Channel) - <https://cwe.mitre.org/data/definitions/941.html>
