# V3: Exigences Concernant la Cryptographie

## Objectif de Contrôle

La cryptographie est un ingrédient essentiel pour la protection des données stockées sur un appareil mobile. C'est aussi une catégorie pour laquelle les choses peuvent très mal se passer, en particulier quand les conventions standards ne sont pas suivies. Le but des contrôles de ce chapitre est de garantir que les applications à valider implémentent la cryptographie en suivant les bonnes pratiques de l'industrie, notamment :

- L'utilisation de librairies cryptographiques éprouvées ;
- Le choix et la configuration pertinents des primitives cryptographiques ;
- L'utilisation d'un générateur de nombres aléatoires convenable lorsque cela est nécessaire.

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description || L2 |
| --- | --- | --- | --- | --- |
| **3.1** | MSTG‑CRYPTO‑1 | L'application n'utilise pas la cryptographie symétrique avec des clés codées en dur comme seule méthode de chiffrement.| ✓ | ✓ |
| **3.2** | MSTG‑CRYPTO‑2 | L'application utilise des implémentations de primitives cryptographiques éprouvées. | ✓ | ✓ |
| **3.3** | MSTG‑CRYPTO‑3 | L'application utilise des primitives cryptographiques appropriées au cas d'utilisation, configurées en adéquation avec les bonnes pratiques de l'industrie. | ✓ | ✓|
| **3.4** | MSTG‑CRYPTO‑4 | L'application n'utilise pas de protocole ou d'algorithme de cryptographie considéré par la communauté comme déprécié pour des raisons de sécurité. | ✓ | ✓|
| **3.5** | MSTG‑CRYPTO‑5 | L'application ne ré-utilise pas la même clé de cryptographie à des fins différentes. | ✓ | ✓ |
| **3.6** | MSTG‑CRYPTO‑6 | Toute valeur aléatoire est générée par un générateur de nombres aléatoires offrant un bon niveau de sécurité. | ✓ | ✓ |

## Références

Le Mobile Security Testing Guide de l'OWASP donne des instructions détaillées pour valider les exigences listées dans cette section.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M5 - Cryptographie Insuffisante: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography>
- CWE: <https://cwe.mitre.org/data/definitions/310.html>
