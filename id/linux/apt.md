---
layout: page
title: linux/apt (Indonesia)
description: "Manajer paket untuk distribusi Linux berbasis Debian."
content_hash: 806fc6f1a0fe5aaf3ee62d9fa0221b6ff338ebe4
related_topics:
  - title: বাংলা version
    url: /bn/linux/apt.html
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
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt

Manajer paket untuk distribusi Linux berbasis Debian.
Pengganti `apt-get` yang direkomendasikan ketika digunakan secara interaktif di Ubuntu versi 16.04 atau yang lebih baru.
Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Memperbarui daftar paket yang tersedia dan versinya (direkomendasikan untuk menggunakan perintah ini sebelum perintah `apt` lainnya.):

`sudo apt update`

- Mencari paket yang tersedia dengan nama atau deskripsi tertentu:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_atau_deskripsi_paket</span>

- Memperlihatkan informasi tentang suatu paket:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Menginstal sebuah paket, atau memperbarui paket ke versi terbaru:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Menghapus sebuah paket (gunakan `sudo apt purge` untuk menghapus paket beserta file konfigurasinya):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Memperbarui seluruh paket yang terpasang ke versi terbaru:

`sudo apt upgrade`

- Memperlihatkan daftar semua paket yang tersedia di dalam repositori:

`apt list`

- Memperlihatkan daftar paket yang telah terpasang:

`apt list --installed`
