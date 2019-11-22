# V3: Requerimientos de Criptografía

## Objetivo de Control

La criptografía es un componente esencial a la hora de proteger los datos almacenados en un dispositivo móvil. También es una categoría en la que las cosas pueden ir terriblemente mal, especialmente cuando no se siguen las convenciones estándar. El propósito de estos controles es asegurarse de que la aplicación utiliza criptografía siguiendo las mejores prácticas de la industria, incluyendo:

- Uso de librerías criptográficas reconocidas y probadas;
- Configuración y elección apropiada de primitivas criptográficas;
- Uso de generadores de números aleatorios suficientemente seguros.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción | L1 | L2 |
| --- | --- | --- | --- | --- |
| **3.1** | MSTG‑CRYPTO‑1 | La aplicación no depende únicamente de criptografía simétrica cuyas claves se encuentran directamente en el código fuente de la misma.| ✓ | ✓ |
| **3.2** | MSTG‑CRYPTO‑2 | La aplicación utiliza implementaciones de criptografía probadas. | ✓ | ✓ |
| **3.3** | MSTG‑CRYPTO‑3 | La aplicación utiliza primitivas de seguridad que son apropiadas para el caso particular y su configuración y parámetros siguen las mejores prácticas de la industria. | ✓ | ✓ |
| **3.4** | MSTG‑CRYPTO‑4 | La aplicación no utiliza protocolos o algoritmos criptográficos ampliamente considerados obsoletos para su uso en seguridad. | ✓ | ✓|
| **3.5** | MSTG‑CRYPTO‑5 | La aplicación no reutiliza una misma clave criptográfica para varios propósitos. | ✓ | ✓ |
| **3.6** | MSTG‑CRYPTO‑6 | Los valores aleatorios son generados utilizando un generador de números aleatorios suficientemente seguro. | ✓ | ✓ |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Para más información, ver también:

- OWASP Top 10 Móvil: M5 (Criptografía Insuficiente) - <https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
