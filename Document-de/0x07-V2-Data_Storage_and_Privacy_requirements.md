# V2: Anforderungen an Datenspeicherung und Datenschutz

## Zielsetzung

Der Schutz sensibler Daten wie Nutzer-Anmeldedaten und privaten Informationen ist ein Schwerpunkt im Bereich mobiler Sicherheit. Zum Beispiel können sensible Daten ungewollt anderen Apps auf dem mobilen Gerät zur Verfügung gestellt werden falls Betriebssystem-Mechanismen wie Interprozesskommunikation auf unsichere Weise genutzt werden. Datenlecks können ungewollt im Bereich Cloud-Daten-Speicherung, Backups oder dem Tastatur-Cache auftreten. Darüber hinaus können mobile Geräte leichter verloren gehen oder gestohlen werden. Die Wahrscheinlichkeit für physische Angriffe ist höher als bei anderen Geräten. In diesem Fall können zusätzliche Schutzmaßnahmen implementiert werden um den Zugriff auf sensible Daten zu erschweren.
Im MASVS steht die App im Mittelpunkt und nicht das mobile Gerät. Security-Lösungen für mobiles Gerätemanagement (MDM) werden aus OWASP Sicht zwar zur Umsetzung von Security-Richtlinien im Unternehmens-Umfeld empfohlen, werden im MASVS jedoch nicht berücksichtigt.

### Definition sensibler Daten

Sensible Daten im Kontext des MASVS sind jegliche Nutzer-Anmeldedaten sowie alle übrigen Daten die entsprechend ihrem Kontext sensibel sind:

- Personenbezogene Daten die für Identitätsdiebstahl genutzt werden können: Sozialversicherungsnummern, Kreditkarteninformationen, Bankdaten und Gesundheitsdaten;
- Hoch sensible Daten deren Kompromittierung zu hohem Reputationsverlust oder finanziellen Aufwänden führen würde: Vertragsinformationen, Informationen die durch Verschwiegenheitserklärungen geschützt sind, Management Informationen;
- Alle Daten die durch gesetzliche Bestimmungen oder aufgrund regulatorischer Vorgaben (Compliance) zu schützen sind.

<div style="page-break-after: always;"></div>

## Anforderungen

Ein Großteil von Datenpannen kann bereits durch Einhaltung einfacher Regeln vermieden werden. Die meisten der Sicherheitsmaßnahmen in dieser Kategorie sind deshalb für alle Prüf-Levels zwingend erforderlich.

| # | MSTG-ID | Beschreibung | L1 | L2 |
| --- | --- | --- | --- | --- |
| **2.1** | MSTG‑STORAGE‑1 | Die App speichert sensible Daten wie personenbezogene Daten, Anmeldedaten oder kryptographische Schlüssel unter Nutzung der vom jeweiligen Betriebssystem angebotenen sicheren Speichermechanismen. | ✓ | ✓ |
| **2.2** | MSTG‑STORAGE‑2 | Es werden keine sensiblen Daten außerhalb des App-Containers oder außerhalb des vom jeweiligen Betriebssystem angebotenen sicheren Speichermechanismus abgelegt. | ✓ | ✓ |
| **2.3** | MSTG‑STORAGE‑3 | Es werden keine sensiblen Daten in die Logfiles der App geschrieben. | ✓ | ✓ |
| **2.4** | MSTG‑STORAGE‑4 | Es werden keine sensiblen Daten mit Dritten geteilt - es sei denn dies wurde in der App-Architektur definiert und ist zur Erfüllung des Zwecks der App erforderlich. | ✓ | ✓ |
| **2.5** | MSTG‑STORAGE‑5 | Der Tastatur-Cache ist für alle sensiblen Texteingaben deaktiviert. | ✓ | ✓ |
| **2.6** | MSTG‑STORAGE‑6 | Es werden keine sensiblen Daten über Interprozesskommunikation zur Verfügung gestellt. | ✓ | ✓ |
| **2.7** | MSTG‑STORAGE‑7 | Es werden keine sensiblen Daten wie Passwörter oder Pins über die Benutzeroberfläche exponiert. | ✓ | ✓ |
| **2.8** | MSTG‑STORAGE‑8 | Es ist sichergestellt, dass betriebssystemgesteuerte Backups keine sensiblen App-Daten enthalten. |   | ✓ |
| **2.9** | MSTG‑STORAGE‑9 | Die App entfernt sensible Daten aus der aktuellen Ansicht wenn der Hintergrundmodus aktiviert wird. |  | ✓ |
| **2.10** | MSTG‑STORAGE‑10 | Die App hält sensible Daten nur solange wie nötig im Speicher und betroffene Speicherbereiche werden nach Nutzung explizit gelöscht. |  | ✓ |
| **2.11** | MSTG‑STORAGE‑11 | Die App erzwingt ein Minimum an Geräteschutz-Richtlinien wie das Definieren eines Gerätepassworts. |  | ✓ |
| **2.12** | MSTG‑STORAGE‑12 | Die App klärt den Nutzer über die Art und Weise der verarbeiteten personenbezogenen Daten auf und gibt dem Nutzer Security-Best-Practice-Empfehlungen zum Umgang mit der App. |  | ✓ |

<div style="page-break-after: always;"></div>

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- Für Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- Für iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M2 - Insecure Data Storage: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M2-Insecure_Data_Storage>
- CWE: <https://cwe.mitre.org/data/definitions/922.html>
