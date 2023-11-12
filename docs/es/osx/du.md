---
layout: page
title: osx/du (español)
description: "Uso del disco: estima y resume el uso del espacio de archivos y directorios."
content_hash: d35de9c75981ce891be291f488d83af869eb9884
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/osx/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Uso del disco: estima y resume el uso del espacio de archivos y directorios.
Más información: <https://ss64.com/osx/du.html>.

- Lista los tamaños de un directorio y de cualquier subdirectorio, en la unidad dada (KiB/MiB/GiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Enumera los tamaños de un directorio y sus subdirectorios, de forma legible (es decir, seleccionando automáticamente la unidad adecuada para cada tamaño):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra el tamaño de un único directorio, en unidades legibles para el ser humano:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra los tamaños legibles de un directorio y de todos los archivos y directorios que contiene:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista los tamaños legibles de un directorio y sus subdirectorios, hasta N niveles de profundidad:

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista el tamaño legible de todos los archivos `.jpg` en los subdirectorios del directorio actual y muestra un total acumulado al final:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
