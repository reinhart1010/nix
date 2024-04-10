---
layout: page
title: sunos/prctl (Indonesia)
description: "Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan."
content_hash: 42ac72cdc2ef0918f12e388c8fd6677ae26ba2f4
last_modified_at: 2024-04-10
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prctl

Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan.
Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1/prctl>.

- Periksa batas dan perizinan proses:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Periksa batas dan perizinan proses dalam format yang dapat diurai mesin:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Ambil batas spesifik dari sebuah proses yang berjalan:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
