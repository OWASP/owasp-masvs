# V2: Exigences Concernant le Stockage des Données et le Respect de la Vie Privée

## Objectif de Contrôle

La protection des données sensibles telles que les références utilisateurs et autres informations privées est un point d'attention central dans la sécurité mobile. Tout d'abord, les données sensibles peuvent être accidentellement exposéesà d'autres applications fonctionnant sur le même appareil si des mécanismes du système d'exploitation tels que la communication inter-processus sont utilisés d'une mauvaise manière. Des données peuvent aussi accidentellement fuiter vers le stockage en nuage, les sauvegardes ou le cache. Aussi, les appareils mobiles peuvent être perdus ou volés plus facilement que les autres types d'appareils, renforçant la probabilité qu'un attaquant ait un accès physique à l'appareil. Dans ce cas, des protections supplémentaires peuvent être implémentées pour rendre l'accès aux données sensibles plus difficile.

Il faut noter que, dans la mesure où le MASVS se concentre sur l'application, il ne couvre pas les politiques du niveau de l'appareil telles que celles mises en oeuvre par les solutions de MDM (Mobile Device Management). L'utilisation de telles politiques est encouragée dans le contexte de l'entreprise pour améliorer la sécurité des données.

### Définition des Données Sensibles

Dans le contexte du MASVS, les données sensibles ont trait aux deux aspects que sont les références utilisateurs ainsi que toute autre donnée considérée comme sensible dans un contexte particulier tel que :

- Information personnellement identifiable (PII) qui peut être utilisée pour un vol d'identité :  numéros de sécurité sociale, numéros de carte de crédit, numéros de comptes bancaires, information de santé ;
- Information hautement sensible pouvant amener à une perte de réputation et/ou un coût financier si elle était divulguée : information contractuelle, information sous le coup de clauses de non-divulgation, information de gestion ;
- Toute information devant être protégée légalement ou pour des raisons de conformité.

<div style="page-break-after: always;"></div>

## Exigences pour la Validation de la Sécurité

La grande majorité des problèmes de divulgation de données peuvent être empêchés en suivant des règles simples. La plupart des contrôles listés dans ce chapitre sont obligatoires pour tous les niveaux de validation.

| # | MSTG-ID | Description || L2 |
| --- | --- | --- | --- | --- |
| **2.1** | MSTG‑STORAGE‑1 | Les fonctions de stockage sécurisées proposées par les systèmes sont utilisées de manière appropriée pour stocker les données sensibles tels que les informations personnellement identifiables (PII), les références des utilisateurs ou les clés cryptographiques. | ✓ | ✓ |
| **2.2** | MSTG‑STORAGE‑2 | Aucune donnée sensible ne devrait être stockée hors du conteneur de l'application ou des fonctions de stockage sécurisées proposées par le système. | ✓ | ✓ |
| **2.3** | MSTG‑STORAGE‑3 | Aucune donnée sensible n'est écrite dans les journaux applicatifs. | ✓ | ✓ |
| **2.4** | MSTG‑STORAGE‑4 | Aucune donnée sensible n'est partagée avec des tierces parties à moins que cela ne soit un besoin de l'architecture. | ✓ | ✓ |
| **2.5** | MSTG‑STORAGE‑5 | Le cache du clavier est désactivé sur les champs d'entrée textuels qui traitent de données sensibles. | ✓ | ✓ |
| **2.6** | MSTG‑STORAGE‑6 | Aucune donnée sensible n'est exposée par les mécanismes d'IPC. | ✓ | ✓ |
| **2.7** | MSTG‑STORAGE‑7 | Aucune donnée sensible, tels que les mots de passe ou les codes PIN, n'est exposée à travers l'interface utilisateur. | ✓ | ✓ |
| **2.8** | MSTG‑STORAGE‑8 | Aucune donnée sensible n'est incluse dans les sauvegardes générées par le système d'exploitation mobile. |   | ✓ |
| **2.9** | MSTG‑STORAGE‑9 | L'application enlève les données sensibles des vues lors de son passage en arrière-plan. |  | ✓ |
| **2.10** | MSTG‑STORAGE‑10 | L'application ne garde pas les données sensibles en mémoire plus longtemps que nécessaire et la mémoire est explicitement nettoyée après son utilisation. |  | ✓ |
| **2.11** | MSTG‑STORAGE‑11 | L'application met en oeuvre un minimum de politique concernant la sécurité de l'accès à l'appareil tel que l'obligation pour l'utilisateur de définir un code d'accès à l'appareil. |  | ✓ |
| **2.12** | MSTG‑STORAGE‑12 | L'application instruit l'utilisateur sur les types d'information personnellement identifiable traités ainsi que sur les bonnes pratiques que l'utilisateur devrait suivre en utilisant l'application. |  | ✓ |

<div style="page-break-after: always;"></div>

## Références

Le Mobile Security Testing Guide de l'OWASP donne des instructions détaillées pour valider les exigences listées dans cette section.

- Pour Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- Pour iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M2 - Stockage de données non-sécurisé: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M2-Insecure_Data_Storage>
- CWE: <https://cwe.mitre.org/data/definitions/922.html>
