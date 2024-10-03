---
layout: page
title: common/rvm (Indonesia)
description: "Alat untuk menginstal, mengatur dan bekerja dengan berbagai lingkungan Ruby."
content_hash: c09f267ba6be9c46435df4cf49b93bf23695d56f
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/rvm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rvm

Alat untuk menginstal, mengatur dan bekerja dengan berbagai lingkungan Ruby.
Informasi lebih lanjut: <https://rvm.io>.

- Pasang suatu atau beberapa versi Ruby:

`rvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi1 versi2 ...</span>

- Tampilkan daftar versi-versi Ruby yang terinstal:

`rvm list`

- Gunakan suatu versi Ruby untuk sesi saat ini:

`rvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Tetapkan versi default Ruby yang akan dipakai:

`rvm --default use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Perbarui suatu versi Ruby:

`rvm upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_saat_ini</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_baru</span>

- Hapus pemasangan versi Ruby namun simpan kode sumbernya:

`rvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Hapus pemasangan versi Ruby beserta kode sumbernya:

`rvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Tampilkan prasyarat piranti lunak tambahan yang perlu dipasang untuk sistem operasi anda:

`rvm requirements`
