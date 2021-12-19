---
layout: page
title: common/wc (español)
description: "Cuenta líneas, palabras, y bytes."
content_hash: 9d7715313d8bff27bc7cce52d45b7cb5c7f223a8
related_topics:
  - title: English version
    url: /en/common/wc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/wc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wc.html
    icon: bi bi-globe
---
# wc

Cuenta líneas, palabras, y bytes.
Más información: <https://www.gnu.org/software/coreutils/wc>.

- Cuenta todas las líneas en un archivo:

`wc --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todas las palabras en un archivo:

`wc --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todos los bytes en un archivo:

`wc --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todos los caracteres en un archivo (considerando los caracteres de varios bytes):

`wc --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todas las lineas, palabras y bytes desde stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`

- Cuenta la longitud de la linea más larga en número de caracteres:

`wc --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
