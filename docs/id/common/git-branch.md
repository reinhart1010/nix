---
layout: page
title: common/git-branch (Indonesia)
description: "Perintah Git utama untuk bekerja dengan cabang (*branch*)."
content_hash: 45a91ae68ac01e1a7c8354cfd465e4a80b5f7035
related_topics:
  - title: Deutsch version
    url: /de/common/git-branch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-branch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
---
# git branch

Perintah Git utama untuk bekerja dengan cabang (*branch*).
Informasi lebih lanjut: <https://git-scm.com/docs/git-branch>.

- Menampilkan daftar cabang lokal. Cabang saat ini ditandai oleh `*`:

`git branch`

- Menampilkan daftar semua cabang (lokal dan remote):

`git branch -a`

- Tunjukkan nama cabang saat ini:

`git branch --show-current`

- Buat cabang baru berdasarkan komit saat ini:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Buat cabang baru berdasarkan komit tertentu:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_komit</span>

- Ganti nama cabang (harus bukan cabang saat ini untuk melakukannya):

`git branch -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_lama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_baru</span>

- Hapus cabang lokal (harus bukan cabang saat ini untuk melakukannya):

`git branch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Hapus cabang remote:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_remote</span>
