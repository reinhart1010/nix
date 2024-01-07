---
layout: page
title: common/git-cat-file (Indonesia)
description: "Dapatkan informasi konten atau jenis dan ukuran untuk objek repositori Git."
content_hash: fdd010e026e0c5a406406c6b4fe43c0bae616673
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-cat-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cat-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cat-file.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cat-file.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cat-file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cat-file

Dapatkan informasi konten atau jenis dan ukuran untuk objek repositori Git.
Informasi lebih lanjut: <https://git-scm.com/docs/git-cat-file>.

- Dapatkan ukuran ([s]ize) untuk komit terkini (HEAD), dalam hitungan bita/byte:

`git cat-file -s HEAD`

- Dapatkan [t]ipe yang direferensikan dalam suatu objek Git (seperti blob, tree, komit, atau tag):

`git cat-file -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8c442dc3</span>

- Cetak isi objek Git yang diberikan berdasarkan jenisnya, dalam format yang mudah dibaca manusia:

`git cat-file -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>
