---
layout: page
title: common/git-clean (español)
description: "Elimina archivos sin rastrear del árbol de trabajo."
content_hash: bab60a68c818d750cb8d5c7d86946acbd1496538
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clean.html
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

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>

- Muestra que archivos serían borrados sin llegar a borrarlos:

`git clean --dry-run`

- Elimina forzosamente los archivos que no son rastreados por Git:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Elimina forzosamente los directorios que no son rastreados por Git:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` -d`

- Elimina archivos sin rastrear, incluyendo los archivos ignorados en `.gitignore` y los excluidos en `.git/info/exclude`:

`git clean -x`
