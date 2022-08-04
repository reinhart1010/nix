---
layout: page
title: android/pm (Indonesia)
description: "Menampilkan daftar pemasangan aplikasi di dalam sebuah perangkat Android."
content_hash: 9354656414d5682229826728dbfa71f12517dabe
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---
# pm

Menampilkan daftar pemasangan aplikasi di dalam sebuah perangkat Android.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb#pm>.

- Menampilkan daftar seluruh aplikasi yang terpasang:

`pm list packages`

- Menampilkan daftar seluruh aplikasi sistem yang terpasang:

`pm list packages -s`

- Menampilkan daftar seluruh aplikasi pihak ketiga yang terpasang:

`pm list packages -3`

- Menampilkan daftar aplikasi dengan kata kunci tertentu:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Menampilkan jalan menuju file APK untuk sebuah aplikasi:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplikasi</span>
