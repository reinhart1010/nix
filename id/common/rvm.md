---
layout: page
title: common/rvm (Indonesia)
description: "Alat untuk menginstal, mengatur dan bekerja dengan berbagai lingkungan Ruby."
content_hash: dfccdf4c35ea5276d8d50ef24f64c32c480232ac
related_topics:
  - title: English version
    url: /en/common/rvm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rvm.html
    icon: bi bi-globe
---
# rvm

Alat untuk menginstal, mengatur dan bekerja dengan berbagai lingkungan Ruby.
Informasi lebih lanjut: <https://rvm.io>.

- Instal satu atau lebih versi Ruby (dipisah dengan spasi):

`rvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version(s)</span>

- Menampilkan daftar versi-versi yang terinstal:

`rvm list`

- Menggunakan spesifik versi Ruby:

`rvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Menyetel versi Ruby bawaan:

`rvm --default use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Memperbarui versi Ruby:

`rvm upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current_version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_version</span>

- Menghapus versi Ruby dan menyimpan kode sumbernya:

`rvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Menghapus versi Ruby sekaligus kode sumbernya:

`rvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Menampilkan spesifik _dependencies_ untuk sistem operasi anda:

`rvm requirements`
