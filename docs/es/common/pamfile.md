---
layout: page
title: common/pamfile (español)
description: "Describe archivos Netpbm (PAM o PNM)."
content_hash: 82a12a567827580dee646c9bac36ecfa6727ec8a
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/pamfile.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamfile.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamfile.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamfile

Describe archivos Netpbm (PAM o PNM).
Más información: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- Describe los archivos Netpbm especificados:

`pamfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Describe cada imagen en cada archivo de entrada (a diferencia de la primera imagen en cada archivo) en un formato legible para la máquina:

`pamfile -allimages -machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra un conteo de cuántas imágenes contiene el archivo:

`pamfile -count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
