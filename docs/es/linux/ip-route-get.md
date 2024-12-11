---
layout: page
title: linux/ip-route-get (español)
description: "Obtiene una única ruta a un destino e imprime su contenido exactamente como el kernel lo ve."
content_hash: 62b0870270038631092a65298c1b02d3eadcb391
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/ip-route-get.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip-route-get.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ip-route-get.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ip route get

Obtiene una única ruta a un destino e imprime su contenido exactamente como el kernel lo ve.
Más información: <https://manned.org/ip-route>.

- Imprime ruta a un destino:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- Imprime la ruta a un destino desde una dirección de origen específica:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origen</span>

- Imprime la ruta a un destino para los paquetes que llegan a una interfaz específica:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` iif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Imprime la ruta a un destino forzando la salida a través de una interfaz específica:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` oif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- Imprime la ruta a un destino con un tipo específico de servicio (ToS):

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` tos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x10</span>

- Imprime la ruta a un destino utilizando una instancia VRF específica (Virtual Routing and Forwarding - Enrutamiento y Reenvío Virtual):

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` vrf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myvrf</span>
