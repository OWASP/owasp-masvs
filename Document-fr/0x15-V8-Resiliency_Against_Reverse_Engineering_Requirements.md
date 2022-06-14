# V8: Exigences Concernant la Résilience

## Objectif de Contrôle

Cette section couvre des mesures de défense en profondeur recommandées dans les cas d'applications qui traitent ou donnent accès à des données ou des fonctionnalités sensibles. L'absence de l'un de ces contrôles n'entraîne pas une vulnérabilité dans la mesure où ils ont pour seul but d'améliorer la résilience de l'application envers la rétro-ingénierie et autres attaques spécifiques côté client.

Les contrôles de cette section devraient être mis en oeuvre autant qu'il est nécessaire, c'est-à-dire tel que requis par une évaluation des risques dûs à une modification non-autorisée de l'application et /ou une rétro-ingénierie du code. Nous ne pouvons que suggérer la consultation du document de l'OWASP "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention" ("Risques Techniques Liés à la Rétro-Ingénierie et Modification de Code Non-Autorisée Rétro-Ingénierie et Prévention de Modification de Code", voir les références ci-dessous) pour une liste des risques liés aux affaires et des menaces techniques associées.

**Il convient de noter que les mécanismes de protection logiciels ne doivent jamais être utilisés en tant que substituts aux contrôles de sécurité. Les contrôles listés dans le MASVR-R ont pour intention de rajouter aux applications des mécanismes de protection supplémentaires, spécifiques à une menace donnée, qui sont compatibles avec les exigences de sécurité du MASVS.**

Il convient de prendre en compte les considérations suivantes :

1. Un modèle de menace doit exister et souligner clairement les menaces côté client contre lesquelles il faut se défendre. De plus, le niveau de protection à atteindre doit être spécifié. Par exemple, un but bien défini pourrait être de forcer les auteurs d'un logiciel malveillant ciblant une application et cherchant à l'instrumenter de devoir investir un effort significatif de rétro-ingénierie manuelle.

2. Le modèle de menaces doit être porteur de sens. Par exemple, cacher une clé de cryptographie dans une implémentation en boîte-blanche n'est pas cohérent dans le cas où l'attaquant a la possiblité de récupérer l'ensemble du code et de l'analyser dans son ensemble.

3. L'efficacité de la protection devrait toujours être validée par un expert humain ayant l'expérience du test des moyens particuliers mis en oeuvre contre la modification du code ou son obscurcissement (voir aussi les chapitres liés à la "rétro-ingénierie" et à la "validation des protections logicielles" dans le Mobile Security Testing Guide).

### Entraver l'Analyse Dynamique et la Modification

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | L'application détecte et réagit à la présence d'appareils rootés ou jailbreakés soit en alertant l'utilisateur ou en mettant fin à l'application. | x |
| **8.2** | MSTG-RESILIENCE-2 | L'application empêche le déboggage et / ou réagit à la présence d'un déboggeur. Tous les protocoles de déboggage disponibles doivent être couverts. | x |
| **8.3** | MSTG-RESILIENCE-3 | L'application détecte et réagit à la modification de fichiers exécutables et de données critiques au sein de son bac à sable. | x |
| **8.4** | MSTG-RESILIENCE-4 | L'application détecte et réagit à la présence d'outils et de frameworks de rétro-ingénierie courants sur l'appareil.| x |
| **8.5** | MSTG-RESILIENCE-5 | L'application détecte et réagit à son exécution dans un émulateur.  | x |
| **8.6** | MSTG-RESILIENCE-6 | L'application détecte et réagit à la modification de code et de données dans son espace mémoire. | x |
| **8.7** | MSTG-RESILIENCE-7 | L'application implémente plusieurs mécanismes parmi les catégories de défense (8.1 à 8.6). Il convient de noter que la résilience augmente avec la quantité et la diversité de l'originalité des mécanismes utilisés. | x |
| **8.8** | MSTG-RESILIENCE-8 | Les mécanismes de détection déclenchent des réponses de différents types, notamment des réponses invisibles de retardement de l'attaque. | x |
| **8.9** | MSTG-RESILIENCE-9 | L'obscurcissement est mis en oeuvre par des défenses programmatiques qui, à leur tour, entravent le dé-obscurcissement via l'analyse dynamique.  | x |

### Liaison avec un Appareil

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | L'application implémente un mécanisme de 'liaison avec l'appareil' utilisant une empreinte de l'appareil dérivée de multiples propriétés uniques à cet appareil. | x |

### Entraver la Compréhension

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 |Tous les fichiers exécutables et les librairies appartenant à l'application sont soit chiffrés au niveau du fichier et / ou le code important et les segments de données à l'intérieur des exécutables sont chiffrés ou compactés. Une analyse statique triviale ne révèle pas de code important ou de données. | x |
| **8.12** | MSTG-RESILIENCE-12 | Si le but de l'obscurcissement est de protéger des traitements sensibles, le schéma d'obscurcissement utilisé est à la fois approprié à la tâche considérée et est résistant envers les méthodes de dé-obscurcissement manuelles et automatiques, en prenant en considération les recherches disponibles. L'efficacité du schéma d'obscurcissement doit être validée à travers du test manuel. Il convient de noter que les fonctionnalités d'isolation au niveau matériel doivent être mises en pratique de préférence à l'obscurcissement toutes les fois que cela est possible. | x |

### Entraver l'écoute

| # | MSTG-ID | Description | R |
| -- | ----------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | Pour une défense en profondeur, en plus d'avoir un durcissement efficace des parties communicantes, le chiffrement des données utilisées au niveau de l'application peut être appliqué pour entraver l'écoute. | x |

## Références

Le Mobile Security Testing Guide de l'OWASP (guide de test de la Sécurité mobile) fournit des instructions détaillées pour valider les exigences listées dans cette section.

- Android : Tester la résilience contre la rétro-ingénierie - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS : Tester la résilience contre la rétro-ingénierie - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

Pour de plus amples informations, il est possible de consulter aussi :

- OWASP Mobile Top 10: M8 (Modification du Code) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Rétro-Ingénierie) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
