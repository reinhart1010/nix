---
layout: page
title: common/ps (español)
description: "Información sobre procesos en ejecución."
content_hash: 83aa584946cd66e79d24ae1640596f9801d79215
last_modified_at: 2024-01-07
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
  - title: 한국어 version
    url: /ko/common/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

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

- Obtén el PID del proceso padre:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Ordena los procesos por consumo de memoria:

`ps --sort size`
