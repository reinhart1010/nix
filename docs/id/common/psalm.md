---
layout: page
title: common/psalm (Indonesia)
description: "Suatu alat analisis kode statis yang dapat dimanfaatkan untuk mencari kesalahan pada aplikasi berbasis PHP."
content_hash: 2843850e1b9c4518349c71de23a7710a3fc7b5e7
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/psalm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# psalm

Suatu alat analisis kode statis yang dapat dimanfaatkan untuk mencari kesalahan pada aplikasi berbasis PHP.
Informasi lebih lanjut: <https://psalm.dev>.

- Buat sebuah berkas konfigurasi Psalm baru:

`psalm --init`

- Periksa kesalahan pada direktori saat ini:

`psalm`

- Periksa kesalahan pada suatu direktori atau berkas:

`psalm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori</span>

- Periksa kesalahan menggunakan suatu berkas konfigurasi:

`psalm --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/psalm.xml</span>

- Lampirkan penemuan-penemuan informasional ke dalam luaran hasil pengecekan:

`psalm --show-info`

- Periksa suatu proyek dan tampilkan hasil statistika:

`psalm --stats`

- Periksa suatu proyek secara paralel denan 4 thread pemrosesan:

`psalm --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
