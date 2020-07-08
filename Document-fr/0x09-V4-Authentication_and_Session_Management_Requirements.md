# V4: Exigences Concernant l'Authentification et la Gestion des Sessions

## Objectif de Contrôle

Dans la plupart des cas, la connexion des utilisateurs à un service distant doit être appréhendée au niveau de l'architecture générale des applications mobiles. Même si la majorité de la logique se passe sur le point terminal, le MASVS définit des exigences de base concernant la manière de gérer les comptes et les sessions des utilisateurs.

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Si l'application donne accès aux utilisateurs à un service distant, un certain niveau d'authentification, tel que l'authentification par nom d'utilisateur / mot de passe, est faite sur le point terminal distant. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | Si des sessions avec état sont utilisées, le point terminal distant utilise des identifiants de session aléatoirement générés pour authentifier les requêtes des clients sans avoir à envoyer les références des utilisateurs.  | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | Si l'authentification sans état basée sur des jetons est utilisée, le serveur fournit des jetons qui ont été signés par un algorithme à la sécurité éprouvée. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | Le point terminal distant met fin à la session existante lorsque l'utilisateur se déconnecte. | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | Une politique de mot de passe existe et est appliquée sur le point terminal distant. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | Le point terminal distant implémente un mécanisme permettant la protection contre les essais répétés de références utilisateurs. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | Les sessions sont dévalidées sur le point terminal distant après une période d'inactivité donnée et les jetons d'accès associés expirent. | ✓ | ✓ |
| **4.8** | MSTG-AUTH-8 | L'authentification biométrique, lorsqu'elle est utilisée, n'est pas basée sur des évènements (c'est-à-dire l'utilisation d'une API qui retourne simplement "vrai" ou "faux"). A la place, son utilisation est basée sur le déverrouillage du trousseau d'accès / du magasin de clé (keychain / keystore). |   | ✓ |
| **4.9** | MSTG-AUTH-9 | Un second facteur d'authentification est disponible sur le point terminal distant et l'exigence d'authentification à deux facteurs est mise en application de façon systématique.  |   | ✓ |
| **4.10** | MSTG-AUTH-10 | Les transactions sensibles requièrent une authentification améliorée.  |   | ✓ |
| **4.11** | MSTG-AUTH-11 | L'application informe les utilisateurs de toutes les activités critiques sur leurs comptes. Les utilisateurs ont accès à la liste des appareils utilisés pour accéder à leurs comptes, accès aux informations contextuelles (adresse IP, localisation, etc...), et peuvent bloquer certains appareils. |  | ✓ |
| **4.12** | MSTG-AUTH-12 | Des modèles d'autorisation doivent être définis et mis en oeuvre au niveau du point terminal distant. | ✓ | ✓ |

## Références

Le Mobile Security Testing Guide de l'OWASP (guide de test de la Sécurité mobile) fournit des instructions détaillées pour valider les exigences listées dans cette section.

- Général : Authentification et gestion des sessions - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Pour Android : Tester l'authentification locale - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- Pour iOS : Tester l'authentification locale - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>
