# Der Mobile Application Security Verification Standard

Der MASVS kann genutzt werden um das Sicherheitsniveau von mobilen Apps nachweisen zu können. Die Anforderungen wurden auf Basis folgender Ziele entwickelt:

- Nutzung als Metrik - Um Entwicklern und Applikations-Verantwortlichen einen Security Standard anzubieten gegen den existierende mobile Apps verglichen werden können;
- Nutzung als Hilfestellung - Um Hilfe zu bieten in allen Phasen mobiler App-Entwicklung und Tests.
- Nutzung bei Beschaffung/Kauf von mobilen Apps - Um als Baseline zur Prüfung der Security von mobilen Apps zu dienen.

## Das Mobile AppSec Model

Der MASVS definiert zwei Prüf-Level (L1 und L2), sowie eine Reihe von Sicherheitsmaßnahmen zur Robustheit gegen Reverse Engineering (MASVS-R). Diese sind flexibel, d.h. adaptierbar an ein App-spezifisches Threat Model. MASVS-L1 enthält generische Sicherheitsanforderungen und wird für alle mobilen Apps empfohlen, während MASVS-L2 für Apps verwendet werden sollte die hochsensible Daten verarbeiten. MASVS-R deckt zusätzliche Schutzmaßnahmen ab, die anzuwenden sind, um Client-seitigen Threats vorzubeugen.

Eine App die alle Anforderungen aus MASVS-L1 erfüllt, folgt Security Best Practices und vermeidet damit typische Schwachstellen. MASVS-L2 fügt weitere Defense-In-Depth Maßnahmen wie SSL-Pinning hinzu, um ein erhöhtes Schutzniveau gegen komplexere Angriffe zu bieten. Dabei gilt die Annahme, dass das mobile Betriebssystem intakt und der Endnutzer nicht als potenzieller Angreifer betrachtet wird. Die Anforderungen aus dem MASVS-R ganz oder teilweise zu erfüllen, hilft dabei spezifische client-seitige Threats (böswilliger Nutzer o. kompromittiertes Betriebssystem) zu verhindern bzw. zu erschweren.

**I: Die Schutzmaßnahmen enthalten in MASVS-R und beschrieben im OWASP Mobile Testing Guide können letztlich alle umgangen werden und dürfen nicht als Ersatz für Sicherheitsmaßnahmen (L1/L2) genutzt werden. Stattdessen sind sie dazu gedacht, um zusätzliche Threat-spezifische Schutzmaßnahmen zu Apps hinzuzufügen, die bereits die MASVS Anforderungen L1 oder L2 erfüllen.**

**II: Bitte beachte das alle Anforderungen, die in MASVS-R aufgelistet und im OWASP Mobile Security Testing Guide beschrieben sind, immer umgangen werden können. Daher sollten diese auch nie als Ersatz für Sicherheitsmaßnahmen verwendet werden. Stattdessen ist die Intention von MASVS-R zusätzliche bedrohungsspezifische Gegenmaßnahmen für Apps zu definieren, die bereits die Anforderungen in MASVS-L1 oder MASVS-L2 erfüllen.**

![Prüf-Level](images/masvs-levels-new.jpg)

### Dokumentstruktur

Der erste Teil des MASVS enthält eine Beschreibung des Security Modells und der Prüf-Level, gefolgt von Empfehlungen zur Nutzung des Standards in der Praxis. Die detaillierten Sicherheitsanforderungen und ihre Einordnung in die Prüf-Level befinden sich im zweiten Teil. Die Anforderungen wurden in acht Kategorien (V1 bis V8), basierend auf technischen Zielen/Scopes, eingeteilt. Die folgende Nomenklatur wird durchgehend im MASVS und MSTG genutzt:

- *Anforderungs Kategorie:* MASVS-Vx, z.B. MASVS-V2: Datenspeicherung und Datenschutz
- *Anforderung:* MASVS-Vx.y, z.B. MASVS-V2.2: "Keine sensiblen Daten werden in Applikations Logs geschrieben."  

### Prüf-Level im Detail

#### MASVS-L1: Standard Security

Eine mobile App die MASVS-L1 entspricht, erfüllt Mobile Application Best Practices. Sie erfüllt Basis-Anforderungen in Bezug auf Codequalität, Umgang mit sensiblen Daten und Interaktion mit dem mobilen Umfeld. Es gibt einen Testprozess, um die Effektivität der Security Maßnahmen zu prüfen. Dieser Level eignet sich für alle mobilen Applikationen.

#### MASVS-L2: Defense-in-Depth

MASVS-L2 führt erweiterte Sicherheitsmaßnahmen ein, die über die Standardanforderungen hinausgehen. Um L2 zu erfüllen, muss ein Threat Model existieren und Security muss ein integraler Teil der App-Architektur sein. Dieser Level ist angedacht für alle Apps, die sensible Daten verarbeiten wie z.B. Apps für mobiles Bezahlen.

#### MASVS-R: Resilienz gegen Reverse Engineering and Manipulation

