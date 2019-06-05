# V6: Requerimientos de Interacción con la Plataforma

## Objetivo de control

Estos controles revisan que se utilicen las APIs de la plataforma y componentes estándar de una manera segura. Además, se cubre la comunicación entre aplicaciones (IPC).

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción || L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | La aplicación requiere la mínima cantidad de permisos. | ✓ | ✓ |
| **6.2** | MSTG‑PLATFORM‑2 | Toda entrada del usuario y fuentes externas es validada y si es necesario sanitizada. Esto incluye información recibida por la UI, y mecanismo IPC como los intents, URLs y fuentes de la red. | ✓ | ✓ |
| **6.3** | MSTG‑PLATFORM‑3 | La aplicación no exporta funcionalidades sensibles vía esquemas de URL, salvo que dichos mecanismos estén debidamente protegidos. | ✓ | ✓ |
| **6.4** | MSTG‑PLATFORM‑4 | La aplicación no exporta funcionalidades sensibles a través de mecanismos IPC salvo que los mecanismos estén debidamente protegidos. | ✓ | ✓ |
| **6.5** | MSTG‑PLATFORM‑5 | JavaScript se encuentra deshabilitado en los WebViews salvo que sea necesario. | ✓ | ✓ |
| **6.6** | MSTG‑PLATFORM‑6 | Los WebViews se encuentran configurados para permitir el mínimo de los manejadores (idealmente, solo https). Manejadores peligrosos como file, tel y app-id  se encuentran deshabilitados. | ✓ | ✓ |
| **6.7** | MSTG‑PLATFORM‑7 | Si objetos nativos son expuestos en WebViews, verificar que solo se cargan JavaScripts contenidos del paquete de la aplicación. | ✓ | ✓ |
| **6.8** | MSTG‑PLATFORM‑8 | Serialización de objetos, si se realiza, se implementa utilizando API seguras. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M1 - Uso inapropiado de la Plataforma: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE: <https://cwe.mitre.org/data/definitions/20.html>
- CWE: <https://cwe.mitre.org/data/definitions/749.html>
