---
layout: page
title: common/nm (español)
description: "Lista los nombres de símbolos en los archivos objeto."
content_hash: 1a5251baf38da4695d36b08012f1a6b5b223f836
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/nm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nm

Lista los nombres de símbolos en los archivos objeto.
Más información: <https://manned.org/nm>.

- Lista de funciones globales (externas) en un archivo (con prefijo T):

`nm -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>

- Lista solo los símbolos no definidos en un archivo:

`nm -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>

- Lista todos los símbolos, incluso símbolos de depuración:

`nm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>

- Reconstruye símbolos C++ (hace que sean legibles):

`nm --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>
