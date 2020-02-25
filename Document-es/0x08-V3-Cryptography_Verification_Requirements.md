# V3: Requerimientos de Criptografía

## Objetivo de Control

La criptografía es un componente esencial a la hora de proteger los datos almacenados en un dispositivo móvil. También es una categoría en la que las cosas pueden ir terriblemente mal, especialmente cuando no se siguen las convenciones estándar. El propósito de estos controles es asegurarse de que la aplicación utiliza criptografía siguiendo las mejores prácticas de la industria, incluyendo:

- Uso de librerías criptográficas reconocidas y probadas;
- Configuración y elección apropiada de primitivas criptográficas;
- Uso de generadores de números aleatorios suficientemente seguros.

## Requerimientos de Verificación de Seguridad

| # | MSTG-ID | Descripción | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | La aplicación no depende únicamente de criptografía simétrica cuyas claves se encuentran directamente en el código fuente de la misma.| ✓ | ✓ |
| **3.2** | MSTG-CRYPTO-2 | La aplicación utiliza implementaciones de criptografía probadas. | ✓ | ✓ |
| **3.3** | MSTG-CRYPTO-3 | La aplicación utiliza primitivas de seguridad que son apropiadas para el caso particular y su configuración y parámetros siguen las mejores prácticas de la industria. | ✓ | ✓ |
| **3.4** | MSTG-CRYPTO-4 | La aplicación no utiliza protocolos o algoritmos criptográficos ampliamente considerados obsoletos para su uso en seguridad. | ✓ | ✓ |
| **3.5** | MSTG-CRYPTO-5 | La aplicación no reutiliza una misma clave criptográfica para varios propósitos. | ✓ | ✓ |
| **3.6** | MSTG-CRYPTO-6 | Los valores aleatorios son generados utilizando un generador de números aleatorios suficientemente seguro. | ✓ | ✓ |

## Referencias

La Guía de Pruebas de Seguridad Móvil de OWASP proporciona instrucciones detalladas para verificar los requisitos listados en esta sección.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Para más información, ver también:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
