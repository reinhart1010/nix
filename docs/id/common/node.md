---
layout: page
title: common/node (Indonesia)
description: "Platform JavaScript sisi server (Node.js)."
content_hash: 63610a708fcc76b0994a45a2a69bf5aa30b084f4
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/common/node.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/node.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/node.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/node.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># node

Platform JavaScript sisi server (Node.js).
Informasi lebih lanjut: <https://nodejs.org>.

- Jalankan berkas program JavaScript:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Jalankan sebuah REPL (shell interaktif):

`node`

- Jalankan berkas program dan jalankan ulang saat isi dari berkas tersebut terubah (membutuhkan Node.js versi 18.11+):

`node --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Evaluasi kode JavaScript dengan memberikanya sebagai sebuah argument:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode</span>`"`

- Evaluasi kode dan cetak hasil, berguna untuk melihat versi dependesni node:

`node -p "process.versions"`

- Aktifkan inspector, yang akan menjeda eksekusi sampai debugger terhubung segera setelah kode sumber sepenuhnya terparser:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
