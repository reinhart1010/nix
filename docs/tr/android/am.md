---
layout: page
title: android/am (Türkçe)
description: "Android aktivite yöneticisi."
content_hash: f44b960d434635a5618537c29335f2af260741d6
related_topics:
  - title: Deutsch version
    url: /de/android/am.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/am.html
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
  - title: português (Brasil) version
    url: /pt_BR/android/am.html
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
# am

Android aktivite yöneticisi.
Daha fazla bilgi: <https://developer.android.com/studio/command-line/adb#am>.

- Belirtilmiş bir aktiviteyi başlat:

`am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.android.settings/.Settings</span>

- Bir aktivite başlatıp veriyi ona aktar:

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>

- Belirtilmiş bir eylem ve kategoriyi karşılayan bir aktivite başlat:

`am start -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.MAIN</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.category.HOME</span>

- Bir kastı URI'a çevir:

`am to-uri -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android.intent.action.VIEW</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
