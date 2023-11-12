---
layout: page
title: sunos/svcs (Türkçe)
description: "Çalışan servislere dair bilgileri sırala."
content_hash: a63d5e1fc52461f2c6b6073a37f1bd8a44c20025
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcs

Çalışan servislere dair bilgileri sırala.
Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1/svcs>.

- Tüm çalışan servisleri sırala:

`svcs`

- Çalışmayan servisleri sırala:

`svcs -vx`

- Belirtilen servise dair bilgileri sırala:

`svcs apache`

- Servis kayıt dosyasının yerini göster:

`svcs -L apache`

- Servis kayıt dosyasının sonunu görüntüle:

`tail $(svcs -L apache)`
