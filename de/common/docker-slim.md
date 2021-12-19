---
layout: page
title: common/docker-slim (Deutsch)
description: "Analysiere und optimiere Docker Images."
content_hash: eef69c1a16a79860623f784c02d34a4224363f63
related_topics:
  - title: English version
    url: /en/common/docker-slim.html
    icon: bi bi-globe
---
# docker-slim

Analysiere und optimiere Docker Images.
Weitere Informationen: <https://github.com/docker-slim/docker-slim>.

- Starte DockerSlim im interaktiven Modus:

`docker-slim`

- Analysiere die Docker Layer eines bestimmten Images:

`docker-slim xray --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Linte ein Dockerfile:

`docker-slim lint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/Dockerfile</span>

- Analysiere und generiere ein optimiertes Docker Image:

`docker-slim build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Zeige Hilfe für einen Unterbefehl:

`docker-slim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unterbefehl</span>` --help`
