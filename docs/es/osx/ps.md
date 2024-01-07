---
layout: page
title: osx/ps (español)
description: "Información sobre los procesos en ejecución."
content_hash: a7bcbb1a6f35dccb98aac24835567998ad74a3d6
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/osx/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

Información sobre los procesos en ejecución.
Más información: <https://www.unix.com/man-page/osx/1/ps/>.

- Lista todos los procesos en ejecución:

`ps aux`

- Lista todos los procesos en ejecución incluyendo la cadena de comandos completa:

`ps auxww`

- Busca un proceso que coincida con una cadena:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>

- Obtén el PID principal de un proceso:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Ordena los procesos por uso de memoria:

`ps -m`

- Ordena los procesos por uso de CPU:

`ps -r`
