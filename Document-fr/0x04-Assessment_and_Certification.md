# Evaluation et Certification

## Position de l'OWASP Concernant la Certification selon le MASVS et les Labels de Confiance

L'OWASP, en tant qu'organisation à but non-lucratif et indépendante de toute influence commerciale, ne certifie aucun fournisseur, aucun organisme de référence ni aucun logiciel.

Toute sorte de garantie de confiance, label ou autre certification n'est pas cautionnée, soutenue ou donnée par l'OWASP ; ainsi toute organisation se reposant sur une telle approche doit être attentive à la confiance accordée à une tierce partie ou à un label de confiance affirmant avoir la certification ASVS.

Ceci ne doit pas empêcher les organisations d'offrir de tels services concernant la confiance, tant qu'elles ne revendiquent pas une certification officielle de la part de l'OWASP.

## Conseils pour la Certification d'Applications Mobiles

La façon recommandée pour vérifier la conformité d'une application mobile par rapport au MASVS est d'efffectuer une revue en mode "livre ouvert", ce qui signifie que les testeurs ont accès aux ressources clés telles que les architectes et les développeurs de l'application, la documentation du projet, le code source et un accès authentifié aux points terminaux, comprenant au moins un accès à un compte pour chaque rôle.

Il est important de noter que le MASVS ne couvre que les (côtés clients des) applications mobiles et leur communication avec les points terminaux distants, ainsi que quelques exigences génériques liées à l'authentification des utilisateurs et à la gestion des sessions. Il ne contient pas d'exigence spécifique aux services distants (e.g. services web) associés à l'application, à l'exception d'un nombre limité d'exigences génériques ayant trait à l'authentification et à la gestion des sessions. Ceci dit, le MASVS V1 spécifie le fait que les services distants doivent être couverts par un modèle de menaces d'ensemble et doivent être validés par des standards appropriés tels que l'ASVS de l'OWASP.

Une organisation certifiante doit inclure dans tout rapport le périmètre de la validation (en particulier quand un composant clé est hors de ce périmètre), un résumé des points principaux, incluant les tests passés avec succès ou en échec, avec de claires indications sur la manière de résoudre les tests en échec. La conservation de documents de travail détaillés, de copies d'écran ou de vidéos, de scripts permettant d'exploiter une vulnérabilité de façon fiable et répétée ainsi que de documents électroniques liés aux tests, tels que les journaux d'interception de proxies et les notes associées telles que les listes d'actions, est considérée comme une pratique standard de l'industrie. Il n'est pas suffisant de lancer simplement un outil et de faire un rapport sur les défauts signalés ; ceci n'amène pas suffisamment de preuves que tous les points pour un niveau de certification donné ont été testés de façon adéquate. En cas de désaccord, il devrait assez de preuves pour démontrer que chaque exigence validée a bien été testée.

### Utiliser le Guide de Test de Sécurité Mobile OWASP Mobile Application Security Testing Guide (MASTG)

Le MASTG de l'OWASP est un manuel pour tester la sécurité des applications mobiles. Il décrit les processus techniques pour valider les exigences listées dans le MASVS. Le MASTG comporte une liste de cas de tests, chacun relié à une exigence du MASVS. Tandis que les exigences du MASVS sont de haut niveau et génériques, le MASTG fournit des recommandations en profondeur et des procédures de test par type de système d'exploitation mobile.

### Le Role des Outils de Test Automatique

L'utilisation d'outils d'analyse de code source ou de test en boîte noire est encouragé dans le but d'améliorer l'efficacité dès que cela est possible. Cependant, il n'est pas possible de mener à bien toute la validation proposée par le MASVS en utilisant seulement des outils automatiques : chaque application mobile a ses spécificités et la compréhension de l'architecture d'ensemble, la logique d'affaire et les limites techniques des technologies et frameworks utilisés est obligatoire pour valider la sécurité d'une application.

## Autres Cas d'Utilisation

### En tant que Source de Conseils Détaillés pour l'Architecture de Sécurité

L'une des utilisations les plus courantes du MASVS est en tant que ressource pour les arhitectes de sécurité. Les deux référentiels principaux d'architecture de sécurité, SABSA et TOGAF, ne fournissent pas beaucoup d'information qui serait nécessaire à la revue de l'architecture de sécurité des applications mobiles.  Le MASVS peut être utilisé pour combler ces manques en permettant aux architectes de sécurité de choisir de meilleurs contrôles par rapport aux problèmes courants des applications mobiles.

### En tant que Substitut aux Listes de Contrôle pour le Codage de Sécurité

Un certain nombre d'organisations peuvent bénéficier de l'adoption du MASVS en choisissant l'un des deux niveaux, ou en s'appropriant le MASVS et en adaptant ce qui est nécessaire à chaque niveau de risque en fonction du domaine d'application ciblé. Nous encourageons ce type d'appropriation tant que la traçabilité est maintenue, de telle manière que si une application a passé l'exigence 4.1 la signification reste la même pour chaque copie lorsque le standard évolue.

### En tant que Base Méthodologique pour le Test de Sécurité

Une bonne méthodologie de test de sécurité pour application mobile devrait couvrir l'ensemble des exigences listées dans le MASVS. Le Mobile Application Security Testing Guide (MASTG) de l'OWASP fournit des cas de test en boîte noire et en boîte blanche pour la validation de chaque exigence.

### En tant que Guide pour les Tests Automatisés et les Tests d'Intégration

Le MASVS a été créé pour être hautement testable, à la seule exception des exigences architecturales. Les tests unitaires, d'intégration et d'acceptation basés sur lex exigences du MASVS peuvent être intégrés dans le cycle de développement continu. Ceci permet d'une part d'améliorer la sensibilisation à la sécurité des développeurs, mais aussi d'autre part d'améliorer la qualité globale de l'application cible et de réduire la quantité de défauts détectés pendant la phase de tests de sécurité avant la mise sur le marché.

### Pour la Formation au Développement de Sécurité

Le MASVS peut aussi être utilisé pour définir les caractéristiques de sécurité des applications mobiles. Un certain nombre de cours de "codage de sécurité" sont juste des cours de piratage éthique avec un soupçon de développement. Ceci n'est pas en faveur des développeurs. Au lieu de cela, les cours de développement de sécurité peuvent utiliser le MASVS, en se focalisant sur les contrôles proactifs documentés dans le MASVS, plutôt que par exemple sur les 10 principales erreurs de sécurité en développement.
