---
layout: page
title: osx/pbpaste (español)
description: "Envía el contenido del portapapeles a la salida estándar."
content_hash: 5dd115155a692096636a49bc2b7ee9593e87ccbf
last_modified_at: 2023-08-09
related_topics:
  - title: Deutsch version
    url: /de/osx/pbpaste.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/pbpaste.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbpaste.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbpaste.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pbpaste

Envía el contenido del portapapeles a la salida estándar.
Comparable a pulsar Cmd + V en el teclado.
Más información: <https://ss64.com/osx/pbpaste.html>.

- Escribe el contenido del portapapeles en un archivo:

`pbpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Utiliza el contenido del portapapeles como entrada de un comando:

`pbpaste | grep foo`
