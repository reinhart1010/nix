---
layout: page
title: common/arp (Türkçe)
description: "Sistemin ARP önbelleğini görüntüle ve manipüle et."
content_hash: 9b2e366fbb10cad92f0c839ac5f0c13f32a17e7d
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
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arp

Sistemin ARP önbelleğini görüntüle ve manipüle et.
Daha fazla bilgi için: <https://manned.org/arp>.

- Mevcut ARP tablosunu göster:

`arp -a`

- Belirli bir girdiyi sil:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>

- ARP tablosunda bir girdi oluştur:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_adresi</span>
