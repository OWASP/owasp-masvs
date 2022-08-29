# Le Standard de Validation de la Sécurité des Applications Mobiles

Le MASVS peut être utilisé pour établir un niveau de confiance dans la sécurité des applications mobiles. Les exigences ont été développées avec les objectifs suivants à l'esprit :

- Utilisation en tant que métrique - Fournir un standard de sécurité pouvant servir de mesure aux développeurs d'applications mobiles et à ceux qui en sont responsables ;
- Utilisation en tant que référence - Donner des points de repère pendant toutes les phases de développement de test et de développement d'applications mobiles ;
- Utilisation en phase d'achat - Permettre de définir un niveau de sécurité minimal attendu lors de la validation de la sécurité d'applications mobiles.

## Modèle de Sécurité Applicative Mobile

Le MASVS définit deux niveaux distincts de validation de la sécurité (L1 et L2) ainsi qu'un ensemble flexible d'exigences concernant la protection contre la rétro-ingénierie (MASVS-R), c'est-à-dire adaptable au modèle de menaces d'une application. MASVS-L1 et MASVS-L2 comprennent des exigences de sécurité génériques et sont recommandés pour toute application mobile (L1) ainsi que pour celles qui gèrent des données hautement sensibles (L2). MASVS-R couvre des contrôles de protection supplémentaires qui peuvent être mis en oeuvre dans le cas où la protection contre les menaces côté client est l'un des buts du design.

Atteindre les exigences du niveau MASVS-L1 amène à une application qui suit les bonnes pratiques de sécurité et ne souffre pas des vulnérabilités couramment rencontrées. MASVS-L2 ajoute de nouveaux contrôles en profondeur tels que le SSL pinning, permettant de rendre l'application résistante à des attaques plus sophistiquées - en supposant que les contrôles de sécurité du système d'exploitation mobile sont intacts et que l'utilisateur final n'est pas considéré en tant que l'attaquant potentiel. Implémenter tout ou partie des exigences de protection logicielles de la partie MASVS-R aide à réduire les menaces côté client où l'utilisateur final serait malicieux et/ou lorsque le système d'exploitation mobile serait corrompu.

**I: Il convient de noter que les contrôles de protection logiciels listés dans le MASVS-R et décrits dans le Guide de Test Mobile de l'OWASP (OWASP Mobile Testing Guide) peuvent toujours être contournés et ne doivent jamais être utilisés en tant que substituts aux contrôles de sécurité. Leur but est d'apporter des contrôles de protection supplémentaires spécifiques aux menaces d'applications qui remplissent aussi les exigences MASVS L1 ou L2.**

**II: Il faut noter que les contrôles de protection des logiciels présentés dans le MASVS-R et décrits dans l'OWASP MASTG peuvent finalement être contournés et ne doivent jamais être utilisés comme alternative aux contrôles de sécurité. Par contre, ils sont conçus pour ajouter des contrôles supplémentaires envers des menaces spécifiques pour les applications qui satisfont aux exigences de MASVS-L1 et MASVS-L2.**

![Verification Levels](images/masvs-levels-new.jpg)

### Structure du Document

La première partie du MASVS contient une description du modèle de sécurité et des niveaux de validation disponibles, suivis par des recommandations sur l'utilisation du standard en pratique. Les exigences de sécurité détaillées, ainsi que leurs associations aux niveaux de validation, sont listées dans la seconde partie. Les exigences ont été groupées en huit catégories (V1 à V8) en fonction des objectifs et des périmètres techniques. La nomenclature suivanteest utilisée tout au long du MASVS et du MASTG:

- *Catégorie de l'exigence :* MASVS-Vx, e.g. MASVS-V2: Stockage de Données et Vie Privée
- *Exigence :* MASVS-Vx.y, e.g. MASVS-V2.2: "Aucune donnée sensible n'est écrite dans les journaux applicatifs."  

### Niveaux de Validation en Détail

#### MASVS-L1: Sécurité Standard

Une application mobile qui remplit les exigences de niveau MASVS-L1 implémente les bonnes pratiques de sécurité de développement d'applications mobiles. Elle implémente les exigences de base en termes de qualité de code, de gestion de données sensibles et d'intéraction avec l'environnement mobile. Un processus de test doit être en place pour valider la bonne implémentation des contrôles de sécurité. Ce niveau convient à tout type d'application mobile.

#### MASVS-L2: Défense en Profondeur

MASVS-L2 introduit des contrôles de sécurité plus poussés qui vont au delà des exigences courantes. Pour atteindre le niveau L2, un modèle de menaces doit exister et la sécurité doit faire partie intégrale de l'architecture de l'application et de son design. Ce niveau est approprié pour des applications qui manipulent des données sensibles telles que les applications mobiles bancaires.

#### MASVS-R: Résistance à la Rétro-Ingénierie et à la Manipulation

L'application implémente des contrôles au niveau de l'état de l'art en matière de sécurité, et est aussi résistante à des attaques clairement spécifiques au côté client telles que la manipulation, le moddage ou la rétro-ingénierie visant à extraire des parties de code ou des données sensibles. Une telle application met en oeuvre des fonctions de sécurité matérielles ou des techniques de protection logicielles vérifiables et offrant un bon niveau de robustesse. MASVS-R est applicable aux applications qui gèrent des données sensibles et peut servir de moyen de protection de propriété intellectuelle ou contre la manipulation d'une application.

