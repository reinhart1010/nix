---
layout: page
title: linux/ip-link (español)
description: "Gestiona interfaces de red."
content_hash: 4f6b0f400eea02d2aa5d4c153387129d7eb848fd
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/ip-link.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip-link.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-link.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip link

Gestiona interfaces de red.
Más información: <https://manned.org/ip-link>.

- Muestra información sobre todas las interfaces de red:

`ip link`

- Muestra información sobre una interfaz de red específica:

`ip link show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>

- Establece una interfaz de red arriba (up) o abajo (down). Usa inglés:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- Establece un nombre significativo a una interfaz de red:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` alias "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LAN Interface</span>`"`

- Cambia la dirección MAC de una interfaz de red:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ff:ff:ff:ff:ff:ff</span>

- Cambia el tamaño de MTU para una interfaz de red para usar marcos jumbo:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9000</span>
