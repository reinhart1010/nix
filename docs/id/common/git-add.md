---
layout: page
title: common/git-add (Indonesia)
description: "Tambahkan file yang diubah ke indeks."
content_hash: 135a89b57ddeab23f5a7b47b388066e9a81ef00a
last_modified_at: 2024-06-20
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git add

Tambahkan file yang diubah ke indeks.
Informasi lebih lanjut: <https://git-scm.com/docs/git-add>.

- Tambahkan file ke indeks:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/file</span>

- Tambahkan semua file (yang terlacak dan tidak terlacak):

`git add -A`

- Hanya tambahkan file yang sudah terlacak:

`git add -u`

- Tambahkan juga file yang diabaikan:

`git add -f`

- Menambahkan file ke status stage secara interaktif:

`git add -p`

- Menambahkan file tertentu ke status stage secara interaktif:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/file</span>

- Stage file secara interaktif:

`git add -i`
