# V4: Anforderungen an Authentifizierung und Session Management

## Zielsetzung

Ein integraler Teil der Architektur einer mobilen App ist der Login eines Nutzers an einem entfernten Service. Obwohl sich ein Großteil der Logik an dem Endpunkt abspielt, definiert der MASVS eine Reihe von Basisanforderungen an Nutzerkonten und Session-Management.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| --- | --- | --- | --- | --- |
| **4.1** | MSTG‑AUTH‑1 | Falls die App Nutzern Zugriff auf entfernte Service APIs bietet wird am API-Endpunkt eine Authentifizierung z.B. mit Nutzername/Passwort durchgeführt. | ✓ | ✓ |
| **4.2** | MSTG‑AUTH‑2 | Kommt Session-Management am API-Endpunkt zum Einsatz, so werden zufällig generierte Session-IDs erzeugt um Client-Anfragen zu authentifizieren und keine Nutzer-Anmeldedaten versandt. | ✓ | ✓ |
| **4.3** | MSTG‑AUTH‑3 | Kommt statuslose Token-basierte Authentifizierung zum Einsatz, so werden die Token am Server mit einem sicheren Algorithmus signiert. | ✓ | ✓ |
| **4.4** | MSTG‑AUTH‑4 | Der API-Endpunkt beendet die existierende Nutzersitzung sobald sich der Nutzer abmeldet. | ✓ | ✓ |
| **4.5** | MSTG‑AUTH‑5 | Es existiert eine Passwort-Richtlinie die am entfernten API-Endpunkt erzwungen wird. | ✓ | ✓ |
| **4.6** | MSTG‑AUTH‑6 | Der entfernte API-Endpunkt implementiert einen Mechanismus um sich gegen eine exzessive Anzahl von Login-Versuchen zu schützen. | ✓ | ✓ |
| **4.7** | MSTG‑AUTH‑7 | Nach einer definierten Inaktivitätsdauer werden Nutzersitzungen am entfernten API-Endpunkt beendet und Zugriffs-Tokens werden nach Ablauf der Gültigkeitsdauer abgelehnt. | ✓ | ✓ |
| **4.8** | MSTG‑AUTH‑8 | Biometrische Authentifizierung basiert auf dem Betriebssystem-basierten Entsperren des Keystores (Android)/der Keychain (iOS) und nicht auf einer z.B. event-basierten API die einfach "true" oder "false" zurück liefert. |   | ✓ |
| **4.9** | MSTG‑AUTH‑9 | Es gibt einen 2. Authentifizierungsfaktor und er wird am entfernten API-Endpunkt konsistent erzwungen. |   | ✓ |
| **4.10** | MSTG‑AUTH‑10 | Sensible Transaktionen erfordern eine zusätzliche Authentifizierung (durch einen weiteren Authentifizierungsfaktor). |   | ✓ |
| **4.11** | MSTG‑AUTH‑11 | Die App informiert den Nutzer über alle Anmelde-Vorgänge am Nutzerkonto. Nutzer können eine Liste aller mit dem Konto verbundenen Geräte sehen und ausgewählte Geräte blockieren. |  | ✓ |

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- Allgemein - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Für Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- Für iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M4 - Insecure Authentication: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M4-Insecure_Authentication>
- OWASP Mobile Top 10: M6 - Insecure Authorization: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M6-Insecure_Authorization>
- CWE:  <https://cwe.mitre.org/data/definitions/287.html>
