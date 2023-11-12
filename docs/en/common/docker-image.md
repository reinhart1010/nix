---
layout: page
title: common/docker-image (English)
description: "Manage Docker images."
content_hash: cd2d7d333121f7396e2b20f4000b9baee351882a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-image.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-image.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-image.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-image.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker image

Manage Docker images.
See also `docker build`, `docker import`, and `docker pull`.
More information: <https://docs.docker.com/engine/reference/commandline/image/>.

- List local Docker images:

`docker image ls`

- Delete unused local Docker images:

`docker image prune`

- Delete all unused images (not just those without a tag):

`docker image prune --all`

- Show the history of a local Docker image:

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
