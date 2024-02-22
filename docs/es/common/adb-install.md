---
layout: page
title: common/adb-install (español)
description: "Instalación de Android Debug Bridge: Envía paquetes a una instancia del emulador de Android o a dispositivos Android conectados."
content_hash: 94cbdc98c3efd5d2488f269c812a0aa7a9c65319
last_modified_at: 2024-02-22
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
  - title: Nederlands version
    url: /nl/common/adb-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-install.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb install

Instalación de Android Debug Bridge: Envía paquetes a una instancia del emulador de Android o a dispositivos Android conectados.
Más información: <https://developer.android.com/tools/adb>.

- Envía una aplicación Android a un emulador/dispositivo:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>

- Envía una aplicación Android a un emulador/dispositivo específico (ignora `$ANDROID_SERIAL`):

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_serie</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>

- Reinstala una aplicación existente, manteniendo sus datos:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>

- Envía una aplicación Android permitiendo bajar el código de versión (sólo paquetes depurables):

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>

- Concede todos los permisos enumerados en el manifiesto de la aplicación:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>

- Actualiza rápidamente un paquete instalado actualizando sólo las partes del APK que han cambiado:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>
