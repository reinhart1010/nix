---
layout: page
title: common/docker-ps (English)
description: "List Docker containers."
content_hash: 33e4df340aeb534697f48f3715a7b3e98ca260e0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-ps.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-ps.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker ps

List Docker containers.
More information: <https://docs.docker.com/engine/reference/commandline/ps/>.

- List currently running docker containers:

`docker ps`

- List all docker containers (running and stopped):

`docker ps --all`

- Show the latest created container (includes all states):

`docker ps --latest`

- Filter containers that contain a substring in their name:

`docker ps --filter="name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Filter containers that share a given image as an ancestor:

`docker ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`"`

- Filter containers by exit status code:

`docker ps --all --filter="exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Filter containers by status (created, running, removing, paused, exited and dead):

`docker ps --filter="status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`"`

- Filter containers that mount a specific volume or have a volume mounted in a specific path:

`docker ps --filter="volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
