---
layout: page
title: common/nvm (Indonesia)
description: "Memasang, melepas, atau mengganti versi Node.js yang dipakai."
content_hash: 2b99b4a0dad438eb30a38b04cb841b9844c604d4
related_topics:
  - title: Deutsch version
    url: /de/common/nvm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nvm.html
    icon: bi bi-globe
---
# nvm

Memasang, melepas, atau mengganti versi Node.js yang dipakai.
Mendukung nomor versi seperti "0.12" or "v4.2", dan label versi seperti "stable", "system", dsb.
Informasi lebih lanjut: <https://github.com/creationix/nvm>.

- Memasang versi Node.js yang ditentukan:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Menggunakan versi Node.js tertentu untuk sesi saat ini:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Menyetel versi Node.js secara default:

`nvm alias default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Menunjukkan daftar versi Node.js yang tersedia dan versi Node.js yang disetel sebagai default:

`nvm list`

- Menghapus sebuah versi Node.js yang terpasang melalui `nvm`:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Menjalankan interpreter (REPL) Node.js dengan versi tertentu:

`nvm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>` --version`

- Menjalankan sebuah file atau aplikasi JavaScript di dalam Node.js versi tertentu:

`nvm exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>` node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>
