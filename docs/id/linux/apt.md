---
layout: page
title: linux/apt (Indonesia)
description: "Manajer paket untuk distribusi Linux berbasis Debian."
content_hash: 0373ab87df17dc6c339a9fc46ab7a6ccaf06b190
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

Manajer paket untuk distribusi Linux berbasis Debian.
Pengganti `apt-get` yang direkomendasikan ketika digunakan secara interaktif di Ubuntu versi 16.04 atau yang lebih baru.
Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `apt`.
Informasi lebih lanjut: <https://manned.org/apt.8>.

- Perbarui daftar paket yang tersedia dan versinya (direkomendasikan untuk menggunakan perintah ini sebelum perintah `apt` lainnya.):

`sudo apt update`

- Cari paket yang tersedia dengan nama atau deskripsi tertentu:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_atau_deskripsi_paket</span>

- Tampilkan informasi tentang suatu paket:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Pasang atau perbarui sebuah paket menuju versi terbaru:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket yang terpasang sebelumnya (gunakan `sudo apt purge` untuk sekaligus menghapus file konfigurasi yang dibuat oleh paket tersebut):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`sudo apt upgrade`

- Tampilkan daftar semua paket yang tersedia di dalam repositori:

`apt list`

- Tampilkan daftar paket yang telah terpasang:

`apt list --installed`
