---
layout: page
title: common/adb (español)
description: "Android Debug Bridge: comunica con una instancia de un emulador Android o conecta dispositivos Android."
content_hash: e0e9f1e4eed7ae94200a87f15d45de47e62f8bb6
last_modified_at: 2023-10-19
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
---
# adb

Android Debug Bridge: comunica con una instancia de un emulador Android o conecta dispositivos Android.
Algunos subcomandos, como `adb shell`, tienen su propia documentación de uso.
Más información: <https://developer.android.com/studio/command-line/adb>.

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

- Obtiene una lista de dispositivos conectados:

`adb devices`
