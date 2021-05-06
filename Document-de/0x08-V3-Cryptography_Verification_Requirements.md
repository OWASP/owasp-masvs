# V3: Anforderungen an Kryptographie

## Zielsetzung

Kryptografie ist ein wesentlicher Eckpfeiler zum Schutz von Daten, die auf mobilen Geräten gespeichert werden. Es ist aber auch eine Kategorie, bei der vieles falsch gemacht werden kann, besonders wenn man keine Standard-Konventionen einhält. Die Kategorie soll sicherstellen, dass eine überprüfte App Kryptografie-Best-Practices nach dem Stand der Technik nutzt:

- Nutzung bewährter Krypto-Bibliotheken,
- Richtige Auswahl und Konfiguration kryptografischer Primitive,
- Nutzung eines geeigneten Zufallszahlengenerators, wenn kryptografisch sichere Zufallszahlen erforderlich sind.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | Verschlüsselung in der App basiert nicht nur auf symmetrischer Kryptografie mit hart-codierten Schlüsseln.| ✓ | ✓ |
| **3.2** | MSTG-CRYPTO-2 | Die App nutzt bewährte Implementierungen zur Umsetzung kryptografischer Primitive. | ✓ | ✓ |
| **3.3** | MSTG-CRYPTO-3 | Die App nutzt kryptografische Primitive passend zum spezifischen Anwendungsfall, konfiguriert nach Best-Practice Vorgaben dem Stand der Technik entsprechend. | ✓ | ✓ |
| **3.4** | MSTG-CRYPTO-4 | Die App nutzt keine kryptografischen Protokolle oder Algorithmen die allgemein als veraltet und unsicher gelten. | ✓ | ✓ |
| **3.5** | MSTG-CRYPTO-5 | Die App verwendet einen kryptografischen Schlüssel für genau einen Zweck und nicht für mehrere Zwecke. | ✓ | ✓ |
| **3.6** | MSTG-CRYPTO-6 | Alle Zufallswerte werden über einen ausreichend sicheren kryptografischen Zufallszahlengenerator erzeugt. | ✓ | ✓ |

<!-- \pagebreak -->

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen, um die Anforderungen aus dieser Kategorie zu überprüfen.

- Android: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
