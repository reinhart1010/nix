---
layout: page
title: linux/ip (español)
description: "Muestra/manipula enrutamientos, dispositivos, políticas de enrutamiento y túneles."
content_hash: 492aa821616df81fb421c73f715d0a27f7488727
last_modified_at: 2024-12-12
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
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip.html
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

Muestra/manipula enrutamientos, dispositivos, políticas de enrutamiento y túneles.
Algunos subcomandados como `address` tienen su propia documentación de uso.
Más información: <https://www.manned.org/ip.8>.

- Lista las interfaces con información detallada:

`ip address`

- Lista las interfaces con información breve de capa de red:

`ip -brief address`

- Lista las interfaces con información breve dada una capa de enlace:

`ip -brief link`

- Muestra la tabla de enrutamiento:

`ip route`

- Muestra vecinos (tabla ARP):

`ip neighbour`

- Establece una interfaz arriba/abajo (up/down). Usa inglés:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- Agrega/borra una dirección IP de una interfaz:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>

- Agrega una ruta predeterminada:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>
