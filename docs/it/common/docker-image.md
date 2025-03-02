---
layout: page
title: common/docker-image (italiano)
description: "Gestisci immagini Docker."
content_hash: 07d8f561a12921ef0c54ced27dc9aa09071e2394
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/docker-image.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-image.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-image.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-image.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-image.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker image

Gestisci immagini Docker.
Vedi anche `docker build`, `docker import` e `docker pull`.
Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/image/>.

- Elenca tutte le immagini Docker locali:

`docker image ls`

- Elimina le immagini Docker locali inutilizzate:

`docker image prune`

- Cancella tutte le immagini inutilizzate (non solo quelle sprovviste di tag):

`docker image prune --all`

- Mostra la cronologia di un'immagine Docker locale:

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine</span>
