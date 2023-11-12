---
layout: page
title: linux/pacman-upgrade (Indonesia)
description: "Kegunaan manajer paket Arch Linux."
content_hash: 89f1cad797a5c12f7c251da53fba8982957e3ab2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

Kegunaan manajer paket Arch Linux.
Guarda anche: `pacman`.
Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Instal satu paket atau lebih dari file:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/paket1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/paket2.pkg.tar.zst</span>

- Instal paket tanpa konfirmasi:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/paket.pkg.tar.zst</span>

- Timpa file yang bentrok selama pemasangan paket:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/paket.pkg.tar.zst</span>

- Instal paket, melewati pemeriksaan versi dependensi:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/paket.pkg.tar.zst</span>

- Tampilkan daftar paket yang akan terpengaruh (tidak menginstal paket apa pun):

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/paket.pkg.tar.zst</span>

- Tampilkan bantuan:

`pacman --upgrade --help`
