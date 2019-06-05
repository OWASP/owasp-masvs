# V6: Exigences Concernant les Interactions avec la Plateforme

## Objectif de Contrôle

Le but des contrôles de ce groupe est de garantir que l'application utilise les API de la plateforme ainsi que ses composants standards d'une façon compatible avec la sécurité. De plus, les contrôles couvrent la communication entre les applications (IPC).

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description |L2 |
| --- | --- | --- | --- | --- |
| **6.1** | MSTG‑PLATFORM‑1 | L'application ne demande qu'une série minimum de permissions nécessaires. | ✓ | ✓ |
| **6.2** | MSTG‑PLATFORM‑2 | Toutes les entrées provenant de sources externes ainsi que des utilisateurs sont validées et si nécessaire assainies. Ceci inclut les données reçues via l'interface utilisateur, les mécanismes IPC tel que les intentions, les URL propres à l'application et les sources sur le réseau.| ✓ | ✓ |
| **6.3** | MSTG‑PLATFORM‑3 | L'application n'exporte pas de fonctionnalité sensible via des schémas d'URL propres à l'application, à moins que ces mécanismes ne soient correctement protégés. | ✓ | ✓ |
| **6.4** | MSTG‑PLATFORM‑4 | L'application n'exporte pas de fonctionnalité sensible à travers les possibilités IPC, à moins que ces mécanismes ne soient correctement protégés. | ✓ | ✓ |
| **6.5** | MSTG‑PLATFORM‑5 | JavaScript est désactivé dans les WebViews à moins qu'il ne soit explicitement requis. | ✓ | ✓ |
| **6.6** | MSTG‑PLATFORM‑6 | Les WebViews sont configurées pour ne permettre que le jeu minimum de gestionnaires de protocoles requis (idéalement, seul https est supporté). Les gestionnaires potentiellement dangereux, tels que ceux pour les fichiers, les appels téléphoniques ou l'identifiant de l'application sont désactivés. | ✓ | ✓ |
| **6.7** | MSTG‑PLATFORM‑7 | Dans le cas où des méthodes natives de l'application sont exposées à une WebView, il convient de valider que la WebView ne rend que le JavaScript contenu dans le package de l'application. | ✓ | ✓ |
| **6.8** | MSTG‑PLATFORM‑8 | La désérialisation des objets, s'il en existe, est implémentée à l'aide d'API de sérialisation de confiance. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Références

Le Mobile Security Testing Guide de l'OWASP (guide de test de la Sécurité mobile) fournit des instructions détaillées pour valider les exigences listées dans cette section.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M1 - Mauvais Utilisation de la Plateforme: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M1-Improper_Platform_Usage>
- CWE: <https://cwe.mitre.org/data/definitions/20.html>
- CWE: <https://cwe.mitre.org/data/definitions/749.html>
