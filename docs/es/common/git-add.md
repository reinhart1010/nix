---
layout: page
title: common/git-add (español)
description: "Añade los archivos cambiados al índice."
content_hash: 55623bcb3a6ab1c9881c0385a129e7972834a65e
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
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
tldri18n_status: 2
---
# git add

Añade los archivos cambiados al índice.
Más información: <https://git-scm.com/docs/git-add>.

- Añade un archivo al índice:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Añade todos los archivos (rastreados o no):

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-A|--all</span>

- Añade todos los archivos en el directorio actual:

`git add .`

- Añade únicamente los archivos ya rastreados:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--update</span>

- Añade también los archivos ignorados:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Añade interactivamente partes de archivos al área de preparación (staging):

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--patch</span>

- Añade interactivamente partes de un archivo dado al área de preparación (staging):

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--patch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Añade un archivo interactivamente al área de preparación (staging):

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>
