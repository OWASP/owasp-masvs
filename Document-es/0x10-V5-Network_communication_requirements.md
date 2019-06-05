# V5: Requerimientos de Comunicación a través de la red

## Objetivo de control

Los controles enumerados en esta categoría tienen por objetivo asegurar la confidencialidad e integridad de la información intercambiada entre la aplicación móvil y los servicios del servidor. Como mínimo se deben utilizar canales seguros y cifrados utilizando el protocolo TLS con las configuraciones apropiadas. En el nivel 2 se establecen medidas en profundidad como fijación de certificados SSL.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción |L2 |
| --- | --- | --- | --- | --- |
| **5.1** | MSTG‑NETWORK‑1 | La información es enviada cifrada utilizando TLS. El canal seguro es usado consistentemente en la aplicación. | ✓ | ✓ |
| **5.2** | MSTG‑NETWORK‑2 | Las configuraciones del protocolo TLS siguen las mejores prácticas o tan cerca posible mientras que el sistema operativo del dispositivo lo permite. | ✓ | ✓ |
| **5.3** | MSTG‑NETWORK‑3 | La aplicación verifica el certificado X.509 del servidor al establecer el canal seguro y solo se aceptan certificados firmados por una CA válida. | ✓ | ✓ |
| **5.4** | MSTG‑NETWORK‑4 | La aplicación utiliza su propio almacén de certificados o realiza una fijación del certificado o la clave pública del servidor y no establece una conexión con servidores que ofrecen otros certificados o clave por más que estén firmados por una CA confiable. |   | ✓ |
| **5.5** | MSTG‑NETWORK‑5 | La aplicación no depende de un único canal de comunicaciones inseguro (email o SMS) para operaciones críticas como registros o recuperación de cuentas. |  | ✓ |
| **5.6** | MSTG‑NETWORK‑6 | La aplicación sólo depende de bibliotecas de conectividad y seguridad actualizadas. |  | ✓ |

<div style="page-break-after: always;"></div>

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M3 - Comunicación Insegura: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M3-Insecure_Communication>
- CWE: <https://cwe.mitre.org/data/definitions/319.html>
- CWE: <https://cwe.mitre.org/data/definitions/295.html>
