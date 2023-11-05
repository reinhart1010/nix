---
layout: page
title: netbsd/pkgin (Nederlands)
description: "Beheer `pkgsrc` binary pakketten op NetBSD."
content_hash: 801fb5963417fc206bf28ad43ace456e35b043b5
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/netbsd/pkgin.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkgin

Beheer `pkgsrc` binary pakketten op NetBSD.
Meer informatie: <https://pkgin.net/#usage>.

- Installeer een pakket:

`pkgin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijder een pakket en zijn afhankelijkheden:

`pkgin remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Upgrade alle pakketten:

`pkgin full-upgrade`

- Zoek naar een pakket:

`pkgin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Toon alle geïnstalleerde pakketten:

`pkgin list`

- Verwijder alle onnodige afhankelijkheden:

`pkgin autoremove`
