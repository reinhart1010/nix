---
layout: page
title: common/nano (español)
description: "Editor sencillo y fácil de usar. Un clon libre y mejorado de `Pico`."
content_hash: 8767bf915ec890110cca92dd1eb80b3b0dab133e
last_modified_at: 2024-11-01
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
tldri18n_status: 2
---
# nano

Editor sencillo y fácil de usar. Un clon libre y mejorado de `Pico`.
Vea también: `emacs`, `helix`, `vim`.
Más información: <https://nano-editor.org>.

- Inicia el editor:

`nano`

- Inicia el editor sin usar archivos de configuración:

`nano --ignorercfiles`

- Abre archivos específicos, moviéndose al siguiente archivo cuando se cierra el anterior:

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Abre un archivo específico, posicionando el cursor en la línea y columna específica:

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">línea</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo específico y activa el ajuste de línea suave (wrapping):

`nano --softwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre un archivo específico y sangra nuevas líneas al nivel de las líneas anteriores:

`nano --autoindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre nano y crea un archivo de respaldo (`ruta/al/archivo~`) cuando se guardan las ediciones:

`nano --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
