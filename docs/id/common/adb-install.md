---
layout: page
title: common/adb-install (Indonesia)
description: "Android Debug Bridge Install: Menginstal paket ke emulator Android atau perangkat Android terhubung."
content_hash: f59f1e67134ba897adb0a46a3db4dba154acaa42
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
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
---
# adb install

Android Debug Bridge Install: Menginstal paket ke emulator Android atau perangkat Android terhubung.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Menginstal aplikasi Android ke emulator/perangkat:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>

- Menginstal ulang aplikasi yang sudah ada, menjaga datanya:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>

- Memberikan semua izin yang terdaftar di manifest aplikasi:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>

- Memperbarui langsung paket terinstal dengan hanya memperbarui bagian dari APK yang berubah:

`Adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>
