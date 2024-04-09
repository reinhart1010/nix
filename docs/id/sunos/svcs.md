---
layout: page
title: sunos/svcs (Indonesia)
description: "Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan."
content_hash: 4d46e9dadfafa24071291358ceb6dac15fdc6e66
last_modified_at: 2024-04-09
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/svcs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svcs

Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan.
Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/svcs>.

- Daftar semua servis yang berjalan:

`svcs`

- Daftar servis-servis yang tidak berjalan:

`svcs -vx`

- Daftar informasi tentang sebuah servis:

`svcs apache`

- Tampilkan lokasi dari berkas catatan servis:

`svcs -L apache`

- Display end of a service log file:

`tail $(svcs -L apache)`
