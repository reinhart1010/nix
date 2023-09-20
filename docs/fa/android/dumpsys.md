---
layout: page
title: android/dumpsys (فارسی)
description: "ارائه اطلاعات درباره سیستم سرویس اندروید."
content_hash: da9864f54782ca647bee42477a0d9520acf5862b
last_modified_at: 2023-09-14
related_topics:
  - title: বাংলা version
    url: /bn/android/dumpsys.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/dumpsys.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/dumpsys.html
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

ارائه اطلاعات درباره سیستم سرویس اندروید.
این دستور فقط از طریق `adb shell` قابل اجراست.
اطلاعات بیشتر: <https://developer.android.com/studio/command-line/dumpsys>.

- دریافت اطلاعات عیب بای تمامی سرویس های سیستمی :

`dumpsys`

- دریافت اطلاعات عیب یابی یک سرویس سیستمی مشخص :

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">سرویس</span>

- فهرستی از تمامی سرویس هایی که `dumpsys` میتواند اطلاعات بدهد :

`dumpsys -l`

- ورودی های یک سرویس مشخص را فهرست میکند :

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">سرویس</span>` -h`

- حذف یک سرویس مشخص از خروجی عیب یابی :

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">سرویس</span>

- تعیین فرصت زمانی بر مبنای ثانیه (پیش فرض 10ثانیه) :

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>