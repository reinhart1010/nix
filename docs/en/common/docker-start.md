---
layout: page
title: common/docker-start (English)
description: "Start one or more stopped containers."
content_hash: f6edc6562c2b895bfda497dbed19b8c066ff981f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-start.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-start.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-start.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-start.html
    icon: bi bi-globe
tldri18n_status: 2
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

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>
