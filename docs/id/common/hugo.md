---
layout: page
title: common/hugo (Indonesia)
description: "Penghasil website statis berbasis template. Menggunakan modul, komponen dan tema."
content_hash: 1e0239dd8feee0a63bc3636d0093112a6272dad1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/hugo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hugo

Penghasil website statis berbasis template. Menggunakan modul, komponen dan tema.
Informasi lebih lanjut: <https://gohugo.io>.

- Membuat website Hugo baru:

`hugo new site `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/website</span>

- Membuat tema Hugo baru (tema juga dapat diunduh dari <https://themes.gohugo.io/>):

`hugo new theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_tema</span>

- Membuat halaman baru:

`hugo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_bagian</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas</span>

- Menbuild website ke direktori `./public`:

`hugo`

- Menbuild website termasuk halaman yang ditandai sebagai "draft":

`hugo --buildDrafts`

- Menbuild website ke direktori yang ditentukan:

`hugo --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/tujuan</span>

- Menbuild website, memulai webserver untuk menyajikannya, dan secara otomatis memuat ulang jika ada halaman yang berubah:

`hugo server`
