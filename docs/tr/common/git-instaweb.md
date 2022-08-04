---
layout: page
title: common/git-instaweb (Türkçe)
description: "gitweb sunucusu başlatmak için yardımcı araç."
content_hash: c504b6f6d7e9bd32c68569cefccd65a3bd9fbc20
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
---
# git instaweb

gitweb sunucusu başlatmak için yardımcı araç.
Daha fazla bilgi: <https://git-scm.com/docs/git-instaweb>.

- Mevcut Git deposu için bir gitweb sunucusu başlat:

`git instaweb --start`

- Yalnızca yerel ağda başlat:

`git instaweb --start --local`

- Belirtilmiş bir port'da başlat:

`git instaweb --start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Belirtilmiş bir http daemon'u kullan:

`git instaweb --start --httpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lighttpd|apache2|mongoose|plackup|webrick</span>

- Ayrıca bir ağ tarayıcısını otomatik olarak başlat:

`git instaweb --start --browser`

- Çalışan mevcut gitweb sunucusunu durdur:

`git instaweb --stop`

- Çalışan mevcut gitweb sunucusunu yeniden başlat:

`git instaweb --restart`
