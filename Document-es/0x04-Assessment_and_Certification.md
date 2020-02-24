# Evaluación y Certificación

## Posición de OWASP en cuanto a Certificaciones MASVS y Marcas de Confianza

OWASP, como una organización sin ánimo de lucro e independiente de toda empresa, no certifica a ningún proveedor, verificador o software.

Ninguna certificación, marca de garantía o confianza actualmente existente ha sido examinada, registrada o certificada oficialmente por OWASP.
Por tanto, una organización que confía en tal opinión debe tener la precaución de la confianza depositada en cualquier tercero o marca de confianza que alega la certificación (M)ASVS.

Esto no debe impedir que las organizaciones ofrezcan tales servicios de seguridad, siempre que no reclamen la certificación oficial OWASP.

## Guía para Certificar Aplicaciones Móviles

La forma recomendada de verificar la conformidad de una aplicación móvil con el MASVS es realizar una revisión de "libro abierto", lo que significa que los verificadores tienen acceso a recursos claves como arquitectos y desarrolladores de la aplicación, documentación del proyecto, código fuente y acceso autenticado a los terminales, incluyendo acceso a al menos una cuenta de usuario para cada función.

Es importante tener en cuenta que el MASVS sólo cubre la seguridad de la aplicación móvil (en el dispositivo del cliente) y la comunicación de red entre la aplicación y sus puntos remotos, así como algunos requerimientos básicos y genéricos relacionados con la autenticación del usuario y la gestión de sesiones. No contiene requerimientos específicos para los servicios remotos (por ejemplo, servicios web) asociados a la aplicación, salvo para un conjunto limitado de requerimientos genéricos relacionados con la autenticación y la gestión de sesiones. No obstante, MASVS-V1 especifica que los servicios remotos deben ser cubiertos por el modelo general de amenazas, y ser verificados contra los estándares apropiados, tales como el OWASP ASVS.

Los informes creados por organismos de certificación deberían incluir los siguientes elementos considerados como práctica estándar de la industria:

- El alcance de la verificación, especialmente cuando un componente clave está fuera de dicho alcance.
- Un resumen de los resultados de la verificación, incluyendo las pruebas superadas y fallidas, con instrucciones claras de cómo resolver las pruebas fallidas.
- Mantener documentos de trabajo detallados, incluyendo capturas de pantalla o vídeos.
- Guiones para explotar de forma fiable y repetida un problema.
- Registros electrónicos de las pruebas, como los _logs_ de un proxy y cualquier nota asociada.

Nòtese que no basta con simplemente ejecutar una herramienta y presentar un informe sobre los fallos; esto no aporta suficientes evidencias de que se han analizado y probado a fondo todos los aspectos a nivel de una certificación. En caso de controversia, debe haber pruebas suficientes para demostrar que todos los requerimientos verificados han sido efectivamente probados.

### Usando la Guía de Pruebas de Seguridad Móvil de OWASP (MSTG)

La OWASP MSTG es una guía para la verificación de la seguridad de las aplicaciones móviles. Describe los procedimientos técnicos para verificar los requerimientos listados en el MASVS. La MSTG incluye una lista de casos de prueba, cada uno de los cuales se corresponde con un requerimiento del MASVS. Mientras que los requerimientos del MASVS son de alto nivel y genéricos, la MSTG proporciona recomendaciones detalladas y procedimientos de verificación para cada uno de los sistemas operativos móviles.

### El Papel de las Herramientas de Pruebas de Seguridad Automatizadas

Se recomienda el uso de escáneres de código fuente y herramientas de auditoría de tipo _black-box_ para aumentar la eficiencia siempre que sea posible. Sin embargo, no es posible completar la verificación MASVS utilizando únicamente herramientas automatizadas: cada aplicación móvil es diferente. Por tanto, la comprensión de la arquitectura general, la lógica de negocio y los problemas específicos de las tecnologías y plataformas que se utilizan es un requerimiento obligatorio para verificar la seguridad de la aplicación.

## Otros Usos

### Como Guía Detallada para una Arquitectura Segura

Uno de los usos más comunes del MASVS es como guía para los arquitectos de seguridad. Los dos principales esquemas de seguridad en la arquitectura, SABSA o TOGAF, carecen de una gran cantidad de información necesaria para completar las revisiones de seguridad en la arquitectura de las aplicaciones móviles. El MASVS se puede utilizar para llenar esos vacíos permitiendo a los arquitectos elegir los mejores controles para los problemas comunes de seguridad en las aplicaciones móviles.

### Como Reemplazo de las _Checklists_ de Desarrollo Seguro de Aplicaciones Móviles

Muchas organizaciones pueden beneficiarse de la adopción del MASVS simplemente eligiendo uno de los niveles, o haciendo su propio _fork_ del MASVS y cambiando lo que se requiera específicamente en el contexto y el nivel de riesgo de cada aplicación. Fomentamos este tipo de _forks_ siempre y cuando se mantenga la trazabilidad, de modo que si una aplicación cumple con un requerimiento del MASVS original, lo mismo ocurre en los _forks_ del estándar cuando éste evoluciona.

### Como Base para las Metodologías de Pruebas de Seguridad

Una buena metodología de pruebas de seguridad para aplicaciones móviles debe cubrir todos los requerimientos listados en el MASVS. La OWASP MSTG describe los casos de prueba de tipo _black-box_ y _white-box_ para cada requerimiento de verificación.

### Como Guía para la Automatización de Pruebas Unitarias y de Integración

El MASVS está diseñado para ser altamente verificable, con la única excepción de los requerimientos de arquitectura. Las pruebas unitarias, de integración y de aceptación automatizadas, basadas en los requerimientos del MASVS, pueden integrarse en el ciclo de vida de desarrollo de software (SDLC, por sus siglas en inglés). Esto no sólo aumenta la conciencia de seguridad de los desarrolladores, sino que también mejora la calidad general de las aplicaciones desarrolladas, y reduce la cantidad de hallazgos durante las pruebas de seguridad en la fase previa al _release_.

### Para el Entrenamiento en Desarrollo Seguro

El MASVS también se puede utilizar para definir características de aplicaciones móviles seguras. Muchos cursos de "desarrollo segura" son simplemente cursos de _hacking_ ético con algunos consejos de programación segura. Esto no ayuda a los desarrolladores. En su lugar, los cursos de desarrollo seguro de aplicaciones móviles pueden utilizar el MASVS, con un fuerte enfoque en los controles proactivos documentados en el MASVS, en lugar de basarse simplemente en, por ejemplo, el "Top 10 de problemas de seguridad en el desarrollo software".
