---
layout: page
title: common/docker-container (English)
description: "Manage Docker containers."
content_hash: 4a73c2eebd93b3cf125c3f8d9a4a1b78082337df
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/common/docker-container.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-container.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-container.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-container.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker container

Manage Docker containers.
More information: <https://docs.docker.com/reference/cli/docker/container/>.

- List currently running Docker containers:

`docker container ls`

- Start one or more stopped containers:

`docker container start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container2_name</span>

- Kill one or more running containers:

`docker container kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Stop one or more running containers:

`docker container stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Pause all processes within one or more containers:

`docker container pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Display detailed information on one or more containers:

`docker container inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Export a container's filesystem as a tar archive:

`docker container export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Create a new image from a container's changes:

`docker container commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
