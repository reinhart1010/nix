---
layout: page
title: common/docker-rm (español)
description: "Elimina contenedores."
content_hash: 2edbe3d9b299188ae706e233e003474818337290
last_modified_at: 2024-11-27
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
tldri18n_status: 2
---
# docker rm

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
