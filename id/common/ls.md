---
layout: page
title: common/ls (Indonesia)
description: "Menampilkan daftar konten pada direktori."
content_hash: 5d2f1b84c58a1a5effbd4e61448c11690a520c9f
related_topics:
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ls.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ls

Menampilkan daftar konten pada direktori.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/ls>.

- Menampilkan daftar berkas dengan satu item tiap baris:

`ls -1`

- Menampilkan daftar semua berkas, termasuk berkas tersembunyi:

`ls -a`

- Menampilkan daftar semua berkas, dengan akhiran `/` ditambahkan ke nama direktori:

`ls -F`

- Menampilkan daftar berformat panjang (menampilkan izin, kepemilikan, ukuran dan waktu modifikasi pada setiap berkas):

`ls -la`

- Menampilkan daftar berformat panjang dan ukuran ditampilkan menggunakan unit yang mudah dibaca manusia (KiB, MiB, GiB):

`ls -lh`

- Menampilkan daftar berformat panjang dan diurutkan berdasarkan ukuran (menurun):

`ls -lS`

- Menampilkan daftar berformat panjang dari semua berkas dan diurutkan berdasarkan tanggal modifikasi (terlama dulu):

`ls -ltr`
