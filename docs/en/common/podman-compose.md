---
layout: page
title: common/podman-compose (English)
description: "Run and manage Compose Specification container definition."
content_hash: e7470f361a36f2f5267b7d52d47a6897bf670451
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/podman-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman-compose

Run and manage Compose Specification container definition.
More information: <https://github.com/containers/podman-compose>.

- List all running containers:

`podman-compose ps`

- Create and start all containers in the background using a local `docker-compose.yml`:

`podman-compose up -d`

- Start all containers, building if needed:

`podman-compose up --build`

- Start all containers using an alternate compose file:

`podman-compose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` up`

- Stop all running containers:

`podman-compose stop`

- Remove all containers, networks, and volumes:

`podman-compose down --volumes`

- Follow logs for a container (omit all container names):

`podman-compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Run a one-time command in a service with no ports mapped:

`podman-compose run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
