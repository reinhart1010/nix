---
layout: page
title: common/nvm (Indonesia)
description: "Memasang, lepas, atau ganti versi Node.js yang dipakai."
content_hash: 041da5b90897d2caf9aba7d28509207ed2963fe0
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/common/nvm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nvm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvm

Memasang, lepas, atau ganti versi Node.js yang dipakai.
Mendukung nomor versi seperti "12.8" or "v16.13.1", dan label versi seperti "stable", "system", dsb.
Informasi lebih lanjut: <https://github.com/creationix/nvm>.

- Pasang suatu versi Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Gunakan suatu versi Node.js untuk sesi saat ini:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Tentukan versi default Node.js untuk sesi-sesi berikutnya:

`nvm alias default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Tunjukkan daftar versi Node.js yang tersedia dan yang disetel sebagai default:

`nvm list`

- Hapus pemasangan versi Node.js yang terpasang melalui `nvm`:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>

- Jalankan interpreter (REPL) Node.js dengan versi tertentu:

`nvm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>` --version`

- Jalankan suatu berkas atau program JavaScript di dalam Node.js versi tertentu:

`nvm exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_node_js</span>` node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>
