---
layout: page
title: linux/nmtui (Türkçe)
description: "NetworkManager'ı denetlemek için metin tabanlı kullanıcı arayüzü."
content_hash: aa68813f93326c5dfe17c80577c2d518fde0e385
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nmtui.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmtui

NetworkManager'ı denetlemek için metin tabanlı kullanıcı arayüzü.
Gezinmek için ok tuşlarını, seçmek için Enter tuşunu kullanın.
Daha fazla bilgi için: <https://networkmanager.dev/docs/api/latest/nmtui.html>.

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
