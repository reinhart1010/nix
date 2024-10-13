---
layout: page
title: common/git-reflog (français)
description: "Affiche un log des changements locaux comme HEAD, tags et branches."
content_hash: e7ecccdda7dc80a54f6ef99865268f50a58832e4
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-reflog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reflog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reflog

Affiche un log des changements locaux comme HEAD, tags et branches.
Plus d'informations : <https://git-scm.com/docs/git-reflog>.

- Afficher le reflog de HEAD :

`git reflog`

- Affiche le reflog d'une branche spécifique :

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Affiche les 5 dernières entrées dans le reflog :

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--max-count</span>` 5`
