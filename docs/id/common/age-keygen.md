---
layout: page
title: common/age-keygen (Indonesia)
description: "Buat pasangan kunci untuk `age`."
content_hash: 2c8bbe30872d19a6ec79a6160a0e6e70c7c0a08f
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/age-keygen.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age-keygen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/age-keygen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># age-keygen

Buat pasangan kunci untuk `age`.
Lihat `age` untuk mengetahui cara membuat/membuka file terenkripsi.
Informasi lebih lanjut: <https://manned.org/age-keygen>.

- Buat pasangan kunci, simpan ke dalam file tanpa enkripsi, dan cetak kunci publik menuju `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Ubah sebuah kunci identitas menjadi penerima dan cetak kunci publik menuju `stdout`:

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>
