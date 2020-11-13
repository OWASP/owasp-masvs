# V6: Exigences Concernant les Interactions avec la Plateforme

## Objectif de Contrôle

Le but des contrôles de ce groupe est de garantir que l'application utilise les API de la plateforme ainsi que ses composants standards d'une façon compatible avec la sécurité. De plus, les contrôles couvrent la communication entre les applications (IPC).

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | L'application ne demande qu'une série minimum de permissions nécessaires. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | Toutes les entrées provenant de sources externes ainsi que des utilisateurs sont validées et si nécessaire assainies. Ceci inclut les données reçues via l'interface utilisateur, les mécanismes IPC tel que les intentions, les URL propres à l'application et les sources sur le réseau.| ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | L'application n'exporte pas de fonctionnalité sensible via des schémas d'URL propres à l'application, à moins que ces mécanismes ne soient correctement protégés. | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | L'application n'exporte pas de fonctionnalité sensible à travers les possibilités IPC, à moins que ces mécanismes ne soient correctement protégés. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | JavaScript est désactivé dans les WebViews à moins qu'il ne soit explicitement requis. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | Les WebViews sont configurées pour ne permettre que le jeu minimum de gestionnaires de protocoles requis (idéalement, seul https est supporté). Les gestionnaires potentiellement dangereux, tels que ceux pour les fichiers, les appels téléphoniques ou l'identifiant de l'application sont désactivés. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | Dans le cas où des méthodes natives de l'application sont exposées à une WebView, il convient de valider que la WebView ne rend que le JavaScript contenu dans le package de l'application. | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | La désérialisation des objets, s'il en existe, est implémentée à l'aide d'API de sérialisation de confiance. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | L'application doit se protéger contre les attaques par recouvrement. (Android seulement) |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | Le cache, le stockage et les ressources téléchargées (JavaScript, etc.) d'une WebView doivent être supprimés avant que la WebView soit détruite. |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | Vérifier que l'application n'autorise pas l'utilisation des claviers tiers personnalisés lors de la saisie des données sensibles. (iOS seulement) |  | ✓ |

## Références

Le Mobile Security Testing Guide de l'OWASP (guide de test de la Sécurité mobile) fournit des instructions détaillées pour valider les exigences listées dans cette section.

- Android : Tester les interactions avec la plateforme - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS : Tester les interactions avec la plateforme - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
