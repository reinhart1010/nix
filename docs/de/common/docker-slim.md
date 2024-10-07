---
layout: page
title: common/docker-slim (Deutsch)
description: "Analysiere und optimiere Docker Images."
content_hash: 063cd32a4541281997b0a4b77aa68b37badb0805
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/docker-slim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-slim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-slim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-slim

Analysiere und optimiere Docker Images.
Weitere Informationen: <https://github.com/slimtoolkit/slim>.

- Starte DockerSlim im interaktiven Modus:

`docker-slim`

- Analysiere die Docker Layer eines bestimmten Images:

`docker-slim xray --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Linte ein Dockerfile:

`docker-slim lint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/Dockerfile</span>

- Analysiere und generiere ein optimiertes Docker Image:

`docker-slim build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Zeige Hilfe für einen Unterbefehl:

`docker-slim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unterbefehl</span>` --help`
