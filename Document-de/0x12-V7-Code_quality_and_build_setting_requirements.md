# V7: Anforderungen zu Code Qualität und Build-Einstellungen

## Zielsetzung

Das Ziel dieser Kategorie ist, sicherzustellen, dass bei der App-Entwicklung Basis-Security-Praktiken eingehalten werden und die enthaltenen Sicherheits-Funktionen des Compilers aktiviert sind.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| --- | --- | --- | --- | --- |
| **7.1** | MSTG‑CODE‑1 | Die App ist signiert und mit einem gültigen Zertifikat provisioniert dessen privater Schlüssel angemessen geschützt ist. | ✓ | ✓ |
| **7.2** | MSTG‑CODE‑2 | Die App wurde im Release-Modus gebaut und mit passenden Release-Einstellungen (kein Debugging). | ✓ | ✓ |
| **7.3** | MSTG‑CODE‑3 | Debugging Symbole wurden von nativen Binärdateien entfernt. | ✓ | ✓ |
| **7.4** | MSTG‑CODE‑4 | Debugging Code wurde entfernt und die App-Logdateien enthalten keine ausführlichen Fehler oder Debug-Meldungen. | ✓ | ✓ |
| **7.5** | MSTG‑CODE‑5 | Bibliotheken und Frameworks von Drittanbietern die die App nutzt wurden auf Schwachstellen geprüft. | ✓ | ✓ |
| **7.6** | MSTG‑CODE‑6 | Die App führt eine sichere Fehlerbehandlung durch indem sie Exceptions abfängt und kontrolliert behandelt.| ✓ | ✓ |
| **7.7** | MSTG‑CODE‑7 | Treten in Sicherheitsfunktionen Fehler auf lehnt die App-Fehlerbehandlung die Zugriffe standardmäßig ab. | ✓ | ✓ |
| **7.8** | MSTG‑CODE‑8 | Das Speichermanagement (Allokation und Freigabe von Speicher) erfolgt in unmanaged code auf sichere Weise. | ✓ | ✓ |
| **7.9** | MSTG‑CODE‑9 | Angebotene Sicherheitsfunktionen der Entwicklungsumgebung wie Byte-Code Minimierung, Stack-Protection, PIE-Support und automatisches Reference-Counting sind aktiviert. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- Für Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- Für iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M7 - Poor Code Quality: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M7-Poor_Code_Quality>
- CWE: <https://cwe.mitre.org/data/definitions/119.html>
- CWE: <https://cwe.mitre.org/data/definitions/89.html>
- CWE: <https://cwe.mitre.org/data/definitions/388.html>
- CWE: <https://cwe.mitre.org/data/definitions/489.html>
