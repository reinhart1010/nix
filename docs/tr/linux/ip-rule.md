---
layout: page
title: linux/ip-rule (Türkçe)
description: "IP yönlendirme politikası veri tabanı yönetimi."
content_hash: 9c4deb9eed075c6dff2cfb1cd677e0b7f668abfd
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/linux/ip-rule.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip rule

IP yönlendirme politikası veri tabanı yönetimi.
Daha fazla bilgi için: <https://manned.org/ip-rule>.

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
