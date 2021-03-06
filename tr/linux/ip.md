---
layout: page
title: linux/ip (Türkçe)
description: "Yönlendirmeyi, aygıtları, kural yönlendirmesini ve tünelleri görüntüle / değiştir."
content_hash: 9ca7f9d13a4157c8cd65cc4986b83d8628a059a3
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ip

Yönlendirmeyi, aygıtları, kural yönlendirmesini ve tünelleri görüntüle / değiştir.
`ip address` gibi bazı alt komutların kendi kullanım belgeleri vardır.
Daha fazla bilgi: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Arayüzlerin bilgilerini ayrıntılı bir şekilde listele:

`ip address`

- Arayüzlerin ağ katmanı bilgilerini kısa bir şekilde listele:

`ip -brief address`

- Arayüzlerin bağlantı katmanı bilgilerini kısa bir şekilde listele:

`ip -brief link`

- Yönlendirme tablosunu görüntüle:

`ip route`

- Komşuları (ARP tablosunu) göster:

`ip neighbour`

- Bir arayüzü etkinleştir/devre dışı bırak:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz</span>` up/down`

- Bir arayüze IP adresi ekle/sil:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maske</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz</span>

- Öntanımlı yönlendirme ekle:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz</span>
