# V5: Exigences Concernant la Communication Réseau

## Objectif de Contrôle

Le but des contrôles listés dans cette section est de garantir la confidentialité et l'intégrité de l'information échangée entre l'application mobile et les services des points terminaux distants. A minima, une application mobile doit mettre en place un canal sécurisé crypté pour la communication réseau en utilisant le protocole TLS avec les bons paramètres. Le niveau 2 liste des mesures additionnelles de défense en profondeur telles que l'épinglage SSL (SSL pinning).

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Les données sont cryptées sur le réseau en utilisant TLS. Le canal sécurisé est utilisé systématiquement à travers toute l'application. | ✓ | ✓ |
| **5.2** | MSTG-NETWORK-2 | Les réglages de TLS sont en ligne avec les meilleures pratiques, ou aussi proches que possible dans le cas où le système d'exploitation ne supporte pas les standards recommandés. | ✓ | ✓ |
| **5.3** | MSTG-NETWORK-3 | L'application valide le certificat X.509 du point terminal distant lors de l'établissement du canal sécurisé. Seuls les certificats signés par une CA de confiance sont acceptés. | ✓ | ✓ |
| **5.4** | MSTG-NETWORK-4 | Soit l'application utilise son propre magasin de certificats, ou bien elle épingle le certificat du point terminal ou sa clé publique, et par là n'établit pas de connexion avec des points terminaux qui proposent des certificats ou des clés différents, même s'ils sont signés par des CA de confiance. |   | ✓ |
| **5.5** | MSTG-NETWORK-5 | L'application ne repose pas sur un canal de communication non-sécurisé unique (e-mail ou SMS) pour les opérations critiques telles que l'enregistrement ou la récupération de compte. |  | ✓ |
| **5.6** | MSTG-NETWORK-6 | L'application implémente l'état de l'art en termes de connectivité et de librairies de sécurité. |  | ✓ |

## Références

Le Mobile Security Testing Guide de l'OWASP (guide de test de la Sécurité mobile) fournit des instructions détaillées pour valider les exigences listées dans cette section.

- Général : Tester la communication réseau - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android : Tester la communication réseau - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS : Tester la communication réseau - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M3 (Insecure Communication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Improper Certificate Validation) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Improper Following of a Certificate's Chain of Trust) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Improper Validation of Certificate with Host Mismatch) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Improper Validation of Certificate Expiration) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Cleartext Transmission of Sensitive Information) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Use of RSA Algorithm without OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Improper Verification of Source of a Communication Channel) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Incorrectly Specified Destination in a Communication Channel) - <https://cwe.mitre.org/data/definitions/941.html>
