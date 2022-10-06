---
layout: page
title: common/arp (Türkçe)
description: "Sistemin ARP önbelleğini görüntüle ve manipüle et."
content_hash: e9d6f04a775e09d9dc42225a22a0cae96bc29be6
related_topics:
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
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># arp

Sistemin ARP önbelleğini görüntüle ve manipüle et.
Daha fazla bilgi: <https://manned.org/arp>.

- Mevcut ARP tablosunu göster:

`arp -a`

- Tüm önbelleği temizle:

`sudo arp -a -d`

- Belirli bir girdiyi sil:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- ARP tablosunda bir girdi oluştur:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>
