---
layout: page
title: common/git-status (español)
description: "Muestra los cambios realizados en los archivos del repositorio Git."
content_hash: 94e3b90e988cbf25075f4f6150cc5c9f5e59bebe
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
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
---
# git status

Muestra los cambios realizados en los archivos del repositorio Git.
Lista los archivos cambiados, añadidos y eliminados comparándolos con el último commit.
Más información: <https://git-scm.com/docs/git-status>.

- Muestra los archivos cambiados que aún no han sido añadidos a un commit:

`git status`

- Muestra la salida en formato breve:

`git status -s`

- No muestra los archivos sin rastrear en la salida:

`git status --untracked-files=no`

- Muestra la salida en formato breve junto a la información del branch:

`git status --short --branch`
