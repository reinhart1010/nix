---
layout: page
title: android/am (हिन्दी)
description: "एंड्रॉइड गतिविधि प्रबंधक।"
content_hash: e369f6db7149a5e331ca8601cfe661a00c1e6b3b
last_modified_at: 2023-10-25
related_topics:
  - title: বাংলা version
    url: /bn/android/am.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/am.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/am.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/am.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/am.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/am.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/android/am.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/android/am.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/am.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/am.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/am.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/am.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/am.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/am.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/am.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/am.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># am

एंड्रॉइड गतिविधि प्रबंधक।
अधिक जानकारी: <https://developer.android.com/studio/command-line/adb#am>.

- एक विशिष्ट गतिविधि प्रारंभ करें:

`am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.android.settings/.Settings</span>

- एक गतिविधि शुरू करें और उसमें डेटा[d] पास करें:

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>

- किसी विशिष्ट क्रिया और श्रेणी[c] से मेल खाती गतिविधि प्रारंभ करें:

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.MAIN</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.category.HOME</span>

- एक उद्देश्य को यूआरआई में बदलें:

`am to-uri -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
