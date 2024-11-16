---
layout: page
title: linux/w (español)
description: "Muestra quien ha iniciado sesión y sus procesos."
content_hash: 413cc9377b9a7daa6d3d62e327ae0dadcafb4c97
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/linux/w.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/w.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/w.html
    icon: bi bi-globe
tldri18n_status: 2
---
# w

Muestra quien ha iniciado sesión y sus procesos.
Más información: <https://www.geeksforgeeks.org/w-command-in-linux-with-examples/>.

- Muestra información sobre todos los usuarios que han iniciado sesión actualmente:

`w`

- Muestra información sobre un usuario específico:

`w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Muestra información sin incluir la cabecera:

`w --no-header`

- Muestra información sin incluir las columnas de inicio de sesión, JCPU y PCPU:

`w --short`
