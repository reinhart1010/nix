---
layout: page
title: linux/dnf (Indonesia)
description: "Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti yum)."
content_hash: dc42dd278b06d079274db7e906e42bc5b0920c11
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
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dnf

Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti yum).
Informasi lebih lanjut: <https://dnf.readthedocs.io>.

- Memperbarui seluruh paket yang terpasang ke versi terbaru:

`sudo dnf upgrade`

- Mencari paket yang tersedia dengan kata kunci tertentu:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Memperlihatkan informasi tentang suatu paket:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Menginstal sebuah paket:

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Menginstal sebuah paket dan jawab ya untuk semua pertanyaan:

`sudo dnf -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Menghapus sebuah paket:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Memperlihatkan daftar semua paket yang telah terpasang:

`dnf list --installed`

- Temukan paket mana yang menyediakan file tertentu:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
