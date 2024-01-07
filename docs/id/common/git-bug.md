---
layout: page
title: common/git-bug (Indonesia)
description: "Manajer laporan masalah/bug yang menggunakan penyimpanan git, sehingga tidak memengaruhi susunan berkas dalam direktori proyek Anda."
content_hash: 0afe37309299d623efc1bd399e586619b4fac060
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-bug.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bug

Manajer laporan masalah/bug yang menggunakan penyimpanan git, sehingga tidak memengaruhi susunan berkas dalam direktori proyek Anda.
Anda dapat memasukkan laporan melalui sumber/hulu jauh (remote) yang sama untuk berinteraksi dengan laporan dan pengguna lainnya seperti mengatur komit dan cabang.
Informasi lebih lanjut: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

- Buat identitas/pengguna baru:

`git bug user create`

- Buat laporan masalah/bug baru:

`git bug add`

- Kumpulkan laporan-laporan baru menuju sumber/hulu jarak jauh:

`git bug push`

- Dapatkan pembaruan atas daftar masalah dari sumber/hulu jarak jauh:

`git bug pull`

- Lihat daftar masalah/bug yang sebelumnya telah dilaporkan:

`git bug ls`

- Saring (filter) dan urutkan (sort) laporan menggunakan kata kunci permintaan tertentu:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">open</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edit</span>`"`

- Cari laporan menurut kata kunci teks:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>`" baz`
