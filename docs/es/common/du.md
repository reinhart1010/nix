---
layout: page
title: common/du (español)
description: "Uso del disco: estima y resume el uso del espacio de archivos y directorios."
content_hash: ac99a66a38848b104031124b05f09026d077560f
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Uso del disco: estima y resume el uso del espacio de archivos y directorios.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Lista los tamaños de un directorio y sus subdirectorios, en la unidad dada (B/KiB/MiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista los tamaños de un directorio y sus subdirectorios, de forma legible (es decir, seleccionando automáticamente la unidad adecuada para cada tamaño):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra el tamaño de un único directorio, en unidades legibles:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista los tamaños legibles de un directorio y de todos los archivos y directorios que contiene:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista los tamaños legibles de un directorio y sus subdirectorios, hasta N niveles de profundidad:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista el tamaño legible de todos los archivos `.jpg` en los subdirectorios del directorio actual y muestra un total acumulado al final:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>

- Lista todos los archivos y directorios (incluidos los ocultos) por encima de un determinado tamaño (útil para investigar qué está ocupando realmente el espacio):

`du --all --human-readable --threshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1G|1024M|1048576K</span>` .[^.]* *`
