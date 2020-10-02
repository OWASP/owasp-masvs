# V6: Anforderungen zur Plattform-Interaktion

## Zielsetzung

Die Anforderungen aus dieser Kategorie sollen sicherstellen, dass Plattform-Komponenten und Standard-Komponenten von der App auf sichere Weise genutzt werden. Zusätzlich decken die Anforderungen auch die Kommunikation (IPC) zwischen Apps ab.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | Die App fordert vom Nutzer nur die unbedingt erforderlichen App-Berechtigungen. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | Alle Eingaben von externen Quellen und dem Nutzer werden validiert und falls erforderlich bereinigt. Dazu gehören Daten aus der GUI, IPC Mechanismen wie Intents oder spezifische URL-Schemas und Netzwerk-Daten. | ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | Die App bietet keine sensible Funktionalität über App-eigene URL-Schemas an - wenn doch, ist der Mechanismus angemessen geschützt.  | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | Die App bietet keine sensible Funktionalität über Interprozesskommunikation (IPC) an - wenn doch, ist der Mechanismus angemessen geschützt. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | JavaScript ist in WebViews deaktiviert wenn es nicht unbedingt erforderlich ist. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | WebViews sind so konfiguriert, dass nur die minimal nötigen Protokoll-Handler erlaubt sind (Idealerweise nur HTTPS). Potentiell gefährliche Handler wie file, tel und app-id sind deaktiviert. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | Wenn eine WebView über Javascript Zugriff auf native Methoden einer App bekommt, ist sichergestellt, dass die WebView nur vorgegebenes Javascript aus der App rendert und kein Javascript aus externen Quellen.  | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | Objektserialisierung wird, falls vorhanden, über eine sichere Serialisierungs-API implementiert. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | Die App verwendet Mechanismen um sich vor Screen Overlay Angriffen zu schützen (nur Android). |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | Cache, Speicher und geladene Ressourcen (JavaScript usw.) eines WebViews sollten gelöscht werden bevor der WebView geschlossen wird.  |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | Die App sollte verhindern das 3rd Party Tastaturen verwendet werden, wenn sensible Daten eingegeben werden (nur iOS). |  | ✓ |

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
