---
layout: page
title: osx/open (Indonesia)
description: "Buka file, direktori, dan aplikasi."
content_hash: 27429458b5e336b0b3d8c78665a43f7e6fa39e4c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># open

Buka file, direktori, dan aplikasi.
Informasi lebih lanjut: <https://ss64.com/osx/open.html>.

- Buka sebuah file di dalam aplikasi default:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.ext</span>

- Buka aplikasi macOS tertentu:

`open -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Aplikasi</span>`"`

- Buka sebuah aplikasi macOS berdasarkan ID pengenal (bundle identifier) tertentu (gunakan `osascript` untuk mencari ID pengenal aplikasi secara mudah dan cepat):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.aplikasi</span>

- Buka direktori saat ini di dalam aplikasi Finder:

`open .`

- Lihat sebuah file di dalam aplikasi Finder:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Buka semua file dengan ekstensi tertentu di dalam aplikasi default pada direktori saat ini:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>
