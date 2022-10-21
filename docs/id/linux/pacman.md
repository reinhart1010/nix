---
layout: page
title: linux/pacman (Indonesia)
description: "Kegunaan manajer paket Arch Linux."
content_hash: 1414d947c182f6b2e534c158c37eadd501e217ba
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman

Kegunaan manajer paket Arch Linux.
Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `pacman sync`.
Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Sinkronkan dan perbarui semua paket:

`sudo pacman -Syu`

- Instal paket baru:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket beserta dependensinya:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Cari paket dalam database berdasarkan regular expression atau kata kunci:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Tampilkan daftar paket dan versi yang diinstal:

`pacman -Q`

- Tampilkan daftar paket dan versi yang diinstal secara eksplisit:

`pacman -Qe`

- Tampilkan daftar paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`pacman -Qtdq`

- Kosongkan seluruh cache pacman:

`sudo pacman -Scc`
