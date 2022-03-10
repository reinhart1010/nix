---
layout: page
title: linux/ip-address (Türkçe)
description: "IP adresi yönetimi alt komutu."
content_hash: 488f9945ef39feb20bf47bec7ac22bf6c84c8801
related_topics:
  - title: Deutsch version
    url: /de/linux/ip-address.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip-address.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-address.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ip address

IP adresi yönetimi alt komutu.
Daha fazla bilgi: <https://manned.org/ip-address>.

- Ağ arayüzlerini ve ilişkili IP adreslerini listele:

`ip address`

- Yalnızca etkin ağ arayüzlerini gösterecek şekilde filtrele:

`ip address show up`

- Belirli bir ağ arayüzü hakkındaki bilgileri görüntüle:

`ip address show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Bir ağ arayüzüne bir IP adresi ekle:

`ip address add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adresi</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Bir ağ arayüzünden bir IP adresini kaldır:

`ip address delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adresi</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Belirli bir kapsamdaki tüm IP adreslerini bir ağ arayüzünden sil:

`ip address flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global|host|link</span>
