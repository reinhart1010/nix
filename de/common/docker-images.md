---
layout: page
title: common/docker-images (Deutsch)
description: "Verwalte Docker Images."
content_hash: 0a2bd0fa3ea47b86121fa5d43ff19e2f3dc1050c
related_topics:
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
  - title: português (Brasil) version
    url: /pt_BR/common/docker-images.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-images.html
    icon: bi bi-globe
---
# docker images

Verwalte Docker Images.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/images/>.

- Liste alle Docker Images auf:

`docker images`

- Liste alle Docker Images inkl. Zwischen-Images auf:

`docker images --all`

- Liste nur die IDs der Docker Images auf:

`docker images --quiet`

- Liste alle Docker Images auf, die nicht von einem Container verwendet werden:

`docker images --filter dangling=true`

- Liste alle Docker Images mit einer bestimmten Zeichenfolge im Namen auf:

`docker images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*name*</span>`"`
