---
layout: page
title: linux/ip-address (español)
description: "Subcomando de manejo de direcciones IP."
content_hash: 14150d60d47367e29fc5f9aa3c259ab1dc22054e
last_modified_at: 2024-12-12
related_topics:
  - title: Deutsch version
    url: /de/linux/ip-address.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip-address.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-address.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip-address.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-address.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip address

Subcomando de manejo de direcciones IP.
Más información: <https://manned.org/ip-address>.

- Lista las interfaces de red y sus direcciones IP asociadas:

`ip address`

- Filtra mostrando solo las interfaces de red activas:

`ip address show up`

- Muestra información sobre una interfaz de red específica:

`ip address show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Añade una dirección IP a una interfaz de red:

`ip address add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Elimina una dirección IP de una interfaz de red:

`ip address delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Elimina todas las direcciones IP en un alcance dado de una interfaz de red:

`ip address flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global|host|link</span>
