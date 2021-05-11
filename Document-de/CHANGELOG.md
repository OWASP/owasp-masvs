# Versionshistorie

## V1.3 - 11 May 2021

We are proud to announce the introduction of a new document build pipeline, which is major milestone for our project. The build pipeline is based on [Pandocker](https://github.com/dalibo/pandocker) and [Github Actions](https://github.com/OWASP/owasp-masvs/tree/master/.github/workflows). This significantly reduces the time spent on creating new releases. We would like to thank:

- Jeroen Willemsen for kick-starting this initiative last year!
- Damien Clochard and Dalibo for supporting and professionalizing the build pipeline.

The build pipeline will also be the foundation for the OWASP MSTG and will be made available for the OWASP ASVS project.

The following changes are part of release 1.3:

- 4 more translations are available, which are Hindi, Farsi, Portuguese and Brazilian Portuguese
- Added requirement MSTG-PLATFORM-11

## V1.2 - 7 März 2020 - Internationale Veröffentlichung

Die folgenden Änderungen sind Teil von Version 1.2:

- Übersetzung des MASVS in verinfachtes Chinesisch verfügbar.
- Änderung des Titles auf dem Cover des MASVS.
- Mobile Top 10 und CWE Referenzen wurden aus dem MSTG entfernt und zu existierenden Referenzen im MASVS hinzugefügt.

## V1.2-RC - 5 Oktober 2019 - Pre-Release

Die folgenden Änderungen sind Teil von Version 1.2-RC:

- "Flagship Status" von OWASP erhalten.
- Anforderung MSTG-Storage-1 verändert.
- Anforderung MSTG-STORAGE-13, MSTG-STORAGE-14 und MSTG-STORAGE-15 wurden hinzugefügt mit Fokus auf Datenschutz.
- Anforderung MSTG-CODE-4 wurde aktualisiert um mehr Fälle als nur Debugging abzudecken.
- Anforderung MSTG-AUTH-11 wurde aktualisiert um "kontextbezogene Informationen".
- Anforderung MSTG-PLATFORM-10 wurde hinzugefügt für einen weiteren Fall um WebViews sicher zu verwenden.
- Anforderung MSTG-AUTH-12 wurde hinzugefügt um Entwickler daran zu erinnern Autorisierung zu implementieren, vor allem im Fall von multi-user Apps.
- Beschreibung hinzugefügt, wie der MASVS in einem Risk Assessment verwendet werden sollte.
- Beschreibung hinzugefügt für Bezahl-Inhalte.
- Anforderung MSTG-ARCH-11 wurde hinzugefügt um Responsible Disclosure Policies zu implementieren.
- Anforderung MSTG-ARCH-12 wurde hinzugefügt um Datenschutzgesetze zu befolgen.
- Anforderung MSTG-PLATFORM-11 wurde hinzugefügt um 3rd Party Tastaturen zu verbieten.
- Anforderung MSTG-RESILIENCE-13 wurde hinzugefügt um das Abhören von Apps zu erschweren.
- Die folgenden Sprachen in denen der MASVS verfügbar ist wurden aktualisiert: Chinesisch (ZHTW), Englisch, Deutsch, Französisch, Russisch, Spanisch und Japanisch

## V1.1.4 - 4 Juli 2019 - Summit edition

Die folgenden Änderungen sind Teil von Version 1.1.4:

- Markdown Fehler wurden alle behoben.
- Französische und Spanische Übersetzung wurden aktualisiert.
- Versionshistorie wurde übersetzt in Chinesisch (ZHTW) und Japanisch.
- Automatische überprüfung der Markdown Syntax und Erreichbarkeit von URLs.
- Jede Anforderung hat eine ID erhalten um die Suche nach Anforderungen und Testfällen zu vereinfachen. Die IDs werden in der kommenden Version des MSTG eingearbeitet.
- Größe des Github Repositories wurde reduziert und das Verzeichnis Generated wurde zum .gitignore hinzugefügt.
- "Code of Conduct" und "Contributing Guidelines" wurden hinzugefügt.
- Ein Pull-Request Template wurde hinzugefügt.
- Die Synchronisation zwischen dem MASVS Repository das für Gitbook genutzt wird und Gitbook wurde aktualisiert.
- Die Skripte zum Erzeugen von XML/JSON/CSV von allen Sprachen wurden aktualisiert.
- Das Vorwort wurde in Chinesisch (ZHTW) übersetzt.

## V1.1.3 - 9 Januar 2019 - Kleine Fehlerbehebungen

Die folgenden Änderungen sind Teil von Version 1.1.3:

- Fix für Spanische Übersetzung von Anforderung 7.1.
- Neue Tabelle für Übersetzer in Danksagungen.
- Kleine fixes in der Japanischen Version.

## V1.1.2 - 3 Januar 2019 - Sponsoren und Internationalisierung

Die folgenden Änderungen sind Teil von Version 1.1.2:

- Danksagung für alle Käufer, die das Buch von [Leanpub](https://leanpub.com/mobile-security-testing-guide) gekauft haben.
- Fehlender link für Authentifizierung und Session Management hinzugefügt und kaputten link in V4 aktualisiert.
- Anforderung 4.7 und 4.8 ausgetauscht in englischer Version.
- Erste internationale Version!
  - Fehler behoben in spanischer Version. Übersetzung ist auf gleichem Stand mit englischer Version (1.1.2).
  - Fehler behoben in russischer Version. Übersetzung ist auf gleichem Stand mit englischer Version (1.1.2).
  - Erste Version auf Chinesisch (ZHTW), Französisch, Deutsch und Japanisch!
- Dokument vereinfacht um Übersetzung zu erleichtern.
- Anleitung für automatische Erstellung von neuen MASVS Versionen hinzugefügt.

## V1.1.0 - 14 Juli 2018

Die folgenden Änderungen sind Teil von Version 1.1:

- Anforderung 2.6 "The clipboard is deactivated on text fields that may contain sensitive data." wurde entfernt.
- Anforderung 2.2 "Es werden keine sensiblen Daten außerhalb des App-Containers oder außerhalb des vom jeweiligen Betriebssystem angebotenen sicheren Speichermechanismus abgelegt." wurde hinzugefügt.
- Anforderung 2.1 wurde umformuliert zu "Die App speichert sensible Daten wie personenbezogene Daten, Anmeldedaten oder kryptographische Schlüssel unter Nutzung der vom jeweiligen Betriebssystem angebotenen sicheren Speichermechanismen.".

## V1.0 - 12 Januar 2018

Die folgenden Änderungen sind Teil von Version 1.0:

- Anforderung 8.9 wurde entfernt, da redundant zu 8.12
- Anforderung 4.6 wurde allgemeiner formuliert
- Kleine fixes (typos etc.)
