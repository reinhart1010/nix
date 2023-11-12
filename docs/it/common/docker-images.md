---
layout: page
title: common/docker-images (italiano)
description: "Gestisci immagini Docker."
content_hash: ed7b4b760203a972f378364f0c791589f520c698
last_modified_at: 2023-11-12
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

Gestisci immagini Docker.
Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/images/>.

- Elenca tutte le immagini Docker:

`docker images`

- Elenca tutte le immagini Docker incluse quelle intermedie:

`docker images -a`

- Elenca in modalità silenziosa (solo gli ID numerici):

`docker images -q`

- Elenca tutte le immagini Docker che non sono usate da alcun container:

`docker images --filter dangling=true`
