---
layout: page
title: linux/avahi-resolve (español)
description: "Traduce entre nombres de host y direcciones IP."
content_hash: 9077648f29be2fd76e0cd3279cf7cd136cfada07
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/avahi-resolve.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/avahi-resolve.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avahi-resolve

Traduce entre nombres de host y direcciones IP.
Más información: <https://www.avahi.org/>.

- Resuelve un servicio local a su dirección IPv4:

`avahi-resolve -4 --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servicio.local</span>

- Resuelve una dirección IP a un nombre de host, de manera detallada:

`avahi-resolve --verbose --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>
