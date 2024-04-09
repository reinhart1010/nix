---
layout: page
title: sunos/truss (Indonesia)
description: "Alat pemecah masalah untuk menelusuri panggilan sistem."
content_hash: 7667ad27792484ade6978938a98d5a99aaa05f1d
last_modified_at: 2024-04-09
related_topics:
  - title: English version
    url: /en/sunos/truss.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/truss.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/sunos/truss.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/truss.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/truss.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># truss

Alat pemecah masalah untuk menelusuri panggilan sistem.
strace untuk SunOS.
Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/truss>.

- Telusuri sebuah program dengan mengeksekusinya dan mengawasi semua proses turunan:

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Mulai menelusuri sebuah proses tertentu berdasarkan PID-nya:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Mulai menelusuri sebuah program dengan mengeksekusinya, tampilkan argumen-argumen dan variabel-variabel lingkungan:

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Menghitung waktu, panggilan, dan error untuk setiap panggilan sistem dan laporkan sebuah ringkasan saat keluar program:

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Telusuri proses berdasarkan keluaran dari panggilan sistem:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_panggilan_sistem</span>