### Utilisation Recommandée

Les applications peuvent être validées par rapport à MASVS L1 ou L2 en fonction des évaluations de risque précédentes et du niveau de sécurité requis. L1 s'applique à tout type d'application mobile tandis que L2 est générallement recommandé pour des applications qui gèrent des données ou des fonctionnalités plus sensibles. MASVS-R (ou du moins une partie) peut être appliqué pour la validation de la résistance à des menaces spécifiques telles que le ré-empaquetage ou l'extraction de données sensibles, *en plus* d'une validation de sécurité appropriée.

En résumé, les typologies de validation suivantes sont disponibles :

- MASVS-L1
- MASVS-L1+R
- MASVS-L2
- MASVS-L2+R

Les différents combinaisons reflètent différents niveaux de sécurité et de résistance. Le but est de permettre une certaine flexibilité : par exemple, un jeu sur mobile pourrait se permettre de ne pas ajouter les contrôles de sécurité MASVS-L2 tels que l'authentification à 2 facteurs pour des considérations de facilité d'utilisation mais pourrait avoir de forts besoins commerciaux concernant la protection contre la manipulation.

#### Determiner la Typologie de Validation à Utiliser

L'implémentation des exigences MASVS L2 améliore la sécurité, mais peut en même temps augmenter les coûts de développement et dégrader potentiellement l'expérience utilisateur (un compromis classique). En général, L2 devrait être utilisé pour toute application où l'analyse risques vs coûts démontre le besoin d'atteindre ce niveau (i.e. lorsque les pertes potentielles causées par la compromission de la confidentialité ou de l'intégrité sont supérieures au coût induit par l'implémentation des contrôles de sécurité supplémentaires). L'évaluation des risques devrait être la première étape avant l'implémentation du MASVS.

<!-- \pagebreak -->

##### Exemples

###### MASVS-L1

- Pour tout type d'application mobile. MASVS-L1 liste les bonnes pratiques de sécurité qui peuvent être suivies avec un impact raisonnable sur les coûts de développement et l'expérience utilisateur. Il est conseillé d'appliquer les exigences de MASVS-L1 pour toute application qui n'a pas vocation à implémenter les exigences des niveaux supérieurs.

###### MASVS-L2

- Industrie de la Santé : Applications mobiles qui stockent des données personnelles (PII) pouvant être utilisées pour du vol d'identité, des paiements frauduleux ou tout autre type de fraude. Pour le secteur de la santé américain, les considérations de conformité incluent Health Insurance Portability and Accountability Act (HIPAA) ainsi que les règlementations sur le respect de la vie privée, la sécurité, la notification des pertes de données et la sûreté des patients.

- Industrie Financière : Applications mobiles qui donnent accès à des informations hautement sensibles telles que des numéros de cartes de crédit, des informations personnelles ou permettent des mouvements de fonds. Ces applications justifient l'implémentation de contrôles de sécurité additionnels pour contrer la fraude. Les applications du monde de la finance doivent être conformes au standard Payment Card Industry Data Security Standard (PCI DSS), au Gramm Leech Bliley Act et au Sarbanes-Oxley Act (SOX).

###### MASVS L1+R

- Applications mobiles où la protection de la propriété intellectuelle est un objectif commercial. Les contrôles contribuant à la résistance listés dans MASVS-R peuvent être utilisés pour augmenter la quantité d'effort requis pour obtenir le code source d'origine et pour entraver les possibilités de manipulation / de piratage.

- Industrie du Jeu : Jeux présentant un fort besoin d'empêcher le moddage et la triche, tels que les jeux de compétition en ligne. La triche est un problème majeur pour les jeux en ligne dans la mesure où un nombre important de tricheurs peut amener à mécontenter la majorité des joueurs et peut entraîner l'échec d'un jeu. MASVS-R fournit des contrôles de base contre la manipulation pour rendre la possibilité de triche plus compliquée.

###### MASVS L2+R

- Industrie Financière : Applications de banque en ligne permettant aux utilisateurs de transférer des fonds et où les techniques d'injection de code et d'instrumentation sur des appareils mobiles compromis entraînent un risque. Dans ce cas, les contrôles du MASVS-R peuvent être mis en oeuvre pour empêcher la manipulation et rendre la vie des créateurs de logiciels malveillants (malwares) plus compliquée.

- Toute application mobile qui, par design, doit stocker des données sensibles sur l'appareil mobile tout en devant fonctionner pour une large game d'appareils et de versions de systèmes d'exploitation. Dans ce cas, des contrôles de résistance peuvent être utilisés en tant que mesures de défense en profondeur pour augmenter la quantité d'effort que doivent fournir les attaquants voulant extraire les données sensibles.

- Les applications avec des fonctionnalités d'achat intégrées doivent idéalement utiliser le côté serveur et les exigences MASVS-L2 pour protéger le contenu payant. Néanmoins, dans quelques cas il est impossible d'utiliser la protection côté serveur. Dans ce cas, les exigences MASVS+R doivent être appliquées en plus des exigences de base pour augmenter les efforts de la rétro-ingénierie et / ou de la manipulation de code.
