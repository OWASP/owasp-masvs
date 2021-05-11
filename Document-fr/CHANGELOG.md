# Changelog

## V1.3 - 11 May 2021

We are proud to announce the introduction of a new document build pipeline, which is major milestone for our project. The build pipeline is based on [Pandocker](https://github.com/dalibo/pandocker) and [Github Actions](https://github.com/OWASP/owasp-masvs/tree/master/.github/workflows). This significantly reduces the time spent on creating new releases. We would like to thank:

- Jeroen Willemsen for kick-starting this initiative last year!
- Damien Clochard and Dalibo for supporting and professionalizing the build pipeline.

The build pipeline will also be the foundation for the OWASP MSTG and will be made available for the OWASP ASVS project.

The following changes are part of release 1.3:

- 4 more translations are available, which are Hindi, Farsi, Portuguese and Brazilian Portuguese
- Added requirement MSTG-PLATFORM-11

## V1.2 - 7 Mars 2020 - Edition Internationale

Les changements suivants ont été intégrés dans la version 1.2:

- Traduction du MASVS en chinois simplifié disponible.
- Changement du titre en couverture du livre sur le MASVS.
- Suppression du Top 10 Mobile et de CWE du MSTG et fusion avec les références existantes dans le MASVS.

## V1.2-RC - 5 Octobre 2019 - Pre-release

Les changement suivants font partie de la livraison 1.2:

- Mise à jour des traductions du MASVS dans les langues suivantes: chinoise (ZHTW), anglaise, allemande, française, russe, espagnole et japonaise.
- Promu au statut flagship.
- Exigence changée : MSTG-STORAGE-1 "doivent être utilisées".
- Les exigences MSTG-STORAGE-13, MSTG-STORAGE-14, MSTG-STORAGE-15 sont ajoutées avec un accent sur la protection des données.
- Exigence MSTG-AUTH-11 mise à jour pour garder les informations contextuelles.
- Exigence MSTG-CODE-4 mise à jour pour avoir une couverture plus large que le déboggage seulement.
- Exigence MSTG-PLATFORM-10 ajoutée pour offrir une protection plus large à l'utilisation des WebViews.
- Exigence MSTG-AUTH-12 ajoutée pour rappeler aux développeurs d'implémenter l'autorisation, surtout pour les applications multi-utilisateurs.
- Ajout de quelques éléments concernant l'utilisation du MASVS pour une évaluation de risque.
- Ajout de quelques éléments concernant la sécurisation du contenu payant.
- Exigence MSTG-ARCH-11 ajoutée pour inclure une politique de divulgation responsable pour les applications L2.
- Exigence MSTG-ARCH-12 ajoutée pour rappeler les exigences provenant des lois et réglementations à travers le monde.
- Création d'un style cohérent pour toutes les références.
- Exigence MSTG-PLATFORM-11 ajoutée pour contrer les menaces pouvant provenir des claviers tiers.
- Exigence MSTG-RESILIENCE-13 pour offrir un niveau de contrôle supplémentaire avec du chiffrement au niveau applicatif afin d'entraver l'écoute par un attaquant.

## V1.1.4 - 4 Juillet 2019 - Summit edition

- Corrections d'erreurs de markdown.
- Mise à jour des traductions française et espagnole.
- Ajout d'une traduction chinoise et japonaise du journal des modifications.
- Vérification automatisée de la syntaxe markdown et de l'accessibilité des URLs.
- Ajout de codes d'identification aux exigences, qui seront inclus dans la future version du MSTG afin de trouver plus facilement les recommandations et les cas de test.
- Réduction de la taille du référentiel et ajout de Generated au .gitignore.
- Ajout d'un code de conduite et de directives contributives.
- Ajout d'un modèle de PR.
- Mise à jour de la synchronisation avec le référentiel utilisé pour l'hébergement du site Web sur Gitbook.
- Mise à jour des scripts pour générer les fichiers XML / JSON / CSV pour toutes les traductions.
- Traduit de l'avant-propos en chinois (ZHTW).

## V1.1.3 - Janvier 2019 - Quelques Améliorations

Les changements suivants font partie de la livraison 1.1.3 :

- Corrections d'erreurs de traduction de l'exigence 7.1 dans la version espagnole
- Nouvelle présentation des traducteurs dans les Remerciements
- Petites corrections pour la version japonaise.

## V1.1.2 - Janvier 2019 - Parrainage et internationalisation

Les changements suivants font partie de la livraison 1.1.2 :

- Ajout d'une note de remerciement pour les acheteurs de l'e-book.
- Ajout d'un lien d'authentification manquant & mise à jour d'un lien d'authentification obsolète dans la V4.
- Correction d'une inversion de 4.7 et de 4.8 en anglais.
- Premières livraisons internationales!
  - Corrections dans la traduction en espagnol. La traduction est dorénavant en phase avec la version anglaise (1.1.2).
  - Corrections dans la traduction en russe. La traduction est dorénavant en phase avec la version anglaise (1.1.2).
  - Ajout des premières livraisons en chinois (ZHTW), français, allemand et japonais!
- Simplification du document afin de faciliter la traduction.
- Ajout d'instructions pour les livraisons automatisées.

## V1.1.0 - 14 Juillet 2018

Les changements suivants font partie de la livraison 1.1 :

- L'exigence 2.6 "Le presse-papier est désactivé sur les champs de texte qui peuvent contenir des données sensibles." a été enlevée.
- L'exigence 2.2 "Aucune donnée sensible ne devrait être stockée hors du container de l'application ou des services de stockage de références fournis par le système." a été ajouté.
- L'exigence 2.1 a été reformulée vers "Les services de stockage de références fournis par le système sont utilisés de façon appropriée pour le stockage de données sensibles telles que les PII, les références des utilisateurs ou les clés de cryptographie.".

## V1.0 - 12 Janvier 2018

Les changements suivants font partie de la livraison 1.0 :

- Suppression de 8.9 en raison d'une redondance avec 8.12
- Reformulation de 4.6 pour la rendre plus générique
- Quelques améliorations (typos, etc.)
