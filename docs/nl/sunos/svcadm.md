---
layout: page
title: sunos/svcadm (Nederlands)
description: "Manipuleer service instanties."
content_hash: 901fb24463503f49cb194d317b102a86d6803cc0
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
---
# svcadm

Manipuleer service instanties.
Meer informatie: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Inschakelen van een service in de service database:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Uitschakelen van een service in de service database:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Herstarten van een draaiende service:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Refresh de configuratie van een service:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Haal een service uit maintenance state, en schakel deze in:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>
