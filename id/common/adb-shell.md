---
layout: page
title: common/adb-shell (Indonesia)
description: "Android Debug Bridge Shell: Menjalankan perintah shell jarak jauh pada emulator Android atau perangkat Android terhubung."
content_hash: 80b9fe165fd73f2c0e7028c3b1c2add0f5c0722e
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
---
# adb shell

Android Debug Bridge Shell: Menjalankan perintah shell jarak jauh pada emulator Android atau perangkat Android terhubung.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Memulai shell interaktif jarak jauh di emulator/perangkat:

`adb shell`

- Mendapatkan semua properti dari emulator/perangkat:

`adb shell getprop`

- Mengembalikan semua izin runtime ke default:

`adb shell pm reset-permissions`

- Mencabut izin berbahaya dari sebuah aplikasi:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">izin</span>

- Memicu sebuah peristiwa penting:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keycode</span>

- Mengosongkan data aplikasi pada emulator/perangkat:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Memulai aktivitas pada emulator/perangkat:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aktivitas</span>

- Memulai aktivitas beranda pada emulator/perangkat:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
