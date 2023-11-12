---
layout: page
title: common/gulp (français)
description: "Système d'exécution de tâches et de construction en continu pour JavaScript."
content_hash: cf7d59558da6fb841ed2a4db13079534b3402400
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/gulp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gulp

Système d'exécution de tâches et de construction en continu pour JavaScript.
Les tâches sont définies dans le fichier `gulpfile.js` à la racine du projet.
Plus d'informations : <https://github.com/gulpjs/gulp-cli>.

- Exécute la tâche par défaut :

`gulp`

- Exécute des tâches individuelles :

`gulp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tâche</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autre_tâche</span>

- Affiche l'arbre de dépendance des tâches pour le gulpfile chargé :

`gulp --tasks`
