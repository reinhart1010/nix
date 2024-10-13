---
layout: page
title: common/adb-logcat (Indonesia)
description: "Dapatkan dan simpan log sistem pada perangkat Android."
content_hash: 5875dd5e0051c6085e1939dc227beec824804f71
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-logcat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb-logcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb logcat

Dapatkan dan simpan log sistem pada perangkat Android.
Informasi lebih lanjut: <https://developer.android.com/tools/logcat>.

- Tampilkan log sistem pada perangkat yang terhubung saat ini:

`adb logcat`

- Saring dan tampilkan log berdasarkan kriteria ekspresi reguler:

`adb logcat -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>

- Saring dan tampilkan log menurut tingkat mode ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent) serta tag pada pesan-pesan log:

`adb logcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mode</span>` *:S`

- Tampilkan pesan-pesan log dari aplikasi berbasis React Native dalam mode [V]erbose, dan jangan tampilkan ([S]ilence) pesan lainnya:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Tampilkan pesan-pesan log yang dikategorikan dalam tingkat mode [W]arning ke atas, tanpa menghiraukan jenis tag yang disaring:

`adb logcat *:W`

- Tampilkan pesan-pesan log dari proses tertentu (menurut kode PID proses tersebut):

`adb logcat --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Tampilkan pesan-pesan log dari aplikasi tertentu (menurut package identifier seperti `com.example.myapp`):

`adb logcat --pid $(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengenal_aplikasi</span>`)`

- Tampilkan log sistem secara warna-warni (biasanya digunakan untuk menyaring pesan-pesan log):

`adb logcat -v color`
