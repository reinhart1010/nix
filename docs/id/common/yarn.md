---
layout: page
title: common/yarn (Indonesia)
description: "Pengelola paket alternatif untuk JavaScript dan Node.js."
content_hash: ac29fa12f58a4b1ba0537ecef04800f7139601d6
related_topics:
  - title: English version
    url: /en/common/yarn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yarn.html
    icon: bi bi-globe
---
# yarn

Pengelola paket alternatif untuk JavaScript dan Node.js.
Informasi lebih lanjut: <https://yarnpkg.com>.

- Memasang modul secara global:

`yarn global add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>

- Memasang semua dependensi yang dirujuk di berkas `package.json` (`install` adalah opsional):

`yarn install`

- Memasang modul dan menyimpannya sebagai dependensi ke berkas `package.json` (tambahkan `--dev` untuk menyimpannya sebagai dependensi pengembangan):

`yarn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Mencopot modul dan menghapusnya dari berkas `package.json`:

`yarn remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>

- Membuat berkas `package.json` secara interaktif:

`yarn init`

- Mengidentifikasi apakah modul merupakan dependensi dan daftar modul lainnya yang bergantung padanya:

`yarn why `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>
