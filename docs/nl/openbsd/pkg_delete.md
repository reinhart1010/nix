---
layout: page
title: openbsd/pkg_delete (Nederlands)
description: "Verwijder pakketten in OpenBSD."
content_hash: 78e3823edaddf45e08a50efcb121b6e099da1d76
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/openbsd/pkg_delete.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkg_delete

Verwijder pakketten in OpenBSD.
Bekijk ook: `pkg_add`, `pkg_info`.
Meer informatie: <https://man.openbsd.org/pkg_delete>.

- Verwijder een pakket:

`pkg_delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijder een pakket, inclusief de ongebruikte afhankelijkheden:

`pkg_delete -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Dry-run verwijdering van een pakket:

`pkg_delete -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>
