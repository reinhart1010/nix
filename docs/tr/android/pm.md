---
layout: page
title: android/pm (Türkçe)
description: "Android cihazındaki uygulamalar ile ilgili bilgi göster."
content_hash: ac12dd3b53339f041f490fd6dbfbb6ed983d591e
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
  - title: தமிழ் version
    url: /ta/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---
# pm

Android cihazındaki uygulamalar ile ilgili bilgi göster.
Daha fazla bilgi için: <https://developer.android.com/studio/command-line/adb#pm>.

- İndirilen tüm uygulamaların sırala:

`pm list packages`

- İndirilen tüm sistem uygulamalarını sırala:

`pm list packages -s`

- İndirilen tüm üçüncü el uygulamaları sırala:

`pm list packages -3`

- Belirtilen anahtar kelimelere uyan uygulamaları sırala:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anahtar_kelimeler</span>

- Belirtilen uygulamanın APK'sine giden yolu görüntüle:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uygulama</span>
