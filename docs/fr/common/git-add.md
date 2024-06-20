---
layout: page
title: common/git-add (français)
description: "Ajoute les fichiers modifiés à l'index."
content_hash: 2a75c698b97fd967e02058794c97e6bb1911ae5d
last_modified_at: 2024-06-20
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git add

Ajoute les fichiers modifiés à l'index.
Plus d'informations : <https://git-scm.com/docs/git-add>.

- Ajouter un fichier à l'index :

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Ajouter tous les fichiers (suivis et non-suivis) :

`git add -A`

- Ajoute les modifications des fichiers déjà suivis :

`git add -u`

- Ajoute aussi les fichiers ignorés :

`git add -f`

- Ajoute des parties de fichiers interactivement :

`git add -p`

- Ajoute interactivement les parties d'un fichier spécifié :

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Ajouter un fichier interactivement :

`git add -i`
