---
layout: page
title: linux/debootstrap (Indonesia)
description: "Membuat sistem Debian dasar."
content_hash: ec4c64a50a597fbca3dd20bb9dd130ebec18fadb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/debootstrap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/debootstrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debootstrap

Membuat sistem Debian dasar.
Informasi lebih lanjut: <https://wiki.debian.org/Debootstrap>.

- Membuat sistem Debian stable didalam direktori `debian-root`:

`sudo debootstrap stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/ke/debian-root/</span>` http://deb.debian.org/debian`

- Membuat sistem minimal termasuk hanya paket yang diperlukan:

`sudo debootstrap --variant=minbase stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/ke/debian-root/</span>

- Membuat sistem Ubuntu 20.04 didalam direktori `focal-root` dengan mirror lokal:

`sudo debootstrap focal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/ke/focal-root/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///jalan/ke/mirror/</span>

- Berpindah ke sistem yang telah di bootstrap:

`sudo chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/ke/root</span>

- Memperlihatkan rilis Debian atau Ubuntu yang tersedia:

`ls /usr/share/debootstrap/scripts/`
