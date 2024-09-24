---
layout: page
title: common/docker-images (Deutsch)
description: "Verwalte Docker Images."
content_hash: ce0f2fb029888771409f080ea270478276b755f1
last_modified_at: 2024-09-24
related_topics:
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
  - title: português (Brasil) version
    url: /pt_BR/common/docker-images.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-images.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker images

Verwalte Docker Images.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/image/ls/>.

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
