---
layout: page
title: osx/opensnoop (español)
description: "Herramienta que rastrea las aperturas de archivos en tu sistema."
content_hash: e0078e212b8f6d1dc93cbf8023a93cc4654ca9f1
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/osx/opensnoop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/opensnoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opensnoop

Herramienta que rastrea las aperturas de archivos en tu sistema.
Más información: <https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- Imprime todos los archivos abiertos a medida que ocurren:

`sudo opensnoop`

- Rastrea todos los archivos abiertos por un proceso por su nombre:

`sudo opensnoop -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_proceso</span>`"`

- Rastrea todos los archivos abiertos por un proceso por PID:

`sudo opensnoop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Seguimiento de los procesos que abren un archivo especificado:

`sudo opensnoop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
