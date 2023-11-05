---
layout: page
title: openbsd/pkg_add (Nederlands)
description: "Installeer/update pakketten in OpenBSD."
content_hash: fa6e6beeea7f082018e47209c6a7d1148ef5aad9
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/openbsd/pkg_add.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkg_add

Installeer/update pakketten in OpenBSD.
Bekijk ook: `pkg_info`, `pkg_delete`.
Meer informatie: <https://man.openbsd.org/pkg_add>.

- Werk alle pakketten bij, inclusief afhankelijkheden:

`pkg_add -u`

- Installeer een nieuw pakket:

`pkg_add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Installeer pakketten van de onbewerkte uitvoer van `pkg_info`:

`pkg_add -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/file</span>
