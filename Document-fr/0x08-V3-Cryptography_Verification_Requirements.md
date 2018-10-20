# V3: Exigences Concernant la Cryptographie

## Objectif de Contrôle

La cryptographie est un ingredient essentiel pour la protection des données stockées sur un appareil mobile. C'est aussi une catégorie pour laquelle les choses peuvent très mal se passer, en particulier quand les conventions standards ne sont pas suivies. Le but des contrôles de ce chapitre est de garantir que les applications à valider implémentent la cryptographie en suivant les bonnes pratiques de l'industrie, notamment :

- L'utilisation de librairies cryptographiques éprouvées ;
- Le choix et la configuration pertinents des primitives cryptographiques ;
- L'utilisation d'un générateur de nombres aléatoires convenable lorsque cela est nécessaire.

## Security Verification Requirements

| # | Description | L1 | L2 |
| --- | --- | --- | --- |
| **3.1** | The app does not rely on symmetric cryptography with hardcoded keys as a sole method of encryption.| ✓ | ✓ |
| **3.2** | The app uses proven implementations of cryptographic primitives. | ✓ | ✓ |
| **3.3** | The app uses cryptographic primitives that are appropriate for the particular use-case, configured with parameters that adhere to industry best practices. | ✓ | ✓|
| **3.4** | The app does not use cryptographic protocols or algorithms that are widely considered depreciated for security purposes. | ✓ | ✓|
| **3.5** | The app doesn't re-use the same cryptographic key for multiple purposes. | ✓ | ✓ |
| **3.6** | All random values are generated using a sufficiently secure random number generator. | ✓ | ✓ |

## Références

Le Mobile Security Testing Guide de l'OWASP donne des instructions détaillées pour valider les exigences listées dans cette section.

- Android - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md
- iOS - https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: [M5 - Cryptographie Insuffisante](https://www.owasp.org/index.php/Mobile_Top_10_2016-M5-Insufficient_Cryptography)
- CWE: https://cwe.mitre.org/data/definitions/310.html
