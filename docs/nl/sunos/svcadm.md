---
layout: page
title: sunos/svcadm (Nederlands)
description: "Manipuleer service instanties."
content_hash: a1c7f4c63cc6560c81ca79a0d671e1c8b1e42ed7
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># svcadm

Manipuleer service instanties.
Meer informatie: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Inschakelen van een service in de service database:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Uitschakelen van een service in de service database:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Herstarten van een draaiende service:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- refresh de configuratie van een service:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Haal een service uit maintenance state, en schakel deze in:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>
