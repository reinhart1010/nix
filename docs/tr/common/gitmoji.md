---
layout: page
title: common/gitmoji (Türkçe)
description: "Commit'lerde emoji kullanmak içni interaktif bir komut satırı aracı."
content_hash: 2c51f993ca9735146011ca46a2d7063a28a3d64f
related_topics:
  - title: English version
    url: /en/common/gitmoji.html
    icon: bi bi-globe
---
# gitmoji

Commit'lerde emoji kullanmak içni interaktif bir komut satırı aracı.
Daha fazla bilgi için: <https://github.com/carloscuesta/gitmoji-cli>.

- Commit sihirbazını çalıştır:

`gitmoji --commit`

- Git hook'u başlat (bu sayede `git commit` çalıştırıldığı zaman `gitmoji` otomatik olarak çalıştırılabilir):

`gitmoji --init`

- Git hook'u sil:

`gitmoji --remove`

- Tüm kullanılabilir emojileri ve açıklamalarını sırala:

`gitmoji --list`

- Belirtilen kelime sırası için emoji sırası ara:

`gitmoji --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kelime1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kelime2</span>

- Ana depodan emojileri güncelle:

`gitmoji --update`

- Genel tercihleri düzenle:

`gitmoji --config`
