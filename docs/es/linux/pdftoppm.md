---
layout: page
title: linux/pdftoppm (español)
description: "Convierte páginas de documentos PDF al formato de imagen Pixmap portátil."
content_hash: 92c72785e92cf613f5533b68f859ed5b8a82b5ee
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/linux/pdftoppm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pdftoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftoppm

Convierte páginas de documentos PDF al formato de imagen Pixmap portátil.
Más información: <https://manned.org/pdftoppm>.

- Especifica el rango de páginas a convertir (N es la primera página, M es la última página):

`pdftoppm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo_del_nombre_de_la_imagen</span>

- Convierte solo la primera página de un PDF:

`pdftoppm -singlefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo_del_nombre_de_la_imagen</span>

- Genera un archivo PBM monocromático (en lugar de un archivo PPM de color):

`pdftoppm -mono `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo_del_nombre_de_la_imagen</span>

- Genera un archivo PGM en escala de grises (en lugar de un archivo PPM de color):

`pdftoppm -gray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo_del_nombre_de_la_imagen</span>

- Genera un archivo PNG en lugar de un archivo PPM:

`pdftoppm -png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo_del_nombre_de_la_imagen</span>
