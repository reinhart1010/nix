---
layout: page
title: linux/readelf (español)
description: "Muestra información sobre archivos ELF."
content_hash: 41971c80486ebc582b2c57fcff48dc2a5f6aaa26
last_modified_at: 2024-05-14
related_topics:
  - title: English version
    url: /en/linux/readelf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/readelf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# readelf

Muestra información sobre archivos ELF.
Más información: <https://manned.org/readelf.1>.

- Muestra toda la información de un archivo ELF:

`readelf -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>

- Muestra todas las cabeceras presentes en un archivo ELF:

`readelf --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>

- Muestra las entradas en la sección de la tabla de símbolos del archivo ELF, si tiene una:

`readelf --symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>

- Muestra la información de la cabecera ELF:

`readelf --file-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>

- Muestra información de cabecera de la sección ELF:

`readelf --section-headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_binario</span>
