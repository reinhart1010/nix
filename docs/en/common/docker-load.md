---
layout: page
title: common/docker-load (English)
description: "Load Docker images from files or `stdin`."
content_hash: a5852470fc50a380c9d445b59df3b9ace3d738b3
last_modified_at: 2024-09-24
related_topics:
  - title: français version
    url: /fr/common/docker-load.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-load.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker load

Load Docker images from files or `stdin`.
More information: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Load a Docker image from `stdin`:

`docker load < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.tar</span>

- Load a Docker image from a specific file:

`docker load --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.tar</span>

- Load a Docker image from a specific file in quiet mode:

`docker load --quiet --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.tar</span>
