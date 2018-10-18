# Le Standard de Validation de la Sécurité des Applications Mobiles

Le MASVS peut être utilisé pour établir un niveau de confiance dans la sécurité des applications mobiles. Les exigences ont été développées avec les objectifs suivants à l'esprit :

* Utilisation en tant que métrique - Fournir un standard de sécurité pouvant servir de mesure aux développeurs d'applications mobiles et à ceux qui en sont responsables ;
* Utilisation en tant que référence - Donner des points de repère pendant toutes les phases de développement de test et de développement d'applications mobiles ;
* Utilisation en phase d'achat - Permettre de définir un niveau de sécurité minimal attendu lors de la validation de la sécurité d'applications mobiles. 

## Modèle de Sécurité Applicative Mobile

Le MASVS définit deux niveaux distincts de validation de la sécurité (L1 et L2) ainsi qu'un ensemble flexible d'exigences concernant la protection contre la rétro-ingénierie (MASVS-R), c'est-à-dire adaptable au modèle de menaces d'une application. MASVS-L1 et MASVS-L2 comprennent des exigences de sécurité génériques et sont recommandés pour toute application mobile (L1) ainsi que pour celles qui gèrent des données hautement sensibles (L2). MASVS-R couvre des contrôles de protection supplémentaires qui peuvent être mis en oeuvre dans le cas où la protection contre les menaces côté client est l'un des buts du design.

Atteindre les exigences du niveau MASVS-L1 amène à une application qui suit les bonnes pratiques de sécurité et ne souffre pas des vulnérabilités couramment rencontrées. MASVS-L2 ajoute de nouveaux contrôles en profondeur tels que le SSL pinning, permettant de rendre l'application résistante à des attaques plus sophistiquées - en supposant que les contrôles de sécurité du système d'exploitation mobile sont intacts et que l'utilisateur final n'est pas considéré en tant que l'attaquant potentiel. Implémenter tout ou partie des exigences de protection logicielles de la partie MASVS-R aide à réduire les menaces côté client où l'utilisateur final serait malicieux et/ou lorsque le système d'exploitation mobile serait corrompu.

**Il convient de noter que les contrôles de protection logiciels listés dans le MASVS-R et décrits dans le Guide de Test Mobile de l'OWASP (OWASP Mobile Testing Guide) peuvent toujours être contournés et ne doivent jamais être utilisés en tant que substituts aux contrôles de sécurité. Leur but est d'apporter des contrôles de protection supplémentaires spécifiques aux menaces d'applications qui remplissent aussi les exigences MASVS L1 ou L2.**

![Verification Levels](images/masvs-levels-new.jpg)

### Structure du Document

La première partie du MASVS contient une description du modèle de sécurité et des niveaux de validation disponibles, suivis par des recommandations sur l'utilisation du standard en pratique. Les exigences de sécurité détaillées, ainsi que leurs associations aux niveaux de validation, sont listées dans la seconde partie. Les exigences ont été groupées en huit catégories (V1 à V8) en fonction des objectifs et des périmètres techniques. La nomenclature suivanteest utilisée tout au long du MASVS et du MSTG:

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

#### Quel Typologie de Validation Utiliser?

L'implémentation des exigences MASVS L2 améliore la sécurité, mais peut en même temps augmenter les coûts de développement et dégrader potentiellement l'expérience utilisateur (un compromis classique). En général, L2 devrait être utilisé pour toute application où l'analyse risques vs coûts démontre le besoin d'atteindre ce niveau (i.e. lorsque les pertes potentielles causées par la compromission de la confidentialité ou de l'intégrité sont supérieures au coût induit par l'implémentation des contrôles de sécurité supplémentaires). L'évaluation des risques devrait être la première étape avant l'implémentation du MASVS.

##### Exemples

###### MASVS-L1

- All mobile apps. MASVS-L1 lists security best practices that can be followed with a reasonable impact on development cost and user experience. Apply the requirements in MASVS-L1 for any app that don't qualify for one of the higher levels.

###### MASVS-L2

- Health-Care Industry: Mobile apps that store personally identifiable information that can be used for identity theft, fraudulent payments, or a variety of fraud schemes. For the US healthcare sector, compliance considerations include the Health Insurance Portability and Accountability Act (HIPAA) Privacy, Security, Breach Notification Rules and Patient Safety Rule. 

- Financial Industry: Apps that enable access to highly sensitive information like credit card numbers, personal information, or allow the user to move funds. These apps warrant additional security controls to prevent fraud. Financial apps need to ensure compliance to the Payment Card Industry Data Security Standard (PCI DSS), Gramm Leech Bliley Act and Sarbanes-Oxley Act (SOX).

###### MASVS L1+R

- Mobile apps where IP protection is a business goal. The resiliency controls listed in MASVS-R can be used to increase the effort needed to obtain the original source code and to impede tampering / cracking.

- Gaming Industry: Games with an essential need to prevent modding and cheating, such as competitive online games. Cheating is an important issue in online games, as a large amount of cheaters leads to a disgruntled the player base and can ultimately cause a game to fail. MASVS-R provides basic anti-tampering controls to help increase the effort for cheaters.

###### MASVS L2+R

- Financial Industry: Online banking apps that allow the user to move funds, where techniques code injection and instrumentation on compromised devices pose a risk. In this case, controls from MASVS-R can be used to impede tampering, raising the bar for malware authors.

- All mobile apps that, by design, need to store sensitive data on the mobile device, and at the same time must support a wide range of devices and operating system versions. In this case, resiliency controls can be used as an defense-in-depth measure to increase the effort for attackers aiming to extract the sensitive data. 
