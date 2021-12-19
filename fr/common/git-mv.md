---
layout: page
title: common/git-mv (français)
description: "Déplacer ou renommer des fichiers inscrits dans l'index."
content_hash: 0a4404a105036204324e09fedb38240db4d961d6
related_topics:
  - title: English version
    url: /en/common/git-mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-mv.html
    icon: bi bi-globe
---
# git mv

Déplacer ou renommer des fichiers inscrits dans l'index.
Plus d'informations : <https://git-scm.com/docs/git-mv>.

- Déplace les fichiers dans l'index Git, valide au prochain commit :

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new/path/to/file</span>

- Renome un fichier et met a jour l'index, valide au prochain commit :

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_filename</span>

- Force l'écrasement d'un fichier :

`git mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cible</span>
