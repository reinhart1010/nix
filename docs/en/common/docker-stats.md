---
layout: page
title: common/docker-stats (English)
description: "Display a live stream of resource usage statistics for containers."
content_hash: 1899d5cf8304fa615e66b47e089e65c1a41c1aca
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-stats.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-stats.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-stats.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-stats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker stats

Display a live stream of resource usage statistics for containers.
More information: <https://docs.docker.com/reference/cli/docker/container/stats/>.

- Display a live stream for the statistics of all running containers:

`docker stats`

- Display a live stream of statistics for one or more containers:

`docker stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Change the columns format to display container's CPU usage percentage:

`docker stats --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Name</span>`:\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.CPUPerc</span>`"`

- Display statistics for all containers (both running and stopped):

`docker stats --all`

- Disable streaming stats and only pull the current stats:

`docker stats --no-stream`
