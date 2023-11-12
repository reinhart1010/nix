---
layout: page
title: linux/ip (Deutsch)
description: "Zeige und manipuliere routing, Geräte, Policy routing und Tunnel."
content_hash: 7b47ea3bbae24ff37234fdbc253de000e08d9e8a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip

Zeige und manipuliere routing, Geräte, Policy routing und Tunnel.
Weitere Informationen: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Zeige Interfaces mit detaillierten Informationen:

`ip address`

- Zeige Interfaces mit kurzen Netzwerkinformationen:

`ip -brief address`

- Zeige Interfaces mit kurzen link layer Informationen:

`ip -brief link`

- Zeige die Routing Tabelle:

`ip route`

- Zeige Nachbarn (ARP Tabelle):

`ip neighbour`

- Schalte ein bestimmtes Interface ein oder aus:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- Entferne oder füge eine IP zu einem Interface hinzu:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Füge eine Standard Route hinzu:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
