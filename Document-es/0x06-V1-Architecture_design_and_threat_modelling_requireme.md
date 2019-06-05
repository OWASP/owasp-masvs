# V1: Requisitos de Arquitectura, Diseño y Modelado de Amenazas

## Objetivo de control

En un mundo perfecto, la seguridad sería considerada en todas las fases del desarrollo. Sin embargo, en la realidad, la seguridad es a menudo sólo considerada en una etapa tardía del desarrollo del software. Además de los controles técnicos, el MASVS requiere que existan procesos que garanticen que la seguridad se ha abordado explícitamente al planificar la arquitectura de la aplicación móvil, y que se conocen los roles funcionales y de seguridad de todos los componentes. Dado que la mayoría de las aplicaciones móviles actúan como clientes de los servicios remotos, debe garantizarse que también se apliquen las medidas de seguridad adecuadas a dichos servicios, no basta con probar la aplicación móvil de forma aislada.

La categoría V1 lista los requerimientos pertinentes a la arquitectura y al diseño de la aplicación. Debido a esto es la única categoría que no se corresponde con casos de test de la Guía de Pruebas Móviles de OWASP. Para cubrir temas tales como el modelado de amenazas, SDLC seguro, gestión de claves, los usuarios del MASVS deben consultar los respectivos proyectos de OWASP y/u otros estándares como los que se encuentran enlazados a debajo.

<div style="page-break-after: always;"></div>

## Requerimientos de Verificación de Seguridad

A continuación, se enumeran los requerimientos para MASVS-L1 y MASVS-L2.

| # | MSTG-ID | Descripción | L1 | L2 |
| --- | --- | --- | --- | --- |
| **1.1** | MSTG‑ARCH‑1 | Todos los componentes se encuentran identificados y asegurar que son necesarios. | ✓ | ✓ |
| **1.2** | MSTG‑ARCH‑2 | Los controles de seguridad nunca se aplican sólo en el cliente, sino que también en los respectivos servidores. | ✓ | ✓ |
| **1.3** | MSTG‑ARCH‑3 | Se definió una arquitectura de alto nivel para la aplicación y los servicios y se incluyeron controles de seguridad en la misma. | ✓ | ✓ |
| **1.4** | MSTG‑ARCH‑4 | Se identificó claramente la información considerada sensible en el contexto de la aplicación móvil. | ✓ | ✓ |
| **1.5** | MSTG‑ARCH‑5 | Todos los componentes de la aplicación están definidos en términos de la lógica de negocio o las funciones de seguridad que proveen. |   | ✓ |
| **1.6** | MSTG‑ARCH‑6 | Se realizó un modelado de amenazas para la aplicación móvil y los servicios en el que se definieron las mismas y sus contramedidas. |   | ✓ |
| **1.7** | MSTG‑ARCH‑7 | La implementación de los controles de seguridad se encuentra centralizada. |   | ✓ |
| **1.8** | MSTG‑ARCH‑8 | Existe una política explícita para el manejo de las claves criptográficas (si se usan) y se refuerza su ciclo de vida. Idealmente siguiendo un estándar del manejo de claves como el NIST SP 800-57. |   | ✓ |
| **1.9** | MSTG‑ARCH‑9 | Existe un mecanismo para imponer las actualizaciones de la aplicación móvil. |   | ✓ |
| **1.10** | MSTG‑ARCH‑10 | Se realizan tareas de seguridad en todo el ciclo de vida de la aplicación. |   | ✓ |

## Referencias

Para más información, ver también:

- OWASP Top 10 Móvil: M10 - Funcionalidades Extrañas: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M10-Extraneous_Functionality>
- "Cheat sheet" de la Seguridad en la Arquitectura de OWASP: <https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet>
- Modelado de Amenazas de OWASP: <https://www.owasp.org/index.php/Application_Threat_Modeling>
- "Cheat sheet" para el ciclo de desarrollo seguro de OWASP: <https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet>
- Microsoft SDL: <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57: <http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf>
