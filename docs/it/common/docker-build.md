---
layout: page
title: common/docker-build (italiano)
description: "Crea un'immagine a partire da un Dockerfile. La creazione di un'immagine Docker è chiamata build."
content_hash: b92c3db156e2d4c3d9bd75f6d4938074a3e77ab2
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/docker-build.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-build.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-build.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-build.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-build.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-build.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-build.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker build

Crea un'immagine a partire da un Dockerfile. La creazione di un'immagine Docker è chiamata build.
Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/build/>.

- Crea un'immagine Docker usando il Dockerfile nella directory corrente:

`docker build .`

- Crea un'immagine Docker usando il Dockerfile disponibile a un dato URL:

`docker build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.com/creack/docker-firefox</span>

- Crea e tagga un'immagine Docker:

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome:tag</span>` .`

- Non usare la cache per la creazione di un'immagine Docker:

`docker build --no-cache --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome:tag</span>` .`

- Crea un'immagine Docker usando un dato Dockerfile:

`docker build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>` .`

- Crea un'immagine Docker usando variabili fornite in fase di build:

`docker build --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HTTP_PROXY=http://10.20.30.2:1234</span>` --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FTP_PROXY=http://40.50.60.5:4567</span>` .`
