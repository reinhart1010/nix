---
layout: page
title: common/df (español)
description: "Muestra una visión general del uso del espacio en disco del sistema de archivos."
content_hash: ae4d43cc89a1038aee2520623986a4f988c84fb8
last_modified_at: 2024-11-11
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># df

Muestra una visión general del uso del espacio en disco del sistema de archivos.
Más información: <https://manned.org/df.1posix>.

- Muestra todos los sistemas de ficheros y su uso de disco usando unidades de 512 bytes:

`df`

- Muestra el sistema de archivos y su uso del disco que contiene el archivo o directorio dado:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Utiliza unidades de 1024 bytes en las columnas de cifras de espacio:

`df -k`

- Muestra la información de forma portátil (formato POSIX):

`df -P`
