# Evaluación y Certificación

## Postura de OWASP sobre las Certificaciones MASVS y Marcas de Confianza

OWASP, como una organización sin fines de lucro e independiente de toda empresa, no certifica a ningún proveedor, verificador o software.

Todas estas afirmaciones de garantía, marcas de confianza o certificaciones no son oficialmente examinadas, registradas o certificadas por OWASP, por lo que una organización que confía en tal opinión debe tener la precaución de la confianza depositada en cualquier tercero o marca de confianza que alega la certificación (M)ASVS.

Esto no debe impedir que las organizaciones ofrezcan tales servicios de seguridad, siempre que no reclamen la certificación oficial OWASP.

## Guía para certificar aplicaciones móviles

La forma recomendada de verificar la conformidad de una aplicación móvil con el MASVS es realizar una revisión de "libro abierto", lo que significa que los verificadores tienen acceso a recursos claves como arquitectos y desarrolladores de la aplicación, documentación del proyecto, código fuente y acceso autenticado a los terminales, incluyendo acceso a al menos una cuenta de usuario para cada función.

Es importante tener en cuenta que el MASVS sólo cubre la seguridad de la aplicación móvil (en el dispositivo del cliente) y la comunicación de red entre la aplicación y su/s punto/s final/es remoto/s, así como algunos requerimientos básicos y genéricos relacionados con la autenticación del usuario y la gestión de sesiones. No contiene requerimientos específicos para los servicios remotos (por ejemplo, servicios web) asociados a la aplicación, salvo para un conjunto limitado de requerimientos genéricos relacionados con la autenticación y la gestión de sesiones. No obstante, MASVS V1 especifica que los servicios remotos deben ser cubiertos por el modelo general de amenazas, y ser verificados contra los estándares apropiados, como el OWASP ASVS.

Una organización que certifica debe incluir en todos los informes el alcance de la verificación (particularmente si un componente clave está fuera del alcance), un resumen de los resultados de la verificación, incluyendo las pruebas aprobadas y fallidas, con instrucciones claras de cómo resolver las pruebas fallidas. Mantener documentos de trabajo detallados, capturas de pantalla o vídeos, guiones para explotar de forma fiable y repetida un problema y registros electrónicos de las pruebas, como los registros de un proxy y notas asociadas, se consideran práctica estándar de la industria. No basta con simplemente ejecutar una herramienta y presentar un informe sobre los fallos; esto no aporta suficientes evidencias de que se han analizado y probado a fondo todos los aspectos a nivel de una certificación. En caso de controversia, debe haber pruebas suficientes para demostrar que todos los requerimientos verificados han sido efectivamente probados.

### Usando la Guía de Pruebas de Seguridad Móvil de OWASP (MSTG)

La OWASP MSTG es una guía para la verificación de la seguridad de las aplicaciones móviles. Describe los procedimientos técnicos para verificar los requerimientos listados en el MASVS. La MSTG incluye una lista de casos de prueba, cada uno de los cuales se corresponde con un requerimiento del MASVS. Mientras que los requerimientos del MASVS son de alto nivel y genéricos, la MSTG proporciona recomendaciones detalladas y procedimientos de verificación para cada uno de los sistemas operativos móviles.

### El papel de las herramientas de pruebas de seguridad automatizadas

Se recomienda el uso de escáneres de código fuente y herramientas de verificación de caja negra para aumentar la eficiencia siempre que sea posible. Sin embargo, no es posible completar la verificación MASVS utilizando únicamente herramientas automatizadas: cada aplicación móvil es diferente, y la comprensión de la arquitectura general, la lógica de negocio y los problemas específicos de las tecnologías y plataformas que se utilizan es un requerimiento obligatorio para verificar la seguridad de la aplicación.

## Otros Usos

### Como guía detallada para una arquitectura segura

Uno de los usos más comunes del Estándar de Verificación de Seguridad de Aplicaciones Móviles es como recurso para los arquitectos de seguridad. Los dos principales esquemas de seguridad en la arquitectura, SABSA o TOGAF, carecen de una gran cantidad de información necesaria para completar las revisiones de seguridad en la arquitectura de las aplicaciones móviles. El MASVS se puede utilizar para llenar esos vacíos permitiendo a los arquitectos elegir mejores controles para los problemas comunes de seguridad en las aplicaciones móviles.

### Como reemplazo de las listas de verificación de codificación segura estándar

Muchas organizaciones se pueden beneficiar de la adopción del MASVS, eligiendo uno de los dos niveles, o bifurcando el MASVS y cambiando lo que se requiere para el nivel de riesgo de cada aplicación de una manera específica al negocio. Fomentamos este tipo de bifurcación siempre y cuando se mantenga la trazabilidad, de modo que si una aplicación cumple el requerimiento 4.1, lo mismo ocurre en las bifurcaciones del estándar cuando éste evoluciona.

### Como base para las metodologías de pruebas de seguridad

Una buena metodología de pruebas de seguridad para aplicaciones móviles debe cubrir todos los requerimientos listados en el MASVS. La Guía de Pruebas de Seguridad Móvil de OWASP (MSTG) describe los casos de prueba de caja negra y caja blanca para cada requerimiento de verificación.

### Como guía para la automatización de pruebas unitarias y de integración

El MASVS está diseñado para ser altamente verificable, con la única excepción de los requerimientos de la arquitectura. Las pruebas unitarias, de integración y de aceptación automatizadas, basadas en los requerimientos del MASVS, pueden integrarse en el ciclo de vida de un desarrollo continuo. Esto no sólo aumenta la conciencia de seguridad de los desarrolladores, sino que también mejora la calidad general de las aplicaciones desarrolladas, y reduce la cantidad de hallazgos durante las pruebas de seguridad en la fase previa al lanzamiento.

### Para el entrenamiento en desarrollo seguro

El MASVS también se puede utilizar para definir características de aplicaciones móviles seguras. Muchos cursos de "codificación segura" son simplemente cursos de hacking ético con algunos consejos de programación segura. Esto no ayuda a los desarrolladores. En su lugar, los cursos de desarrollo seguro móvil pueden utilizar el MASVS, con un fuerte enfoque en los controles proactivos documentados en el MASVS, en lugar de, por ejemplo, el Top 10 móvil de problemas de seguridad del código de OWASP.
