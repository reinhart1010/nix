---
layout: page
title: common/docker-rm (español)
description: "Elimina contenedores."
content_hash: 2edbe3d9b299188ae706e233e003474818337290
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/common/docker-rm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker-rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker rm

Elimina contenedores.
Más información: <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Elimina los contenedores:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor1 contenedor2 ...</span>

- Elimina de manera forzada contenedores:

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor1 contenedor2 ...</span>

- Elimina un contenedor y sus volúmenes:

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor</span>

- Muestra la ayuda:

`docker rm --help`
