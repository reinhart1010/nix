---
layout: page
title: common/clamscan (Indonesia)
description: "Sebuah program pemindai virus berbasis command-line."
content_hash: f5fc735459655b54b7465fbdba0f1fe7810a4a13
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/common/clamscan.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clamscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamscan.html
    icon: bi bi-globe
---
# clamscan

Sebuah program pemindai virus berbasis command-line.
Informasi lebih lanjut: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Pindai kerentanan sebuah file:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Pindai seluruh file dalam sebuah direktori secara rekursif:

`clamscan -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Pindai data dari input `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` | clamscan -`

- Gunakan basis data (database) definisi virus yang terkandung dalam sebuah file atau direktori:

`clamscan --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori_basis_data</span>

- Pindai direktori saat ini dan hanya tampilkan file yang terinfeksi:

`clamscan --infected`

- Simpan hasil laporan pemindaian kepada sebuah file log:

`clamscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_log</span>

- Pindahkan file-file yang terinfeksi kepada suatu direktori:

`clamscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_karantina</span>

- Hapus file-file yang terinfeksi:

`clamscan --remove`
