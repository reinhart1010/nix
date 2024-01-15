---
layout: page
title: common/git-branch (français)
description: "Commande Git principale pour travailler avec des branches."
content_hash: 0313f8c27b71d46204498bb0f2c89884a0ccc06a
last_modified_at: 2024-01-15
related_topics:
  - title: Deutsch version
    url: /de/common/git-branch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-branch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-branch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-branch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-branch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git branch

Commande Git principale pour travailler avec des branches.
Plus d'informations : <https://git-scm.com/docs/git-branch>.

- Liste toutes les branches (locale et distantes) :

`git branch --all`

- Affiche le nom de la branche courante :

`git branch --show-current`

- Crée une nouvelle branche depuis le commit courant :

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Crée une nouvelle branche depuis un commit en particulier :

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>

- Renommer une branche (ne pas se trouver sur la branche pour le faire) :

`git branch -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_nom_de_branche</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_nom_de_branche</span>

- Supprimer un branche locale (ne pas se trouver sur la branche pour le faire) :

`git branch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Supprimer une branche distante :

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche_distante</span>
