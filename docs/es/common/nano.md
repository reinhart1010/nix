---
layout: page
title: common/nano (español)
description: "Editor sencillo y fácil de usar. Un clon libre y mejorado de Pico."
content_hash: 9e44497651d1dc152a56b9e7f49e6f01ab2b0467
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/nano.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/nano.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nano.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nano.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nano

Editor sencillo y fácil de usar. Un clon libre y mejorado de Pico.
Más información: <https://nano-editor.org>.

- Abre un nuevo archivo en nano:

`nano`

- Abre un archivo específico:

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo específico, posicionando el cursor en la línea y columna específica:

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linea</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo específico y activa el ajuste de línea:

`nano --softwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo específico y sangra nuevas líneas a la sangría de las líneas anteriores:

`nano --autoindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre nano y crea un archivo de resguardo (`archivo~`) cuando se guardan las ediciones:

`nano --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
