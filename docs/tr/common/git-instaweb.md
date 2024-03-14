---
layout: page
title: common/git-instaweb (Türkçe)
description: "gitweb sunucusu başlatmak için yardımcı araç."
content_hash: 61d520295909812e31a0a60bb8715da540666801
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/git-instaweb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-instaweb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-instaweb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git instaweb

gitweb sunucusu başlatmak için yardımcı araç.
Daha fazla bilgi için: <https://git-scm.com/docs/git-instaweb>.

- Mevcut Git deposu için bir gitweb sunucusu başlat:

`git instaweb --start`

- Yalnızca yerel ağda başlat:

`git instaweb --start --local`

- Belirtilmiş bir port'da başlat:

`git instaweb --start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Belirtilmiş bir HTTP daemon'u kullan:

`git instaweb --start --httpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lighttpd|apache2|mongoose|plackup|webrick</span>

- Ayrıca bir ağ tarayıcısını otomatik olarak başlat:

`git instaweb --start --browser`

- Çalışan mevcut gitweb sunucusunu durdur:

`git instaweb --stop`

- Çalışan mevcut gitweb sunucusunu yeniden başlat:

`git instaweb --restart`
