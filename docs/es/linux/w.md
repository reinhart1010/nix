---
layout: page
title: linux/w (español)
description: "Muestra quien ha iniciado sesión y sus procesos."
content_hash: bfb92e0607417c703eb684a60b2cb573955ecfbb
related_topics:
  - title: English version
    url: /en/linux/w.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/w.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># w

Muestra quien ha iniciado sesión y sus procesos.
Más información: <https://www.geeksforgeeks.org/w-command-in-linux-with-examples/>.

- Muestra información sobre todos los usuarios que han iniciado sesión actualmente:

`w`

- Muestra información sobre un usuario específico:

`w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- Muestra información sin incluir la cabecera:

`w --no-header`

- Muestra información sin incluir las columnas de inicio de sesión, JCPU y PCPU:

`w --short`
