---
layout: page
title: common/docker-compose (English)
description: "Run and manage multi container docker applications."
content_hash: b833fb27438abae6ba7d2ac0386d5f1452c02ca1
last_modified_at: 2023-11-12
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
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Start all containers by specifying a project name and using an alternate compose file:

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` up`

- Stop all running containers:

`docker compose stop`

- Stop and remove all containers, networks, images, and volumes:

`docker compose down --rmi all --volumes`

- Follow logs for all containers:

`docker compose logs --follow`

- Follow logs for a specific container:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
