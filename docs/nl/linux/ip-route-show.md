---
layout: page
title: linux/ip-route-show (Nederlands)
description: "Toon subcommando voor IP routeringstabel management."
content_hash: 18210ff498e4cbf76d226781a28512ba2227dc2f
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/linux/ip-route-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-route-show.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ip-route-show.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ip route show

Toon subcommando voor IP routeringstabel management.
Meer informatie: <https://manned.org/ip-route>.

- Toon de routingtabel:

`ip route show`

- Toon de hoofdrouteringstabel (hetzelfde als eerste voorbeeld):

`ip route show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|254</span>

- Toon de lokale routingtabel:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|255</span>

- Toon Alle routetafels:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|unspec|0</span>

- Toon alleen routes van een bepaald apparaat:

`ip route show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Toon routes binnen een bepaalde scope:

`ip route show scope link`

- Toon de routeringscache:

`ip route show cache`

- Toon alleen IPv6 of IPv4 routes:

`ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-6|-4</span>` route show`
