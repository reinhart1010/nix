---
layout: page
title: common/docker-network (English)
description: "Create and manage docker networks."
content_hash: 6e0e3c81a186b6c399ff47c4f58299c37b6d5465
related_topics:
  - title: Deutsch version
    url: /de/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
---
# docker network

Create and manage docker networks.
More information: <https://docs.docker.com/engine/reference/commandline/network/>.

- List all available and configured networks on docker daemon:

`docker network ls`

- Create a user-defined network:

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">driver_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>

- Display detailed information of a space-separated list of networks:

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>

- Connect a container to a network using a name or ID:

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name|ID</span>

- Disconnect a container from a network:

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name|ID</span>

- Remove all unused (not referenced by any container) networks:

`docker network prune`

- Remove a space-separated list of unused networks:

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>
