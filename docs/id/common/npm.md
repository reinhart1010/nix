---
layout: page
title: common/npm (Indonesia)
description: "Manajer paket JavaScript dan Node.js."
content_hash: e60d378ee78ee32f9a502a3cc9dd11a5daaf9b78
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/npm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

Manajer paket JavaScript dan Node.js.
Mengelola proyek Node.js dan dependensi modulnya.
Informasi lebih lanjut: <https://www.npmjs.com>.

- Membuat file `package.json` secara interaktif:

`npm init`

- Unduh semua paket yang terdaftar sebagai dependensi di package.json:

`npm install`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar dependensi di `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Unduh paket dan menambahkan ke daftar dependensi dev di package.json:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- Unduh paket dan instal secara global:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>

- Copot pemasangan paket dan hapus dari daftar dependensi di `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>

- Mencetak pohon dependensi yang diinstal secara lokal:

`npm list`

- Buat daftar modul tingkat atas yang diinstal secara global:

`npm list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
