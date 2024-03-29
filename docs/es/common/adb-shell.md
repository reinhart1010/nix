---
layout: page
title: common/adb-shell (español)
description: "Android Debug Bridge Shell: Ejecuta comandos shell remotos en una instancia del emulador de Android o en dispositivos Android conectados."
content_hash: b244a1159eb7b17983fa817500b15b2ad2e6d8e5
last_modified_at: 2024-02-22
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
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
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb shell

Android Debug Bridge Shell: Ejecuta comandos shell remotos en una instancia del emulador de Android o en dispositivos Android conectados.
Más información: <https://developer.android.com/tools/adb>.

- Inicia una shell interactiva remota en el emulador o dispositivo:

`adb shell`

- Obtén todas las propiedades del emulador o dispositivo:

`adb shell getprop`

- Revierte todos los permisos de ejecución a sus valores por defecto:

`adb shell pm reset-permissions`

- Revoca un permiso peligroso para una aplicación:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permission</span>

- Activa un evento de clave:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keycode</span>

- Borra los datos de una aplicación en un emulador o dispositivo:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Inicia una actividad en el emulador o dispositivo:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activity</span>

- Inicia la actividad de inicio en un emulador o dispositivo:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
