---
layout: page
title: common/aapt (русский)
description: "Утилита для упаковки ресурсов для Android."
content_hash: 0342d7896f588b54604eed85744437b27398c6d6
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/aapt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aapt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aapt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aapt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aapt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aapt

Утилита для упаковки ресурсов для Android.
Компилирует и упаковывает ресурсы приложений Android.
Больше информации: <https://elinux.org/Android_aapt>.

- Вывести список файлов содержащихся в APK-архиве:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/приложения.apk</span>

- Отобразить мета-данные приложения (версия, разрешения, и т.д.):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/приложения.apk</span>

- Создать новый APK-архив с файлами из указанной папки:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/приложения.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>
