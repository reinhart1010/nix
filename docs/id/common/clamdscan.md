---
layout: page
title: common/clamdscan (Indonesia)
description: "Sebuah program pemindai virus berbasis command-line."
content_hash: e4a7f5e8991f75c6a4bf3aaa8dd99a7760c78f6a
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/clamdscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamdscan.html
    icon: bi bi-globe
---
# clamdscan

Sebuah program pemindai virus berbasis command-line.
Informasi lebih lanjut: <https://www.clamav.net>.

- Pindai kerentanan suatu file atau direktori tertentu:

`clamdscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Pindai data dari input `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` | clamdscan -`

- Pindai direktori saat ini dan hanya tampilkan file yang terinfeksi:

`clamdscan --infected`

- Simpan hasil laporan pemindaian kepada sebuah file log:

`clamdscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_log</span>

- Pindahkan file-file yang terinfeksi kepada suatu direktori:

`clamdscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_karantina</span>

- Hapus file-file yang terinfeksi:

`clamdscan --remove`

- Gunakan lebih dari satu thread untuk memindai sebuah direktori:

`clamdscan --multiscan`

- Pindai file dengan memberikan deskriptor kepada daemon daripada mengoper isi mentah file tersebut seperti biasa:

`clamdscan --fdpass`
