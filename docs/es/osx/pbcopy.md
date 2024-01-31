---
layout: page
title: osx/pbcopy (español)
description: "Copia datos de `stdin` al portapapeles."
content_hash: d6b004394ea33745847656506fefc4a6a38740b8
last_modified_at: 2024-01-31
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
tldri18n_status: 2
---
# pbcopy

Copia datos de `stdin` al portapapeles.
Comparable a pulsar Cmd + C en el teclado.
Más información: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>.

- Coloca el contenido de un archivo específico en el portapapeles:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Coloca los resultados de un comando específico en el portapapeles:

`find . -type t -name "*.png" | pbcopy`
