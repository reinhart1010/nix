---
layout: page
title: common/docker-image (Deutsch)
description: "Verwalte Docker Images."
content_hash: e36e8ffa34877697cedbaabd6097d3d7baa2cbcf
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/docker-image.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-image.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-image.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-image.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker image

Verwalte Docker Images.
Siehe auch `docker build`, `docker import` und `docker pull`.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/image/>.

- Liste lokale Docker Images auf:

`docker image ls`

- Lösche nicht verwendete, lokale Docker Images:

`docker image prune`

- Lösche alle nicht verwendeten Docker Images (nicht nur die ohne Tag):

`docker image prune --all`

- Zeige die Geschichte eines lokalen Docker Images:

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
