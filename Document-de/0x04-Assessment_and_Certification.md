# Bewertung und Zertifizierung

## OWASP's Standpunkt zu MASVS Zertifizierungen und Gütesiegeln

OWASP ist eine herstellerunabhängige Non-Profit-Organisation und führt keine Zertifizierungen von Herstellern, Prüfern oder Software durch.

OWASP distanziert sich von derartigen Bescheinigungen, Qualitätssiegeln oder Zertifikaten. Diese sind in keinem Fall durch OWASP freigegeben, registriert oder zertifiziert. Eine Organisation/Unternehmen sollte vorsichtig und misstrauisch gegenüber derartigen Gütesiegeln sein.

Dies sollte Organisationen nicht davon abhalten Dienstleistungen auf Basis des (M)ASVS Standard anzubieten, solange keine offiziellen OWASP Zertifikate ausgestellt werden.

## Anleitung zur Zertifizierung von mobilen Apps

Der empfohlene Weg um eine mobile App gegen den MASVS zu prüfen ist das offene Review-Format. Dabei erhalten Tester Zugriff auf Schlüsselressourcen wie Architekten und App-Entwickler, Projekt-Dokumentation, Quellcode und authentifizierten Zugriff auf API-Endpunkte (mindestens ein Nutzeraccount für jede Rolle)

Es ist wichtig zu erwähnen, dass der MASVS nur die Security auf der client-seitigen mobilen App und der Netzwerkkommunikation zwischen App und API-Endpunkt(en) sowie einige Basisanforderungen in Bezug auf Nutzerauthentifizierung und Session Management abdeckt. Er enthält darüber hinaus keine spezifischen Security-Anforderungen für remote Services z.B. Webservices die von der App genutzt werden. Jedoch schreibt MASVS V1 vor, dass API-Endpunkte von einem übergreifenden Threat Model berücksichtigt und gegen entsprechende Standards wie ASVS geprüft werden müssen.

Eine Zertifizierungsstelle muss in jedem Report den Scope der Überprüfung (insbesondere wenn eine Schlüsselkomponente out of scope ist), eine Zusammenfassung der Prüfungs-Findings, inklusive einer Auflistung aller erfolgreich durchgeführten sowie gescheiterten Tests sowie klare Lösungshinweise zu allen gescheiterten Tests aufführen. Eine Sammlung detaillierter Arbeitspapiere, Screenshots oder Demo-Videos, Skripte um eine gefundene Schwachstelle zuverlässig und wiederholt zu exploiten aber auch elektronische Aufzeichnungen/Logs wie Traffic-Mitschnitte durch einen Proxy und zugehörige Notizen wie z.B. eine ToDo-Liste oder Cleanup-Liste aufzubewahren gilt als "Best Practice". Es ist unzureichend einfach nur ein Tool zu starten und die Findings zu berichten. Stattdessen ist es wichtig Beweise zu liefern, dass alle geforderten Themenpunkte gründlich getestet wurden. Für den Fall von Streitigkeiten sollten ausreichend Nachweise vorliegen um darlegen zu können, dass jede zu prüfende Anforderung tatsächlich getestet wurde.

### Nutzung des OWASP Mobile Application Security Testing Guide (MASTG)

Der OWASP MASTG ist eine Anleitung zum Testen der Sicherheit von mobilen Apps. Der Guide beschreibt den technischen Prozess zur Überprüfung der Anforderungen aus dem MASVS. Der MASTG enthält eine Liste von Testfällen. Jeder Testfall referenziert eine einzelne Anforderung im MASVS. Während der MASVS eher grobe und generische Anforderungen enthält, bietet der MASTG detaillierte Empfehlungen und Testprozeduren je mobilem Betriebssystem.

### Die Rolle von Werkzeugen für automatisierte Security Tests

Die Nutzung von Quellcode-Scannern und Black-Box-Test-Werkzeugen erhöht die Effizienz und wird klar empfohlen. Allerdings ist eine vollständige MASVS Überprüfung allein mit automatisierten Werkzeugen unmöglich. Jede mobile App ist unterschiedlich und ein Verständnis der Gesamtarchitektur, der Geschäftslogik und technischer Fallstricke genutzter Technologien und Frameworks ist eine zwingende Voraussetzung um die Sicherheit einer App zu prüfen.

## Andere Anwendungsfälle

### Als detaillierter Security-Architektur-Guide

Der MASVS ist eine wertvolle Ressource für Security Architekten. Den 2 wichtigsten Security-Architektur-Frameworks SABSA und TOGAF fehlen wesentliche Teile um Security-Architektur-Reviews für mobile Apps durchführen zu können. Der MASVS kann genutzt werden, um diese Lücken zu schließen und ist eine wertvolle Hilfe bei der Auswahl geeigneter Security Maßnahmen im Bereich mobiler Apps.

### Als Ersatz für pauschale Secure Coding Checklisten

Viele Organisationen können davon profitieren, den MASVS zu adaptieren, indem Sie einen geeigneten Level wählen oder den MASVS als Ausgangsbasis nutzen (Forking) und die Inhalte entsprechend zum Risikoprofil und Domänen-Kontext der jeweiligen App anpassen. Dieser Weg des Forkens wird empfohlen wobei darauf zu achten ist, die Nachverfolgbarkeit der einzelnen Themenpunkte zu gewährleisten. So sollte z.B. Anforderung 4.1 auch nach zukünftigen Änderungen die gleiche semantische Bedeutung behalten.

### Als Basis für Security Tests

Eine gute Testmethodik für Security Tests mobiler Apps sollte alle Anforderungen aus dem MASVS abdecken. Der OWASP MASTG beschreibt Black-box und White-box Testfälle für jede Anforderungen aus dem MASVS.

### Als Vorgabe für automatisierte Unit- und Integrationstests

Um die Anzahl von Findings in der Vorproduktions-Phase zu reduzieren, sollten bereits während der Entwicklung automatische Unit-, Integrations- und Akzeptanztests durchgeführt werden. Um dies zu unterstützen wurde der MASVS mit starkem Fokus auf Testbarkeit entwickelt. Eine Ausnahme bilden die Anforderungen aus dem Bereich Architektur. Teams, die die Anforderungen aus dem ASVS (über automatisierte Tests) umsetzen erhöhen dadurch nicht nur die Qualität der entwickelten Apps, sondern verbessern auch die Security Awareness der Entwickler.

### Zum Training für sichere Software-Entwicklung

Der MASVS kann darüber hinaus genutzt werden, um die Merkmale zu beschreiben, die eine sichere mobile App haben sollte. Viele Kurse für "sichere Softwareentwicklung" sind simple Kurse über Hacking-Techniken und bieten kaum wertvolle Tipps für Entwickler. Kurse die auf Basis des MASVS proaktive Schutz-Maßnahmen in den Vordergrund stellen, anstatt z.B. die Top 10 Schwachstellen zu behandeln, bieten wesentlichen Mehrwert für Entwickler.
