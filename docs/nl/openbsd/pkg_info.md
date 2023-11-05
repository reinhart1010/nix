---
layout: page
title: openbsd/pkg_info (Nederlands)
description: "Bekijk informatie over pakketten in OpenBSD."
content_hash: f192c6919fa6e12fe254589fa6b7838216aae7c6
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/openbsd/pkg_info.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkg_info

Bekijk informatie over pakketten in OpenBSD.
Bekijk ook: `pkg_add`, `pkg_delete`.
Meer informatie: <https://man.openbsd.org/pkg_info>.

- Zoek naar een pakket met behulp van de pakket-naam:

`pkg_info -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Toon een lijst met geïnstalleerde pakketen voor het gebruik met `pkg_add -l`:

`pkg_info -mz`
