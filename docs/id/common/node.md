---
layout: page
title: common/node (Indonesia)
description: "Platform JavaScript sisi server (Node.js)."
content_hash: ab1ba38803d1d7fb3d702eefc09f6a612d72515c
last_modified_at: 2023-11-12
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

- Menjalankan berkas JavaScript:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas</span>

- Memulai sebuah REPL (shell interaktif):

`node`

- Mengevaluasi kode JavaScript dengan memberikanya sebagai sebuah argument:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode</span>`"`

- Mengevaluasi dan mencetak hasil, berguna untuk melihat versi dependesni node:

`node -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process.versions</span>`"`

- Mengaktifkan inspector, menjeda eksekusi sampai debugger terhubung segera setelah kode sumber sepenuhnya terparser:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas</span>
