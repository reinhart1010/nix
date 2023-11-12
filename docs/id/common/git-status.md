---
layout: page
title: common/git-status (Indonesia)
description: "Menampilkan perubahan pada file dalam repositori Git."
content_hash: fa25fe2069b7c64bfaf574365e1a99a9265b259f
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/common/git-status.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git status

Menampilkan perubahan pada file dalam repositori Git.
Menmapilkan daftar perubahan , menambahkan dan menghapus file dibandingkan dengan komit yang saat ini di check-out.
Informasi lebih lanjut: <https://git-scm.com/docs/git-status>.

- Tampilkan file yang diubah yang belum ditambahkan untuk komit:

`git status`

- Berikan keluaran dalam format [s]hort (pendek):

`git status -s`

- Jangan tampilkan file yang tidak terlacak di output:

`git status --untracked-files=no`

- Tampilkan keluaran dalam format [s]hort (pendek) bersama dengan [b] info cabangnya:

`git status -sb`
