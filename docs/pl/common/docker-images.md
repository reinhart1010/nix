---
layout: page
title: common/docker-images (polski)
description: "Zarządzaj obrazami Dockera."
content_hash: 8c1f54e2c9eda7d9ae0ca248a4ff7bc897fa79d8
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
  - title: português (Brasil) version
    url: /pt_BR/common/docker-images.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-images.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-images.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker images

Zarządzaj obrazami Dockera.
Więcej informacji: <https://docs.docker.com/engine/reference/commandline/images/>.

- Wyświetl wszystkie obrazy Docker:

`docker images`

- Wyświetl wszystkie obrazy Dockera, w tym intermediates:

`docker images -a`

- Wyświetl dane wyjściowe w trybie quiet (tylko identyfikatory numeryczne):

`docker images -q`

- Wyświetl wszystkie obrazy Docker nieużywane przez żaden kontener:

`docker images --filter dangling=true`
