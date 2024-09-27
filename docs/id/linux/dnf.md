---
layout: page
title: linux/dnf (Indonesia)
description: "Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti yum)."
content_hash: 38c9750aba27fd71e7a55c2561fff8b4bb9da57c
last_modified_at: 2024-09-27
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf

Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti yum).
Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `dnf`.
Informasi lebih lanjut: <https://dnf.readthedocs.io>.

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`sudo dnf upgrade`

- Cari paket yang tersedia dengan kata-kata kunci tertentu:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci1 kata_kunci2 ...</span>

- Tampilkan informasi tentang suatu paket:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Pasang kumpulan paket (gunakan `-y` jawab untuk ya semua pertanyaan):

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket1 paket2 ...</span>

- Hapus kumpulan paket:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket1 paket2 ...</span>

- Tampilkan daftar semua paket yang telah terpasang:

`dnf list --installed`

- Temukan paket mana yang menyediakan perintah tertentu:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Lihat informasi riwayat penugasan `dnf`:

`dnf history`
