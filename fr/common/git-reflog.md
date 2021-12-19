---
layout: page
title: common/git-reflog (français)
description: "Affiche un log des changements locaux comme HEAD, tags et branches."
content_hash: 62f2127ce84fb29bd4b1b0470fca59d20ca8e354
related_topics:
  - title: English version
    url: /en/common/git-reflog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reflog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reflog.html
    icon: bi bi-globe
---
# git reflog

Affiche un log des changements locaux comme HEAD, tags et branches.
Plus d'informations : <https://git-scm.com/docs/git-reflog>.

- Afficher le reflog de HEAD :

`git reflog`

- Affiche le reflog d'une branche spécifique :

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Affiche les 5 dernières entrées dans le reflog :

`git reflog -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
