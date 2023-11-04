---
layout: page
title: osx/ps (español)
description: "Información sobre los procesos en ejecución."
content_hash: 3d0e008d79d3e046e9bba478fa2c64861d5964ae
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/osx/ps.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ps

Información sobre los procesos en ejecución.
Más información: <https://www.unix.com/man-page/osx/1/ps/>.

- Lista todos los procesos en ejecución:

`ps aux`

- Lista todos los procesos en ejecución incluyendo la cadena de comandos completa:

`ps auxww`

- Busca un proceso que coincida con una cadena:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>

- Obtiene el PID principal de un proceso:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Ordena los procesos por uso de memoria:

`ps -m`

- Ordena los procesos por uso de CPU:

`ps -r`
