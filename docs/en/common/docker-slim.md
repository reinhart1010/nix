---
layout: page
title: common/docker-slim (English)
description: "Analyze and optimize Docker images."
content_hash: 77c945175591f8669433ea68cfcad15f752abc71
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-slim.html
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

Analyze and optimize Docker images.
More information: <https://github.com/docker-slim/docker-slim>.

- Start DockerSlim on interactive mode:

`docker-slim`

- Analyze Docker layers from a specific image:

`docker-slim xray --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Lint a Dockerfile:

`docker-slim lint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Dockerfile</span>

- Analyze and generate an optimized Docker image:

`docker-slim build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Display help for a subcommand:

`docker-slim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
