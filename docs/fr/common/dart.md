---
layout: page
title: common/dart (français)
description: "Ligne de commande pour gérer un projet Dart."
content_hash: 03e4f6dffc560ae92969648b2cdf195b6fe2169f
related_topics:
  - title: Deutsch version
    url: /de/common/dart.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dart.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dart

Ligne de commande pour gérer un projet Dart.
Plus d'informations : <https://dart.dev/tools/dart-tool>.

- Initialise un nouveau projet Dart dans un dossier du même nom :

`dart create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_projet</span>

- Exécuter un fichier Dart :

`dart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.dart</span>

- Télécharger les dépendences pour le projet courant :

`dart pub get`

- Exécuter les tests unitaire pour le projet courant :

`dart test`

- Mettre à jour les dépendances d'un projet pour supporter null-safety :

`dart pun upgrade --null-safety`

- Compiler un fichier Dart vers un binaire natif :

`dart compile exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.dart</span>
