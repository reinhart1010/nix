---
layout: page
title: linux/ip-rule (Türkçe)
description: "IP yönlendirme politikası veri tabanı yönetimi."
content_hash: 14be7adaea013cba3b04a5f83fba89b6b1039c4d
related_topics:
  - title: English version
    url: /en/linux/ip-rule.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ip rule

IP yönlendirme politikası veri tabanı yönetimi.
Daha fazla bilgi: <https://man7.org/linux/man-pages/man8/ip-rule.8.html>.

- Yönlendirme politikasını göster:

`ip rule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- Paket kaynak adreslerine dayalı yeni bir kural ekle:

`sudo ip rule add from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Paket hedef adreslerine dayalı yeni bir kural ekle:

`sudo ip rule add to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Paket kaynak adreslerine dayalı bir kuralı sil:

`sudo ip rule delete from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Paket hedef adreslerine dayalı bir kuralı sil:

`sudo ip rule delete to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Silinen tüm kuralları temizle:

`ip rule flush`

- Tüm kuralları bir dosyaya kaydet:

`ip rule save > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_kuralları.dat/dosyasının/yolu</span>

- Tüm kuralları bir dosyadan geri yükle:

`ip rule restore < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_kuralları.dat/dosyasının/yolu</span>
