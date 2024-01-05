---
layout: page
title: android/logcat (فارسی)
description: "تخلیه یک لاگ از پیاهم های سیستمی، شامل پشته رهگیری زمان وقوع خطا، و اطلاعات پیام های لاگ شده توسط برنامه ها."
content_hash: 365d7d441a16b24f54d712f389b8aca38c15420b
last_modified_at: 2024-01-05
related_topics:
  - title: বাংলা version
    url: /bn/android/logcat.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/logcat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/android/logcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/logcat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/logcat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/logcat.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/logcat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/logcat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/logcat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/logcat.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logcat

تخلیه یک لاگ از پیاهم های سیستمی، شامل پشته رهگیری زمان وقوع خطا، و اطلاعات پیام های لاگ شده توسط برنامه ها.
اطلاعات بیشتر: <https://developer.android.com/studio/command-line/logcat>.

- نمایش لاگ سیستمی :

`logcat`

- نوشتن لاگ سیستمی به یک فایل :

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- نمایش خطاهای منطبق با الگوی ورودی :

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- نمایش لاگ های مربوط به یک PID مشخص :

`logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- نمایش لاگ های پروسه های مربوط به یک بسته مشخص :

`logcat --pid=$(pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`)`
