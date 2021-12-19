---
layout: page
title: common/git-clean (français)
description: "Supprimer les fichiers non-suivis d'un dépôt Git."
content_hash: 9577b65135cd4923aeae806ecc4ad9ba7ad8704b
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
---
# git clean

Supprimer les fichiers non-suivis d'un dépôt Git.
Plus d'informations : <https://git-scm.com/docs/git-clean>.

- Supprimer les fichiers non-suivis :

`git clean`

- Supprimer les fichiers non-suivis de manière interactive :

`git clean -i`

- Affiche les fichiers non-suivis qui peuvent être supprimés :

`git clean --dry-run`

- Nettoyage forcé des fichiers non-suivis :

`git clean -f`

- Nettoyage forcé des répertoires non-suivis :

`git clean -fd`

- Supprime tous les fichiers suivis, incluant ceux répertoriés par `.gitignore` et `.git/info/exclude` :

`git clean -x`
