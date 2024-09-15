---
layout: page
title: common/git-commit (Indonesia)
description: "Komit berkas ke dalam sebuah repositori."
content_hash: 9d8a50758139e2e3b80ac2fdd804c3c358473b6c
last_modified_at: 2024-09-15
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
  - title: 한국어 version
    url: /ko/common/git-commit.html
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
tldri18n_status: 2
---
# git commit

Komit berkas ke dalam sebuah repositori.
Informasi lebih lanjut: <https://git-scm.com/docs/git-commit>.

- Komit berkas bertahap ke repositori dengan sebuah pesan:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`"`

- Komit berkas bertahap dengan pesan yang disimpan dalam suatu berkas:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_pesan_komit</span>

- Ubah secara otomatis semua berkas yang dimodifikasi menjadi ke status stage dan menambahkan sebuah pesan:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`"`

- Komit berkas bertahap kemudian tandatangani komit tersebut menggunakan kunci GPG (atau kunci yang didefinisikan dalam berkas konfigurasi jika tidak didefinisikan):

`git commit --gpg-sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_kunci_gpg</span>` --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`"`

- Ganti komit terakhir dengan perubahan yang ada di status stage saat ini:

`git commit --amend`

- Komit berkas tertentu (yang sudah di status stage):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Buat komit kosong, tanpa berkas bertahap:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`" --allow-empty`
