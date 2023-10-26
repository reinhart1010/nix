---
layout: page
title: linux/ip (italiano)
description: "Mostra / manipola routing, dispositivi, criteri di routing e tunnel."
content_hash: fefdba0520e77e0206b59b8c28cee4f6633b8e60
last_modified_at: 2023-10-26
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
---
# ip

Mostra / manipola routing, dispositivi, criteri di routing e tunnel.
Alcuni sottocomandi, come `ip address`, hanno una propria documentazione d'uso. Maggiori informazioni: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Elenca le interfacce con informazioni dettagliate:

`ip address`

- Elenca le interfacce con informazioni brevi sul livello di rete:

`ip -brief address`

- Elenca le interfacce con informazioni brevi sul livello di collegamento:

`ip -brief link`

- Visualizza la tabella di routing:

`ip route`

- Mostra i vicini (tabella ARP):

`ip neighbour`

- Attiva/disattiva un'interfaccia:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaccia</span>` up/down`

- Aggiungi/elimina un indirizzo IP a/da un'interfaccia:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaccia</span>

- Aggiungi una route predefinita:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaccia</span>
