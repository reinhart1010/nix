---
layout: page
title: android/pm (Indonesia)
description: "Tampilkan daftar pemasangan aplikasi di dalam sebuah perangkat Android."
content_hash: cdb0a1dc3382931da31be40272c7353d9b7c9301
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/android/pm.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/pm.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/pm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/pm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/pm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/pm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/pm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/pm.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pm

Tampilkan daftar pemasangan aplikasi di dalam sebuah perangkat Android.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb#pm>.

- Tampilkan daftar seluruh aplikasi yang terpasang:

`pm list packages`

- Tampilkan daftar seluruh aplikasi sistem yang terpasang:

`pm list packages -s`

- Tampilkan daftar seluruh aplikasi pihak ketiga yang terpasang:

`pm list packages -3`

- Tampilkan daftar aplikasi dengan kata kunci tertentu:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Tampilkan jalan menuju file APK untuk sebuah aplikasi:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplikasi</span>
