---
layout: page
title: common/git-add (Indonesia)
description: "Tambahkan berkas yang diubah ke indeks."
content_hash: 2907e8f8469984e47ad5d1b6fbe5f36da13a7f4c
last_modified_at: 2024-09-10
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

Tambahkan berkas yang diubah ke indeks.
Informasi lebih lanjut: <https://git-scm.com/docs/git-add>.

- Tambahkan suatu berkas ke dalam indeks:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tambahkan seluruh berkas (baik yang terlacak maupun tidak terlacak):

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-A|--all</span>

- Tambahkan seluruh berkas pada folder saat ini:

`git add .`

- Hanya tambahkan berkas yang sudah terlacak:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--update</span>

- Tambahkan juga berkas yang diabaikan:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Tambahkan berkas ke status stage secara interaktif:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--patch</span>

- Tambahkan berkas tertentu ke status stage secara interaktif:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--patch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Stage file secara interaktif:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>
