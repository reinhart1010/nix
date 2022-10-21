---
layout: page
title: linux/pacman-query (Indonesia)
description: "Kegunaan manajer paket Arch Linux."
content_hash: d55dcaad6b5f4ecc5d7f35d334de154e1646b607
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman --query

Kegunaan manajer paket Arch Linux.
Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Tampilkan daftar paket yang diinstal beserta versinya:

`pacman --query`

- Tampilkan daftar paket yang diinstal beserta versinya secara eksplisit:

`pacman --query --explicit`

- Temukan paket mana yang memiliki file:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namafile</span>

- Tampilkan informasi paket yang diinstal:

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan daftar file yang dimiliki oleh paket:

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan daftar paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`pacman --query --unrequired --deps --quiet`

- Tampilkan daftar paket yang diinstal tidak ditemukan di tempat penyimpanan:

`pacman --query --foreign`

- Tampilkan daftar paket usang:

`pacman --query --upgrades`
