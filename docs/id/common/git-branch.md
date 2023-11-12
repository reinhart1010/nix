---
layout: page
title: common/git-branch (Indonesia)
description: "Perintah Git utama untuk bekerja dengan cabang (_branch_)."
content_hash: c526b7b31306779ebc28a633aab85d59ba1eca16
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-branch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git branch

Perintah Git utama untuk bekerja dengan cabang (_branch_).
Informasi lebih lanjut: <https://git-scm.com/docs/git-branch>.

- Tampilkan daftar semua cabang (lokal dan remote; cabang saat ini ditandai oleh `*`) :

`git branch --all`

- Tampilkan daftar semua cabang yang memiliki komit Git tertentu di dalam riwayat:

`git branch --all --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_komit</span>

- Tampilkan nama cabang saat ini:

`git branch --show-current`

- Buat cabang baru berdasarkan komit saat ini:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Buat cabang baru berdasarkan komit tertentu:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_komit</span>

- Ubah nama cabang (harus bukan cabang saat ini untuk melakukannya):

`git branch -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_lama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_baru</span>

- Hapus cabang lokal (harus bukan cabang saat ini untuk melakukannya):

`git branch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Hapus cabang remote:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_remote</span>
