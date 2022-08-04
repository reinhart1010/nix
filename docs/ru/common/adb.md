---
layout: page
title: common/adb (русский)
description: "Android Debug Bridge: управление запущенным эмулятором Android или подключенным устройством Android."
content_hash: 98277f74ba730831f783dc0954dc931880d2b585
related_topics:
  - title: English version
    url: /en/common/adb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
---
# adb

Android Debug Bridge: управление запущенным эмулятором Android или подключенным устройством Android.
Некоторые подкоманды, такие как `adb shell`, имеют собственную документацию по использованию.
Больше информации: <https://developer.android.com/studio/command-line/adb>.

- Проверить, запущен ли процесс сервера adb и запустить его:

`adb start-server`

- Завершить процесс сервера adb:

`adb kill-server`

- Запустить удалённую оболочку на целевом эмуляторе/устройстве:

`adb shell`

- Установить приложение Android на эмуляторе/устройстве:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.apk</span>

- Скопировать файл/папку с целевого устройства:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки_или_файла_на_устройстве</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/локальной_папки</span>

- Скопировать файл/папку на целевое устройство:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/локального_файла_или_папки</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/целевой_папки_на_устройстве</span>

- Вывести список подключенных устройств:

`adb devices`
