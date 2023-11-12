---
layout: page
title: common/git-status (français)
description: "Affiche les changements sur les fichiers dans la branche courante."
content_hash: 41a7d33aad9beaecfc1f32b2ed1cb9d6587e8cca
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-status.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-status.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-status.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-status.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git status

Affiche les changements sur les fichiers dans la branche courante.
Affiche les fichiers édités, déplacés, renommés, ajoutés, supprimés par rapport à la référence de la branche courante.
Plus d'informations : <https://git-scm.com/docs/git-status>.

- Affiche les fichiers modifiés qui n'ont pas encore été ajoutés pour le commit :

`git status`

- Affiche les fichiers modifiés (version courte) :

`git status -s`

- Affiche les fichiers modifiés, sans tenir des comptes des fichiers non-suivis :

`git status --untracked-files=no`

- Affiche les fichiers modifiés (version courte) avec les informations de branche :

`git status -sb`
