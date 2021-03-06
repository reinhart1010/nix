---
layout: page
title: common/docker-system (English)
description: "Manage Docker data and display system-wide information."
content_hash: ab4749e025edc8845f7a42ad2590ef15e24872c9
related_topics:
  - title: Deutsch version
    url: /de/common/docker-system.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-system.html
    icon: bi bi-globe
---
# docker system

Manage Docker data and display system-wide information.
More information: <https://docs.docker.com/engine/reference/commandline/system/>.

- Show help:

`docker system`

- Show docker disk usage:

`docker system df`

- Show detailed information on disk usage:

`docker system df --verbose`

- Remove unused data:

`docker system prune`

- Remove unused data created more than a specified amount of time in the past:

`docker system prune --filter="until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hours</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m"`

- Display real-time events from the Docker daemon:

`docker system events`

- Display real-time events from containers streamed as valid JSON Lines:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- Display system-wide information:

`docker system info`
