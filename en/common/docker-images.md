---
layout: page
title: common/docker-images (English)
description: "Manage Docker images."
content_hash: 97a94daec5404d375b933194048bcad8718460bc
related_topics:
  - title: Deutsch version
    url: /de/common/docker-images.html
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

Manage Docker images.
More information: <https://docs.docker.com/engine/reference/commandline/images/>.

- List all Docker images:

`docker images`

- List all Docker images including intermediates:

`docker images --all`

- List the output in quiet mode (only numeric IDs):

`docker images --quiet`

- List all Docker images not used by any container:

`docker images --filter dangling=true`

- List images that contain a substring in their name:

`docker images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*name*</span>`"`
