# V7: Anforderungen zu Code Qualität und Build-Einstellungen

## Zielsetzung

Das Ziel dieser Kategorie ist, sicherzustellen, dass bei der App-Entwicklung Basis-Security-Praktiken eingehalten werden und die enthaltenen Sicherheits-Funktionen des Compilers aktiviert sind.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | Die App ist signiert und mit einem gültigen Zertifikat provisioniert dessen privater Schlüssel angemessen geschützt ist. | x | x |
| **7.2** | MSTG-CODE-2 | Die App wurde im Release-Modus gebaut und mit passenden Release-Einstellungen (kein Debugging). | x | x |
| **7.3** | MSTG-CODE-3 | Debugging Symbole wurden von nativen Binärdateien entfernt. | x | x |
| **7.4** | MSTG-CODE-4 | Debugging Code und "Entwicklerüberbleibsel" (z.B. Test Code, backdoors oder versteckte Einstellungen) wurden entfernt und die App-Logdateien enthalten keine ausführlichen Fehler oder Debug-Meldungen. | x | x |
| **7.5** | MSTG-CODE-5 | Bibliotheken und Frameworks von Drittanbietern, die die App nutzt, wurden auf Schwachstellen geprüft. | x | x |
| **7.6** | MSTG-CODE-6 | Die App führt eine sichere Fehlerbehandlung durch, indem sie Exceptions abfängt und kontrolliert behandelt. | x | x |
| **7.7** | MSTG-CODE-7 | Treten in Sicherheitsfunktionen Fehler auf, lehnt die App-Fehlerbehandlung die Zugriffe standardmäßig ab. | x | x |
| **7.8** | MSTG-CODE-8 | Das Speichermanagement (Allokation und Freigabe von Speicher) erfolgt in unmanaged code auf sichere Weise. | x | x |
| **7.9** | MSTG-CODE-9 | Angebotene Sicherheitsfunktionen der Entwicklungsumgebung wie Byte-Code Minimierung, Stack-Protection, PIE-Support und automatisches Reference-Counting sind aktiviert. | x | x |

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen, um die Anforderungen aus dieser Kategorie zu überprüfen.

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
