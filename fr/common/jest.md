---
layout: page
title: common/jest (français)
description: "Une plateforme de test JavaScript sans configuration."
content_hash: 2914de236508d7cf7817c031aae0e8854553db22
related_topics:
  - title: English version
    url: /en/common/jest.html
    icon: bi bi-globe
---
# jest

Une plateforme de test JavaScript sans configuration.
Plus d'informations : <https://jestjs.io>.

- Exécuter tous les tests disponibles :

`jest`

- Exécuter les suites de test de fichiers donnés :

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier2</span>

- Exécuter les suites de test pour des fichiers, dans le répertoire courant et ses sous-répertoires, dont le chemin correspond à l'expression régulière indiquée :

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_régulière</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_régulière</span>

- Exécuter les tests dont les noms correspondent aux expressions régulières indiquées :

`jest --testNamePattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_test</span>

- Exécuter les suites de test associées à un fichier source donné :

`jest --findRelatedTests `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_source.js</span>

- Exécuter les suites de test associées à tous les fichiers non commités :

`jest --onlyChanged`

- Surveiller les changements sur les fichiers et ré-exécuter les tests associés :

`jest --watch`

- Montrer l'aide :

`jest --help`
