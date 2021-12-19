---
layout: page
title: common/docker-image (italiano)
description: "Gestisci immagini Docker."
content_hash: cf0178ff3880db1b3563a7e88a7a2ef3b8130cf8
related_topics:
  - title: Deutsch version
    url: /de/common/docker-image.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-image.html
    icon: bi bi-globe
---
# docker image

Gestisci immagini Docker.
Vedi anche `docker build`, `docker import` e `docker pull`.
Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/image/>.

- Elenca tutte le immagini Docker locali:

`docker image ls`

- Elimina le immagini Docker locali inutilizzate:

`docker image prune`

- Cancella tutte le immagini inutilizzate (non solo quelle sprovviste di tag):

`docker image prune --all`

- Mostra la cronologia di un'immagine Docker locale:

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine</span>
