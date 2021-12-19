---
layout: page
title: android/logcat (Indonesia)
description: "Menampilkan dan menyimpan log sistem."
content_hash: 416495d87a58590b60ce7b0bef0096e7811b0e80
related_topics:
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
---
# logcat

Menampilkan dan menyimpan log sistem.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/logcat>.

- Menampilkan log sistem:

`logcat`

- Menyimpan log sistem di dalam sebuah file:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Menyaring informasi log berdasarkan sintaks ekspresi reguler (regex) tertentu:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>
