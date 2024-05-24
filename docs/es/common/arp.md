---
layout: page
title: common/arp (español)
description: "Muestra y manipula la caché ARP del sistema."
content_hash: 0b4d858f93d4104939c30b106ee993d59c29d4ce
last_modified_at: 2024-05-24
related_topics:
  - title: Deutsch version
    url: /de/common/arp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arp

Muestra y manipula la caché ARP del sistema.
Más información: <https://manned.org/arp>.

- Muestra la tabla ARP actual:

`arp -a`

- Borra una entrada específica:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección</span>

- Añade una nueva entrada en la tabla ARP:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_mac</span>
