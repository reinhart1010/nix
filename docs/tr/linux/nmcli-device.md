---
layout: page
title: linux/nmcli-device (Türkçe)
description: "NetworkManager ile donanım aygıtı yönetimi."
content_hash: 85e3023f3c3c6fd63097e4c5e411f82fcc4d72bd
last_modified_at: 2024-10-10
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
Daha fazla bilgi için: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Tüm ağ arayüzlerinin durumlarını yazdır:

`nmcli device status`

- Kullanılabilir kablosuz erişim noktalarını yazdır:

`nmcli device wifi`

- Belirtilen ad ve parola ile kablosuz ağa bağlan:

`nmcli --ask device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>

- Geçerli kablosuz ağ için parola ve QR kodunu yazdır:

`nmcli device wifi show-password`
