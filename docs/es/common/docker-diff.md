---
layout: page
title: common/docker-diff (español)
description: "Inspecciona cambios en archivos o directorios en el sistema de archivos de un contenedor."
content_hash: 67fdfc45a66a63c2392f8fbe4d327195a9fc0ee5
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/common/docker-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-diff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-diff.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker-diff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-diff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker diff

Inspecciona cambios en archivos o directorios en el sistema de archivos de un contenedor.
Más información: <https://docs.docker.com/reference/cli/docker/container/diff/>.

- Inspecciona los cambios en un contenedor desde que se creó:

`docker diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor</span>

- Muestra la ayuda:

`docker diff --help`
