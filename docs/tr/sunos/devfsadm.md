---
layout: page
title: sunos/devfsadm (Türkçe)
description: "`/dev` için yönetim komutu. `/dev` ad alanına yönetir."
content_hash: 17b0d91927f93ca68572972791f46f4db571c5d5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

`/dev` için yönetim komutu. `/dev` ad alanına yönetir.
Daha fazla bilgi için: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Yeni disk ara:

`devfsadm -c disk`

- Sarkab /dev bağlantılarını temizle ve yeni bir cihaz ara:

`devfsadm -C -v`

- Komut çalıştırılacağı takdirde ne olacağını gör ancak herhangi bir düzenleme yapma:

`devfsadm -C -v -n`
