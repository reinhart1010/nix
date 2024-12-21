---
layout: page
title: linux/ldd (español)
description: "Muestra dependencias de bibliotecas compartidas de un binario."
content_hash: 3c6cfd9d01159ecee931b022145d7f7b04a26a44
last_modified_at: 2024-12-21
related_topics:
  - title: Deutsch version
    url: /de/linux/ldd.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ldd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ldd

Muestra dependencias de bibliotecas compartidas de un binario.
No use en un binario no confiable, use `objdump` para esto en su lugar.
Más información: <https://manned.org/ldd>.

- Muestra dependencias de biblioteca compartidas de un binario:

`ldd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Muestra toda la información sobre las dependencias:

`ldd --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Muestra dependencias directas no utilizadas:

`ldd --unused `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Reporta objetos de datos perdidos y realiza reubicaciones de datos:

`ldd --data-relocs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Reporta objetos y funciones de datos ausentes y los reubica a ambos:

`ldd --function-relocs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>
