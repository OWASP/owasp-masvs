# V7: Requerimientos de Calidad de Código y Configuración del Compilador

## Objetivo de control

Estos controles buscan asegurar que se siguieron las prácticas de seguridad básicas en el desarrollo de la aplicación. Y que se activaron las funcionalidades "gratuitas" ofrecidas por el compilador.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción |1 | L2 |
| --- | --- | --- | --- | --- |
| **7.1** | MSTG‑CODE‑1 | La aplicación es firmada y provista con un certificado válido, del cual se protege debidamente su clave privada. | ✓ | ✓ |
| **7.2** | MSTG‑CODE‑2 | La aplicación fue liberada en modo release y con las configuraciones apropiadas para el mismo (ej. non-debuggable). | ✓ | ✓ |
| **7.3** | MSTG‑CODE‑3 | Los símbolos de debug fueron removidos de los binarios nativos. | ✓ | ✓ |
| **7.4** | MSTG‑CODE‑4 | La aplicación no contiene código de prueba y no realiza log de errores o mensajes de debug. | ✓ | ✓ |
| **7.5** | MSTG‑CODE‑5 | Todos los componentes de terceros se encuentran identificados y revisados por vulnerabilidades conocidas. | ✓ | ✓ |
| **7.6** | MSTG‑CODE‑6 | La aplicación captura y maneja debidamente las posibles excepciones. | ✓ | ✓ |
| **7.7** | MSTG‑CODE‑7 | Los controles de seguridad deniegan el acceso por defecto. | ✓ | ✓ |
| **7.8** | MSTG‑CODE‑8 | En código no administrado, la memoria es pedida, usada y liberada de manera correcta. | ✓ | ✓ |
| **7.9** | MSTG‑CODE‑9 | Las funcionalidades de seguridad gratuitas de las herramientas, como minificación del byte-code, protección de la pila, soporte PIE y conteo automático de referencias, se encuentran activadas. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M7 - Mala calidad del Código: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M7-Poor_Code_Quality>
- CWE: <https://cwe.mitre.org/data/definitions/119.html>
- CWE: <https://cwe.mitre.org/data/definitions/89.html>
- CWE: <https://cwe.mitre.org/data/definitions/388.html>
- CWE: <https://cwe.mitre.org/data/definitions/489.html>
