---
layout: page
title: common/adb (español)
description: "Android Debug Bridge: comunica con una instancia de un emulador Android o conecta dispositivos Android."
content_hash: 6205e8a2c53e302ce387aca8f65c2d1937acf66d
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/common/adb.html
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
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb

Android Debug Bridge: comunica con una instancia de un emulador Android o conecta dispositivos Android.
Algunos subcomandos, como `shell`, tienen su propia documentación de uso.
Más información: <https://developer.android.com/tools/adb>.

- Verifica si el proceso del servidor adb está ejecutandose y lo inicia:

`adb start-server`

- Termina el proceso del servidor adb:

`adb kill-server`

- Inicia una terminal remota en la instancia del emulador/dispositivo de destino:

`adb shell`

- Instala una aplicación Android a un emulador/dispositivo:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>

- Copia un archivo/directorio desde el dispositivo de destino:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio_en_el_dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_destino_local</span>

- Copia un archivo/directorio al dispositivo de destino:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio_local</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_de_destino_en_el_dispositivo</span>

- Obtén una lista de dispositivos conectados:

`adb devices`
