# V7: Requerimientos de Calidad de Código y Configuración del Compilador

## Objetivo de Control

Estos controles buscan asegurar que se siguieron las prácticas de seguridad básicas en el desarrollo de la aplicación. Y que se activaron las funcionalidades "gratuitas" ofrecidas por el compilador.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción |1 | L2 |
| --- | --- | --- | --- | --- |
| **7.1** | MSTG‑CODE‑1 | La aplicación es firmada y provista con un certificado válido, cuya clave privada está debidamente protegida. | ✓ | ✓ |
| **7.2** | MSTG‑CODE‑2 | La aplicación fue publicada en modo release y con las configuraciones apropiadas para el mismo (por ejemplo, non-debuggable). | ✓ | ✓ |
| **7.3** | MSTG‑CODE‑3 | Los símbolos de depuración fueron eliminados de los binarios nativos. | ✓ | ✓ |
| **7.4** | MSTG‑CODE‑4 | Cualquier código de depuración y/o de asistencia al desarrollador (p. ej. código de test, backdoors, configuraciones ocultas) debe ser eliminado. La aplicación no hace logs detallados de errores ni de mensajes de depuración. | ✓ | ✓ |
| **7.5** | MSTG‑CODE‑5 | Todos los componentes de terceros se encuentran identificados y revisados en cuanto a vulnerabilidades conocidas. | ✓ | ✓ |
| **7.6** | MSTG‑CODE‑6 | La aplicación captura y gestiona debidamente las posibles excepciones. | ✓ | ✓ |
| **7.7** | MSTG‑CODE‑7 | Los controles de seguridad deniegan el acceso por defecto. | ✓ | ✓ |
| **7.8** | MSTG‑CODE‑8 | En código no administrado, la memoria es solicitada, utilizada y liberada de manera correcta. | ✓ | ✓ |
| **7.9** | MSTG‑CODE‑9 | Las funcionalidades de seguridad gratuitas de las herramientas, tales como minificación del byte-code, protección de la pila, soporte PIE y conteo automático de referencias, se encuentran activadas. | ✓ | ✓ |

<div style="page-break-after: always;">
</div>

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M7 (Mala Calidad del Código) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M7-Poor_Code_Quality>
- CWE 119 (Restricción Inapropiada de Operaciones Fuera de los Límites de un Búfer de Memoria) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 89 (Neutralización Inapropiada de Elementos Epeciales Usados en un Comando SQL) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 388 (Errores 7PK) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Restos de Código de Depuración) - <https://cwe.mitre.org/data/definitions/489.html>
