---
layout: page
title: common/docker-images (português (Brasil))
description: "Gerencia imagens Docker."
content_hash: d52373f5ded92654b46c7930273530202e655424
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/common/docker-images.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-images.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-images.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker images

Gerencia imagens Docker.
Mais informações: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Lista todas as imagens Docker:

`docker images`

- Lista todas as imagens Docker incluindo imagens intermedirárias:

`docker images --all`

- Lista no modo silencioso (somente IDs numéricos):

`docker images --quiet`

- Lista todas as imagens Docker não usadas por nenhum container:

`docker images --filter dangling=true`

- Lista imagens que contenham um substring no seu nome:

`docker images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*nome*</span>`"`

- Classifica imagens pelo tamanho:

`docker images --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort -k 2 -h`
