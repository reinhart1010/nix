---
layout: page
title: linux/ip-route (español)
description: "Subcomando de gestión de tablas de enrutamiento IP."
content_hash: 56e2f7c9b0e3ca6d87830fc0f1c59bdd38dde65e
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/ip-route.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip-route.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip route

Subcomando de gestión de tablas de enrutamiento IP.
Más información: <https://manned.org/ip-route>.

- Muestra la tabla de enrutamiento:

`ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- Agrega una ruta predeterminada usando reenvío de puerta de enlace (gateway):

`sudo ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_de_gateway</span>

- Añade una ruta predeterminada utilizando `eth0`:

`sudo ip route add default dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Añade una ruta estática:

`sudo ip route add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_destino</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_de_gateway</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Elimina una ruta estática:

`sudo ip route del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_destino</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Cambia o reemplaza una ruta estática:

`sudo ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_destino</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_de_gateway</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Muestra qué ruta será utilizada por el kernel para llegar a una dirección IP:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_destino</span>
