---
layout: page
title: windows/scoop-bucket (Indonesia)
description: "Mengelola bucket: Repository Git yang berisi berkas yang menjelaskan bagaimana scoop menginstall aplikasi."
content_hash: 885f040ab24b00811e3c6fa93316b04c17e690cf
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop-bucket.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scoop bucket

Mengelola bucket: Repository Git yang berisi berkas yang menjelaskan bagaimana scoop menginstall aplikasi.
Jika Scoop tidak tahu dimana sebuah bucket terletak, lokasi repository harus ditentukan.
Informasi lebih lanjut: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Menampilkan daftar semua bucket yang sedang digunakan:

`scoop bucket list`

- Menampilkan daftar semua bucket yang dikenal:

`scoop bucket known`

- Menambahkan bucket yang dikenal berdasarkan namanya:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>

- Menambahkan bucket yang tidak dikenal bersarkan nama dan URL repository Git:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://contoh.com/repository.git</span>

- Menghapus bucket berdasarkan namanya:

`scoop bucket rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>
