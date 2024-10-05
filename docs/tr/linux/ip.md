---
layout: page
title: linux/ip (Türkçe)
description: "Yönlendirmeyi, aygıtları, kural yönlendirmesini ve tünelleri görüntüle / değiştir."
content_hash: a79a465e2bfe56fe75df3c4de04949a49ade932c
last_modified_at: 2024-10-05
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
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip

Yönlendirmeyi, aygıtları, kural yönlendirmesini ve tünelleri görüntüle / değiştir.
`address` gibi bazı alt komutların kendi kullanım belgeleri vardır.
Daha fazla bilgi için: <https://www.manned.org/ip.8>.

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

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- Bir arayüze IP adresi ekle/sil:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maske</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz</span>

- Öntanımlı yönlendirme ekle:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arayüz</span>
