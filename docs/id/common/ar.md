---
layout: page
title: common/ar (Indonesia)
description: "Buat, olah, dan ekstrak berkas dalam format arsip Unix. Biasanya dimanfaatkan untuk pustaka statis (`.a`) dan paket piranti lunak Debian (`.deb`)."
content_hash: 1a59d5ea417142aa940c9d9b61f82a8c310a1f73
last_modified_at: 2024-06-14
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ar

Buat, olah, dan ekstrak berkas dalam format arsip Unix. Biasanya dimanfaatkan untuk pustaka statis (`.a`) dan paket piranti lunak Debian (`.deb`).
Lihat juga: `tar`.
Informasi lebih lanjut: <https://manned.org/ar>.

- E[x]trak seluruh berkas dalam suatu arsip:

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.a</span>

- Lihat daf[t]ar isi dari suatu arsip:

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.ar</span>

- Gantikan ([r]eplace) atau tambahkan suatu berkas ke dalam arsip:

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/debian-binary jalan/menuju/control.tar.gz jalan/menuju/data.tar.xz ...</span>

- Ma[s]ukkan suatu berkas objek (setara dengan penggunaan `ranlib`):

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.a</span>

- Buat suatu arsip berisikan kumpulan berkas tertentu, dan suatu berkas daftar indeks para objek:

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1.o jalan/menuju/berkas2.o ...</span>
