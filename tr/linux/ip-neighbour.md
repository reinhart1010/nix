---
layout: page
title: linux/ip-neighbour (Türkçe)
description: "Komşu/ARP tablosu yönetimi IP alt komutu."
content_hash: c27d47a06a0189e851d0ce161ae2d31713befbf8
related_topics:
  - title: English version
    url: /en/linux/ip-neighbour.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ip-neighbour

Komşu/ARP tablosu yönetimi IP alt komutu.
Daha fazla bilgi: <https://manned.org/ip-neighbour.8>.

- Komşu/ARP tablosu girdilerini görüntüle:

`ip neighbour`

- `eth0` aygıtının komşu tablosundaki girdileri kaldır:

`sudo ip neighbour flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Bir komşu araması gerçekleştir ve bir komşu girdisi döndür:

`ip neighbour get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranacak_ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- `eth0` arayüzüne komşu IP adresi için bir ARP girdisi ekle veya sil:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|del</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adresi</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_adresi</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` nud reachable`

- `eth0` arayüzünde komşu IP adresi için bir ARP girdisini değiştir:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adresi</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_mac_adresi</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>
