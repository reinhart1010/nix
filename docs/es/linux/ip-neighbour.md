---
layout: page
title: linux/ip-neighbour (español)
description: "Subcomando de gestión de tablas IP de vecinos/ARP."
content_hash: 7f44a71b7976bf260ca4bd750712157aeb955174
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/ip-neighbour.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip-neighbour.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-neighbour.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip neighbour

Subcomando de gestión de tablas IP de vecinos/ARP.
Más información: <https://manned.org/ip-neighbour.8>.

- Muestra las entradas de la tabla de vecinos/ARP:

`ip neighbour`

- Elimina entradas en la tabla de vecinos del dispositivo `eth0`:

`sudo ip neighbour flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Realiza una búsqueda de vecinos y devuelve una entrada de vecinos:

`ip neighbour get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lookup_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Agrega o elimina una entrada ARP a los vecinos IP de `eth0`:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|del</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` nud reachable`

- Cambia o reemplaza una entrada ARP para la dirección IP vecina a `eth0`:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nueva_mac_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>
