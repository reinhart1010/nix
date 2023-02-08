---
layout: page
title: common/docker-compose (English)
description: "Run and manage multi container docker applications."
content_hash: b1e30ba5fd6b6cf8860b35c5de8caf6e82259638
last_modified_at: 2023-02-08
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
---
# docker compose

Run and manage multi container docker applications.
More information: <https://docs.docker.com/compose/reference/>.

- List all running containers:

`docker compose ps`

- Create and start all containers in the background using a `docker-compose.yml` file from the current directory:

`docker compose up --detach`

- Start all containers, rebuild if necessary:

`docker compose up --build`

- Start all containers using an alternate compose file:

`docker compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` up`

- Stop all running containers:

`docker compose stop`

- Stop and remove all containers, networks, images, and volumes:

`docker compose down --rmi all --volumes`

- Follow logs for all containers:

`docker compose logs --follow`

- Follow logs for a specific container:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
