---
layout: page
title: common/adb-reverse (русский)
description: "Android Debug Bridge Reverse: обратное соединение от эмулятора Android или подключенного устройства Android."
content_hash: cb212e86edc1c13798489a9e8b4506d84c36a473
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-reverse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-reverse.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reverse.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-reverse.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-reverse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reverse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb reverse

Android Debug Bridge Reverse: обратное соединение от эмулятора Android или подключенного устройства Android.
Больше информации: <https://developer.android.com/studio/command-line/adb>.

- Вывести список всех обратных соединений от эмуляторов и устройств:

`adb reverse --list`

- Создать обратное соединение по TCP-порту от эмулятора или устройства до localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">удалённый_порт</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">локальный_порт</span>

- Удалить обратное соединение из эмулятора или устройства:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">удалённый_порт</span>

- Удалить все обратные соединения на всех эмуляторах и устройствах:

`adb reverse --remove-all`
