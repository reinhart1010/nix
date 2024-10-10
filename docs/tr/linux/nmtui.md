---
layout: page
title: linux/nmtui (Türkçe)
description: "NetworkManager'ı denetlemek için metin tabanlı kullanıcı arayüzü."
content_hash: 9c7e64d406104c84225543932255deb5fec2d174
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/linux/nmtui.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmtui.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmtui

NetworkManager'ı denetlemek için metin tabanlı kullanıcı arayüzü.
Gezinmek için ok tuşlarını, seçmek için Enter tuşunu kullanın.
Daha fazla bilgi için: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Kullanıcı arayüzünü aç:

`nmtui`

- Etkinleştirme veya devre dışı bırakma seçeneğiyle birlikte kullanılabilir bağlantıların bir listesini göster:

`nmtui connect`

- Belirtilen ağa bağlan:

`nmtui connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ad|uuid|aygıt|SSID</span>

- Belirtilen ağı düzenle/ekle/sil:

`nmtui edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ad|kimlik</span>

- Sistem ana makine adını ayarla:

`nmtui hostname`
