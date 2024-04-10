---
layout: page
title: sunos/dmesg (Indonesia)
description: "Tulis pesan kernel ke `stdout`."
content_hash: 478fd4dc8f9421ef49788fd9e5a98be91bc30d21
last_modified_at: 2024-04-10
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Tulis pesan kernel ke `stdout`.
Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Tampilkan pesan kernel:

`dmesg`

- Tampilkan berapa memori fisik yang tersedia di sistem ini:

`dmesg | grep -i memory`

- Tampilkan pesan kernel 1 halaman dalam 1 waktu:

`dmesg | less`
