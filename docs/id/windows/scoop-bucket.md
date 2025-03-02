---
layout: page
title: windows/scoop-bucket (Indonesia)
description: "Kelola bucket: Repository Git yang berisi berkas yang menjelaskan bagaimana scoop menginstall aplikasi."
content_hash: 8817aab3847c127adb4da61c9a4a94e2dcfff664
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop-bucket.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scoop bucket

Kelola bucket: Repository Git yang berisi berkas yang menjelaskan bagaimana scoop menginstall aplikasi.
Jika Scoop tidak tahu di mana sebuah bucket terletak, maka lokasi repositori harus ditentukan.
Informasi lebih lanjut: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Tampilkan daftar semua bucket yang sedang digunakan:

`scoop bucket list`

- Tampilkan daftar semua bucket yang dikenal:

`scoop bucket known`

- Tambahkan bucket yang dikenal berdasarkan namanya:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>

- Tambahkan bucket yang tidak dikenal bersarkan nama dan URL repository Git:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/repository.git</span>

- Hapus suatu bucket berdasarkan namanya:

`scoop bucket rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>
