# V1: Anforderungen an Architektur, Design und Bedrohungsanalysen

## Zielsetzung

In einer perfekten Welt würde Security über alle Phasen der Softwareentwicklung berücksichtigt werden. In der Realität wird Security jedoch meist erst spät im Entwicklungsprozess berücksichtigt. Neben den technischen Maßnahmen fordert der MASVS auch organisatorische Maßnahmen die sicherstellen, dass Security in der Planungsphase sowie beim Design der mobilen App entsprechend Berücksichtigung gefunden hat. Für jede Komponente der App muss der fachliche Funktionsumfang und Sicherheitsfunktionen klar definiert und bekannt sein. Die meisten Apps kommunizieren mit entfernten Schnittstellen (API-Endpunkten). Deshalb müssen auch für diese API-Endpunkte angemessene Security Standards umgesetzt sein. Der isolierte Test einer mobilen App ohne die Endpunkte ist unzureichend!

Die Kategorie "V1" enthält Sicherheitsanforderungen an die Architektur und das Design einer App. Aufgrund dessen ist dies die einzige Kategorie die nicht auf technische Testfälle in den OWASP Mobile Testing Guide referenziert. Um Themen wie Bedrohungsanalyse, sichere Softwareentwicklungsprozesse und Schlüssel-Management abzudecken, sollten Anwender des MASVS die jeweiligen OWASP Projekte und/oder Standards wie die unten verlinkten Dokumente berücksichtigen.

<div style="page-break-after: always;"></div>

## Security Anforderungen

Die Anforderungen für MASVS-L1 und MASVS-L2 sind nachfolgend aufgelistet.

| # | MSTG-ID | Beschreibung | L1 | L2 |
| --- | --- | --- | --- | --- |
| **1.1** | MSTG‑ARCH‑1 | Alle Komponenten der mobilen App sind identifiziert und für den Betrieb der App erforderlich. | ✓ | ✓ |
| **1.2** | MSTG‑ARCH‑2 | Sicherheitsfunktionen sind niemals nur auf Client-Seite implementiert sondern immer auch im entsprechenden entfernten API-Endpunkt. | ✓ | ✓ |
| **1.3** | MSTG‑ARCH‑3 | Es existiert eine Architekturübersicht über die mobile App und alle verbundenen API-Endpunkte und Security wurde in der Gesamtarchitektur berücksichtigt. | ✓ | ✓ |
| **1.4** | MSTG‑ARCH‑4 | Alle sensiblen Daten im Kontext der mobilen App wurden klar identifiziert. | ✓ | ✓ |
| **1.5** | MSTG‑ARCH‑5 | Für jede Komponente der App ist der angebotene fachliche Funktionsumfang und/oder Sicherheitsfunktionen/-mechanismen klar definiert.  |   | ✓ |
| **1.6** | MSTG‑ARCH‑6 | Für die mobile App und die genutzten API-Endpunkte wurde eine Bedrohungsanalyse durchgeführt und potentielle Bedrohungen und Gegenmaßnahmen identifiziert. |   | ✓ |
| **1.7** | MSTG‑ARCH‑7 | Alle Sicherheitsfunktionen wurden in Form von zentralen Komponenten implementiert. |   | ✓ |
| **1.8** | MSTG‑ARCH‑8 | Eine dedizierte Richtlinie zum Management von kryptographischen Schlüsseln (falls in der App genutzt) beschreibt den sicheren Umgang mit Schlüsseln über den gesamten Lebenszyklus, idealerweise basierend auf Standards wie NIST SP 800-57. |   | ✓ |
| **1.9** | MSTG‑ARCH‑9 | Es gibt einen Mechanismus in der mobilen App um App-Aktualisierungen zu erzwingen. |   | ✓ |
| **1.10** | MSTG‑ARCH‑10 | Security wird in allen Teilen des Softwareentwicklungszyklus berücksichtigt. |   | ✓ |

<div style="page-break-after: always;"></div>

## Referenzen

Für weitere Informationen:

- OWASP Mobile Top 10: M10 - Extraneous Functionality: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M10-Extraneous_Functionality>
- OWASP Security Architecture cheat sheet: <https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet>
- OWASP Thread modelling: <https://www.owasp.org/index.php/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet: <https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet>
- Microsoft SDL: <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57: <https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-4/final>
