---
layout: page
title: linux/ip-route (Türkçe)
description: "IP yönlendirme tablosu yönetimi alt komutu."
content_hash: d6b03227a07164ff387ddabce6a4d9a515d01c08
related_topics:
  - title: English version
    url: /en/linux/ip-route.html
    icon: bi bi-globe
---
# ip route

IP yönlendirme tablosu yönetimi alt komutu.
Daha fazla bilgi için: <https://manned.org/ip-route>.

- Yönlendirme tablosunu görüntüle:

`ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- Ağ geçidini kullanan öntanımlı bir yönlendirme ekle:

`sudo ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_geçidi_ip_adresi</span>

- `eth0` arayüzünü kullanan öntanımlı bir yönlendirme ekle:

`sudo ip route add default dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Statik bir yönlendirme ekle:

`sudo ip route add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef_ip_adresi</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_geçidi_ip_adresi</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Statik bir yönlendirmeyi sil:

`sudo ip route del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef_ip_adresi</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Statik bir yönlendirmeyi değiştir:

`sudo ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef_ip_adresi</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_geçidi_ip_adresi</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Bir IP adresine ulaşmak için çekirdek tarafından hangi yönlendirmenin kullanılacağını göster:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef_ip_adresi</span>
