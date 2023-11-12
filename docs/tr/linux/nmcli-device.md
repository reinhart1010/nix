---
layout: page
title: linux/nmcli-device (Türkçe)
description: "NetworkManager ile donanım aygıtı yönetimi."
content_hash: 8e85160d29c7fed6d9d9c78a06ee7ac66a29fd1a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nmcli-device.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli device

NetworkManager ile donanım aygıtı yönetimi.
Daha fazla bilgi için: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Tüm ağ arayüzlerinin durumlarını yazdır:

`nmcli device status`

- Kullanılabilir kablosuz erişim noktalarını yazdır:

`nmcli device wifi`

- Belirtilen ad ve parola ile kablosuz ağa bağlan:

`nmcli device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>` password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parola</span>

- Geçerli kablosuz ağ için parola ve QR kodunu yazdır:

`nmcli device wifi show-password`
