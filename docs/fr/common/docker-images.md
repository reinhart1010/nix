---
layout: page
title: common/docker-images (français)
description: "Gérer les images Docker."
content_hash: ba9aee57901a0c05cada5e61645ec14cdf84858a
last_modified_at: 2024-09-24
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

Gérer les images Docker.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Lister toutes les images Docker :

`docker images`

- Lister toutes les images Docker, y compris les intermédiaires :

`docker images --all`

- Lister les images Docker en mode silencieux (seulement les IDs numériques) :

`docker images --quiet`

- Lister toutes les images Docker non utilisées par un conteneur :

`docker images --filter dangling=true`

- Lister les images Docker qui contiennent une sous-chaîne dans leur nom :

`docker images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*nom*</span>`"`
