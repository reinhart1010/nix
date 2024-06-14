---
layout: page
title: common/apropos (Indonesia)
description: "Lakukan pencarian nama dan deskripsi perintah dalam buku panduan program baris perintah (`manpages`)."
content_hash: 463b1ff17e83fa8580124eaa2f2d2cbf9ca1711b
last_modified_at: 2024-06-14
related_topics:
  - title: Deutsch version
    url: /de/common/apropos.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/apropos.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apropos.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apropos.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apropos.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apropos.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apropos.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/apropos.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apropos

Lakukan pencarian nama dan deskripsi perintah dalam buku panduan program baris perintah (`manpages`).
Informasi lebih lanjut: <https://manned.org/apropos>.

- Cari daftar dokumentasi perintah yang mengandung kata dengan format kata kunci ekspresi reguler (regex):

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>

- Jangan pangkas tampilan teks hasil pencarian menurut panjang jendela terminal:

`apropos -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>

- Cari daftar dokumentasi perintah yang mengandung seluruh ([a]ll) kriteria kata dalam bentuk ekspresi reguler (regex):

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler_1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler_2</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler_3</span>
