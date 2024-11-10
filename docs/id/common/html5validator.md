---
layout: page
title: common/html5validator (Indonesia)
description: "Lakukan proses validasi sintaks terhadap suatu berkas HTML5."
content_hash: f0d9849894d2b2f0a5039ab08ab06cd610097b43
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/html5validator.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/html5validator.html
    icon: bi bi-globe
tldri18n_status: 2
---
# html5validator

Lakukan proses validasi sintaks terhadap suatu berkas HTML5.
Informasi lebih lanjut: <https://github.com/svenkreiss/html5validator>.

- Lakukan proses validasi terhadap suatu berkas:

`html5validator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Lakukan validasi terhadap seluruh berkas HTML pada suatu direktori:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Tampilkan seluruh pesan peringatan (warning) dan galat (error):

`html5validator --show-warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Lakukan proses validasi terhadap kumpulan berkas yang memenuhi glob kriteria nama berkas:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>` --match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html *.php</span>`"`

- Jangan lakukan validasi terhadap nama-nama berkas tertentu:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>` --blacklist "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_modules vendor</span>`"`

- Tampilkan laporan hasil analisa dalam format tertentu:

`html5validator --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnu|xml|json|text</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan log validasi dalam tingkat verbositas tertentu:

`html5validator --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>` --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warning</span>
