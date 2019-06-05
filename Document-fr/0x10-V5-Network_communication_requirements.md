# V5: Exigences Concernant la Communication Réseau

## Objectif de Contrôle

Le but des contrôles listés dans cette section est de garantir la confidentialité et l'intégrité de l'information échangée entre l'application mobile et les services des points terminaux distants. A minima, une application mobile doit mettre en place un canal sécurisé crypté pour la communication réseau en utilisant le protocole TLS avec les bons paramètres. Le niveau 2 liste des mesures additionnelles de défense en profondeur telles que l'épinglage SSL (SSL pinning).

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description |L2 |
| --- | --- | --- | --- | --- |
| **5.1** | MSTG‑NETWORK‑1 | Les données sont cryptées sur le réseau en utilisant TLS. Le canal sécurisé est utilisé systématiquement à travers toute l'application. | ✓ | ✓ |
| **5.2** | MSTG‑NETWORK‑2 | Les réglages de TLS sont en ligne avec les meilleures pratiques, ou aussi proches que possible dans le cas où le système d'exploitation ne supporte pas les standards recommandés. | ✓ | ✓ |
| **5.3** | MSTG‑NETWORK‑3 | L'application valide le certificat X.509 du point terminal distant lors de l'établissement du canal sécurisé. Seuls les certificats signés par une CA de confiance sont acceptés. | ✓ | ✓ |
| **5.4** | MSTG‑NETWORK‑4 | Soit l'application utilise son propre magasin de certificats, ou bien elle épingle le certificat du point terminal ou sa clé publique, et par là n'établit pas de connexion avec des points terminaux qui proposent des certificats ou des clés différents, même s'ils sont signés par des CA de confiance. |   | ✓ |
| **5.5** | MSTG‑NETWORK‑5 | L'application ne repose pas sur un canal de communication non-sécurisé unique (e-mail ou SMS) pour les opérations critiques telles que l'enregistrement ou la récupération de compte. |  | ✓ |
| **5.6** | MSTG‑NETWORK‑6 | L'application implémente l'état de l'art en termes de connectivité et de librairies de sécurité. |  | ✓ |

<div style="page-break-after: always;"></div>

## Références

Le Mobile Security Testing Guide de l'OWASP (guide de test de la Sécurité mobile) fournit des instructions détaillées pour valider les exigences listées dans cette section.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M3 - Communication Non-Sécurisée : <https://www.owasp.org/index.php/Mobile_Top_10_2016-M3-Insecure_Communication>
- CWE: <https://cwe.mitre.org/data/definitions/319.html>
- CWE: <https://cwe.mitre.org/data/definitions/295.html>
