---
layout: page
title: common/asciitopgm (Indonesia)
description: "Ubah format gambar ASCII menuju suatu berkas PGM."
content_hash: ccb2d41462910b2bfcd97713f305f6d42a3b61d2
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/asciitopgm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciitopgm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/asciitopgm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># asciitopgm

Ubah format gambar ASCII menuju suatu berkas PGM.
Informasi lebih lanjut: <https://netpbm.sourceforge.net/doc/asciitopgm.html>.

- Baca data ASCII sebagai input dan hasilkan gambar PGM dengan nilai piksel yang merupakan perkiraan "kecerahan" karakter ASCII:

`asciitopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/input</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/output.pgm</span>

- Tampilkan informasi versi:

`asciitopgm -version`
