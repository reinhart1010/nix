---
layout: page
title: common/git-grep (español)
description: "Encuentra dentro de archivos en cualquier parte del historial del repositorio."
content_hash: 373f21d3173bebf7d3faaaed782408668cf08d56
related_topics:
  - title: English version
    url: /en/common/git-grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-grep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-grep.html
    icon: bi bi-globe
---
# git-grep

Encuentra dentro de archivos en cualquier parte del historial del repositorio.
Acepta una gran cantidad de opciones, de la misma manera que el comando `grep`.
Más información: <https://git-scm.com/docs/git-grep>.

- Busca una cadena en los archivos rastreados:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>

- Busca una cadena en archivos que coincidan con un patrón entre los archivos rastreados:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_archivos</span>

- Busca una cadena en los archivos rastreados, incluyendo submodulos:

`git grep --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>

- Busca una cadena en un punto específico del historial:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>

- Busca una cadena a través de todas las ramas:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>` $(git rev-list --all)`
