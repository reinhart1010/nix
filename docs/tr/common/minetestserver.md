---
layout: page
title: common/minetestserver (Türkçe)
description: "Çok oyunculu sınırsız dünyalı bloklu sanbox sunucusu."
content_hash: 9051285a6125cfda2f223672f182472c92faa003
related_topics:
  - title: English version
    url: /en/common/minetestserver.html
    icon: bi bi-globe
---
# minetestserver

Çok oyunculu sınırsız dünyalı bloklu sanbox sunucusu.
Ayrıca `minetest` sayfasına bakılması önerilir.
Daha fazla bilgi için: <https://wiki.minetest.net/Setting_up_a_server>.

- Sunucuyu başlar:

`minetestserver`

- Müsait dünyaları sırala:

`minetestserver --world list`

- Yüklenecek dünya ismini belirt:

`minetestserver --world `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dunya_ismi</span>

- Müsait oyun ID'lerini sırala:

`minetestserver --gameid list`

- Kullanılacak oyunu belirt:

`minetestserver --gameid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oyun_id'si</span>

- Belirtilmiş bir port'u dinle:

`minetestserver --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">34567</span>

- Başka bir veritabanı yazılımına göç et:

`minetestserver --migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqlite3|leveldb|redis</span>

- Sunucuyu başlattıktan sonra interaktif bir terminal aç:

`minetestserver --terminal`
