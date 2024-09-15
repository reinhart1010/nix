---
layout: page
title: common/hugo (Indonesia)
description: "Penghasil situs web statis berbasis template. Menggunakan modul, komponen dan tema."
content_hash: 9d3e1cef1c90367c6e2a5b375a0d17bf2307a27d
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/common/hugo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hugo

Penghasil situs web statis berbasis template. Menggunakan modul, komponen dan tema.
Informasi lebih lanjut: <https://gohugo.io>.

- Buat sebuah proyek situs web Hugo baru:

`hugo new site `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/website</span>

- Buat sebuah proyek tema Hugo baru (tema juga dapat diunduh dari <https://themes.gohugo.io/>):

`hugo new theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_tema</span>

- Buat sebuah halaman situs web baru:

`hugo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_bagian</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_halaman</span>

- Bangun situs web dari direktori sumber menuju direktori `./public`:

`hugo`

- Bangun situs web termasuk halaman yang ditandai sebagai "draft":

`hugo --buildDrafts`

- Bangun situs web dengan untuk dijalankan pada alamat IP lokal:

`hugo server --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip-lokal</span>` --baseURL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://ip-lokal</span>

- Bangun situs web menuju direktori yang ditentukan:

`hugo --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/tujuan</span>

- Bangun situs web dan jalankan peladen (server) untuk menyajikannya, dengan memuat ulang saat terdapat halaman yang berubah:

`hugo server`
