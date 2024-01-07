---
layout: page
title: common/git-check-ignore (Indonesia)
description: "Analisa kumpulan file yang diabaikan/dikecualikan oleh Git (didefinisikan dalam \".gitignore\")."
content_hash: 6a2c9a8a0d82c6c4967198df35581e3fb781f984
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-check-ignore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-check-ignore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-check-ignore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-check-ignore.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ignore

Analisa kumpulan file yang diabaikan/dikecualikan oleh Git (didefinisikan dalam ".gitignore").
Informasi lebih lanjut: <https://git-scm.com/docs/git-check-ignore>.

- Cek apakah suatu file atau direktori telah diabaikan:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Cek apakah lebih dari satu file atau direktori telah diabaikan:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...</span>

- Cek pengecualian file dan direktori menggunakan daftar yang didefinisikan dalam `stdin`:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_daftar</span>

- Jangan cek index Git (biasanya dipakai untuk mengetahui mengapa terdapat jalur yang tetap dilacak Git dan tak diabaikan):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...</span>

- Tampilkan informasi pola pengecualian `.gitignore` yang dipakai untuk mengecualikan setiap jalur:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...</span>
