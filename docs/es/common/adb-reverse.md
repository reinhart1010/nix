---
layout: page
title: common/adb-reverse (español)
description: "Android Debug Bridge Reverse: conexiones de socket inversas desde una instancia de emulador de Android o dispositivos Android conectados."
content_hash: c5e0ec83e2b2d123120d88dc4c3c4b321f1fc694
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
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
  - title: русский version
    url: /ru/common/adb-reverse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reverse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb reverse

Android Debug Bridge Reverse: conexiones de socket inversas desde una instancia de emulador de Android o dispositivos Android conectados.
Más información: <https://developer.android.com/studio/command-line/adb>.

- Lista de todas las conexiones de socket inverso de emuladores y dispositivos:

`adb reverse --list`

- Invertir un puerto TCP desde un emulador o dispositivo a localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>

- Eliminar una conexión de socket inversa de un emulador o dispositivo:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- Elimina todas las conexiones de socket inverso de todos los emuladores y dispositivos:

`adb reverse --remove-all`
