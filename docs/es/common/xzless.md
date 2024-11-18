---
layout: page
title: common/xzless (español)
description: "Muestra texto de archivos comprimidos `xz` y `lzma`."
content_hash: 9953a2ef35e49c60b9f7674bb8e336a92a174e08
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/xzless.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/xzless.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xzless.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xzless

Muestra texto de archivos comprimidos `xz` y `lzma`.
Vea también: `less`.
Más información: <https://manned.org/xzless>.

- Muestra un archivo comprimido:

`xzless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra un archivo comprimido incluyendo el números de línea:

`xzless --LINE-NUMBERS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra un archivo comprimido y sale si el archivo entero se puede mostrar en la primera pantalla:

`xzless --quit-if-one-screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
