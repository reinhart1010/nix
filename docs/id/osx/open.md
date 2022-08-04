---
layout: page
title: osx/open (Indonesia)
description: "Membuka file, direktori, dan aplikasi."
content_hash: 23becd2ee8439ce607da95f95f471fff7bee9035
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># open

Membuka file, direktori, dan aplikasi.
Informasi lebih lanjut: <https://ss64.com/osx/open.html>.

- Membuka sebuah file di dalam aplikasi default:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Membuka aplikasi macOS tertentu:

`open -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Aplikasi</span>`"`

- Membuka sebuah aplikasi macOS berdasarkan ID pengenal (bundle identifier) tertentu (gunakan `osascript` untuk mencari ID pengenal aplikasi secara mudah dan cepat):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.aplikasi</span>

- Buka direktori saat ini di dalam aplikasi Finder:

`open .`

- Lihat sebuah file di dalam aplikasi Finder:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Buka semua file dengan ekstensi tertentu di dalam aplikasi default pada direktori saat ini:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>
