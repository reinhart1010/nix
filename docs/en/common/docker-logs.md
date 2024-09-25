---
layout: page
title: common/docker-logs (English)
description: "Print container logs."
content_hash: 9160437b7fdaa9d66a4179b8f564bf2650f348dc
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/common/docker-logs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-logs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-logs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-logs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-logs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker logs

Print container logs.
More information: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Print logs from a container:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Print logs and follow them:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Print last 5 lines:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Print logs and append them with timestamps:

`docker logs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Print logs from a certain point in time of container execution (i.e. 23m, 10s, 2013-01-02T13:23:37):

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time</span>
