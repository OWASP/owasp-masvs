# V5: Anforderungen an Netzwerkkommunikation

## Zielsetzung

Der Zweck dieser Kategorie ist es die Vertraulichkeit und Integrität übertragener Daten zwischen mobiler App und entferntem Server zu gewährleisten. Dazu muss eine mobile App einen sicheren, verschlüsselten Kanal zur Netzwerkkommunikation unter Nutzung des TLS-Protokolls mit adäquaten TLS-Einstellungen aufbauen. Level 2 benennt zusätzliche Defense-in-Depth Maßnahmen wie SSL-Pinning.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Daten werden zur Netzwerkkommunikation innerhalb der App durchgängig mit TLS verschlüsselt. | ✓ | ✓ |
| **5.2** | MSTG-NETWORK-2 | Die TLS-Einstellungen entsprechen aktuellen Best Practices, oder erfüllen die Best Practices so gut wie möglich falls das mobile Betriebssystem die Empfehlung nicht unterstützt. | ✓ | ✓ |
| **5.3** | MSTG-NETWORK-3 | Die App überprüft das X.509-Zertifikat des Servers beim TLS-Handshake. Die App akzeptiert nur Zertifikate die von einer vertrauenswürdigen Zertifizierungsstelle signiert wurden.  | ✓ | ✓ |
| **5.4** | MSTG-NETWORK-4 | Die App nutzt entweder ihren eigenen Zertifikatspeicher oder nutzt Public Key-/ Zertifikats-Pinning und akzeptiert deshalb keine Verbindungen zu Endpunkten die andere Zertifikate/Schlüssel präsentieren - selbst wenn die Zertifikate von einer vertrauenswürdigen Zertifizierungstelle signiert sind. |   | ✓ |
| **5.5** | MSTG-NETWORK-5 | Die App nutzt keine unsicheren Kommunikationskanäle wie Email oder SMS für kritische Operationen wie Konten-Registrierung oder Konten-Reaktivierung. |  | ✓ |
| **5.6** | MSTG-NETWORK-6 | Die App nutzt aktuelle Bibliotheken zum Aufbau von sicheren Kommunikationsverbindungen. |  | ✓ |

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- General: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M3 (Insecure Communication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Improper Certificate Validation) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Improper Following of a Certificate's Chain of Trust) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Improper Validation of Certificate with Host Mismatch) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Improper Validation of Certificate Expiration) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Cleartext Transmission of Sensitive Information) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Use of RSA Algorithm without OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Improper Verification of Source of a Communication Channel) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Incorrectly Specified Destination in a Communication Channel) - <https://cwe.mitre.org/data/definitions/941.html>
