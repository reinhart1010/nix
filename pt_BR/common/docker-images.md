---
layout: page
title: common/docker-images (português (Brasil))
description: "Gerencia imagens Docker."
content_hash: caca88d805b362f84d9aa4e5e6aa1303fc05a343
related_topics:
  - title: Deutsch version
    url: /de/common/docker-images.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-images.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-images.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-images.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/docker-images.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-images.html
    icon: bi bi-globe
---
# docker images

Gerencia imagens Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/images/>.

- Lista todas as imagens Docker:

`docker images`

- Lista todas as imagens Docker incluíndo imagens intermedirárias:

`docker images --all`

- Lista no modo silencioso (somente IDs numéricos):

`docker images --quiet`

- Lista todas as imagens Docker não usadas por nenhum container:

`docker images --filter dangling=true`

- Lista imagens que contenham um substring no seu nome:

`docker images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*nome*</span>`"`
