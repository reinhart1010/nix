---
layout: page
title: common/arp (polski)
description: "Pokaż i manipuluj systemową pamięcią podręczną ARP."
content_hash: 99ddb7f5e55d5faffa195b6e2cf93ea2484257d0
last_modified_at: 2024-09-04
related_topics:
  - title: Deutsch version
    url: /de/common/arp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/arp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/arp.html
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

Pokaż i manipuluj systemową pamięcią podręczną ARP.
Więcej informacji: <https://manned.org/arp>.

- Pokaż bieżącą tabelę ARP:

`arp -a`

- Usuń konkretny wpis:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>

- Utwórz nowy wpis w tabeli ARP:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_mac</span>
