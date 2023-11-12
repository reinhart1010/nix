---
layout: page
title: android/dumpsys (українська)
description: "Отримати інформацію про системні сервіси Android."
content_hash: 57fb604cd171ced994c6b034e1b1df98da6cc15f
last_modified_at: 2023-11-12
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
  - title: فارسی version
    url: /fa/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/dumpsys.html
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
tldri18n_status: 2
---
# dumpsys

Отримати інформацію про системні сервіси Android.
Ця команда може бути виконана тільки за допомогою `adb shell`.
Більше інформації: <https://developer.android.com/studio/command-line/dumpsys>.

- Отримати дані діагностики для всіх системних сервісів:

`dumpsys`

- Отримати дані діагностики для конкретного системного сервісу:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">сервіс</span>

- Вивести усі сервіси `dumpsys`, про які може бути надана інформація:

`dumpsys -l`

- Вивести специфічні аргументи для сервісу:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">сервіс</span>` -h`

- Виключити специфічний сервіс з виводу діагностики:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">сервіс</span>

- Визначити таймаут в секундах (стандартно 10 секунд):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>
