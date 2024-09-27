---
layout: page
title: linux/cfdisk (Indonesia)
description: "Atur tabel dan partisi alokasi penyimpanan pada perangkat penyimpanan keras menggunakan tampilan antarmuka teks interaktif berbasis curses."
content_hash: 1241153306539a9d6033382a457ce4d314f128fe
last_modified_at: 2024-09-27
related_topics:
  - title: Deutsch version
    url: /de/linux/cfdisk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cfdisk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cfdisk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cfdisk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cfdisk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cfdisk

Atur tabel dan partisi alokasi penyimpanan pada perangkat penyimpanan keras menggunakan tampilan antarmuka teks interaktif berbasis curses.
Informasi lebih lanjut: <https://manned.org/cfdisk>.

- Jalankan program pengalokasi partisi terhadap suatu perangkat penyimpanan keras:

`cfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Buat kemudian kelola tabel partisi baru terhadap suatu perangkat penyimpanan keras:

`cfdisk --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
