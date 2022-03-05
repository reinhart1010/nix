---
layout: page
title: linux/nmtui (Türkçe)
description: "NetworkManager'ı denetlemek için metin tabanlı kullanıcı arayüzü."
content_hash: 6b6ec0272fa9241e08109b0dc245704d370a4852
related_topics:
  - title: English version
    url: /en/linux/nmtui.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nmtui

NetworkManager'ı denetlemek için metin tabanlı kullanıcı arayüzü.
Gezinmek için ok tuşlarını, seçmek için Enter tuşunu kullanın.
Daha fazla bilgi: <https://networkmanager.dev/docs/api/latest/nmtui.html>.

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
