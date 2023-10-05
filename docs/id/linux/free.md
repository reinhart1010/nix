---
layout: page
title: linux/free (Indonesia)
description: "Menampilkan jumlah memori kosong/tersedia dan memori yang digunakan dalam sistem."
content_hash: b2c3993f8b297252ae36c4adb5124568131d3994
last_modified_at: 2023-10-05
related_topics:
  - title: català version
    url: /ca/linux/free.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/free.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/free.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/free.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/free.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># free

Menampilkan jumlah memori kosong/tersedia dan memori yang digunakan dalam sistem.
Informasi lebih lanjut: <https://manned.org/free>.

- Tampilkan memori sistem:

`free`

- Tampilkan memori dalam Bytes/KB/MB/GB:

`free -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m|g</span>

- Tampilkan memori dalam unit yang dapat dibaca manusia:

`free -h`

- Tampilkan output setiap 2 detik:

`free -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
