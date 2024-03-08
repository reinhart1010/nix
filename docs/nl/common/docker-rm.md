---
layout: page
title: common/docker-rm (Nederlands)
description: "Verwijder een of meer containers."
content_hash: e0147b1abe0a6e9e3e7b18c22bfcc0eeffd689f3
last_modified_at: 2024-03-08
related_topics:
  - title: English version
    url: /en/common/docker-rm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rm

Verwijder een of meer containers.
Meer informatie: <https://docs.docker.com/engine/reference/commandline/rm>.

- Verwijder containers:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Verwijdeer een container geforceerd:

`docker rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>

- Verwijder een container en de volumes:

`docker rm --volumes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Toon de help:

`docker rm --help`
