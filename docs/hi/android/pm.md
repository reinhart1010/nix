---
layout: page
title: android/pm (हिन्दी)
description: "एंड्रॉइड डिवाइस पर ऐप्स के बारे में जानकारी प्रदर्शित करें।"
content_hash: f236ce463e7e4d0afd7ef419046024644345f130
last_modified_at: 2023-11-04
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
  - title: Indonesia version
    url: /id/android/pm.html
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
---
# pm

एंड्रॉइड डिवाइस पर ऐप्स के बारे में जानकारी प्रदर्शित करें।
अधिक जानकारी: <https://developer.android.com/studio/command-line/adb#pm>.

- सभी इंस्टॉल किए गए ऐप्स की सूची बनाएं:

`pm list packages`

- सभी इंस्टॉल किए गए सिस्टम ऐप्स की सूची बनाएं:

`pm list packages -s`

- सभी इंस्टॉल किए गए तृतीय-पक्ष ऐप्स की सूची बनाएं:

`pm list packages -3`

- विशिष्ट कीवर्ड से मेल खाने वाले ऐप्स की सूची बनाएं:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कीवर्ड1 कीवर्ड2 ...</span>

- किसी विशिष्ट ऐप के एपीके का पथ प्रदर्शित करें:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप</span>
