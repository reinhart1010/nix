---
layout: page
title: common/docker-service (English)
description: "Manage the services on a Docker daemon."
content_hash: 73373cf824b6aa96827b829f4907ad577b06c80c
last_modified_at: 2024-09-28
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

Manage the services on a Docker daemon.
More information: <https://docs.docker.com/reference/cli/docker/service/>.

- List the services on a Docker daemon:

`docker service ls`

- Create a new service:

`docker service create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Display detailed information about one or more services:

`docker service inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name_or_ID1 service_name_or_ID2</span>

- List the tasks of one or more services:

`docker service ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name_or_ID1 service_name_or_ID2 ...</span>

- Scale to a specific number of replicas for a space-separated list of services:

`docker service scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count_of_replicas</span>

- Remove one or more services:

`docker service rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name_or_ID1 service_name_or_ID2</span>
