# V6: Anforderungen zur Plattform-Interaktion

## Zielsetzung

Die Anforderungen aus dieser Kategorie sollen sicherstellen, dass Plattform-Komponenten und Standard-Komponenten von der App auf sichere Weise genutzt werden. Zusätzlich decken die Anforderungen auch die Kommunikation (IPC) zwischen Apps ab.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | Die App fordert vom Nutzer nur die unbedingt erforderlichen App-Berechtigungen. | ✓ | ✓ |
| **6.2** | MSTG‑PLATFORM‑2 | Alle Eingaben von externen Quellen und dem Nutzer werden validiert und falls erforderlich bereinigt. Dazu gehören Daten aus der GUI, IPC Mechanismen wie Intents oder spezifische URL-Schemas und Netzwerk-Daten. | ✓ | ✓ |
| **6.3** | MSTG‑PLATFORM‑3 | Die App bietet keine sensible Funktionalität über App-eigene URL-Schemas an - wenn doch, ist der Mechanismus angemessen geschützt.  | ✓ | ✓ |
| **6.4** | MSTG‑PLATFORM‑4 | Die App bietet keine sensible Funktionalität über Interprozesskommunikation (IPC) an - wenn doch, ist der Mechanismus angemessen geschützt. | ✓ | ✓ |
| **6.5** | MSTG‑PLATFORM‑5 | JavaScript ist in WebViews deaktiviert wenn es nicht unbedingt erforderlich ist. | ✓ | ✓ |
| **6.6** | MSTG‑PLATFORM‑6 | WebViews sind so konfiguriert, dass nur die minimal nötigen Protokoll-Handler erlaubt sind (Idealerweise nur HTTPS). Potentiell gefährliche Handler wie file, tel und app-id sind deaktiviert. | ✓ | ✓ |
| **6.7** | MSTG‑PLATFORM‑7 | Wenn eine WebView über Javascript Zugriff auf native Methoden einer App bekommt, ist sichergestellt, dass die WebView nur vorgegebenes Javascript aus der App rendert und kein Javascript aus externen Quellen.  | ✓ | ✓ |
| **6.8** | MSTG‑PLATFORM‑8 | Objektserialisierung wird, falls vorhanden, über eine sichere Serialisierungs-API implementiert. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- Für Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- Für iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M1 - Improper Platform Usage: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE: <https://cwe.mitre.org/data/definitions/20.html>
- CWE: <https://cwe.mitre.org/data/definitions/749.html>
