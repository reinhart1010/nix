---
layout: page
title: osx/open (Indonesia)
description: "Buka file, direktori, dan aplikasi."
content_hash: 08e4b6bb1d6235bfeb790f3fce0dfc0217a2479b
last_modified_at: 2024-01-31
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
Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/open.1.html>.

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
