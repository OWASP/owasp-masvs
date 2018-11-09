# V6: Anforderungen zur Plattform-Interaktion

## Zielsetzung

Die Anforderungen aus dieser Kategorie sollen sicherstellen, dass Plattform-Komponenten und Standard-Komponenten von der App auf sichere Weise genutzt werden. Zusätzlich decken die Anforderungen auch die Kommunikation (IPC) zwischen Apps ab.

## Anforderungen

| # | Beschreibung | L1 | L2 |
| --- | --- | --- | --- |
| **6.1** | Die App fordert vom Nutzer nur die unbedingt erforderlichen App-Berechtigungen. | ✓ | ✓ |
| **6.2** | Alle Eingaben von externen Quellen und dem Nutzer werden validiert und falls erforderlich bereinigt. Dazu gehören Daten aus der GUI, IPC Mechanismen wie Intents oder spezifische URL-Schemas und Netzwerk-Daten. | ✓ | ✓ |
| **6.3** | Die App bietet keine sensible Funktionalität über App-eigene URL-Schemas - wenn doch, ist der Mechanismus angemessen geschützt.  | ✓ | ✓ |
| **6.4** | Die App bietet keine sensible Funktionalität über Interprozesskommunikation (IPC) an - wenn doch, ist der Mechanismus angemessen geschützt. | ✓ | ✓ |
| **6.5** | JavaScript ist in WebViews deaktiviert wenn es nicht unbedingt erforderlich ist. | ✓ | ✓ |
| **6.6** | WebViews sind so konfiguriert, dass nur die minimal nötigen Protokoll-Handler erlaubt sind (Idealerweise nur https). Potentiell gefährliche Handler wie file, tel und app-id sind deaktiviert. | ✓ | ✓ |
| **6.7** | Wenn eine WebView über Javascript Zugriff auf native Methoden einer App bekommt, ist sichergestellt, dass die WebView nur vorgegebenes Javascript aus der App rendert und kein Javascript aus externen Quellen.  | ✓ | ✓ |
| **6.8** | Objektserialisierung wird, falls vorhanden, über eine sichere Serialisierungs-API implementiert. | ✓ | ✓ |

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md
- iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md

Weitere Informationen unter:

- OWASP Mobile Top 10: M1 - Improper Platform Usage
- CWE: https://cwe.mitre.org/data/definitions/20.html
- CWE: https://cwe.mitre.org/data/definitions/749.html
