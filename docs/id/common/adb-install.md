---
layout: page
title: common/adb-install (Indonesia)
description: "Android Debug Bridge Install: Memasang paket ke emulator Android atau perangkat Android terhubung."
content_hash: bd51e678cfbdf6b7cb9837b44c1f40a6129c808b
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-install.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb install

Android Debug Bridge Install: Memasang paket ke emulator Android atau perangkat Android terhubung.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Pasang aplikasi Android ke emulator/perangkat:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>

- Pasang aplikasi Android menuju emulator/perangkat tertentu (berdasarkan nomor serial yang didapatkan dari `adb devices`, mengesampingkan nilai `$ANDROID_SERIAL`):

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_serial</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.apk</span>

- Pasang ulang aplikasi yang sudah ada, menjaga datanya:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>

- Pasang aplikasi Android versi lawas dari aplikasi Android yang sudah terpasang pada perangkat (khusus aplikasi debug):

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>

- Berikan semua izin yang terdaftar di manifest aplikasi:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>

- Perbarui langsung paket terinstal dengan hanya memperbarui bagian dari APK yang berubah:

`Adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>
