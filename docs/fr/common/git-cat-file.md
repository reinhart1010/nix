---
layout: page
title: common/git-cat-file (français)
description: "Fournir des informations sur le contenu ou le type et la taille des objets du dépôt Git."
content_hash: 9f10d61a197f90362d7f77c96ed615083d328366
related_topics:
  - title: English version
    url: /en/common/git-cat-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cat-file.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cat-file.html
    icon: bi bi-globe
---
# git cat-file

Fournir des informations sur le contenu ou le type et la taille des objets du dépôt Git.
Plus d'informations : <https://git-scm.com/docs/git-cat-file>.

- Obtenir la taille [s] du commit HEAD en octets :

`git cat-file -s HEAD`

- Obtenir le type [t] (blob, tree, commit, tag) d'un objet Git spécifié :

`git cat-file -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8c442dc3</span>

- Affiche le contenu [p] d'un objet Git basé sur son type :

`git cat-file -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>
