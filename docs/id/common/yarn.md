---
layout: page
title: common/yarn (Indonesia)
description: "Pengelola paket alternatif untuk JavaScript dan Node.js."
content_hash: bf4fb5fcaf13b26814be22a1cb8b69472678eb22
last_modified_at: 2024-10-03
related_topics:
  - title: Deutsch version
    url: /de/common/yarn.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/yarn.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yarn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yarn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yarn

Pengelola paket alternatif untuk JavaScript dan Node.js.
Informasi lebih lanjut: <https://yarnpkg.com>.

- Pasang suatu modul secara global:

`yarn global add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>

- Pasang semua pustaka prasyarat (dependency) yang dirujuk dalam berkas `package.json` (perintah `install` adalah opsional):

`yarn install`

- Pasang dan catat suatu modul sebagai prasyarat ke dalam berkas `package.json` (tambahkan `--dev` jika hendak menyimpannya sebagai prasyarat khusus tahap pengembangan):

`yarn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Hapus pemasangan modul beserta entrinya dalam berkas `package.json`:

`yarn remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>

- Membuat berkas `package.json` secara interaktif:

`yarn init`

- Periksa apakah suatu modul merupakan suatu prasyarat serta tampilkan daftar modul lainnya yang bergantung kepadanya:

`yarn why `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>
