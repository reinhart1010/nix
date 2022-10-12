---
layout: page
title: common/adb-install (русский)
description: "Android Debug Bridge Install: Установка пакетов на эмулятор Android или подключённое устройство Android."
content_hash: 6234b21a59d0cb004506580a5548c1c710b04d45
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-install.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adb-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adb install

Android Debug Bridge Install: Установка пакетов на эмулятор Android или подключённое устройство Android.
Больше информации: <https://developer.android.com/studio/command-line/adb>.

- Установить приложение Android на эмулятор/устройство:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Установить приложение Android на конкретный эмулятор/устройство (отменяет использование `$ANDROID_SERIAL`):

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">серийный_номер</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Переустановить существующее приложение, оставив его данные:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Установить приложение Android, разрешив понижение версии (только для отлаживаемых пакетов):

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Дать все разрешения, перечисленные в манифесте приложения:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Быстрое обновление установленного пакета путём обновления только тех частей APK, которые изменились:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>
