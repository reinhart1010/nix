---
layout: page
title: linux/pacman-remove (Indonesia)
description: "Kegunaan manajer paket Arch Linux."
content_hash: f641f33772e35672fa403ecd2c214667725363e1
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --remove

Kegunaan manajer paket Arch Linux.
Guarda anche: `pacman`.
Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Hapus paket beserta dependensinya:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket beserta dependensi dan file konfigurasi-nya:

`sudo pacman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus tanpa konfirmasi:

`sudo pacman --remove --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Hapus paket dan semua paket yang bergantung pada paket tersebut:

`sudo pacman --remove --cascade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan daftar paket yang akan terpengaruh (tidak menghapus paket apa pun):

`pacman --remove --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan bantuan untuk subperintah ini:

`pacman --remove --help`
