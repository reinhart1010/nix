---
layout: page
title: linux/ip-route-show (español)
description: "Subcomando para mostrar la gestión de tablas de enrutamiento IP."
content_hash: d640c048eba6c37d605276ad6252ab0bfaf46bbc
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ip-route-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-route-show.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip-route-show.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/ip-route-show.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip-route-show.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip route show

Subcomando para mostrar la gestión de tablas de enrutamiento IP.
Más información: <https://manned.org/ip-route>.

- Muestra la tabla de enrutamiento:

`ip route show`

- Muestra la tabla principal de enrutamiento (igual al primer ejemplo):

`ip route show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|254</span>

- Muestra la tabla de enrutamiento local:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|255</span>

- Muestra todas las tablas de enrutamiento:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|unspec|0</span>

- Lista solamente las rutas desde un dispositivo dado:

`ip route show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Lista las rutas dentro de un alcance determinado:

`ip route show scope link`

- Muestra el caché de enrutamiento:

`ip route show cache`

- Muestra solo rutas IPv6 o IPv4:

`ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-6|-4</span>` route show`
