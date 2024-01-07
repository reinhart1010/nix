---
layout: page
title: common/git-annex (Indonesia)
description: "Kelola file dengan Git, tanpa memeriksa isi kontennya."
content_hash: a761021584cd66bbf504794fa7fa27ce4ec1bc6a
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-annex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-annex.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-annex.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git annex

Kelola file dengan Git, tanpa memeriksa isi kontennya.
Saat file dianeksasi, kontennya dipindahkan ke penyimpanan key-value, dan symlink dibuat yang mengarah ke konten tersebut.
Informasi lebih lanjut: <https://git-annex.branchable.com>.

- Inisialisasi sebuah repositori dengan Git annex:

`git annex init`

- Tambahkan file ke dalam repositori:

`git annex add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Tampilkan status file atau direktori saat ini:

`git annex status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Sinkronisasikan repositori lokal dengan sumber remote:

`git annex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>

- Dapatkan isi file atau direktori:

`git annex get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Tampilkan informasi bantuan:

`git annex help`
