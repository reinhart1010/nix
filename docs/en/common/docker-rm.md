---
layout: page
title: common/docker-rm (English)
description: "Remove one or more containers."
content_hash: e04ec76e81508afc6245a4189bf08b77796abf67
last_modified_at: 2023-10-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker rm

Remove one or more containers.
More information: <https://docs.docker.com/engine/reference/commandline/rm>.

- Remove containers:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Force remove a container:

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Remove a container and its volumes:

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Display help:

`docker rm`