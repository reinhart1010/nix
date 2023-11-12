---
layout: page
title: common/git-clean (español)
description: "Elimina archivos sin rastrear del árbol de trabajo."
content_hash: 50b16d51af3e705ff7c1cdc8cebd330bfa2b26e7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clean

Elimina archivos sin rastrear del árbol de trabajo.
Más información: <https://git-scm.com/docs/git-clean>.

- Elimina archivos que no son rastreados por Git:

`git clean`

- Elimina interactivamente archivos que no son rastreados por Git:

`git clean -i`

- Muestra que archivos serían borrados sin llegar a borrarlos:

`git clean --dry-run`

- Elimina forzosamente los archivos que no son rastreados por Git:

`git clean -f`

- Elimina forzosamente los directorios que no son rastreados por Git:

`git clean -fd`

- Elimina archivos sin rastrear, incluyendo los archivos ignorados en `.gitignore` y los excluidos en `.git/info/exclude`:

`git clean -x`
