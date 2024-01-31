---
layout: page
title: osx/pbpaste (español)
description: "Envía el contenido del portapapeles a la salida estándar."
content_hash: f82a550d6a1ebdc520f93368c18c1409666f383c
last_modified_at: 2024-01-31
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
tldri18n_status: 2
---
# pbpaste

Envía el contenido del portapapeles a la salida estándar.
Comparable a pulsar Cmd + V en el teclado.
Más información: <https://keith.github.io/xcode-man-pages/pbpaste.1.html>.

- Escribe el contenido del portapapeles en un archivo:

`pbpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Utiliza el contenido del portapapeles como entrada de un comando:

`pbpaste | grep foo`
