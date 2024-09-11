---
layout: page
title: common/git-status (Indonesia)
description: "Tampilkan perubahan pada berkas dalam repositori Git."
content_hash: 798cce025dc9e8d774d6ddc022c7ac4f1cb60330
last_modified_at: 2024-09-11
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-status.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-status.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-status.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-status.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git status

Tampilkan perubahan pada berkas dalam repositori Git.
Menampilkan daftar perubahan, menambahkan dan menghapus berkas dibandingkan dengan komit yang saat ini diperiksa (checkout).
Informasi lebih lanjut: <https://git-scm.com/docs/git-status>.

- Tampilkan daftar berkas yang diubah yang belum ditambahkan untuk komit:

`git status`

- Tampilkan informasi dalam format [s]ingkat:

`git status --short`

- Tampilkan informasi secara terperinci ([v]erbose) baik dalam panggung rencana perubahan (staging) dan direktori kerja saat ini:

`git status --verbose --verbose`

- Tampilkan informasi mengenai cabang ([b]ranch) dan status pelacakan dari remote:

`git status --branch`

- Tampilkan daftar berkas beserta informasi cabang ([b]ranch) dalam format [s]ingkat:

`git status --short --branch`

- Tampilkan jumlah entri yang disimpan ke dalam kumpulan stash:

`git status --show-stash`

- Jangan tampilkan berkas yang tidak terlacak:

`git status --untracked-files=no`
