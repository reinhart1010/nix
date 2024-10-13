---
layout: page
title: common/git-branch (Indonesia)
description: "Perintah Git utama untuk bekerja dengan cabang (_branch_)."
content_hash: 9fa81cfe93fddadb8cbd35ca2c136787c7097cba
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-branch.html
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

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--move</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_lama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_baru</span>

- Hapus cabang lokal (harus bukan cabang saat ini untuk melakukannya):

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Hapus cabang remote:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang_remote</span>
