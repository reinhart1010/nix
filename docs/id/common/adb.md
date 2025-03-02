---
layout: page
title: common/adb (Indonesia)
description: "Android Debug Bridge: berkomunikasi dengan emulator Android atau perangkat Android terhubung."
content_hash: a8da8e9b40efd1198cecb6d32183a8f8de71e430
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/adb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb

Android Debug Bridge: berkomunikasi dengan emulator Android atau perangkat Android terhubung.
Beberapa subperintah seperti `shell` mempunyai dokumentasi terpisah.
Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Periksa apakah proses server adb telah dimulai dan memulainya:

`adb start-server`

- Hentikan proses server adb:

`adb kill-server`

- Mulai shell jarak jauh pada emulator/perangkat tujuan:

`adb shell`

- Pasang suatu aplikasi Android menuju emulator/perangkat tujuan:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>

- Salin berkas/direktori dari perangkat tujuan:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori_perangkat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_lokal_tujuan</span>

- Salin berkas/direktori menuju perangkat tujuan:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori_lokal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_perangkat_tujuan</span>

- Tampilkan daftar perangkat yang terhubung:

`adb devices`

- Tentukan perangkat yang diinstruksikan (berdasarkan nomor induk / Device ID) jika terdapat lebih dari satu perangkat yang terhubung secara bersamaan:

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>
