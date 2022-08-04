---
layout: page
title: common/aapt (español)
description: "Herramienta para empaquetado de activos de Android."
content_hash: dd91bea5e4a7a7f837764eee6330b1ecc7a198fe
related_topics:
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
---
# aapt

Herramienta para empaquetado de activos de Android.
Compila y empaqueta recursos de una app de Android.
Más información: <https://elinux.org/Android_aapt>.

- Lista los archivos contenidos en un archivo APK:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/app.apk</span>

- Muestra la metadata de una app (versión, permisos, etc.):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/app.apk</span>

- Crea un nuevo archivo APK con archivos de un directorio especificado:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/app.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
