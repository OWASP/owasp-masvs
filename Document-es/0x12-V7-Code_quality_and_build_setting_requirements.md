# V7: Requerimientos de Calidad de Código y Configuración del Compilador

## Objetivo de Control

Estos controles buscan asegurar que se siguieron las prácticas de seguridad básicas en el desarrollo de la aplicación. Y que se activaron las funcionalidades "gratuitas" ofrecidas por el compilador.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | La aplicación es firmada y provista con un certificado válido, cuya clave privada está debidamente protegida. | x | x |
| **7.2** | MSTG-CODE-2 | La aplicación fue publicada en modo release y con las configuraciones apropiadas para el mismo (por ejemplo, non-debuggable). | x | x |
| **7.3** | MSTG-CODE-3 | Los símbolos de depuración fueron eliminados de los binarios nativos. | x | x |
| **7.4** | MSTG-CODE-4 | Cualquier código de depuración y/o de asistencia al desarrollador (p. ej. código de test, backdoors, configuraciones ocultas) debe ser eliminado. La aplicación no hace logs detallados de errores ni de mensajes de depuración. | x | x |
| **7.5** | MSTG-CODE-5 | Todos los componentes de terceros se encuentran identificados y revisados en cuanto a vulnerabilidades conocidas. | x | x |
| **7.6** | MSTG-CODE-6 | La aplicación captura y gestiona debidamente las posibles excepciones. | x | x |
| **7.7** | MSTG-CODE-7 | Los controles de seguridad deniegan el acceso por defecto. | x | x |
| **7.8** | MSTG-CODE-8 | En código no administrado, la memoria es solicitada, utilizada y liberada de manera correcta. | x | x |
| **7.9** | MSTG-CODE-9 | Las funcionalidades de seguridad gratuitas de las herramientas, tales como minificación del byte-code, protección de la pila, soporte PIE y conteo automático de referencias, se encuentran activadas. | x | x |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Para más información, ver también:

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
