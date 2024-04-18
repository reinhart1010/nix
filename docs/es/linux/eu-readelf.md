---
layout: page
title: linux/eu-readelf (español)
description: "Muestra información sobre archivos ELF."
content_hash: 4fdfb4630c711c202bf94d7d16b5528656a0aae9
last_modified_at: 2024-04-18
related_topics:
  - title: English version
    url: /en/linux/eu-readelf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eu-readelf

Muestra información sobre archivos ELF.
Más información: <https://manned.org/eu-readelf>.

- Muestra toda la información extraíble en un archivo ELF:

`eu-readelf --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra el contenido de todos los segmentos y secciones de NOTE, o de un segmento o sección en particular:

`eu-readelf --notes[=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.note.ABI-tag</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/fichero</span>
