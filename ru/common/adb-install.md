---
layout: page
title: common/adb-install (русский)
description: "Android Debug Bridge Install: Установка пакетов на эмулятор Android или подключенное устройство Android."
content_hash: da44b2c30be3f8d710ff71e43fca7f62e759e241
related_topics:
  - title: English version
    url: /en/common/adb-install.html
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
# adb install

Android Debug Bridge Install: Установка пакетов на эмулятор Android или подключенное устройство Android.
Больше информации: <https://developer.android.com/studio/command-line/adb>.

- Установить приложение Android на эмулятор/устройство:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Переустановить существующее приложение, оставив его данные:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Дать все разрешения, перечисленные в манифесте приложения:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Быстрое обновление установленного пакета путём обновления только тех частей APK, которые изменились:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>
