---
layout: page
title: common/arp (polski)
description: "Pokaż i manipuluj pamięcią podręczną ARP systemu."
content_hash: 06e5a2cc960fdd7e9a19ae937b477e5ff89af124
last_modified_at: 2023-11-12
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

Pokaż i manipuluj pamięcią podręczną ARP systemu.
Więcej informacji: <https://manned.org/arp>.

- Pokaż bieżącą tabelę arp:

`arp -a`

- Usuń konkretny wpis:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>

- Utwórz wpis:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_mac</span>
