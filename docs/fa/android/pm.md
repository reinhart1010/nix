---
layout: page
title: android/pm (فارسی)
description: "نمایش اطلاعات مربوط به برنامه های یک دستگاه اندروید."
content_hash: 38b7754e0fb17ac976d8c4b15bdb702d7c43b256
last_modified_at: 2023-09-14
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
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
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
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pm

نمایش اطلاعات مربوط به برنامه های یک دستگاه اندروید.
اطلاعات بیشتر: <https://developer.android.com/studio/command-line/adb#pm>.

- فهرست تمامی برنامه های نصب شده :

`pm list packages`

- فهرست تمامی برنامه های سیستمی نصب شده :

`pm list packages -s`

- فهرست تمامی برنامه های نصب شده شخض ثالث :

`pm list packages -3`

- فهرست برنامه های منطبق با کلید واژه(ها) :

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">کلمه کلیدی 1 کلمه کلیدی 2 ...</span>

- نمایش مسیر فایل APK یک برنامه مشخص :

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>
