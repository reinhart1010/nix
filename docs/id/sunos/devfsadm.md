---
layout: page
title: sunos/devfsadm (Indonesia)
description: "Perintah administrasi untuk `/dev`. Kelola namespace `/dev`."
content_hash: cb25868071508f8bb57b69faa1e7268d095de6cc
last_modified_at: 2024-04-10
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
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

Perintah administrasi untuk `/dev`. Kelola namespace `/dev`.
Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Pindai piringan baru:

`devfsadm -c disk`

- Bersihkan semua tautan /dev yang beruntai dan memindai perangkat baru:

`devfsadm -C -v`

- Dry-run - luaran yang akan dirubah tapi tanpa membuat modifikasi:

`devfsadm -C -v -n`
