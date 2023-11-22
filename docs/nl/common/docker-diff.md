---
layout: page
title: common/docker-diff (Nederlands)
description: "Inspecteer wijzigingen in bestanden of mappen op het bestandssysteem van een container."
content_hash: 18ffe4b5932679a915c4e2991f25abf4181f3262
last_modified_at: 2023-11-22
related_topics:
  - title: English version
    url: /en/common/docker-diff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-diff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker diff

Inspecteer wijzigingen in bestanden of mappen op het bestandssysteem van een container.
Meer informatie: <https://docs.docker.com/engine/reference/commandline/diff>.

- Inspecteer de wijzigingen in een container sinds deze is gemaakt:

`docker diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Hulp weergeven:

`docker diff --help`
