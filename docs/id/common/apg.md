---
layout: page
title: common/apg (Indonesia)
description: "Buat kata sandi secara acak dan kompleks."
content_hash: 635eef50a4cad59a2158150803dd3402eeafbc19
last_modified_at: 2024-06-14
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/apg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/apg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apg

Buat kata sandi secara acak dan kompleks.
Informasi lebih lanjut: <https://manned.org/apg>.

- Buat sebuah kata sandi secara acak (panjang default bagi kata sandi adalah 8):

`apg`

- Buat sebuah kata sandi dengan minimum 1 simbol (S), 1 nomor (N), 1 huruf kapital (C), dan 1 huruf kecil (L):

`apg -M SNCL`

- Buat kata sandi dengan panjang 16 karakter:

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Buat kata sandi dengan panjang ma[x]imum 16 karakter:

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Buat sebuah kata sandi yang tidak mengandung kata yang terkandung di dalam suatu berkas kamus:

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_kamus</span>