Die App hat state-of-the-art Security und ist resilient (robust) gegen spezifische, klar definierte Client-seitige Angriffe wie Manipulation, Modifizierung oder Reverse Engineering um sensiblen Quellcode oder Daten zu extrahieren. Solch eine App nutzt Hardware Security Funktionen oder ausreichend starke und überprüfbare Software-Schutzmaßnahmen. MASVS-R ist geeignet für Apps, die hochsensible Daten verarbeiten, um geistiges Eigentum zu schützen oder um eine App manipulationssicher zu machen.

### Empfohlene Nutzung

Nach vorheriger Bewertung des Risikos und des erforderlichen Sicherheitsniveaus können Apps gegen MASVS L1 oder L2 geprüft werden. L1 ist geeignet für alle mobilen Apps, während L2 für Apps mit mehr sensiblen Daten oder sensibler Funktionalität empfohlen wird. MASVS-R (oder Teile davon) können genutzt werden um *zusätzlich zu bereits implementierten Sicherheitsfunktionen* die Resilienz der App gegen spezifische Threats wie Repackaging oder Extraktion von sensiblen Daten zu prüfen.

Insgesamt gibt es folgende Prüfkombinationen:

- MASVS-L1
- MASVS-L1+R
- MASVS-L2
- MASVS-L2+R

Die Kombinationen stellen verschiedene Graduierungen der Security und Resilienz dar. Das Ziel ist Flexibilität: Eine Gaming-App z.B. wird aus Usability-Gesichtspunkten darauf verzichten, MASVS-L2 Maßnahmen wie 2-Faktor Authentifizierung zu nutzen hat jedoch aus Business-Sicht hohen Schutzbedarf gegen Code-Manipulation (Tampering).

#### Prüfvariante wählen

Die Anforderungen aus MASVS L2 zu implementieren erhöht die Sicherheit - dies kann sich jedoch negativ auf die Endnutzerakzeptanz auswirken (klassischer Kompromiss). Zeitgleich steigen die Entwicklungskosten.

##### Beispiele

###### MASVS-L1

- Geeignet für alle mobilen Apps. MASVS-L1 benennt Security Best Practices mit akzeptablen Auswirkungen auf Entwicklungskosten und Nutzererlebnis. Sollte für jede App genutzt werden die keinen höheren Level erfordert.

###### MASVS-L2

- Gesundheitswesen: Mobile Apps, die personenbezogene Daten speichern, die für Identitätsdiebstahl, Zahlungsbetrug und eine Reihe anderer Betrugsvorhaben genutzt werden können. Zu den für den US-Gesundheitsbereich geltenden Compliance-Regeln gehören der Health Insurance Portability and Accountability Act (HIPAA), Datenschutz, Security und Vorgaben/Regeln zur Benachrichtigung bei Datenpannen sowie Patientensicherheit.
- Banken/Finanzwesen: Apps mit Zugriff auf hochsensible Daten wie Kreditkarten, personenbezogene Daten oder die Zahlungsflüsse erlauben. Diese Apps erfordern erweiterte Security Maßnahmen, um Betrug zu vermeiden. Finanz-Apps müssen Compliance-Anforderungen aus dem Payment Card Industry Data Security Standard (PCI DSS), Gramm Leech Bliley Act und Sarbanes-Oxley Act (SOX) erfüllen.

###### MASVS L1+R

- Mobile Apps für die der Schutz des geistigen Eigentums geschäftskritisch ist. Die Resilienz-Maßnahmen aus MASVS-R dienen dazu, für Angreifer den Aufwand zu erhöhen um an den Original-Quellcode zu gelangen und Manipulation der Apps (Tampering/Cracking) zu erschweren.
- Gaming Industrie: Spiele mit hohem Bedarf Modding und Cheating zu verhindern, wie Online-Games. Cheating ist ein großes Problem in Online-Spielen, da eine hohe Anzahl von Cheatern die regulären Nutzer verärgern und ein erfolgreiches Game letztlich zum Scheitern bringen kann. MASVS-R bietet Basis-Maßnahmen, um den Aufwand für Cheater zu erhöhen.

###### MASVS L2+R

- Finanzwesen: Online Banking Apps, die Nutzern Geldtransfers erlauben und bei denen Techniken wie Code-Injektion oder Instrumentierung auf kompromittierten Geräten Risiken darstellen. In diesem Fall können Maßnahmen aus dem MASVS-R genutzt werden, um Manipulationen zu erschweren und den Aufwand für Malware Autoren zu erhöhen.
- Alle mobilen Apps, die sensible Daten auf dem mobilen Gerät speichern und gleichzeitig eine hohe Kompatibilität zu diversen Geräten und Betriebssystemversionen bieten müssen. In diesem Fall können Resilienz-Maßnahmen als defense-in-depth genutzt werden um den Aufwand für Angreifer, die sensible Daten extrahieren wollen, zu erhöhen.

- Apps die In-App Bezahlung anbieten, sollten die Anforderungen in MASVS-L2 und server-seitige Schutzmaßnahmen benutzen, um bezahlte Inhalte zu beschützen. In Fällen in denen server-seite Schutzmaßnahmen nicht verwendet werden können, sollten die Anforderungen von MASVS-R berücksichtigt werden, um Reverse Engineering zu erschweren.
