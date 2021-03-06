---
layout: page
title: common/7zr (Indonesia)
description: "Pengarsip file dengan rasio kompresi yang tinggi."
content_hash: 3876bb867b81980ef2f0e9e38d75b40ca0fe0fc4
related_topics:
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7zr.html
    icon: bi bi-globe
---
# 7zr

Pengarsip file dengan rasio kompresi yang tinggi.
Serupa dengan `7z` namun mendukung format file arsip `.7z` saja.
Informasi lebih lanjut: <https://www.7-zip.org>.

- Meng[a]rsipkan sebuah file atau direktori:

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/arsip.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Mengenkripsi sebuah file arsip (termasuk nama-nama file yang terkandung di dalamnya):

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/arsip_terenkripsi.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata sandi</span>` -mhe=on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/arsip.7z</span>

- Mengekstrak sebuah file arsip dengan mempertahankan struktur direktori asli:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/arsip.7z</span>

- Mengekstrak sebuah file arsip ke dalam direktori yang ditentukan:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/arsip.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Mengekstrak sebuah file arsip menuju stdout:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/arsip.7z</span>` -so`

- Me[l]ihat daftar isi dari sebuah file arsip:

`7zr l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/arsip.7z</span>

- Mengetahui daftar format file arsip yang didukung:

`7zr i`
