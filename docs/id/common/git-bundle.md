---
layout: page
title: common/git-bundle (Indonesia)
description: "Bungkus seluruh objek dan referensi internal Git ke dalam suatu berkas arsip."
content_hash: e6354d22953ce36f32ba003c4b48480bf21c0dc2
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/git-bundle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-bundle.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bundle.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bundle

Bungkus seluruh objek dan referensi internal Git ke dalam suatu berkas arsip.
Informasi lebih lanjut: <https://git-scm.com/docs/git-bundle>.

- Buat sebuah berkas (bundle) dengan seluruh objek dan referensi Git pada cabang tertentu:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Bungkus objek dan referensi untuk seluruh cabang:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>` --all`

- Bungkus objek dan referensi untuk lima komit terakhir pada cabang saat ini:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>` -5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Bungkus objek dan referensi untuk perubahan sejak 7 hari terakhir:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>` --since 7.days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Cek apakah suatu berkas bundle bersifat valid dan dapat diaplikasikan ke dalam repositori saat ini:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>

- Cetak daftar berkas referensi yang terkandung dalam berkas bundle menuju `stdout`:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>

- Buka dan pakai isi bungkusan untuk suatu cabang pada repositori saat ini:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_cabang</span>

- Buat sebuah repositori baru dari suatu berkas bundle:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.bundle</span>
