---
layout: page
title: common/docker-start (English)
description: "Start one or more stopped containers."
content_hash: d5c431cd7f82c8c9b7f18e7ffd5c06a666baffc9
last_modified_at: 2022-12-04
related_topics:
  - title: Deutsch version
    url: /de/common/docker-start.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-start.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-start.html
    icon: bi bi-globe
---
# docker start

Start one or more stopped containers.
More information: <https://docs.docker.com/engine/reference/commandline/start/>.

- Show help:

`docker start`

- Start a docker container:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Start a container, attaching `stdout` and `stderr` and forwarding signals:

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Start one or more space-separated containers:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container(s)</span>
