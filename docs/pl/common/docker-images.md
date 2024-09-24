---
layout: page
title: common/docker-images (polski)
description: "Zarządzaj obrazami Dockera."
content_hash: 2dc9e29b7b16af1a5f10b60d0882f1bbdbdc77dd
last_modified_at: 2024-09-24
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

Zarządzaj obrazami Dockera.
Więcej informacji: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Wyświetl wszystkie obrazy Docker:

`docker images`

- Wyświetl wszystkie obrazy Dockera, w tym intermediates:

`docker images -a`

- Wyświetl dane wyjściowe w trybie quiet (tylko identyfikatory numeryczne):

`docker images -q`

- Wyświetl wszystkie obrazy Docker nieużywane przez żaden kontener:

`docker images --filter dangling=true`
