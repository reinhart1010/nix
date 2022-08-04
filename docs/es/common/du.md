---
layout: page
title: common/du (español)
description: "Uso de disco: estima y resume el uso de espacio en disco de archivos y directorios."
content_hash: 28c984c5d46d4279ba0aabe8985fcb7be47587a7
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># du

Uso de disco: estima y resume el uso de espacio en disco de archivos y directorios.
Más información: <https://www.gnu.org/software/coreutils/du>.

- Lista los tamaños de un directorio y sus subdirectorios en las unidades dadas (B/KiB/MiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista los tamaños de un directorio y sus subdirectorios en formato legible para humanos (es decir, seleccionando automáticamente las unidades apropiadas para cada tamaño):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra el tamaño de un solo directorio en formato legible para humanos:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista los tamaños legibles para humanos de un directorio y de todos los archivos y directorios dentro del mismo:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista los tamaños legibles para humanos de un directorio y sus subdirectorios hasta N niveles de profundidad:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista el tamaño legible para humanos de todos los archivos `.jpg` en subdirectorios del directorio actual y muestra un total al final:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
