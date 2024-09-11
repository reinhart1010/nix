---
layout: page
title: common/git-init (Indonesia)
description: "Inisialisasikan sebuah repositori Git lokal."
content_hash: 737e639da08fef34d3859c7b79c72abafd62fa90
last_modified_at: 2024-09-11
related_topics:
  - title: Deutsch version
    url: /de/common/git-init.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-init.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-init.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-init.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-init.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-init.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-init.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-init.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git init

Inisialisasikan sebuah repositori Git lokal.
Informasi lebih lanjut: <https://git-scm.com/docs/git-init>.

- Inisialisasikan suatu direktori menjadi repositori lokal baru:

`git init`

- Inisialisasikan sebuah repositori dengan nama cabang (branch) awal yang ditentukan:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Inisialisasikan sebuah repositori menggunakan format hash objek berbasis SHA256 (membutuhkan Git versi 2.29+):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Inisialisasikan sebuah repositori kosong (barebones) yang dapat digunakan sebagai remote melalui koneksi SSH:

`git init --bare`
