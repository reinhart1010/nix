---
layout: page
title: freebsd/pkg (Indonesia)
description: "Manajer paket untuk FreeBSD."
content_hash: 0283d029134d987349793f4cf8101e134f731c06
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/freebsd/pkg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/pkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg

Manajer paket untuk FreeBSD.
Informasi lebih lanjut: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Pasang sebuah paket:

`pkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus pemasangan paket:

`pkg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Perbarui seluruh paket yang terpasang ke dalam versi terbaru:

`pkg upgrade`

- Cari paket yang tersedia dalam repositori:

`pkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Tampilkan daftar paket yang terpasang:

`pkg info`

- Hapus paket penunjang (dependency) yang sudah tidak dipakai:

`pkg autoremove`
