---
layout: page
title: common/arp (polski)
description: "Pokaż i manipuluj pamięcią podręczną ARP systemu."
content_hash: 025913fe27540e7b16a286242a38fdb5c43cd915
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
---
# arp

Pokaż i manipuluj pamięcią podręczną ARP systemu.
Więcej informacji: <https://manned.org/arp>.

- Pokaż bieżącą tabelę arp:

`arp -a`

- Wyczyść całość cache:

`sudo arp -a -d`

- Usuń konkretny wpis:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>

- Utwórz wpis:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_mac</span>
