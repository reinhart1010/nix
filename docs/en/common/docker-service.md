---
layout: page
title: common/docker-service (English)
description: "Manage the services on a docker daemon."
content_hash: 203780c30ffa3d890986df223d81688b738cd81c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-service.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-service.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-service.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker service

Manage the services on a docker daemon.
More information: <https://docs.docker.com/engine/reference/commandline/service/>.

- List the services on a docker daemon:

`docker service ls`

- Create a new service:

`docker service create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Display detailed information of a space-separated list of services:

`docker service inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name|ID</span>

- List the tasks of a space-separated list of services:

`docker service ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name|ID</span>

- Scale to a specific number of replicas for a space-separated list of services:

`docker service scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count_of_replicas</span>

- Remove a space-separated list of services:

`docker service rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name|ID</span>
