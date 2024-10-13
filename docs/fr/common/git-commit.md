---
layout: page
title: common/git-commit (français)
description: "Enregistrer (`commit`) les fichiers dans le dépôt."
content_hash: 0759514b15e164dc4f23ba7a4e156c9ee790eb4c
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git commit

Enregistrer (`commit`) les fichiers dans le dépôt.
Plus d'informations : <https://git-scm.com/docs/git-commit>.

- Commit les fichiers en stage dans le dépôt avec un message :

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Commit tous les fichiers modifiés avec un message :

`git commit -am "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Met à jour le dernier commit avec les modifications en stage :

`git commit --amend`

- Commit seulement les fichiers spécifiés (qui sont déjà en stage) :

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/mon/fichier1 chemin/vers/mon/fichier2 ...</span>
