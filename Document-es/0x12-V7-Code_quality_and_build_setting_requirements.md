# V7: Requerimientos de Calidad de Código y Configuración del Compilador

## Objetivo de control

Estos controles buscan asegurar que se siguieron las prácticas de seguridad básicas en el desarrollo de la aplicación. Y que se activaron las funcionalidades "gratuitas" ofrecidas por el compilador.

## Requerimientos de Verificación de Seguridad

| # | Descripción | L1 | L2 |
| --- | --- | --- | --- |
| **7.1** | La aplicación es firmada y provista con un certificado válido. | ✓ | ✓ |
| **7.2** | La aplicación fue liberada en modo release y con las configuraciones apropiadas para el mismo (ej. non-debuggable). | ✓ | ✓ |
| **7.3** | Los símbolos de debug fueron removidos de los binarios nativos. | ✓ | ✓ |
| **7.4** | La aplicación no contiene código de prueba y no realiza log de errores o mensajes de debug. | ✓ | ✓ |
| **7.5** | Todos los componentes de terceros se encuentran identificados y revisados por vulnerabilidades conocidas. | ✓ | ✓ |
| **7.6** | La aplicación captura y maneja debidamente las posibles excepciones.	 | ✓ | ✓ |
| **7.7** | Los controles de seguridad deniegan el acceso por defecto.	 | ✓ | ✓ |
| **7.8** | En código no administrado, la memoria es pedida, usada y liberada de manera correcta. | ✓ | ✓ |
| **7.9** | Funcionalidades de seguridad gratuitas se encuentran activadas. | ✓ | ✓ |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md
- iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md

Para más información, ver también:

- Top 10 Móvil de OWASP:  M7 - Calidad del Código en el Cliente
- CWE: https://cwe.mitre.org/data/definitions/119.html
- CWE: https://cwe.mitre.org/data/definitions/89.html
- CWE: https://cwe.mitre.org/data/definitions/388.html
- CWE: https://cwe.mitre.org/data/definitions/489.html
