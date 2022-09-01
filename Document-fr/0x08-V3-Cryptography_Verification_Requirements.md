# V3: Exigences Concernant la Cryptographie

## Objectif de Contrôle

La cryptographie est un ingrédient essentiel pour la protection des données stockées sur un appareil mobile. C'est aussi une catégorie pour laquelle les choses peuvent très mal se passer, en particulier quand les conventions standards ne sont pas suivies. Le but des contrôles de ce chapitre est de garantir que les applications à valider implémentent la cryptographie en suivant les bonnes pratiques de l'industrie, notamment :

- L'utilisation de librairies cryptographiques éprouvées ;
- Le choix et la configuration pertinents des primitives cryptographiques ;
- L'utilisation d'un générateur de nombres aléatoires convenable lorsque cela est nécessaire.

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | L'application n'utilise pas la cryptographie symétrique avec des clés codées en dur comme seule méthode de chiffrement.| x | x |
| **3.2** | MSTG-CRYPTO-2 | L'application utilise des implémentations de primitives cryptographiques éprouvées. | x | x |
| **3.3** | MSTG-CRYPTO-3 | L'application utilise des primitives cryptographiques appropriées au cas d'utilisation, configurées en adéquation avec les bonnes pratiques de l'industrie. | x | x |
| **3.4** | MSTG-CRYPTO-4 | L'application n'utilise pas de protocole ou d'algorithme de cryptographie considéré par la communauté comme déprécié pour des raisons de sécurité. | x | x |
| **3.5** | MSTG-CRYPTO-5 | L'application ne ré-utilise pas la même clé de cryptographie à des fins différentes. | x | x |
| **3.6** | MSTG-CRYPTO-6 | Toute valeur aléatoire est générée par un générateur de nombres aléatoires offrant un bon niveau de sécurité. | x | x |

## Références

Le Mobile Application Security Testing Guide de l'OWASP donne des instructions détaillées pour valider les exigences listées dans cette section.

- Android - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS - <https://github.com/OWASP/owasp-mastg/blob/master/Document/0x06e-Testing-Cryptography.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
