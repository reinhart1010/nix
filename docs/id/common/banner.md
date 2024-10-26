---
layout: page
title: common/banner (Indonesia)
description: "Cetak argumen perintah ini sebagai suatu seni teks ASCII (ASCII art)."
content_hash: a0017d6d05ed0cfcbff3306141358c5aece27977
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/banner.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/banner.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/banner.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/banner.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/banner.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/banner.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/banner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># banner

Cetak argumen perintah ini sebagai suatu seni teks ASCII (ASCII art).
Informasi lebih lanjut: <https://manned.org/banner>.

- Tampilkan sebuah pesan teks sebagai teks spanduk teks ASCII besar (penggunaan tanda petik bersifat opsional):

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Halo Dunia</span>`"`

- Tampilkan pesan dengan ukuran lebar ([w]idth) sebesar 50 karakter:

`banner -w 50 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Halo Dunia</span>`"`

- Baca teks dari `stdin`:

`banner`
