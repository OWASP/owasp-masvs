# V7: Exigences Concernant la Qualité du Code et les Paramètres de Génération

## Objectif de Contrôle

Le but de ce contrôle est d'assurer que les pratiques de codage de base concernant la sécurité sont suivies pendant le développement de l'application et que les fonctionnalités de sécurité "gratuites" fournies par le compilateur sont activées.

## Exigences pour la Validation de la Sécurité

| # | MSTG-ID | Description |1 | L2 |
| --- | --- | --- | --- | --- |
| **7.1** | MSTG‑CODE‑1 | L'application est signée et livrée avec un certificat en cours de validité, dont la clé privée est correctement protégée. | ✓ | ✓ |
| **7.2** | MSTG‑CODE‑2 | L'application a été générée en mode release avec des réglages appropriés à ce mode (c.a.d. sans les possibilités de déboggage). | ✓ | ✓ |
| **7.3** | MSTG‑CODE‑3 | Les symboles pour le déboggage ont été enlevés des binaires natifs. | ✓ | ✓ |
| **7.4** | MSTG‑CODE‑4 | Le code de déboggage a été enlevé de l'application et celle-ci ne journalise ni de messages d'erreur inutilement longs ni de messages de déboggage. | ✓ | ✓ |
| **7.5** | MSTG‑CODE‑5 | Tous les composants utilisés par l'application provenant de sources externes, notamment les librairies et les frameworks, ont été identifiés et analysés à la recherche de vulnérabilités connues. | ✓ | ✓ |
| **7.6** | MSTG‑CODE‑6 | L'application intercepte et gère les exceptions potentielles.| ✓ | ✓ |
| **7.7** | MSTG‑CODE‑7 | La logique de gestion des erreurs dans les contrôles de sécurité refuse tout accès par défaut. | ✓ | ✓ |
| **7.8** | MSTG‑CODE‑8 | Dans le code non-géré, la mémoire est allouée, libérée et utilisée de façon sécurisée.  | ✓ | ✓ |
| **7.9** | MSTG‑CODE‑9 | Les fonctionnalités de sécurité intégrées dans les outils de la chaîne de génération, par exemple ceux pour la minification de byte-code, pour la protection de la pile, pour le support PIE ou le comptage de références automatiques, sont activées. | ✓ | ✓ |

<div style="page-break-after: always;"></div>

## Références

Le Mobile Security Testing Guide de l'OWASP (guide de test de la Sécurité mobile) fournit des instructions détaillées pour valider les exigences listées dans cette section.

- Android - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M7 - Qualité du Code Client: <https://www.owasp.org/index.php/Mobile_Top_10_2016-M7-Poor_Code_Quality>
- CWE: <https://cwe.mitre.org/data/definitions/119.html>
- CWE: <https://cwe.mitre.org/data/definitions/89.html>
- CWE: <https://cwe.mitre.org/data/definitions/388.html>
- CWE: <https://cwe.mitre.org/data/definitions/489.html>
