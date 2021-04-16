# V8: Requerimientos de Resistencia ante la Ingeniería Inversa

## Objetivo de Control

En esta sección se cubren protecciones recomendadas para aplicaciones que maneja o brindan acceso a información o funcionalidades sensibles. La falta de estos controles no generan vulnerabilidades - sino que, están pensados para incrementar la resistencia contra la ingeniería inversa de la aplicación, dificultándole al adversario el acceso a los datos o el entendimiento del modo de ejecución de la aplicación.

 Los controles de esta sección deben aplicarse según sea necesario, basándose en una evaluación de los riesgos causados por la manipulación no autorizada de la aplicación y/o la ingeniería inversa del código. Sugerimos consultar el documento de OWASP "Ingeniería Inversa - Amenazas de la Ingeniería Inversa de OWASP" (vea las referencias a continuación) para obtener una lista de los riesgos del negocio, así como las amenazas técnicas asociadas.

Para que cualquiera de los controles de la lista siguiente sea eficaz, la aplicación debe cumplir al menos todos los requerimientos del nivel MASVS-L1 (es decir, deben existir sólidos controles de seguridad), así como todos los requerimientos de números más bajos en V8. Por ejemplo, los controles de ofuscación listados en la sección "impedir la comprensión" deben combinarse con el "impedir el análisis dinámico y la manipulación" y la "atadura al dispositivo".

**Tenga en cuenta que los controles de software nunca deben utilizarse como reemplazo de los controles de seguridad. Los controles listados en MASVR-R buscan añadir controles de protección adicionales y específicos contra las amenazas a las aplicaciones que también cumplen con los requerimientos de seguridad del MASVS.**

Se aplican las siguientes consideraciones:

1. Debe definirse un modelo de amenaza que defienda claramente las amenazas del lado del cliente. Además, debe especificarse el grado de protección que debe proporcionar el sistema. Por ejemplo, un objetivo podría ser obligar a los autores de malware dirigido que quieren usar la aplicación a que tengan que invertir importantes esfuerzos para realizar la ingeniería inversa.

2. El modelo de amenaza debe ser sensato. Por ejemplo, ocultar una clave criptográfica en una implementación de caja blanca es un problema si el atacante puede simplemente utilizar la aplicación como un todo.

3. La eficiencia de la protección siempre debe ser verificada por un experto con experiencia en el testeo de tipos particulares de anti-manipulación y ofuscación utilizados (ver también los capítulos "ingeniería inversa" y "evaluación de protecciones del software" en la Guía de Pruebas de Seguridad Móvil).

<!-- \pagebreak -->

### Impedir el Análisis Dinámico y la Manipulación

| # | MSTG-ID | Descripción | R |
| -- | ----------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | La aplicación detecta y responde a la presencia de un dispositivo rooteado, ya sea alertando al usuario o finalizando la ejecución de la aplicación. | ✓ |
| **8.2** | MSTG-RESILIENCE-2 | La aplicación impide la depuración o detecta y responde a la misma. Se deben cubrir todos los protocolos de depuración. | ✓ |
| **8.3** | MSTG-RESILIENCE-3 | La aplicación detecta y responde a cualquier modificación de ejecutables y datos críticos de la propia aplicación. | ✓ |
| **8.4** | MSTG-RESILIENCE-4 | La aplicación detecta la presencia de herramientas de ingeniería inversa o frameworks comunmente utilizados. | ✓ |
| **8.5** | MSTG-RESILIENCE-5 | La aplicación detecta y responde a ser ejecutada en un emulador.  | ✓ |
| **8.6** | MSTG-RESILIENCE-6 | La aplicación detecta y responde ante modificaciones de código o datos en su propio espacio de memoria. | ✓ |
| **8.7** | MSTG-RESILIENCE-7 | La aplicación implementa múltiples mecanismos de detección para los puntos del 8.1 al 8.6. Nótese que, a mayor cantidad y diversidad de mecanismos usados, mayor será la resistencia. | ✓ |
| **8.8** | MSTG-RESILIENCE-8 | Los mecanismos de detección provocan distintos tipos de respuestas, incluyendo respuestas retardadas y silenciosas. | ✓ |
| **8.9** | MSTG-RESILIENCE-9 | La ofuscación se aplica a las defensas del programa, lo que a su vez impide la desofuscación mediante análisis dinámico. | ✓ |

### Asociación del Dispositivo

| # | MSTG-ID | Descripción | R |
| -- | ----------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | La aplicación implementa un “enlace al dispositivo” utilizando una huella del dispositivo derivado de varias propiedades únicas al mismo. | ✓ |

<!-- \pagebreak -->

### Impedir la Comprensión

| # | MSTG-ID | Descripción | R |
| -- | ----------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | Todos los archivos ejecutables y bibliotecas correspondientes a la aplicación se encuentran cifrados, o bien los segmentos importantes de código se encuentran cifrados o "empaquetados" (packed). De este modo cualquier análisis estático trivial no revelará código o datos importantes. | ✓ |
| **8.12** | MSTG-RESILIENCE-12 | Si el objetivo de la ofuscación es proteger código propietario, debe utilizarse un esquema de ofuscación apropiado para la tarea particular y robusto contra métodos de desofuscación manual y automatizada, considerando la investigación actual publicada. La eficacia del esquema de ofuscación debe verificarse mediante pruebas manuales. Nótese que, siempre que sea posible, las características de aislamiento basadas en hardware son preferibles a la ofuscación. | ✓ |

### Impedir el Eavesdropping

| # | MSTG-ID | Descripción | R |
| -- | ----------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | A modo de defensa en profundidad, además de incluir un refuerzo (hardening) sólido de la comunicación, puede implementarse el cifrado de datos (payloads) a nivel de aplicación como medida adicional contra ataques de eavesdropping. | ✓ |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M8 (Modificación de Código) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Top 10 Móvil: M9 (Ingeniería Inversa) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- Amenazas de Ingeniería Inversa (OWASP) - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- Ingeniería Inversa y Prevención de Modificación de Código (OWASP) - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
