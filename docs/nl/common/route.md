---
layout: page
title: common/route (Nederlands)
description: "Gebruik het route-commando om de routetabel in te stellen."
content_hash: 5968cb67080554e65a4d196791cb85f260bc50d8
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/route.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# route

Gebruik het route-commando om de routetabel in te stellen.
Meer informatie: <https://manned.org/route>.

- Toon de informatie van de routetabel:

`route -n`

- Voeg een routeregel toe:

`sudo route add -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>` netmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netmask_adres</span>` gw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gw_adres</span>

- Verwijder een routeregel:

`sudo route del -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>` netmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netmask_adres</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gw_adres</span>
