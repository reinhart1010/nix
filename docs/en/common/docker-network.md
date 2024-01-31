---
layout: page
title: common/docker-network (English)
description: "Create and manage docker networks."
content_hash: 24f600f88b72934fbf5cd5ccade9b13f5ee14082
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/common/docker-network.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker network

Create and manage docker networks.
More information: <https://docs.docker.com/engine/reference/commandline/network/>.

- List all available and configured networks on docker daemon:

`docker network ls`

- Create a user-defined network:

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">driver_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>

- Display detailed information about one or more networks:

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name1 network_name2 ...</span>

- Connect a container to a network using a name or ID:

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name|ID</span>

- Disconnect a container from a network:

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name|ID</span>

- Remove all unused (not referenced by any container) networks:

`docker network prune`

- Remove one or more unused networks:

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_name1 network_name2 ...</span>
