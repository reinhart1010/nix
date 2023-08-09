---
layout: page
title: osx/pbcopy (español)
description: "Copia datos de `stdin` al portapapeles."
content_hash: a262394258e6640a3c4b6515ac3f024474489120
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pbcopy

Copia datos de `stdin` al portapapeles.
Comparable a pulsar Cmd + C en el teclado.
Más información: <https://ss64.com/osx/pbcopy.html>.

- Coloca el contenido de un archivo específico en el portapapeles:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Coloca los resultados de un comando específico en el portapapeles:

`find . -type t -name "*.png" | pbcopy`
