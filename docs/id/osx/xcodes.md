---
layout: page
title: osx/xcodes (Indonesia)
description: "Unduh, pasang, dan atur pemasangan aplikasi Xcode dalam versi yang berbeda."
content_hash: ae6898fbacabf13929c770670f84d92d071ff704
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/osx/xcodes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcodes

Unduh, pasang, dan atur pemasangan aplikasi Xcode dalam versi yang berbeda.
Informasi lebih lanjut: <https://github.com/xcodesorg/xcodes>.

- Tampilkan daftar versi Xcode yang terpasang:

`xcodes installed`

- Tampilkan daftar versi Xcode yang tersedia:

`xcodes list`

- Pilih versi Xcode yang hendak digunakan sebagai default, dengan menyertakan versi atau lokasi aplikasi:

`xcodes select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_xcode|jalan/menuju/Xcode.app</span>

- Unduh dan pasang Xcode versi tertentu:

`xcodes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_xcode</span>

- Pasang aplikasi Xcode terkini dan pilih sebagai versi default:

`xcodes install --latest --select`

- Unduh Xcode versi tertentu ke sebuah direktori tanpa memasangnya ke dalam perangkat:

`xcodes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_xcode</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>
