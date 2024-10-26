---
layout: page
title: common/atom (Indonesia)
description: "Editor teks yang dapat dipasang lintas platform."
content_hash: 505c52034431ac8057744a30fe7b761c4bf4e904
last_modified_at: 2024-10-26
related_topics:
  - title: Deutsch version
    url: /de/common/atom.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/atom.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atom.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atom.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/atom.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atom.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/atom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atom

Editor teks yang dapat dipasang lintas platform.
Plugin dikelola oleh `apm`.
Catatan: Dukungan aplikasi Atom telah ditutup dan tidak lagi dikelola secara aktif.
Informasi lebih lanjut: <https://atom.io/>.

- Buka suatu berkas atau direktori:

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori</span>

- Buka berkas atau direktori dalam jendela baru:

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori</span>

- Buka berkas atau direktori di jendela yang sudah ada:

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori</span>

- Buka Atom dalam mode aman (tidak memuat paket plugin tambahan apa pun):

`atom --safe`

- Jalankan Atom sebagai subproses pada sesi terminal saat ini, jangan memuat Atom sebagai proses latar belakang:

`atom --foreground`

- Tunggu jendela Atom untuk ditutup sebelum kembali ke sesi terminal saat ini (berguna untuk editor komit Git):

`atom --wait`
