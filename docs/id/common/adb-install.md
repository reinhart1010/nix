---
layout: page
title: common/adb-install (Indonesia)
description: "Android Debug Bridge Install: Menginstal paket ke emulator Android atau perangkat Android terhubung."
content_hash: 75a7dcfedcfdeb850b34b05d1d1479e602b78c6b
last_modified_at: 2023-11-12
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb install

Android Debug Bridge Install: Menginstal paket ke emulator Android atau perangkat Android terhubung.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Instal aplikasi Android ke emulator/perangkat:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>

- Instal ulang aplikasi yang sudah ada, menjaga datanya:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>

- Berikan semua izin yang terdaftar di manifest aplikasi:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>

- Perbarui langsung paket terinstal dengan hanya memperbarui bagian dari APK yang berubah:

`Adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>
