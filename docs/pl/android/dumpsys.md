---
layout: page
title: android/dumpsys (polski)
description: "Dostarczanie informacji o usługach systemu Android."
content_hash: 618c0e0bd86c6fac0d19f9e5aa20631d0a4fff32
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
  - title: Indonesia version
    url: /id/android/dumpsys.html
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

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dumpsys

Dostarczanie informacji o usługach systemu Android.
Ta komenda może być używana tylko poprzez `adb shell`.
Więcej informacji: <https://developer.android.com/studio/command-line/dumpsys>.

- Uzyskaj dane diagnostyczne dla wszystkich usług systemowych:

`dumpsys`

- Uzyskaj dane diagnostyczne dla określonej usługi systemowej:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usługa</span>

- Lista wszystkich usług, o których `dumpsys` może dać informacje:

`dumpsys -l`

- Lista argumentów specyficznych dla usługi:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usługa</span>` -h`

- Wykluczenie określonej usługi z wyjścia diagnostycznego:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usługa</span>

- Określenie czasu oczekiwania w sekundach (domyślnie 10s):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sekundy</span>
