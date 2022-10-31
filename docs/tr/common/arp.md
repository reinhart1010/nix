---
layout: page
title: common/arp (Türkçe)
description: "Sistemin ARP önbelleğini görüntüle ve manipüle et."
content_hash: f6f0a621476b1c8ea9461895c095d61559f4db72
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
# arp

Sistemin ARP önbelleğini görüntüle ve manipüle et.
Daha fazla bilgi için: <https://manned.org/arp>.

- Mevcut ARP tablosunu göster:

`arp -a`

- Tüm önbelleği temizle:

`sudo arp -a -d`

- Belirli bir girdiyi sil:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- ARP tablosunda bir girdi oluştur:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>
