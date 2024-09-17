---
layout: page
title: common/docker-rm (English)
description: "Remove containers."
content_hash: 8b9f834b20cba9105481c8fc95e1a0e8332d2927
last_modified_at: 2024-09-17
related_topics:
  - title: français version
    url: /fr/common/docker-rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rm

Remove containers.
More information: <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Remove containers:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Force remove a container:

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Remove a container and its volumes:

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Display help:

`docker rm --help`
