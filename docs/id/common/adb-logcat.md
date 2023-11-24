---
layout: page
title: common/adb-logcat (Indonesia)
description: "Dapatkan dan simpan log sistem pada perangkat Android."
content_hash: ce7ee60657d5c74c5de47c611fc1ca88c64f6dce
last_modified_at: 2023-11-24
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
  - title: Nederlands version
    url: /nl/common/adb-logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adb-logcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adb-logcat

Dapatkan dan simpan log sistem pada perangkat Android.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/logcat>.

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

`adb logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Tampilkan pesan-pesan log dari aplikasi tertentu (menurut package identifier seperti `com.example.myapp`):

`adb logcat --pid=$(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengenal_aplikasi</span>`)`

- Tampilkan log sistem secara warna-warni (biasanya digunakan untuk menyaring pesan-pesan log):

`adb logcat -v color`
