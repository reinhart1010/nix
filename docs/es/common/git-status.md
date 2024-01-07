---
layout: page
title: common/git-status (español)
description: "Muestra los cambios realizados en los archivos del repositorio Git."
content_hash: 451c1f74273dd085de3453fbf81a9277049b8650
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
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

Muestra los cambios realizados en los archivos del repositorio Git.
Lista los archivos cambiados, añadidos y eliminados comparándolos con el último commit.
Más información: <https://git-scm.com/docs/git-status>.

- Muestra los archivos cambiados que aún no han sido añadidos a un commit:

`git status`

- Muestra la salida en formato breve:

`git status -s`

- Muestra los archivos rastreados:

`git status --untracked-files=no`

- Muestra la salida en formato breve junto a la información del branch:

`git status --short --branch`
