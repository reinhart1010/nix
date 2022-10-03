---
layout: page
title: android/dumpsys (Indonesia)
description: "Berikan informasi tentang layanan (daemon) sistem milik Android."
content_hash: fb863396bfcd88d6772f31f124763a43f333ac31
related_topics:
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/dumpsys.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/dumpsys.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/dumpsys.html
    icon: bi bi-globe
---
# dumpsys

Berikan informasi tentang layanan (daemon) sistem milik Android.
Perintah ini hanya dapat dijalankan melalui `adb shell`.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/dumpsys>.

- Tampilkan informasi diagnostik terhadap seluruh layanan sistem Android:

`dumpsys`

- Tampilkan informasi diagnostik untuk layanan sistem tertentu:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layanan</span>

- Tampilkan daftar layanan sistem yang diketahui oleh `dumpsys`:

`dumpsys -l`

- Tampilkan daftar argumen yang diterima oleh sebuah layanan sistem:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layanan</span>` -h`

- Kecualikan layanan sistem tertentu dari informasi diagnostik yang ditampilkan:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layanan</span>

- Tetapkan periode waktu habis dalam hitungan detik (10 detik secara default):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detik</span>
