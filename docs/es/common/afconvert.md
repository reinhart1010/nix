---
layout: page
title: common/afconvert (español)
description: "Convierte entre formatos de archivo AFF y raw."
content_hash: 9d353a9bfeb2bc13448fdea695fb414a4758db50
last_modified_at: 2023-02-13
related_topics:
  - title: English version
    url: /en/common/afconvert.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/afconvert.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># afconvert

Convierte entre formatos de archivo AFF y raw.
Más información: <https://manned.org/afconvert.1>.

- Utiliza una extensión específica (predeterminado: `aff`):

`afconvert -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida1 ruta/al/archivo_salida2 ...</span>

- Utiliza un nivel de compresión específico (predeterminado: `7`):

`afconvert -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida1 ruta/al/archivo_salida2 ...</span>
