---
layout: page
title: common/adb-shell (русский)
description: "Android Debug Bridge Shell: Запуск удалённой командной оболочки на эмуляторе Android или подключенном устройстве Android."
content_hash: 9b79e937c9e24cc139f691dffcc25f69e73063f6
last_modified_at: 2024-02-22
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-shell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-shell.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb shell

Android Debug Bridge Shell: Запуск удалённой командной оболочки на эмуляторе Android или подключенном устройстве Android.
Больше информации: <https://developer.android.com/tools/adb>.

- Запустить удалённую интерактивную оболочку на эмуляторе или устройстве:

`adb shell`

- Получить все свойства от эмулятора или устройства:

`adb shell getprop`

- Вернуть всем разрешениям значение по умолчанию:

`adb shell pm reset-permissions`

- Отозвать опасные разрешения для приложения:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">разрешения</span>

- Вызвать событие клавиши:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">код_клавиши</span>

- Очистить данные приложения на эмуляторе или устройстве:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Запустить activity на эмуляторе или устройстве:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">активность</span>

- Запустить базовый activity на эмуляторе или устройстве:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
