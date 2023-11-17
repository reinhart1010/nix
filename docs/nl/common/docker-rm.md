---
layout: page
title: common/docker-rm (Nederlands)
description: "Verwijder een of meer containers."
content_hash: 94ccf452cc37ae96a01267c491418733555cd032
last_modified_at: 2023-11-17
related_topics:
  - title: English version
    url: /en/common/docker-rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
