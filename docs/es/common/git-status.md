---
layout: page
title: common/git-status (español)
description: "Muestra los cambios realizados en los archivos del repositorio Git."
content_hash: d80a87f8402ad0b5f2dd98589a734559613ffc3a
last_modified_at: 2024-11-03
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
  - title: 한국어 version
    url: /ko/common/git-status.html
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
Lista los archivos cambiados, añadidos y eliminados comparándolos con la confirmación (commit) actual.
Más información: <https://git-scm.com/docs/git-status>.

- Muestra los archivos modificados que aún no se han añadido para hacer una confirmación (commit):

`git status`

- Muestra la salida en formato breve:

`git status --short`

- Muestra información detallada sobre cambios tanto en el área de preparación (staging) como en el directorio de trabajo:

`git status --verbose --verbose`

- Muestra la rama (branch) e información de seguimiento:

`git status --branch`

- Muestra la salida en formato breve junto a la información de la rama (branch):

`git status --short --branch`

- Muestra el número de entradas en rama temporal (stash):

`git status --show-stash`

- Muestra los archivos rastreados, excluyendo los no rastreados (untracked):

`git status --untracked-files=no`
