# V6: Requerimientos de Interacción con la Plataforma

## Objetivo de Control

Estos controles revisan que se utilicen las APIs de la plataforma y componentes estándar de una manera segura. Además, se cubre la comunicación entre aplicaciones (IPC).

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción || L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | La aplicación requiere la cantidad de permisos mínimamente necesaria. | ✓ | ✓ |
| **6.2** | MSTG‑PLATFORM‑2 | Todo dato ingresado por el usuario o cualquier fuente externa debe ser validado y, si es necesario, saneado. Esto incluye información recibida por la UI o mecanismos IPC como los Intents, URLs y datos provenientes de la red. | ✓ | ✓ |
| **6.3** | MSTG‑PLATFORM‑3 | La aplicación no expone ninguna funcionalidad sensible a través esquemas de URL salvo que dichos mecanismos estén debidamente protegidos. | ✓ | ✓ |
| **6.4** | MSTG‑PLATFORM‑4 | La aplicación no expone ninguna funcionalidad sensible a través de mecanismos IPC salvo que dichos mecanismos estén debidamente protegidos. | ✓ | ✓ |
| **6.5** | MSTG‑PLATFORM‑5 | JavaScript se encuentra deshabilitado en los WebViews salvo que sea necesario. | ✓ | ✓ |
| **6.6** | MSTG‑PLATFORM‑6 | Las WebViews se configuran para permitir el mínimo de los esquemas (idealmente, sólo https). Esquemas peligrosos como file, tel y app-id están deshabilitados. | ✓ | ✓ |
| **6.7** | MSTG‑PLATFORM‑7 | Si objetos nativos son expuestos en WebViews, debe verificarse que cualquier componente JavaScript se carga exclusivamente desde el contenedor de la aplicación. | ✓ | ✓ |
| **6.8** | MSTG‑PLATFORM‑8 | La serialización de objetos, si se realiza, debe implementarse utilizando API seguras. | ✓ | ✓ |
| **6.9** | MSTG‑PLATFORM‑9 | La aplicación se protege contra ataques de tipo screen overlay. (sólo Android) |  | ✓ |
| **6.10** | MSTG‑PLATFORM‑10 | La caché, el almacenamiento y los recursos cargados (JavaScript, etc.) de las WebViews deben de borrarse antes de destruir la WebView. |  | ✓ |
| **6.11** | MSTG‑PLATFORM‑11 | Verificar que la aplicación impide el uso de teclados de terceros siempre que se introduzca información sensible. |  | ✓ |

<div style="page-break-after: always;">
</div>

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M1 (Uso Inapropiado de la Plataforma) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE 20 (Validación Inapropiada de Inputs de Usuario) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 749 (Exposición de Métodos o Funciones Pelogrosas) - <https://cwe.mitre.org/data/definitions/749.html>
