---
layout: page
title: osx/opensnoop (español)
description: "Herramienta que rastrea las aperturas de archivos en tu sistema."
content_hash: 3a5fdc478301ba1c3281e6b2714c59503ae0c09b
last_modified_at: 2023-07-08
related_topics:
  - title: English version
    url: /en/osx/opensnoop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/opensnoop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># opensnoop

Herramienta que rastrea las aperturas de archivos en tu sistema.
Más información: <https://ss64.com/osx/opensnoop.html>.

- Imprime todos los archivos abiertos a medida que ocurren:

`sudo opensnoop`

- Rastrea todos los archivos abiertos por un proceso por su nombre:

`sudo opensnoop -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_proceso</span>`"`

- Rastrea todos los archivos abiertos por un proceso por PID:

`sudo opensnoop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Seguimiento de los procesos que abren un archivo especificado:

`sudo opensnoop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
