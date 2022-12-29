---
layout: page
title: common/pnpm (Indonesia)
description: "Manajer paket JavaScript dan Node.js yang cepat dan efisien."
content_hash: 706f6e1ef2cb10e4a35349e4c6d584b818cd01d4
last_modified_at: 2022-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/pnpm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pnpm.html
    icon: bi bi-globe
---
# pnpm

Manajer paket JavaScript dan Node.js yang cepat dan efisien.
Mengelola proyek Node.js dan dependensi modulnya.
Informasi lebih lanjut: <https://pnpm.io>.

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
