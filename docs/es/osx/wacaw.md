---
layout: page
title: osx/wacaw (español)
description: "Herramienta de línea de comandos para macOS para capturar imágenes fijas y videos desde una cámara adjunta."
content_hash: a414f568360c4f3e8b6dadd0c671d66764776c86
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/wacaw.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/wacaw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wacaw

Herramienta de línea de comandos para macOS para capturar imágenes fijas y videos desde una cámara adjunta.
Más información: <http://webcam-tools.sourceforge.net>.

- Toma una foto desde la cámara web:

`wacaw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Graba un video:

`wacaw --video `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` --duration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration_in_seconds</span>

- Toma una foto con resolución personalizada:

`wacaw --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Copia imagen recién tomada al portapapeles:

`wacaw --to-clipboard`

- Lista de los dispositivos disponibles:

`wacaw --list-devices`
