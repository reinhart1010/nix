---
layout: page
title: common/adb (Indonesia)
description: "Android Debug Bridge: berkomunikasi dengan emulator Android atau perangkat Android terhubung."
content_hash: 84310c76bf5758914ab58b85a6db866eb986bf9b
last_modified_at: 2023-11-12
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
Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `adb shell`.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Cek apakah proses server adb telah dimulai dan memulainya:

`adb start-server`

- Hentikan proses server adb:

`adb kill-server`

- Mulai shell jarak jauh pada emulator/perangkat tujuan:

`adb shell`

- Instal aplikasi Android ke emulator/perangkat tujuan:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas.apk</span>

- Salin berkas/direktori dari perangkat tujuan:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas_atau_direktori_perangkat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/direktori_lokal_tujuan</span>

- Salin berkas/direktori ke perangkat tujuan:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas_atau_direktori_lokal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/direktori_perangkat_tujuan</span>

- Dapatkan daftar perangkat yang terhubung:

`adb devices`
