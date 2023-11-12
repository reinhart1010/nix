---
layout: page
title: android/pm (русский)
description: "Показать информацию о приложениях на устройстве Android."
content_hash: 6853f755437e9f78621cbf0c0514c9786437d93e
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

Показать информацию о приложениях на устройстве Android.
Больше информации: <https://developer.android.com/studio/command-line/adb#pm>.

- Показать список всех установленных приложений:

`pm list packages`

- Показать список всех установленных системных приложений:

`pm list packages -s`

- Показать список всех установленных сторонних приложений:

`pm list packages -3`

- Показать список приложений по ключевым словам:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ключевые_слова</span>

- Показать путь к APK определенного приложения:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">приложение</span>
