---
layout: page
title: linux/pacman-sync (Indonesia)
description: "Kegunaan manajer paket Arch Linux."
content_hash: 6cb665d981669fc210b8cea76956736cd8a18ce7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --sync

Kegunaan manajer paket Arch Linux.
Guarda anche: `pacman`.
Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Instal paket baru:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Sinkronkan dan perbarui semua paket (tambahkan `--downloadonly` untuk unduh paket dan tidak memperbarui-nya):

`sudo pacman --sync --refresh --sysupgrade`

- Perbarui semua paket dan instal paket baru tanpa konfirmasi:

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Cari paket dalam database berdasarkan regular expression atau kata kunci:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Tampilkan informasi sebuah paket:

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Timpa file yang bentrok selama pembaruan paket:

`sudo pacman --sync --refresh --sysupgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Sinkronkan dan perbarui semua paket, namun abaikan paket tertentu (dapat digunakan lebih dari sekali):

`sudo pacman --sync --refresh --sysupgrade --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket yang tidak terpasang dan repositori yang tidak digunakan dari cache (gunakan dua tanda `--clean` untuk bersihkan semua paket):

`sudo pacman --sync --clean`
