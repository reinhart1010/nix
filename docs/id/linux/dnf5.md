---
layout: page
title: linux/dnf5 (Indonesia)
description: "Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti dnf5, yang juga dirancang sebagai pengganti yum)."
content_hash: 6253c3e0904e1ac89614b61b2eeb2051e7b78057
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/linux/dnf5.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf5

Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti dnf5, yang juga dirancang sebagai pengganti yum).
DNF5 adalah hasil penulisan ulang program manajemen paket DNF dalam C++ dengan performa yang lebih baik dan ukuran program yang lebih kecil.
Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `dnf5`.
Informasi lebih lanjut: <https://dnf5.readthedocs.io>.

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`sudo dnf5 upgrade`

- Cari paket yang tersedia dengan kata-kata kunci tertentu:

`dnf5 search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci1 kata_kunci2 ...</span>

- Tampilkan informasi tentang suatu paket:

`dnf5 info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Pasang kumpulan paket (gunakan `-y` jawab untuk ya semua pertanyaan):

`sudo dnf5 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket1 paket2 ...</span>

- Hapus kumpulan paket:

`sudo dnf5 remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket1 paket2 ...</span>

- Tampilkan daftar semua paket yang telah terpasang:

`dnf5 list --installed`

- Temukan paket mana yang menyediakan perintah tertentu:

`dnf5 provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Hapus atau tandai data cache sebagai kedaluwarsa:

`sudo dnf5 clean all`
