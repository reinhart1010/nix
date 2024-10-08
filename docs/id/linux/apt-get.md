---
layout: page
title: linux/apt-get (Indonesia)
description: "Manajemen paket untuk Debian dan Ubuntu."
content_hash: 0dcab17f668e5a96dacf6dd668d36145bf0f56ab
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Manajemen paket untuk Debian dan Ubuntu.
Cari paket menggunakan `apt-cache`.
Informasi lebih lanjut: <https://manned.org/apt-get.8>.

- Perbarui daftar paket yang tersedia beserta versinya (hal ini direkomendasikan untuk dijalankan sebelum menjalankan perintah `apt-get` yang lain):

`apt-get update`

- Pasang sebuah paket, atau perbarui ke versi terbaru yang tersedia:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Hapus sebuah paket:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Hapus sebuah paket dan file konfigurasinya:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Perbarui semua paket yang terpasang ke versi terbaru yang tersedia:

`apt-get upgrade`

- Bersihkan repositori lokal, hapus file paket (`.deb`) yang sebelumnya gagal diunduh dan tidak bisa diunduh kembali:

`apt-get autoclean`

- Hapus semua paket yang tidak diperlukan kembali:

`apt-get autoremove`

- Perbarui paket yang terinstal (mirip `upgrade`), namun hapus paket yang tidak dipakai kembali dan pasang paket tambahan untuk memenuhi dependensi baru:

`apt-get dist-upgrade`
