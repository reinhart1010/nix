---
layout: page
title: android/settings (українська)
description: "Отримайте інформацію про операційну систему Android."
content_hash: d725bc751d2d088bf215bd188325407381c8979e
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/android/settings.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/settings.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/settings.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/settings.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/settings.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/settings.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/settings.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/settings.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/settings.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/settings.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/settings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/settings.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/settings.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/settings.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/settings.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/settings.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/settings.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/settings.html
    icon: bi bi-globe
tldri18n_status: 2
---
# settings

Отримайте інформацію про операційну систему Android.
Більше інформації: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Вивести список налаштувань в глобальному (`global`) просторі імен:

`settings list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>

- Отримайте значення конкретного налаштування:

`settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">airplane_mode_on</span>

- Встановіть значення для налаштування:

`settings put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen_brightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Видаліть визначене налаштування:

`settings delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secure</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screensaver_enabled</span>
