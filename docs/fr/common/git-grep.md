---
layout: page
title: common/git-grep (français)
description: "Rechercher une occurrence de texte n'importe où dans l'historique d'un dépôt git."
content_hash: b31e20dba9fb8d38ef2fb8282a3906c6cd093bb3
related_topics:
  - title: English version
    url: /en/common/git-grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-grep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-grep.html
    icon: bi bi-globe
---
# git-grep

Rechercher une occurrence de texte n'importe où dans l'historique d'un dépôt git.
Comprend la plupart des arguments du `grep` classique.
Plus d'informations : <https://git-scm.com/docs/git-grep>.

- Rechercher une occurrence dans les fichiers suivis :

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaine_recherché</span>

- Rechercher une occurrence dans les fichiers suivis d'après un pattern de fichiers :

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaine_recherché</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_glob_pattern</span>

- Rechercher une occurrence dans les fichiers suivis et les sous-modules :

`git grep --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaine_recherché</span>

- Rechercher une occurrence à partir d'un point spécifique dans l'historique :

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaine_recherché</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>

- Rechercher une occurrence dans toutes les branches :

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaine_recherché</span>` $(git rev-list --all)`
