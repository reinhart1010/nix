---
layout: page
title: common/ruby (français)
description: "Interpréteur du langage de programmation Ruby."
content_hash: 46a834498e2c7bd9c6848eaafa929daa9eb52de2
last_modified_at: 2023-10-08
related_topics:
  - title: English version
    url: /en/common/ruby.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ruby.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ruby.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ruby

Interpréteur du langage de programmation Ruby.
Voir aussi : `gem`, `bundler`, `rake`, `irb`.
Plus d'informations : <https://www.ruby-lang.org>.

- Exécute un script Ruby :

`ruby `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.rb</span>

- Exécute une seule commande Ruby dans la ligne de commande :

`ruby -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Vérifie les erreurs de syntaxe d'un script Ruby donné :

`ruby -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.rb</span>

- Démarre le serveur HTTP intégré sur le port 8080 dans le répertoire actuel :

`ruby -run -e httpd`

- Exécute localement un binaire Ruby sans installer la bibliothèque requise dont il dépend :

`ruby -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_bibliothèque</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_chargement_bibliothèque</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_bin/nom_bin</span>

- Affiche la version de Ruby utilisée :

`ruby -v`
