# V3: Anforderungen an Kryptographie

## Zielsetzung

Kryptographie ist eine wesentlicher Eckpfeiler zum Schutz von Daten, die auf mobilen Geräten gespeichert werden. Es ist aber auch eine Kategorie bei der vieles falsch gemacht werden kann, besonders wenn man keine Standard-Konventionen einhält. Die Kategorie soll sicherstellen, dass eine überprüfte App Kryptographie-Best-Practices nach dem Stand der Technik nutzt:

- Nutzung bewährter Krypto-Bibliotheken,
- Richtige Auswahl und Konfiguration kryptographischer Primitive,
- Nutzung eines geeigneten Zufallszahlengenerators wenn kryptographisch sichere Zufallszahlen erforderlich sind.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| --- | --- | --- | --- | --- |
| **3.1** | MSTG‑CRYPTO‑1 | Verschlüsselung in der App basiert nicht nur auf symmetrischer Kryptographie mit hart-codierten Schlüsseln.| ✓ | ✓ |
| **3.2** | MSTG‑CRYPTO‑2 | Die App nutzt bewährte Implementierungen zur Umsetzung kryptographischer Primitive. | ✓ | ✓ |
| **3.3** | MSTG‑CRYPTO‑3 | Die App nutzt kryptographische Primitive passend zum spezifischen Anwendungsfall, konfiguriert nach Best-Practice Vorgaben dem Stand der Technik entsprechend. | ✓ | ✓|
| **3.4** | MSTG‑CRYPTO‑4 | Die App nutzt keine kryptographischen Protokolle oder Algorithmen die allgemein als veraltet und unsicher gelten. | ✓ | ✓|
| **3.5** | MSTG‑CRYPTO‑5 | Die App verwendet einen kryptographischen Schlüssel für genau einen Zweck und nicht für mehrere Zwecke. | ✓ | ✓ |
| **3.6** | MSTG‑CRYPTO‑6 | Alle Zufallswerte werden über einen ausreichend sicheren kryptographischen Zufallszahlengenerator erzeugt. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- Für Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- Für iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M5 - Insufficient Cryptography: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography>
- CWE: <https://cwe.mitre.org/data/definitions/310.html>
