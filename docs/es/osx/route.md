---
layout: page
title: osx/route (español)
description: "Manipula manualmente las tablas de enrutamiento."
content_hash: 8055d205e0c632efc7be96edd8e4f40c0d6b4956
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/route.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/route.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# route

Manipula manualmente las tablas de enrutamiento.
Necesita ser root.
Más información: <https://www.manpagez.com/man/8/route/>.

- Añade una ruta a un destino a través de una puerta de enlace:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip_destino</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_puerta</span>`"`

- Añade una ruta a una subred /24 a través de una puerta de enlace:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip_subred</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_puerta</span>`"`

- Ejecuta en modo de prueba (no hace nada, sólo imprime):

`sudo route -t add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip_destino</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_puerta</span>`"`

- Elimina todas las rutas:

`sudo route flush`

- Elimina una ruta específica:

`sudo route delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip_destino</span>`/24"`

- Busca y muestra la ruta de un destino (nombre de host o dirección IP):

`sudo route get "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>`"`
