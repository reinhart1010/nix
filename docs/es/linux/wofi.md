---
layout: page
title: linux/wofi (español)
description: "Un lanzador de aplicaciones para compositores Wayland basados en wlroots, similar a `rofi` y `dmenu`."
content_hash: cc884a029f1744fa81aee04b8d6f7a807ad00334
last_modified_at: 2024-09-13
related_topics:
  - title: English version
    url: /en/linux/wofi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wofi

Un lanzador de aplicaciones para compositores Wayland basados en wlroots, similar a `rofi` y `dmenu`.
Más información: <https://hg.sr.ht/~scoopta/wofi>.

- Muestra la lista de aplicaciones:

`wofi --show drun`

- Muestra la lista de todos los comandos:

`wofi --show run`

- Envía una lista de elementos a `stdin` e imprime el elemento seleccionado en `stdout`:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Choice1\nChoice2\nChoice3</span>`" | wofi --dmenu`
