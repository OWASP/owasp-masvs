# V4: Anforderungen an Authentifizierung und Session Management

## Zielsetzung

Ein integraler Teil der Architektur einer mobilen App ist der Login eines Nutzers an einem entfernten Service. Obwohl sich ein Großteil der Logik an dem Endpunkt abspielt, definiert der MASVS eine Reihe von Basisanforderungen an Nutzerkonten und Session-Management.

## Anforderungen

| # | MSTG-ID | Beschreibung | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Falls die App Nutzern Zugriff auf entfernte Service APIs bietet wird am API-Endpunkt eine Authentifizierung z.B. mit Nutzername/Passwort durchgeführt. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | Kommt Session-Management am API-Endpunkt zum Einsatz, so werden zufällig generierte Session-IDs erzeugt um Client-Anfragen zu authentifizieren und keine Nutzer-Anmeldedaten versandt. | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | Kommt statuslose Token-basierte Authentifizierung zum Einsatz, so werden die Token am Server mit einem sicheren Algorithmus signiert. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | Der API-Endpunkt beendet die existierende Nutzersitzung sobald sich der Nutzer abmeldet. | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | Es existiert eine Passwort-Richtlinie die am entfernten API-Endpunkt erzwungen wird. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | Der entfernte API-Endpunkt implementiert einen Mechanismus um sich gegen eine exzessive Anzahl von Login-Versuchen zu schützen. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | Nach einer definierten Inaktivitätsdauer werden Nutzersitzungen am entfernten API-Endpunkt beendet und Zugriffs-Tokens werden nach Ablauf der Gültigkeitsdauer abgelehnt. | ✓ | ✓ |
| **4.8** | MSTG-AUTH-8 | Biometrische Authentifizierung basiert auf dem Betriebssystem-basierten Entsperren des Keystores (Android)/der Keychain (iOS) und nicht auf einer z.B. event-basierten API die einfach "true" oder "false" zurück liefert. |   | ✓ |
| **4.9** | MSTG-AUTH-9 | Es gibt einen 2. Authentifizierungsfaktor und er wird am entfernten API-Endpunkt konsistent erzwungen. |   | ✓ |
| **4.10** | MSTG-AUTH-10 | Sensible Transaktionen erfordern eine zusätzliche Authentifizierung (durch einen weiteren Authentifizierungsfaktor). |   | ✓ |
| **4.11** | MSTG-AUTH-11 | Die App informiert den Nutzer über alle Anmelde-Vorgänge am Nutzerkonto. Nutzer können eine Liste aller mit dem Konto verbundenen Geräte sowie kontextbezogene Informationen (IP Adresse, Lokation usw.) sehen und ausgewählte Geräte blockieren. |  | ✓ |
| **4.12** | MSTG-AUTH-12 | Authentifizierung wird am API-Endpunkt definiert und überprüft. |  | ✓ |

## Referenzen

Der OWASP Mobile Security Testing Guide bietet detaillierte Anleitungen um die Anforderungen aus dieser Kategorie zu überprüfen.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Weitere Informationen unter:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
