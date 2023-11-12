---
layout: page
title: common/git-commit (Indonesia)
description: "Komit file ke dalam sebuah repositori."
content_hash: 5c57acc0241f8dc8fa300d008308b395b893cef1
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git commit

Komit file ke dalam sebuah repositori.
Informasi lebih lanjut: <https://git-scm.com/docs/git-commit>.

- Komit file bertahap ke repositori dengan sebuah pesan:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`"`

- Otomatis merubah semua file yang dimodifikasi menjadi ke status stage dan menambahkan sebuah pesan:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`"`

- Ganti komit terakhir dengan perubahan yang ada di status stage saat ini:

`git commit --amend`

- Komit file tertentu (yang sudah di status stage):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/file/saya1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/file/saya2</span>
