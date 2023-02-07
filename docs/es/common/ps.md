---
layout: page
title: common/ps (español)
description: "Información sobre procesos en ejecución."
content_hash: e6965139c68c8e61771e75ad48dca5844752b186
last_modified_at: 2023-02-07
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ps

Información sobre procesos en ejecución.
Más información: <https://manned.org/ps>.

- Lista todos los procesos en ejecución:

`ps aux`

- Lista todos los procesos en ejecución incluyendo el comando completo:

`ps auxww`

- Busca un proceso que coincida con la cadena de texto:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>

- Lista todos los procesos del usuario actual en formato supercompleto:

`ps --user $(id -u) -F`

- Lista todos los procesos del usuario actual como un árbol:

`ps --user $(id -u) f`

- Obtiene el PID del proceso padre:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Ordena los procesos por consumo de memoria:

`ps --sort size`
