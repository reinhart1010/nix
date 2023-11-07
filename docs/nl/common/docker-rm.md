---
layout: page
title: common/docker-rm (Nederlands)
description: "Verwijder een of meer containers."
content_hash: 94ccf452cc37ae96a01267c491418733555cd032
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/common/docker-rm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker rm

Verwijder een of meer containers.
Meer informatie: <https://docs.docker.com/engine/reference/commandline/rm>.

- Verwijder containers:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Verwijdeer een container geforceerd:

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Verwijder een container en de volumes:

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Hulp weergeven:

`docker rm`
