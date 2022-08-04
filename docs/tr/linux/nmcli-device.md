---
layout: page
title: linux/nmcli-device (Türkçe)
description: "NetworkManager ile donanım aygıtı yönetimi."
content_hash: 9fbaa2f1b6b7fbb1221d9c5494737f2ad6b623c9
related_topics:
  - title: English version
    url: /en/linux/nmcli-device.html
    icon: bi bi-globe
---
# nmcli device

NetworkManager ile donanım aygıtı yönetimi.
Daha fazla bilgi: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Tüm ağ arayüzlerinin durumlarını yazdır:

`nmcli device status`

- Kullanılabilir kablosuz erişim noktalarını yazdır:

`nmcli device wifi`

- Belirtilen ad ve parola ile kablosuz ağa bağlan:

`nmcli device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>` password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parola</span>

- Geçerli kablosuz ağ için parola ve QR kodunu yazdır:

`nmcli device wifi show-password`
