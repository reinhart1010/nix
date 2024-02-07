---
layout: page
title: linux/man (Indonesia)
description: "Format dan tampilkan halaman manual."
content_hash: d04745a95ace221f28706cea76226ce9587cf9e8
last_modified_at: 2024-02-07
related_topics:
  - title: English version
    url: /en/linux/man.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/man.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/man.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/man.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/man.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/man.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># man

Format dan tampilkan halaman manual.
Informasi lebih lanjut: <https://manned.org/man>.

- Tampilkan halaman manual untuk sebuah perintah:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Tampilkan halaman manual untuk perintah dari bagian 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Tampilkan semua bagian yang tersedia untuk suatu perintah:

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Tampilkan jalur yang dicari untuk halaman manual:

`man --path`

- Tampilkan lokasi sebuah halaman manual alih-alih halaman manual itu sendiri:

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Tampilkan halaman manual menggunakan locale tertentu:

`man --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">locale</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Cari halaman manual yang berisi string pencarian:

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string_pencarian</span>`"`
