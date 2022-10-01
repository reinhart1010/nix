---
layout: page
title: common/pnpm (Indonesia)
description: "Manajer paket JavaScript dan Node.js yang cepat dan efisien."
content_hash: 2f41e9537561b316581702804c25908709db6c87
related_topics:
  - title: English version
    url: /en/common/pnpm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pnpm

Manajer paket JavaScript dan Node.js yang cepat dan efisien.
Mengelola proyek Node.js dan dependensi modulnya.
Informasi lebih lanjut:: <https://pnpm.io>.

- Buat file `package.json` file:

`pnpm init`

- Unduh semua paket yang terdaftar sebagai dependensi di package.json:

`pnpm install`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar dependensi di package.json:

`pnpm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Unduh paket dan menambahkan ke daftar dependensi [D]ev di package.json:

`pnpm add -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Unduh paket dan instal secara [g]lobal:

`pnpm add -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Copot pemasangan paket dan hapus dari daftar dependensi di package.json:

`pnpm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Mencetak pohon dependensi yang diinstal secara lokal:

`pnpm list`

- Buat daftar modul tingkat atas yang diinstal secara [g]lobal:

`pnpm list -g --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
