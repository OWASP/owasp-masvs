# V8: Anforderungen an Manipulationssicherheit/Resilienz

## Zielsetzung

Diese Kategorie behandelt Defense-in-Depth-Maßnahmen empfohlen für Apps, die Zugriff auf sensible Daten oder sensible Funktionalitäten beinhalten. Sind diese Maßnahmen nicht umgesetzt, führt dies nicht unmittelbar zu einer Schwachstelle - jedoch erhöhen die Maßnahmen die Robustheit der App gegen Client-seitige Angriffe und Reverse Engineering.

Die Schutzmechanismen in diesem Abschnitt sollten nach Bedarf angewendet werden. Anhand einer Risikoprüfung sollten Risiken wie unerlaubte Manipulation der App oder Reverse Engineering des Codes bewertet werden. Es wird empfohlen das OWASP Dokument "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention" (siehe Referenzen) zu nutzen um eine Liste mit Geschäftsrisiken und zugeordneten technischen Bedrohungen zu identifizieren.

Um die hier aufgeführten Schutzmechanismen effektiv umsetzen zu können muss eine App mindestens alle Anforderungen aus MASVS-L1 sowie die jeweiligen Anforderungen aus Kategorie V8 in aufsteigender Reihenfolge umsetzen. So setzen die Schutzmaßnahmen unter "Nachvollziehbarkeit verhindern" voraus, dass auch die Anforderungen aus "Dynamische Analyse und Manipulation verhindern" und "Gerätebindung" umgesetzt werden.

**Achtung: Diese Software-Schutzmaßnahmen sind kein Ersatz für die Umsetzung adäquater Sicherheitsmaßnahmen. Die Maßnahmen aus MASVR-R sind gedacht, um auf Basis App-spezifischer konkreter Bedrohungen zusätzliche Schutzmaßnahmen über die bereits umgesetzten Sicherheitsmaßnahmen aus MASVS hinaus umzusetzen.**

Folgende Eckpunkte gelten:

1. Eine Bedrohungsanalyse wurde durchgeführt. Darin werden wesentliche Client-seitige Bedrohungen und Gegenmaßnahmen sowie der erforderliche Schutzbedarf dargestellt. Ein Aspekt zum Schutzbedarf könnte beispielsweise sein den Aufwand zum manuellen Reverse Engineering einer App für Malware-Autoren, die die App instrumentieren wollen, signifikant zu erhöhen.

2. Die Bedrohungsanalyse muss realistisch und vernünftig erfolgen. Zum Beispiel nützt es nichts, einen kryptografischen Schlüssel in einer White-Box-Implementierung zu "verbergen" wenn doch der Angreifer ohne weiteres an den Code kommt.

3. Die Effektivität der Schutzmaßnahmen sollte immer von einem Experten mit ausgewiesener Erfahrung im Bereich Anti-Code-Manipulation und Code-Obfuskierung überprüft werden (siehe auch Kapitel "reverse engineering" and "assessing software protections" im Mobile Security Testing Guide).

<!-- \pagebreak -->

### Dynamische Analyse und Manipulation verhindern

| # | MSTG-ID | Beschreibung | R |
| -- | -------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | Die App erkennt und reagiert auf ein gerootetes Gerät oder Geräte mit Jailbreak, indem der Nutzer gewarnt oder die App beendet wird. | ✓ |
| **8.2** | MSTG-RESILIENCE-2 | Die App verhindert Debugging und/oder erkennt und reagiert auf einen Debugger. Alle verfügbaren Debugging-Protokolle müssen abgedeckt werden. | ✓ |
| **8.3** | MSTG-RESILIENCE-3 | Die App erkennt und reagiert auf Manipulationen an ausführbaren Dateien und kritischen Daten innerhalb der App-eigenen Sandbox. | ✓ |
| **8.4** | MSTG-RESILIENCE-4 | Die App erkennt und reagiert auf typische und allgemein bekannte Reverse Engineering Tools und Frameworks auf dem Gerät.| ✓ |
| **8.5** | MSTG-RESILIENCE-5 | Die App erkennt und reagiert darauf, wenn sie in einem Emulator ausgeführt wird.  | ✓ |
| **8.6** | MSTG-RESILIENCE-6 | Die App erkennt und reagiert auf Manipulation von Code und Daten im eigenen Arbeitsspeicherbereich. | ✓ |
| **8.7** | MSTG-RESILIENCE-7 | Die App realisiert mehrere Mechanismen in jeder Kategorie (8.1 bis 8.6). Die Resilienz steigt mit der Anzahl, Vielfalt und Originalität der genutzten Mechanismen. | ✓ |
| **8.8** | MSTG-RESILIENCE-8 | Die Erkennungsmechanismen der App lösen verschiedene Arten von Reaktionen aus z.B. verzögerte, versteckte oder heimliche Reaktionen. | ✓ |
| **8.9** | MSTG-RESILIENCE-9 | Programmatische Abwehrmaßnahmen werden durch Obfuskierung geschützt was wiederum De-Obfuskierung mittels dynamischer Analyse verhindert. | ✓ |

### Gerätebindung

| # | MSTG-ID | Beschreibung | R |
| -- | -------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | Die App implementiert einen Mechanismus zur Gerätebindung, bei dem der Geräte-Fingerabdruck aus mehreren einzigartigen Geräteeigenschaften ermittelt wird. | ✓ |

### Nachvollziehbarkeit verhindern

| # | MSTG-ID | Beschreibung | R |
| -- | -------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | Alle ausführbaren Dateien und Bibliotheken der App sind entweder auf Dateiebene verschlüsselt und/oder wichtige Code- und Datensegmente in ausführbaren Dateien sind verschlüsselt oder durch Packing obfuskiert. Triviale statische Analyse offenbart keinen wichtigen Code oder Daten. | ✓ |
| **8.12** | MSTG-RESILIENCE-12 | Wenn das Ziel der Obfuskierung der Schutz sensibler Logik wie Algorithmen oder Berechnungen ist, so wird ein angemessener Obfuskierungsmechanismus, dem Stand der Technik entsprechend, genutzt der resilient gegen manuelle und automatisierte De-Obfuskierungsangriffe ist. Die Wirksamkeit der Obfuskierungsmethode muss durch manuelle Tests überprüft werden. Es ist zu beachten, dass hardware-basierte Isolations-Mechanismen softwarebasierter Obfuskierung vorzuziehen sind. | ✓ |

### Abhören erschweren

| # | MSTG-ID | Beschreibung | R |
| -- | -------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | Neben einer gehärteten Kommunikation zwischen Client und API-Endpunkt, sollte auch der übertragene Payload verschlüsselt werden, um das Abhören von Daten zu erschweren. | ✓ |

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen, um die Anforderungen aus dieser Kategorie zu überprüfen.

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
